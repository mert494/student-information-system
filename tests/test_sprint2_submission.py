"""Issue #40: temporary fixtures only; no repository evidence is fabricated."""
import contextlib
import copy
import importlib.util
import io
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest
from unittest.mock import patch


SPEC = importlib.util.spec_from_file_location(
    "checker", Path(__file__).resolve().parents[1] / "tools/check_sprint2_submission.py")
checker = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(checker)


def manifest():
    return dict(schema_version=1, expected_commit="", expected_documents=[], scan_documents=[],
                categories={k: {p: [] for p in parts} for k, parts in checker.REQUIRED.items()},
                members={m: {"evidence": []} for m in checker.MEMBERS}, release={})


class CheckerTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.m = manifest()

    def write(self, name, content):
        p = self.root / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")

    def check(self, rule, status=None, m=None, ref=None):
        result = checker.run(self.root, m or self.m, ref)
        return [c for c in result["checks"] if c["id"] == rule and
                (status is None or c["status"] == status)]

    def test_missing_all_suboutputs_never_pass(self):
        self.assertEqual(len(self.check("evidence.missing", "PENDING")), 9)
        self.assertEqual(set(checker.run(self.root, self.m)["categories"].values()), {"PENDING"})

    def test_missing_empty_and_nonempty_files(self):
        self.write("empty.md", " \n")
        self.write("ok.md", "# Actual temporary test output")
        self.m["expected_documents"] = ["missing.md", "empty.md", "ok.md"]
        self.assertEqual(len(self.check("file.read", "ERROR")), 1)
        self.assertEqual(len(self.check("file.empty", "ERROR")), 1)
        self.assertEqual(len(self.check("file.exists", "PASS")), 1)

    def test_valid_relative_inline_image_reference_and_unicode(self):
        self.write("docs/Türkçe dosya.md", "Fixture")
        self.write("docs/a.md", '[x](T%C3%BCrk%C3%A7e%20dosya.md)\n'
                   '![x](<Türkçe dosya.md>)\n[x][doc]\n[x][]\n'
                   '[doc]: <Türkçe dosya.md>\n[x]: <Türkçe dosya.md>\n')
        self.m["scan_documents"] = ["docs/a.md"]
        self.assertFalse(self.check("link.local", "ERROR"))
        self.assertEqual(len(self.check("link.local", "PASS")), 6)

    def test_broken_escape_and_missing_reference(self):
        self.write("a.md", "[bad](missing.md)\n[escape](../secret.md)\n[x][unknown]")
        self.m["scan_documents"] = ["a.md"]
        self.assertEqual(len(self.check("link.local", "ERROR")), 2)
        self.assertEqual(len(self.check("link.unverified", "PENDING")), 1)

    def test_code_blocks_and_inline_code_are_ignored(self):
        self.write("a.md", '```md\n[x](missing.md) TODO\n```\n`[x](missing.md) Pending`\n')
        self.m["scan_documents"] = ["a.md"]
        self.assertFalse(self.check("link.local"))
        self.assertFalse(self.check("decision.marker"))

    def test_anchor_complex_syntax_and_html_pending(self):
        self.write("a.md", '[x](a.md#heading)\n[x](complex(name).md)\n<a href="x">x</a>')
        self.m["scan_documents"] = ["a.md"]
        self.assertEqual(len(self.check("link.anchor", "PENDING")), 1)
        self.assertEqual(len(self.check("link.unverified", "PENDING")), 2)

    def test_context_markers_remain_visible(self):
        self.write("template.md", "[TODO] summary")
        self.write("srs.md", "Pending decision\nDo not mark Pending decisions approved")
        self.m["scan_documents"] = ["template.md"]
        self.m["categories"]["srs_backlog"]["srs"] = [
            {"kind": "file", "value": "srs.md", "version": "fixture-v1"}]
        findings = self.check("decision.marker", "PENDING")
        self.assertEqual([f["blocking"] for f in findings], [False, True, True])

    def test_planning_and_planning_pr_cannot_substitute(self):
        self.m["categories"]["srs_backlog"]["srs"] = [
            {"kind": "file", "value": "docs/sprint2/Sprint2_Plan.md"},
            {"kind": "url", "value": "https://github.com/mert494/student-information-system/pull/25"}]
        self.assertEqual(len(self.check("evidence.planning", "ERROR")), 2)

    def test_figma_format_and_access_separate(self):
        self.assertTrue(checker.figma_url("https://www.figma.com/design/fixture/Title?node-id=1-2"))
        for url in ("http://figma.com/file/key", "https://figma.com.evil.test/design/key",
                    "https://figma.com/", "https://user@figma.com/file/key"):
            self.assertFalse(checker.figma_url(url))
        cat = self.m["categories"]["figma_flows"]
        cat["figma"] = [{"kind": "url", "value": "https://figma.com/proto/fixture", "version": "test"}]
        cat["access"] = {"status": "verified", "reviewer": "fixture"}
        self.assertEqual(len(self.check("url.format", "PASS")), 1)
        self.assertEqual(len(self.check("figma.access", "PENDING")), 1)
        self.assertEqual(len(self.check("url.access", "PENDING")), 1)

    def test_contribution_issue_alone_and_review_claim(self):
        self.m["members"]["mert494"]["evidence"] = [
            {"type": "issue", "url": "https://github.com/example/test/issues/1"}]
        self.m["members"]["azrayy"]["evidence"] = [
            {"type": "review", "url": "https://github.com/example/test/pull/2#review"}]
        findings = self.check("contribution.evidence", "PENDING")
        self.assertEqual(len(findings), 6)
        self.assertIn("insufficient", findings[0]["message"])
        self.assertIn("needs review", findings[-1]["message"])

    def test_malformed_configuration(self):
        for mutation in (lambda m: m.update(schema_version=2),
                         lambda m: m["categories"].pop("architecture"),
                         lambda m: m["categories"]["srs_backlog"].update(srs="bad"),
                         lambda m: m["members"].update(mert494={"evidence": ["bad"]})):
            bad = copy.deepcopy(self.m)
            mutation(bad)
            with self.assertRaises(ValueError):
                checker.validate_manifest(bad)

    def test_positive_automatic_evidence_without_false_acceptance(self):
        for category, parts in checker.REQUIRED.items():
            for part in parts:
                if part == "figma":
                    entry = {"kind": "url", "value": "https://figma.com/design/fixture", "version": "v1"}
                else:
                    name = part + ".md"
                    self.write(name, "# Temporary fixture\nContent for automated existence check.")
                    entry = {"kind": "file", "value": name, "version": "v1"}
                self.m["categories"][category][part] = [entry]
        report = checker.run(self.root, self.m)
        self.assertFalse(self.check("evidence.missing"))
        self.assertEqual(report["summary"]["ERROR"], 0)
        self.assertEqual(report["summary"]["status"], "PENDING")
        self.assertTrue(self.check("file.exists", "PASS"))

    def test_cli_json_text_exit_codes_and_no_file_mutations(self):
        self.write("manifest.json", json.dumps(self.m))
        before = {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        for fmt in ("json", "text"):
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                code = checker.main(["--root", str(self.root), "--manifest", "manifest.json", "--format", fmt])
            self.assertEqual(code, 2)
            if fmt == "json":
                parsed = json.loads(out.getvalue())
                self.assertEqual(parsed["source"]["mode"], "worktree")
                self.assertIn("manifest_sha256", parsed)
            else:
                self.assertIn("Overall: PENDING", out.getvalue())
        after = {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        self.assertEqual(before, after)
        self.write("manifest.json", "{}")
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(checker.main(["--root", str(self.root), "--manifest", "manifest.json"]), 3)

    @unittest.skipUnless(shutil.which("git"), "Local Git unavailable")
    def test_git_snapshot_dirty_sha_and_annotated_tag(self):
        def g(*args):
            return subprocess.check_output(["git", "-C", str(self.root), *args], stderr=subprocess.PIPE).decode().strip()
        g("init", "-q")
        self.write("a.md", "# Fixture")
        g("add", "a.md")
        # Isolated temporary test repository; explicit synthetic identity, never user's repository.
        g("-c", "user.name=Test Fixture", "-c", "user.email=fixture@example.invalid",
          "-c", "commit.gpgsign=false", "commit", "-qm", "fixture")
        sha = g("rev-parse", "HEAD")
        self.m["expected_commit"] = sha
        self.m["expected_documents"] = ["a.md"]
        self.assertTrue(self.check("git.expected", "PASS"))
        self.write("a.md", "")
        report = checker.run(self.root, self.m, sha)
        self.assertTrue(report["source"]["dirty"])
        self.assertEqual(report["source"]["mode"], "commit")
        self.assertFalse([c for c in report["checks"] if c["id"] == "file.empty"])
        self.assertTrue(self.check("file.empty", "ERROR"))
        g("-c", "user.name=Test Fixture", "-c", "user.email=fixture@example.invalid",
          "-c", "tag.gpgsign=false", "tag", "-a", "fixture-s2", "-m", "fixture")
        self.m["release"] = {"tag": "fixture-s2", "commit": sha}
        self.assertTrue(self.check("release.tag", "PASS", ref=sha))
        self.m["release"]["tag"] = "absent"
        self.assertTrue(self.check("release.tag", "PENDING"))
        self.m["release"]["tag"] = "sprint-1"
        self.assertTrue(self.check("release.tag", "ERROR"))
        self.m["expected_commit"] = "0" * 40
        self.assertTrue(self.check("git.expected", "ERROR"))
        with self.assertRaises(ValueError):
            checker.run(self.root, self.m, "0" * 40)

    def test_git_unavailable_is_pending(self):
        with patch.object(checker, "git", return_value=None):
            report = checker.run(self.root, self.m)
        self.assertIsNone(report["source"]["commit"])
        self.assertEqual(report["summary"]["status"], "PENDING")

    def test_missing_artifact_is_category_error(self):
        self.m["categories"]["srs_backlog"]["srs"] = [
            {"kind": "file", "value": "absent.md", "version": "Pending"}]
        r = checker.run(self.root, self.m)
        self.assertEqual(r["categories"]["srs_backlog"], "ERROR")
        self.assertTrue(self.check("evidence.version", "PENDING"))

    def test_malformed_markdown_url_is_finding(self):
        self.write("a.md", "[x](https://[)")
        self.m["scan_documents"] = ["a.md"]
        self.assertTrue(self.check("link.url", "ERROR"))

    def test_error_cli_exit_and_output_parity(self):
        self.m["expected_documents"] = ["absent.md"]
        self.write("manifest.json", json.dumps(self.m))
        reports = []
        for fmt in ("text", "json"):
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                self.assertEqual(checker.main(["--root", str(self.root), "--manifest",
                                               "manifest.json", "--format", fmt]), 1)
            reports.append(out.getvalue())
        parsed = json.loads(reports[1])
        self.assertIn("Counts: " + json.dumps(parsed["summary"], sort_keys=True), reports[0])


    def test_base_is_informational_and_expected_is_optional(self):
        sha = "a" * 40
        self.m["base_commit"] = "b" * 40
        for omit in (False, True):
            m = copy.deepcopy(self.m)
            if omit:
                m.pop("expected_commit")
            with patch.object(checker, "git", return_value=sha):
                report = checker.run(self.root, m)
            self.assertEqual(report["summary"]["ERROR"], 0)
            self.assertEqual(report["source"]["base_commit"], "b" * 40)
            self.assertEqual(report["source"]["expected_commit"], "")
            self.assertEqual(report["source"]["inspected_commit"], sha)
            self.assertEqual(report["source"]["mode"], "worktree")
            self.assertTrue(report["source"]["dirty"])
            finding = next(c for c in report["checks"] if c["id"] == "git.expected")
            self.assertFalse(finding["blocking"])

    def test_legacy_expected_commit_still_compares_exactly(self):
        sha = "a" * 40
        for expected, status in ((sha, "PASS"), ("b" * 40, "ERROR")):
            self.m["expected_commit"] = expected
            with patch.object(checker, "git", return_value=sha):
                report = checker.run(self.root, self.m)
            self.assertEqual(report["source"]["base_commit"], "")
            self.assertEqual(report["source"]["inspected_commit"], sha)
            self.assertEqual(report["source"]["commit"], sha)
            finding = next(c for c in report["checks"] if c["id"] == "git.expected")
            self.assertEqual(finding["status"], status)
        for field in ("base_commit", "expected_commit"):
            bad = copy.deepcopy(self.m)
            bad[field] = 123
            with self.assertRaises(ValueError):
                checker.validate_manifest(bad)

    def test_commit_snapshot_identity_is_not_worktree_head(self):
        inspected, head = "a" * 40, "b" * 40
        def local_git(root, *args):
            if args[0] == "rev-parse":
                return inspected if args[-1].startswith(inspected) else head
            if args[0] == "status":
                return "?? modified.md"
            return ""
        self.m["base_commit"] = head
        self.m["expected_commit"] = inspected
        with patch.object(checker, "git", side_effect=local_git):
            report = checker.run(self.root, self.m, inspected)
        self.assertEqual(report["source"]["mode"], "commit")
        self.assertEqual(report["source"]["inspected_commit"], inspected)
        self.assertEqual(report["source"]["base_commit"], head)
        self.assertTrue(report["source"]["dirty"])
        self.assertFalse(any(c["id"] == "git.dirty" for c in report["checks"]))
        self.assertEqual(next(c["status"] for c in report["checks"]
                              if c["id"] == "git.expected"), "PASS")

    def test_json_roundtrip_on_windows_codepages_with_unicode_paths(self):
        name = "Türkçe/İçerik_şğ_東京_😀.md"
        self.write(name, "# Ölçüm 東京 😀")
        self.m["expected_documents"] = [name]
        self.write("manifest.json", json.dumps(self.m, ensure_ascii=False))
        for encoding in ("cp1254", "cp1252", "ascii"):
            with self.subTest(encoding=encoding):
                raw = io.BytesIO()
                stream = io.TextIOWrapper(raw, encoding=encoding, errors="strict")
                with contextlib.redirect_stdout(stream):
                    code = checker.main(["--root", str(self.root), "--manifest",
                                         "manifest.json", "--format", "json"])
                stream.flush()
                data = raw.getvalue()
                self.assertTrue(data.isascii())
                parsed = json.loads(data.decode("ascii"))
                self.assertEqual(code, 2)
                self.assertIn(name, parsed["file_sha256"])
                self.assertTrue(any(c["file"] == name for c in parsed["checks"]))
                stream.detach()

    def test_json_configuration_errors_are_lossless_on_ascii_stdout(self):
        missing = "yok_şğ_東京_😀.json"
        raw = io.BytesIO()
        stream = io.TextIOWrapper(raw, encoding="ascii", errors="strict")
        with contextlib.redirect_stdout(stream):
            code = checker.main(["--root", str(self.root), "--manifest", missing,
                                 "--format", "json"])
        stream.flush()
        parsed = json.loads(raw.getvalue().decode("ascii"))
        self.assertEqual(code, 3)
        self.assertIn(missing, parsed["configuration_error"])
        stream.detach()

    def test_text_retains_unicode_and_new_commit_labels(self):
        name = "Türkçe_東京_😀.md"
        self.write(name, "# İçerik")
        self.m["expected_documents"] = [name]
        rendered = checker.render_text(checker.run(self.root, self.m))
        self.assertIn(name, rendered)
        self.assertIn("inspected_commit=", rendered)
        self.assertIn("Base commit (informational):", rendered)
        self.assertIn("Overall: PENDING", rendered)


if __name__ == "__main__":
    unittest.main()
