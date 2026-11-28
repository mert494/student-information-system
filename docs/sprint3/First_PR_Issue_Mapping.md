# First PR versus the 16-Issue Sprint 3 proposal

Status: bounded scope mapping, updated 28 November 2026. `S3-01` through `S3-16` are planning identifiers. Related actual Issues: [#53 — S3-02 scaffold/test harness](https://github.com/mert494/student-information-system/issues/53) and [#54 — S3-03 CI/coverage](https://github.com/mert494/student-information-system/issues/54); delivery: [Draft PR #69](https://github.com/mert494/student-information-system/pull/69). Neither Issue is complete or automatically closed by this foundation slice.

## Existing Issues for this PR

Use #53 for the scaffold/test harness and #54 for CI/coverage. No additional Issue is proposed.

Parent mapping: a bounded delivery slice of **S3-02 (scaffold/test harness) and S3-03 (CI/coverage)**, conditional on S3-01 approvals. Mert coordinates; proposed technical owners remain Barış for build/CI, Arda for architecture, Azra for frontend and Ahmet for tests. These are suggestions, not GitHub assignments or completed contributions.

Proposed acceptance criteria:

- A minimal Java 21 process-health endpoint and React/TypeScript connectivity screen build and run locally; no authentication or academic operations are implied.
- Backend/frontend have meaningful unit tests, separate line reports and minimum 50% gates over all included handwritten production code.
- PR workflow targets develop/main, uses least privilege, preserves error exits and retains diagnostic reports. Existing checker tests execute separately.
- Setup, exact candidate paths, validation exits, limitations and pending architecture/product approvals are reviewable.
- Existing repository identity, legacy documents, API, release refs and individual contribution history are preserved.
- Before this Issue/PR can be accepted, Arda/PO scope decisions, independent review and revision-specific GitHub Actions evidence must be recorded. The historical original run passed; updated-head checks and remaining #54 failure/artifact evidence are still needed.

## Exact mapping

| Planning ID | Original proposal | This first PR | Remaining work / status |
| --- | --- | --- | --- |
| S3-01 | Approve architecture/scope slices and reconcile OpenAPI | Records assumptions and pending gates only | No approvals or contract changes; remains pending. |
| [S3-02 / #53](https://github.com/mert494/student-information-system/issues/53) | Backend/frontend scaffold and unit-test harness | Entry point, health/connectivity, pinned builds, wrappers/lockfile and sample unit tests | **Partial delivery slice**: original proposed session-revocation test/first functional slice is deliberately absent until FR-01/02 decisions. Do not mark all S3-02 AC complete. |
| [S3-03 / #54](https://github.com/mert494/student-information-system/issues/54) | PR CI, coverage gates and artifacts | Workflow, separate ≥50% line gates, report validation and local failure-safety tests | **Partial delivery slice**: Original hosted run and upload steps passed; updated-head validation, artifact downloads/contents and deliberate hosted failure cases remain unverified; required-check settings are not changed. |
| S3-04 | Schema migrations and synthetic fixtures | Optional untested PostgreSQL compose/example only | No schema, FK/unique implementation, session store or fixtures. Not complete. |
| S3-05 | Login/revocation/role-record authorization | None | Blocked by approved security/contract slice. |
| S3-06 | Student create/list/PATCH | None | Fields/status/PATCH/permission decisions and auth required. |
| S3-07 | Course maintenance and offering lookup | None | Course uniqueness/offering/term/API decisions and auth required. |
| S3-08 | Enrollment and own-registration listing | None | Data, eligibility, capacity/prerequisite/concurrency and API decisions required. |
| S3-09 | Instructor grade save/read, publication/student read | None | Registration plus academic/publication/instructor-GET decisions required. |
| S3-10 | Frontend shell and real login/logout | Health-only React shell | No login/logout, tokens or role routes. Original feature remains incomplete. |
| S3-11 | Staff Student/Course forms/lists | None | Approved contracts and real backend needed. |
| S3-12 | Enrollment and grade UI | None | Relevant product decisions/backends needed. |
| S3-13 | PostgreSQL/API/security/coverage verification | Scaffold unit evidence and gate-tool tests only | No DB concurrency, runtime product contract, auth or independent final QA. Not complete. |
| S3-14 | Reproducible runtime/demo | Local scaffold commands and prior health smoke evidence | No persistent SIS runtime, Docker verification, deployment or end-to-end product demonstration. |
| S3-15 | Release/submission/contribution evidence | Local PR draft, inventory and test record | Issues #53/#54, commit and Draft PR #69 exist; no release/submission or complete acceptance is established. |
| S3-16 | Usability and built-UI accessibility | No sessions or conformance audit | Participant recruitment and test planning may begin; results remain pending. |

## Why the boundary matters

The first PR title contains “MVP and CI foundation” as requested by Mert. It does not claim that the MVP is implemented. A healthy process, mocked component test or scaffold percentage cannot satisfy FR-01–FR-07.

The earlier draft's PostgreSQL CI job belongs with a real configured integration profile and tests. It is not copied as an empty/skipped job. This candidate provides two measured application unit suites, tool safety tests and legacy checker regression tests. Integration coverage must remain separate from unit coverage when added.

Optional database examples may be excluded by the reviewers without changing the primary S3-02/S3-03 mapping. Any scope or file change requires refreshing the inventory/evidence before staging or publication.
