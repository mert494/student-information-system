# Sprint 2 submission checker

Related Issue: [#40 — S2-15](https://github.com/mert494/student-information-system/issues/40).
This read-only helper supports the existing [submission checklist](Sprint2_Submission_Checklist.md),
[plan](Sprint2_Plan.md) and [traceability analysis](Sprint2_Requirements_Traceability.md).
It creates no submissions, assignments, approvals, tags, branches or GitHub changes.
Deadline date: 24 November 2026; official timezone/format confirmation remains a human check.

## Running

Python 3.9+ and its standard library are required. Git is optional for worktree content checks
and required for commit snapshots/local tag resolution. No packages are installed.
Run from the repository root. On this machine the available interpreter is
`C:/anaconda/python.exe`; substitute your own Python path as needed.

```text
python -B tools/check_sprint2_submission.py --format text
python -B tools/check_sprint2_submission.py --format json
python -B tools/check_sprint2_submission.py --ref 2945b81c934ee14c2c7a5875ad5cbcae79fc1f96 --format json
python -B -m unittest discover -s tests -v
```

The configuration is [submission_manifest.json](submission_manifest.json).
`--root` selects the repository; `--manifest` is relative to that root.
The manifest always comes from the worktree, even in `--ref` mode, and its SHA-256 is reported.
`--ref` must be a full commit SHA already in local Git; the tool never fetches or switches branches.
An unavailable ref is a configuration error. Worktree mode includes modified/untracked files;
the reported HEAD is metadata, not a claim that those files are committed.
The report includes content hashes of inspected local documents and the Git dirty file list.
Use stdout redirection if a report file is wanted; the checker itself writes no reports.

Exit codes: 0 = no blocking findings, 1 = blocking ERROR, 2 = blocking PENDING,
3 = configuration/input error. ERROR takes precedence over PENDING.
Manual gates intentionally remain PENDING in this first version, so a report cannot certify
full submission acceptance even when every automatic check passes.

## Filling actual evidence

The shipped manifest leaves missing evidence empty. It does not populate colleague decisions
or infer contributions from assignment.

Commit identities are separate (schema version 1 remains supported):

- `base_commit`: optional informational starting point used to develop the checker.
  A difference from the inspected commit never causes an error.
- `expected_commit`: optional exact submission commit explicitly selected by the user.
  Empty or omitted means no comparison was requested; no SHA is invented.
  The `git.expected` finding is nonblocking PENDING in that case. If supplied, a mismatch
  is ERROR; unavailable local Git identity is PENDING.
- `source.inspected_commit`: the commit actually resolved through Git. Snapshot mode uses
  the resolved `--ref`; worktree mode reports HEAD metadata while inspecting files that may
  include uncommitted changes. Mode and dirty state remain explicit.

The shipped manifest records the development baseline as `base_commit` and leaves
`expected_commit` empty. Older manifests containing only `expected_commit` retain their
strict comparison behavior; they are not silently migrated to informational baselines.
JSON `source.commit` remains an alias of `source.inspected_commit` for older consumers.
The source object also reports the declared base and expected identities.

Each required sub-output is an array of evidence entries. An entry has `kind` (`file` or `url`),
`value` (repository-relative path or HTTPS URL), and `version` (actual version/commit identifier).
One real document may serve several sub-outputs if the relevant content is present; human review
must verify that claim. The mandatory keys are:

| Category | Sub-outputs |
| --- | --- |
| srs_backlog | srs, refined_backlog |
| nfr_quality | nfr, quality_measures |
| figma_flows | figma, user_flows |
| architecture | architecture_document, c4, uml |

`expected_documents` lists support files that must exist; `scan_documents` lists additional
support Markdown files to inspect. These lists never establish category completion.
The five planning/analysis filenames and PR #24/#25 URLs cannot substitute for technical outputs.
This guard is limited: renaming a planning document does not transform it into a deliverable;
semantic correctness always needs human review.

Optional category `review` and Figma `access` objects may record actual `reviewer`, `version`,
`date`, `evidence_url`, `status` and audience details. They are printed as human declarations,
never treated as automatically verified approval/access. Do not insert fictitious values.
All external evidence requires manual existence/access and version checks.

Each of the six member records has an `evidence` array. Entries contain `type` (`pr`, `commit`,
`review`, `artifact` or `issue`) and `url`. Multiple evidence types are welcome; a commit is
not mandatory for every member. Issue assignment alone is insufficient. URL format validation
does not establish ownership, authorship, contribution quality or member acceptance.
Empty records do not mean a member made no contribution; they mean evidence is not supplied here.

`release` holds the actual `tag`, full `commit` SHA and HTTPS `url`. Only local tag-to-commit
resolution is checked (including annotated tags). Missing local objects/tags are PENDING;
mismatches are ERROR. A release publication, assets, remote refs and uploaded package remain
unverified. The checker rejects `sprint-1` as Sprint 2 evidence and never modifies it.

## Findings and limitations

- ERROR: claimed file missing/empty, invalid URL, broken file link, planning document used as
  technical evidence, SHA mismatch, or local tag pointing to a different audited commit.
- PENDING: evidence unspecified, version missing, open decision, unsupported link syntax,
  unresolved manual acceptance/access/contribution/release/submission checks.
- PASS: a particular automatic check succeeded (for example a file exists). This is not a
  category acceptance, PO decision, successful runtime test or Teams receipt.

JSON schema version 1 contains `source`, `manifest_sha256`, `file_sha256`, `summary`,
`categories`, `checks` and `limitations`. Findings include a stable rule ID, status, blocking flag,
file/line where applicable, category, message and `verification_method`.
Text renders the same findings. Nonblocking PENDING findings remain visible in counts.

JSON output uses ASCII Unicode escapes (including configuration errors), so Windows code
pages such as cp1254/cp1252 and ASCII can encode it without replacement or loss.
Standard JSON decoding restores the original Turkish paths and all Unicode characters,
including supplementary characters. A UTF-8 terminal or `-X utf8` is not required for JSON.
Stdout is not reconfigured; human-readable text retains Unicode and the terminal's existing
encoding behavior.

Markdown checks cover inline links/images, reference definitions and full/collapsed reference
uses, percent-encoded paths and UTF-8 files. Fenced blocks and inline code are ignored.
Only configured Markdown/support files and declared local deliverables are scanned;
linked files are checked for existence, not recursively scanned. Add them to the manifest
when their contents need inspection. Repository escapes (including symlinks outside root)
are rejected. Anchors, HTML links, complex/nested link syntax and shortcut references are
not fully implemented; anchors and recognized unsupported syntax are reported PENDING.
This is not a full CommonMark validator.

TODO/Pending/Proposed matches include file/line and context. Markers in support/planning/template
files are nonblocking PENDING. Markers in declared technical Markdown remain blocking, including
instruction-like text flagged for manual classification. This conservative heuristic can produce
false positives; the tool does not silently erase or approve decisions. No suppression mechanism
is included in the first version.

Figma URLs require HTTPS, an exact figma.com/www.figma.com hostname and a supported
design/file/proto/board path with a key. The URL is not requested over the network.
A valid format always leaves access PENDING. No login page or successful HTTP response is
treated as proof of reviewer access.

The tool cannot judge SRS completeness, metrics feasibility, diagram semantics/readability,
prototype navigation, authorization rules, official assignment requirements, or truthful review
and contribution declarations. It does not validate YAML/OpenAPI or run product/performance tests.
There is no Teams upload and no automatic Issue closure or readiness percentage.
