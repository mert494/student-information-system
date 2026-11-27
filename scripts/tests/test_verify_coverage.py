"""Coverage-gate safety tests; these do not count as application unit coverage."""
import contextlib
import importlib.util
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location(
    "verify_coverage", Path(__file__).resolve().parents[1] / "verify_coverage.py")
gate = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(gate)


class CoverageGateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.tests = self.root / "unit.xml"
        self.tests.write_text('<testsuites><testsuite tests="2" skipped="0" failures="0" '
                              'errors="0"/></testsuites>', encoding="utf-8")

    def run_gate(self, component, report, minimum="50"):
        with patch.dict("os.environ", {"GITHUB_STEP_SUMMARY": ""}), \
                contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            return gate.main([component, "--coverage", str(report), "--tests", str(self.tests),
                              "--minimum", minimum])

    def backend(self, covered, missed):
        path = self.root / "jacoco.xml"
        path.write_text(f'<report><counter type="LINE" covered="{covered}" '
                        f'missed="{missed}"/></report>', encoding="utf-8")
        return path

    def test_exactly_fifty_percent_passes(self):
        self.assertEqual(0, self.run_gate("backend", self.backend(5, 5)))

    def test_below_fifty_percent_fails(self):
        self.assertEqual(1, self.run_gate("backend", self.backend(4, 6)))

    def test_missing_and_empty_coverage_fail(self):
        self.assertEqual(1, self.run_gate("backend", self.root / "missing.xml"))
        self.assertEqual(1, self.run_gate("backend", self.backend(0, 0)))

    def test_no_executed_tests_fails_even_with_full_coverage(self):
        self.tests.write_text('<testsuite tests="2" skipped="2"/>', encoding="utf-8")
        self.assertEqual(1, self.run_gate("backend", self.backend(10, 0)))

    def test_reported_test_failure_fails(self):
        self.tests.write_text('<testsuite tests="2" failures="1"/>', encoding="utf-8")
        self.assertEqual(1, self.run_gate("backend", self.backend(10, 0)))

    def test_frontend_uses_its_own_line_counts(self):
        report = self.root / "frontend.json"
        report.write_text('{"total":{"lines":{"covered":5,"total":10}}}', encoding="utf-8")
        self.assertEqual(0, self.run_gate("frontend", report))
        self.assertEqual(1, self.run_gate("frontend", report, "51"))

    def test_malformed_or_impossible_counts_fail(self):
        self.assertEqual(1, self.run_gate("backend", self.backend(-1, 2)))
        report = self.root / "frontend.json"
        report.write_text('{"total":{"lines":{"covered":11,"total":10}}}', encoding="utf-8")
        self.assertEqual(1, self.run_gate("frontend", report))


if __name__ == "__main__":
    unittest.main()
