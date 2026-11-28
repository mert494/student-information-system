"""Fail closed on absent, empty, failing or below-threshold unit reports.

Related Sprint 3 Issue: #54 (CI/coverage). Unit coverage is separate for each component.
"""
import argparse
import json
import math
import os
from pathlib import Path
import sys
import xml.etree.ElementTree as ET


def nonnegative_integer(value):
    if isinstance(value, bool):
        raise ValueError("Boolean is not a line/test count")
    number = int(value)
    if number < 0 or number != float(value):
        raise ValueError("Expected a nonnegative integer count")
    return number


def test_count(paths):
    executed = 0
    for path in paths:
        root = ET.parse(path).getroot()
        suites = [s for s in root.iter("testsuite") if s.find("testsuite") is None]
        if not suites:
            raise ValueError("No test suites in " + str(path))
        for suite in suites:
            tests = nonnegative_integer(suite.get("tests", 0))
            skipped = nonnegative_integer(suite.get("skipped", 0))
            disabled = nonnegative_integer(suite.get("disabled", 0))
            failures = nonnegative_integer(suite.get("failures", 0))
            errors = nonnegative_integer(suite.get("errors", 0))
            if failures or errors:
                raise ValueError("Failing tests in " + str(path))
            if skipped + disabled > tests:
                raise ValueError("Invalid skipped-test counts")
            executed += tests - skipped - disabled
    if executed <= 0:
        raise ValueError("No non-skipped unit tests")
    return executed


def coverage_counts(component, path):
    if component == "backend":
        counter = ET.parse(path).getroot().find("counter[@type='LINE']")
        if counter is None:
            raise ValueError("Missing aggregate JaCoCo LINE counter")
        covered = nonnegative_integer(counter.get("covered"))
        total = covered + nonnegative_integer(counter.get("missed"))
    else:
        lines = json.loads(path.read_text(encoding="utf-8"))["total"]["lines"]
        covered = nonnegative_integer(lines["covered"])
        total = nonnegative_integer(lines["total"])
    if total == 0 or covered > total:
        raise ValueError("Empty or invalid executable-line denominator")
    return covered, total


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("component", choices=["backend", "frontend"])
    parser.add_argument("--coverage", type=Path, required=True)
    parser.add_argument("--tests", type=Path, required=True)
    parser.add_argument("--minimum", type=float, default=50.0)
    args = parser.parse_args(argv)
    try:
        if not math.isfinite(args.minimum) or not 0 <= args.minimum <= 100:
            raise ValueError("Minimum must be a percentage from 0 to 100")
        paths = sorted(args.tests.glob("TEST-*.xml")) if args.tests.is_dir() else [args.tests]
        tests = test_count(paths)
        covered, total = coverage_counts(args.component, args.coverage)
        percentage = covered / total * 100
        result = dict(component=args.component, unit_tests=tests, covered_lines=covered,
                      total_lines=total, line_coverage_percent=round(percentage, 4),
                      minimum_percent=args.minimum)
        print(json.dumps(result, sort_keys=True))
        if os.environ.get("GITHUB_STEP_SUMMARY"):
            with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as summary:
                summary.write(f"\n{args.component} unit lines: {covered}/{total} "
                              f"({percentage:.2f}%), minimum {args.minimum:g}%.\n")
        if percentage < args.minimum:
            raise ValueError(f"{args.component} unit line coverage {percentage:.2f}% "
                             f"is below {args.minimum:g}%")
    except (OSError, ValueError, TypeError, OverflowError, KeyError, ET.ParseError) as error:
        print("Coverage gate FAILED: " + str(error), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
