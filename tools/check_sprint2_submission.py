"""Read-only Sprint 2 evidence checks. Related Issue: #40 (S2-15).

PASS describes an individual mechanical check, never academic acceptance.
Only Python's standard library is required; local Git checks use git if present.
"""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit


REQUIRED = {
    "srs_backlog": ("srs", "refined_backlog"),
    "nfr_quality": ("nfr", "quality_measures"),
    "figma_flows": ("figma", "user_flows"),
    "architecture": ("architecture_document", "c4", "uml"),
}
MEMBERS = ("mert494", "nsnkcc", "ardaberkkara1", "ahmetserdar41",
           "baryyss-001", "azrayy")
PLANNING = {
    "Sprint2_Plan.md", "Sprint2_Task_Breakdown.md",
    "Sprint2_Submission_Checklist.md", "Sprint2_Requirements_Traceability.md",
    "Sprint2_Gap_Analysis.md", "Submission_Checker_Usage.md",
}
MARKERS = re.compile(r"\b(?:TODO|Pending|Proposed)\b", re.I)


def https_url(value):
    try:
        u = urlsplit(value)
        return (u.scheme == "https" and bool(u.hostname) and not u.username
                and not u.password and not re.search(r"\s", value))
    except ValueError:
        return False


def figma_url(value):
    if not https_url(value):
        return False
    u = urlsplit(value)
    return (u.hostname in ("figma.com", "www.figma.com")
            and re.match(r"^/(?:design|file|proto|board)/[A-Za-z0-9_-]+(?:/|$)", u.path)
            is not None)


def git(root, *args):
    try:
        p = subprocess.run(["git", "--no-optional-locks", "-C", str(root), *args],
                           capture_output=True, timeout=20, check=False)
        if p.returncode == 0:
            return p.stdout.decode("utf-8", errors="replace").strip()
    except (OSError, subprocess.TimeoutExpired):
        pass
    return None


def validate_manifest(m):
    """Reject malformed input rather than silently skipping required sections."""
    if not isinstance(m, dict) or m.get("schema_version") != 1:
        raise ValueError("schema_version must be 1")
    if not isinstance(m.get("categories"), dict):
        raise ValueError("categories must be an object")
    for key, parts in REQUIRED.items():
        category = m["categories"].get(key)
        if not isinstance(category, dict):
            raise ValueError("Missing category: " + key)
        for part in parts:
            entries = category.get(part)
            if not isinstance(entries, list):
                raise ValueError(key + "." + part + " must be an array")
            for e in entries:
                if (not isinstance(e, dict) or e.get("kind") not in ("file", "url")
                        or not isinstance(e.get("value"), str) or not e["value"].strip()
                        or not isinstance(e.get("version", ""), str)):
                    raise ValueError("Evidence needs kind=file/url, value and optional string version")
        for field in ("review", "access"):
            if field in category and not isinstance(category[field], dict):
                raise ValueError(key + "." + field + " must be an object")
    if not isinstance(m.get("members"), dict) or not isinstance(m.get("release"), dict):
        raise ValueError("members and release must be objects")
    for name, member in m["members"].items():
        if not isinstance(member, dict) or not isinstance(member.get("evidence", []), list):
            raise ValueError("Invalid member record: " + name)
        for e in member.get("evidence", []):
            if (not isinstance(e, dict) or e.get("type") not in
                    ("pr", "commit", "review", "artifact", "issue")
                    or not isinstance(e.get("url"), str)):
                raise ValueError("Invalid contribution evidence: " + name)
    for key in ("expected_documents", "scan_documents"):
        if not isinstance(m.get(key, []), list) or any(
                not isinstance(x, str) for x in m.get(key, [])):
            raise ValueError(key + " must be a string array")
    for key in ("base_commit", "expected_commit"):
        if not isinstance(m.get(key, ""), str):
            raise ValueError(key + " must be a string")
    for key in ("tag", "commit", "url"):
        if not isinstance(m["release"].get(key, ""), str):
            raise ValueError("release." + key + " must be a string")


class Source:
    def __init__(self, root, ref=None):
        self.root = Path(root).resolve()
        self.ref = ref
        self.commit = git(self.root, "rev-parse", "--verify", (ref or "HEAD") + "^{commit}")
        if ref and (not re.fullmatch(r"[0-9a-fA-F]{40,64}", ref)
                    or not self.commit):
            raise ValueError("--ref must be an available full local commit SHA")
        self.files = set()
        if ref:
            raw = git(self.root, "ls-tree", "-r", "--name-only", "-z", self.commit)
            self.files = set((raw or "").split("\0"))

    def normalize(self, path):
        if "\\" in path or re.match(r"^[A-Za-z]:", path) or path.startswith("/"):
            raise ValueError("Use repository-relative POSIX paths")
        parts = []
        for part in PurePosixPath(path).parts:
            if part == "..":
                if not parts:
                    raise ValueError("Path escapes repository")
                parts.pop()
            elif part not in (".", ""):
                parts.append(part)
        result = "/".join(parts)
        if not result or ".git" in parts:
            raise ValueError("Invalid evidence path")
        if not self.ref:
            (self.root / result).resolve().relative_to(self.root)
        return result

    def read(self, path):
        path = self.normalize(path)
        if self.ref:
            if path not in self.files:
                raise FileNotFoundError(path)
            # Read bytes without newline/encoding conversion for evidence hashing.
            p = subprocess.run(["git", "--no-optional-locks", "-C", str(self.root),
                                "show", self.commit + ":" + path],
                               capture_output=True, timeout=20, check=False)
            if p.returncode:
                raise OSError("Cannot read snapshot file: " + path)
            return p.stdout
        return (self.root / path).read_bytes()


def prose_lines(text):
    """Small documented Markdown subset: ignore fenced blocks and inline code."""
    fence = None
    for n, line in enumerate(text.splitlines(), 1):
        m = re.match(r"^\s*(`{3,}|~{3,})", line)
        if m:
            token = m.group(1)
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            continue
        if fence is None:
            yield n, re.sub(r"(`+).*?\1", "", line)


def markdown_links(lines):
    """Yield (line, target, supported). No claim to implement CommonMark."""
    definitions = {}
    for n, line in lines:
        m = re.match(r"^\s{0,3}\[([^]]+)\]:\s*(<[^>]+>|\S+)", line)
        if m:
            definitions[m[1].casefold()] = m[2].strip("<>")
    for n, line in lines:
        if re.match(r"^\s{0,3}\[[^]]+\]:", line):
            # Validate definition targets even if unused.
            m = re.match(r"^\s{0,3}\[[^]]+\]:\s*(<[^>]+>|\S+)", line)
            if m:
                yield n, m[1].strip("<>"), True
            continue
        inline = r"!?\[[^]\n]*\]\((<[^>]+>|[^\s()]+)(?:\s+\"[^\"]*\")?\)"
        for m in re.finditer(inline, line):
            yield n, m[1].strip("<>"), True
        remaining = re.sub(inline, "", line)
        for m in re.finditer(r"!?\[([^]\n]+)\]\[([^]\n]*)\]", remaining):
            label = (m[2] or m[1]).casefold()
            yield n, definitions.get(label, label), label in definitions
        remaining = re.sub(r"!?\[[^]\n]+\]\[[^]\n]*\]", "", remaining)
        if re.search(r"\]\(|<a\b|<img\b", remaining, re.I):
            yield n, "Unsupported Markdown/HTML link syntax", False


def run(root, manifest, ref=None):
    validate_manifest(manifest)
    source = Source(root, ref)
    checks = []

    def add(code, status, message, file=None, line=None, blocking=True,
            method="automatic", category=None):
        checks.append(dict(id=code, status=status, message=message, file=file,
                           line=line, blocking=blocking, verification_method=method,
                           category=category))

    status = git(source.root, "status", "--porcelain=v1", "--untracked-files=all")
    meta = dict(mode="commit" if ref else "worktree", root=str(source.root),
                commit=source.commit, inspected_commit=source.commit, ref=ref,
                base_commit=manifest.get("base_commit", ""),
                expected_commit=manifest.get("expected_commit", ""),
                branch=git(source.root, "symbolic-ref", "--short", "HEAD"),
                dirty=None if status is None else bool(status),
                worktree_changes=[] if status is None else status.splitlines())
    add("git.available", "PASS" if source.commit else "PENDING",
        "Local commit identified" if source.commit else "Local Git commit unavailable")
    expected = manifest.get("expected_commit", "")
    if expected:
        add("git.expected", "PASS" if source.commit == expected else
            ("PENDING" if source.commit is None else "ERROR"),
            "Expected commit: " + expected)
    else:
        add("git.expected", "PENDING", "Optional expected commit not specified; comparison not requested",
            blocking=False)
    if status and not ref:
        add("git.dirty", "PENDING", "Worktree contains changes; HEAD is not the checked content")

    scanned = set()
    digests = {}

    def document(path, support=False):
        try:
            path = source.normalize(path)
            data = source.read(path)
        except (ValueError, OSError, subprocess.TimeoutExpired) as exc:
            add("file.read", "ERROR", str(exc), file=path)
            return False
        if not data.strip():
            add("file.empty", "ERROR", "Empty evidence file", file=path)
            return False
        digests[path] = hashlib.sha256(data).hexdigest()
        add("file.exists", "PASS", "Nonempty local file", file=path)
        if path.endswith(".md") and path not in scanned:
            scanned.add(path)
            try:
                lines = list(prose_lines(data.decode("utf-8-sig")))
            except UnicodeError:
                add("markdown.encoding", "ERROR", "Markdown must be UTF-8", file=path)
                return False
            for n, target, supported in markdown_links(lines):
                if not supported:
                    add("link.unverified", "PENDING", target, path, n)
                    continue
                try:
                    u = urlsplit(target)
                except ValueError:
                    add("link.url", "ERROR", "Malformed URL: " + target, path, n)
                    continue
                if u.scheme or u.netloc:
                    if u.scheme in ("https", "http"):
                        add("link.external", "PENDING", "Remote access not checked: " + target,
                            path, n, blocking=False)
                    else:
                        add("link.scheme", "PENDING", "Unsupported link scheme: " + target,
                            path, n)
                    continue
                try:
                    target_path = (str(PurePosixPath(path).parent / unquote(u.path))
                                   if u.path else path)
                    source.read(target_path)
                    add("link.local", "PASS", target, path, n)
                    if u.fragment:
                        add("link.anchor", "PENDING", "Anchor not checked: " + target,
                            path, n)
                except (ValueError, OSError, subprocess.TimeoutExpired) as exc:
                    add("link.local", "ERROR", target + ": " + str(exc), path, n)
            for n, line in lines:
                if MARKERS.search(line):
                    template = "template" in path.lower() or support
                    instructional = bool(re.search(
                        r"do not|must not|never|remain|preserve|should|only after", line, re.I))
                    context = "support/template" if template else (
                        "instruction (manual classification)" if instructional else "open decision")
                    add("decision.marker", "PENDING", context + ": " + line.strip()[:240],
                        path, n, blocking=not template)
        return True

    for path in manifest.get("expected_documents", []):
        document(path, support=True)
    for path in manifest.get("scan_documents", []):
        document(path, support=True)

    for category, parts in REQUIRED.items():
        cat = manifest["categories"][category]
        for part in parts:
            entries = cat[part]
            if not entries:
                add("evidence.missing", "PENDING", "Missing " + part, category=category)
            for e in entries:
                value = e["value"]
                if MARKERS.search(value) or value.strip().lower() in ("tbd", "unknown"):
                    add("evidence.placeholder", "PENDING", part + ": " + value, category=category)
                    continue
                if (PurePosixPath(urlsplit(value).path).name in PLANNING
                        or re.search(r"/pull/(24|25)(?:$|[/?#])", value)):
                    add("evidence.planning", "ERROR", "Planning cannot substitute for " + part,
                        category=category)
                    continue
                if not e.get("version") or MARKERS.search(e["version"]):
                    add("evidence.version", "PENDING", "Version unspecified: " + part, category=category)
                if e["kind"] == "file":
                    if part == "figma":
                        add("figma.url", "ERROR", "Figma requires a URL", category=category)
                    start = len(checks)
                    document(value)
                    for finding in checks[start:]:
                        finding["category"] = category
                else:
                    valid = figma_url(value) if part == "figma" else https_url(value)
                    add("url.format", "PASS" if valid else "ERROR", value, category=category)
                    add("url.access", "PENDING", "Remote existence/access not automatically verified",
                        category=category)
        # Claimed manual reviews remain declarations, never automatically PASS.
        add("review.manual", "PENDING", "Human acceptance required; declared review: " +
            json.dumps(cat.get("review", {}), ensure_ascii=False),
            method="manual_required", category=category)
        if category == "figma_flows":
            add("figma.access", "PENDING", "Manually verify audience/version/access; declaration: " +
                json.dumps(cat.get("access", {}), ensure_ascii=False),
                method="manual_required", category=category)

    for member in MEMBERS:
        record = manifest["members"].get(member, {})
        evidence = record.get("evidence", [])
        substantive = False
        for e in evidence:
            valid = https_url(e["url"])
            add("contribution.url", "PASS" if valid else "ERROR", member + ": " + e["url"])
            if e["type"] != "issue" and valid:
                substantive = True
        add("contribution.evidence", "PENDING", member + (
            ": contribution evidence declared; ownership/content needs review" if substantive else
            ": no substantive contribution evidence (assignment/Issue alone is insufficient)"),
            method="manual_required")

    release = manifest["release"]
    tag, commit = release.get("tag", ""), release.get("commit", "")
    if not tag:
        add("release.tag", "PENDING", "Sprint 2 tag unspecified")
    elif tag == "sprint-1":
        add("release.tag", "ERROR", "Sprint 1 tag cannot represent Sprint 2")
    else:
        resolved = git(source.root, "rev-parse", "--verify", "refs/tags/" + tag + "^{commit}")
        expected_release = git(source.root, "rev-parse", "--verify", commit + "^{commit}") if re.fullmatch(
            r"[0-9a-fA-F]{40,64}", commit) else None
        add("release.tag", "PENDING" if not resolved or not expected_release else
            ("PASS" if resolved == expected_release else "ERROR"),
            "Local tag commit: " + str(resolved) + "; expected: " + str(commit))
        if resolved and source.commit and resolved != source.commit:
            add("release.source", "ERROR", "Tag does not identify the audited commit")
    if release.get("url"):
        add("release.url", "PASS" if https_url(release["url"]) else "ERROR", release["url"])
    add("release.remote", "PENDING", "Release publication/assets not checked (offline)",
        method="manual_required")
    add("submission.manual", "PENDING", "Confirm official format/timezone, package, six-member "
        "evidence and Teams receipt against Issue #40; no submission performed",
        method="manual_required")
    counts = Counter(x["status"] for x in checks)
    overall = "ERROR" if any(x["status"] == "ERROR" and x["blocking"] for x in checks) else (
        "PENDING" if any(x["status"] == "PENDING" and x["blocking"] for x in checks) else "PASS")
    return dict(schema_version=1, source=meta, file_sha256=digests,
                summary=dict(status=overall, **{s: counts[s] for s in ("PASS", "ERROR", "PENDING")}),
                categories={key: "ERROR" if any(x["category"] == key and x["status"] == "ERROR"
                                               for x in checks) else "PENDING" for key in REQUIRED},
                checks=checks,
                limitations=["Offline mechanical checks do not establish human acceptance.",
                             "Markdown subset only; anchors and remote access require review."])


def render_text(report):
    s = report["source"]
    lines = ["Sprint 2 submission checker — Issue #40 / S2-15",
             "Source: {mode}; inspected_commit={inspected_commit}; branch={branch}; dirty={dirty}".format(**s),
             "Base commit (informational): {base_commit}; expected_commit={expected_commit}".format(**s),
             "Overall: " + report["summary"]["status"] + " (not an acceptance certificate)"]
    lines.extend("{}: {}".format(k, v) for k, v in report["categories"].items())
    for c in report["checks"]:
        location = (c["file"] or "") + (":" + str(c["line"]) if c["line"] else "")
        lines.append("[{status}] {id} {loc} ({verification_method}, blocking={blocking}) {message}".format(
            loc=location, **c))
    lines.append("Counts: " + json.dumps(report["summary"], sort_keys=True))
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".")
    parser.add_argument("--manifest", default="docs/sprint2/submission_manifest.json",
                        help="Path relative to root (configuration always read from worktree)")
    parser.add_argument("--ref", help="Audit files at an available full local commit SHA")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    args = parser.parse_args(argv)
    try:
        config_source = Source(args.root)
        manifest = json.loads(config_source.read(args.manifest).decode("utf-8-sig"))
        report = run(args.root, manifest, args.ref)
        report["manifest_sha256"] = hashlib.sha256(config_source.read(args.manifest)).hexdigest()
    except (ValueError, OSError, subprocess.TimeoutExpired) as exc:
        payload = {"schema_version": 1, "summary": {"status": "ERROR"}, "configuration_error": str(exc)}
        print(json.dumps(payload, ensure_ascii=True) if args.format == "json" else "Configuration ERROR: " + str(exc))
        return 3
    # ASCII JSON escapes preserve every Unicode code point across Windows code pages.
    # Do not reconfigure stdout or replace characters; leave text output unchanged.
    print(json.dumps(report, ensure_ascii=True, indent=2) if args.format == "json" else render_text(report))
    return {"PASS": 0, "ERROR": 1, "PENDING": 2}[report["summary"]["status"]]


if __name__ == "__main__":
    sys.exit(main())
