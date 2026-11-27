# Proposed first Sprint 3 integration PR

**Title:** `chore(sprint3): initialize MVP and CI foundation`

**Head:** `feature/sprint3-mvp-ci-foundation`

**Base:** `develop`
**Status:** Local draft; **41 files staged: 39 additions and 2 modifications**. Staging/review and documentation corrections are authorized. No candidate commits or remote changes have occurred; Arda's architecture approval and Nurefşan's scope approval remain pending.

## Summary

The repository currently contains Sprint 2 design documents and submission-checker tooling without an application build. This candidate adds a minimal Java 21/Spring Boot process-health endpoint and React/TypeScript connection screen, with builds, meaningful unit tests and a GitHub Actions workflow enforcing separate 50% line-coverage gates.

The result is a technical foundation for future MVP work. Authentication, Student/Course management, registration, grades, database schema and authorization are not implemented. No placeholder security or fake product-success endpoint is included.

## Related Issue

GitHub Issue: **[TODO]** — none created. Proposed Issue title: **[Sprint 3] Initialize technical scaffold and unit-test CI**. This is a bounded S3-02/S3-03 delivery slice under the existing 16-item local proposal; it does not complete those original Issues' full acceptance criteria. See `docs/sprint3/First_PR_Issue_Mapping.md`.

Mert coordinates Issue linkage. Do not invent a number or assume automatic closure for a PR to develop. Replace the placeholder only after separately authorized Issue creation or linkage to an actual Issue.

## Changes Made

- Java 21/Spring Boot 4.2.0 candidate entry point, loopback-only configuration and GET /health with current process uptime.
- Maven 3.9.16 / Wrapper 3.3.4 with checksum validation; JUnit Jupiter 5.14.4, Mockito 5.24.0 and JaCoCo 0.8.16.
- React 19.3.1, TypeScript 7.0.2 and Vite 8.3.8 frontend with same-origin dev proxy, validated health payloads, loading/failure/retry/cancellation/timeout states and pinned lockfile.
- Workflow for PRs to develop/main and pushes to both, read-only repository permissions, pinned actions and 30-day coverage/diagnostic artifacts.
- Independent backend/frontend line gates and a report checker that rejects missing/empty results, zero executed tests and test failures. Its safety tests and the legacy 24-test checker suite execute outside application coverage.
- Preserve existing README project/course identity and every .gitignore rule; append relevant setup/ignore content. Scope line-ending rules to new Sprint 3 paths.
- Carry optional PostgreSQL compose/dummy examples as unverified architecture candidates, with no application DB integration. Reviewers may defer these two files.
- Integration notes, exact file inventory, measured local test report, Issue mapping and next-PR sequence.

Original Sprint 1/2 documents, API, templates, history and release refs are unchanged. Extra blank EOF lines were removed only from newly imported files flagged by Git; no application logic/dependency/test-expectation change was made from the validated foundation.

## Testing Performed

These are **historical local results from the integration validation run before staging**, not GitHub Actions execution or new results from this documentation-only correction. The corrections do not change application code, configuration or test inputs; the recorded results below are preserved without rerunning unrelated builds.

| Check | Result |
| --- | --- |
| Maven clean verify on Java 21 | PASS; 4 tests, 0 failures/errors/skips, executable package produced |
| JaCoCo bundle line check | PASS at ≥50%; 9/13 executable lines = **69.23%** |
| npm ci / TypeScript / Vite production build | PASS |
| Vitest unit suite and frontend line gate | PASS; 13 tests; 28/31 lines = **90.32%** |
| Coverage-report tooling safety suite | PASS; 7 tests, outside application metrics |
| Existing Sprint 2 submission-checker suite | PASS; 24 tests, outside application metrics |
| actionlint 1.7.12 | PASS locally; ShellCheck/Pyflakes integrations disabled because unavailable |

Backend coverage includes its uncovered application entry/configuration. Frontend coverage includes its uncovered bootstrap. No handwritten production class/module is excluded and no combined percentage is claimed. The percentages cover this small scaffold, not a future expanded MVP.

Commands, report paths, environment limits and final diff/inventory/preservation checks are recorded in `docs/sprint3/Test_Report.md`. GitHub run URL, tested merge SHA and artifact links: **[TODO — no remote run exists]**.

## Architecture assumptions awaiting Arda

Approve the candidate stack/versions, namespace, module layout, health route, dev proxy, runtime config and test/CI tools. Spring Boot 4.2 defaults to JUnit 6; this candidate explicitly pins its JUnit BOM property to 5.14.4 and uses plain unit tests without Spring Test. Future Spring integration tests need a compatibility review.

The provisional shared OpenAPI is unchanged. Token/session response, logout/`sid` mapping, roles/record relationships, offering lookup/reference, instructor GET, publication, errors and PATCH behavior still need Arda-owned reconciliation.

## Scope dependencies awaiting Nurefşan

Accept the limited foundation as a Sprint 3 delivery slice and confirm the first real feature scope and priorities. Product fields/status/permissions, enrollment dates/timezone/capacity/prerequisites and academic grading/publication rules remain unresolved where their existing sources say Pending/Open.

Preserve approved JWT `sid`/server revocation, Registration→Student/CourseOffering, unique pair, Grade→Registration, separate authorized Instructor GET, and inactive Student login with registration rejection. This PR implements none of those product flows or resolves their remaining policy details.

## Documentation Updated

`README.md` plus `docs/sprint3/Candidate_Foundation.md`, `File_Inventory.md`, `Test_Report.md`, `First_PR_Issue_Mapping.md`, `Next_Development_Sequence.md` and this PR draft. The existing four planning proposals remain unchanged outside the repository.

Exact changed paths are in `docs/sprint3/File_Inventory.md`. Generated dependencies/build output, local logs/caches and coverage reports are not PR source files.

## Screenshots (if applicable)

No screenshot attached. No interactive browser acceptance or accessibility-conformance claim. Local technical validation does not establish a deployed working-system URL.

## Suggested independent reviewers

- **Arda (`ardaberkkara1`):** architecture, versions, health/API/proxy boundaries.
- **Barış (`baryyss-001`):** workflow, wrapper/cache/artifact behavior and optional infrastructure.
- **Ahmet (`ahmetserdar41`):** test value, full denominator, gates, regressions and evidence.

No review request has been sent. Substitute a qualified non-author when a suggested reviewer authors or last-pushes the PR. Existing rules require at least one approval for develop, two for main, last-push approval, dismissed stale approvals and resolved threads; merge commits only.

## Known technical limitations

- Docker is unavailable locally; PostgreSQL compose/image/volume behavior is untested. No DB driver, migrations, fixtures or integration suite exists.
- Local JDK 21.0.1 has a native-agent Unicode-path issue; the verifier uses existing ASCII aliases for cache/temp/coverage data without moving the active repository or disabling coverage.
- Mockito emits non-failing dynamic-agent warnings on this JDK.
- Linux and GitHub Actions runner/cache/artifact behavior are unverified. actionlint is static validation.
- No deployment, full security validation, performance/recovery measurement, usability sessions or MVP acceptance is claimed.
- This branch has 41 staged files (39 additions and 2 modifications) and remains uncommitted, with no remote changes. Arda's architecture decision, Nurefşan's scope decision and Mert's further publication authorizations are still required.

## Reviewer Checklist

- [ ] Arda has approved the technical decisions with actual dated evidence.
- [ ] Nurefşan has accepted the scoped foundation and recorded remaining product gates.
- [ ] Scope and Issue linkage match the proposed S3-02/S3-03 slice.
- [ ] Backend/frontend tests, separate denominators and legacy-tool distinction reviewed.
- [ ] README/ignore reconciliation and preservation of all legacy documents/release refs reviewed.
- [ ] Optional DB examples accepted or explicitly removed before final inventory/validation.
- [ ] Real PR checks and artifact downloads verified after authorized publication.
- [ ] Secret, whitespace, exact-file and index checks reviewed.
- [ ] Blocking comments resolved and required independent approvals cover the latest push.

## Definition of Done

Local preparation is staged and reviewable; integration acceptance is pending. Mert authorized staging/review and these documentation corrections. Commit still needs separate authorization; pushing, Issue/PR creation and merging each need applicable separate approval. No direct main/develop commit, force push, Sprint 2 tag change, settings change or release action is part of this PR preparation.

After authorized merge, Mert coordinates actual Issue/Project/evidence updates. A successful local scaffold build does not mark the whole Sprint 3 plan, MVP or submission complete.
