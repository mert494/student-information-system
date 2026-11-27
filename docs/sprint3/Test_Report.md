# Integration candidate — local validation report

Date: 25 November 2026, Europe/Istanbul. Status: local scaffold evidence; **no remote GitHub Actions run** and no architecture/product approval. Related Issue: [TODO].

Base: `5aca26068e2b640f96041f630463d82b73041a4e` (remote develop). Local branch: `feature/sprint3-mvp-ci-foundation`. The current local state is **41 files staged: 39 additions and 2 modifications**, with no candidate commits or remote changes; architecture and scope approvals remain pending. See [File_Inventory.md](File_Inventory.md). The build/test results below were obtained from the earlier unstaged preparation snapshot. These documentation-only corrections change current-state wording and report-link presentation, not application/configuration/test content; unrelated builds were not rerun.

## Historical integration validation (before staging)

| Check / actual command | Exit | Actual result |
| --- | --- | --- |
| `.\scripts\verify-local.ps1 -JavaHome 'C:\Program Files\Java\jdk-21'` | 0 | Complete documented Windows verifier succeeded in the new clone. |
| Maven Wrapper `clean verify` through that verifier | 0 | BUILD SUCCESS; 4 backend tests, 0 failures/errors/skips; executable JAR; JaCoCo report and ≥50% line check passed. Maven reported 40.124 seconds on this run. |
| `npm ci --no-fund --no-audit` | 0 | Locked clean installation; 88 packages installed. No dependency/lockfile update. |
| `npm run build` | 0 | TypeScript check and Vite production bundle completed. |
| `npm run test:coverage` | 0 | 2 files / 13 tests passed; independent frontend ≥50% line gate passed. |
| Backend report validator | 0 | 4 executed tests; 9 covered / 13 executable lines = **69.2308%**. |
| Frontend report validator | 0 | 13 executed tests; 28 covered / 31 executable lines = **90.3226%**. |
| `python -B -m unittest discover -s scripts/tests -v` | 0 | Seven gate-tool safety tests passed; 0 failures/errors. |
| `python -X utf8 -B -m unittest discover -s tests -p test_sprint2_submission.py -v` | 0 | Existing 24 submission-checker tests passed; 0 failures/errors/skips; 7.575 seconds. |
| actionlint 1.7.12, `-shellcheck= -pyflakes= .github/workflows/ci.yml` | 0 | Updated workflow YAML/syntax/type checks passed. Unavailable ShellCheck/Pyflakes integrations were disabled. |
| Local packaged runtime/proxy smoke | 0 | Backend health JSON, frontend HTML, real Vite /api/health proxy and absent-product-route checks passed. Owned test processes stopped. |

**Historical preparation snapshot (before staging):** Static integration checks were **PASS (exit 0)** — tracked/untracked whitespace, 41-path inventory and secret-pattern scan, document links/tables, preserved legacy files/release refs, unchanged original inputs and an empty staged diff were verified locally at that checkpoint. The empty staged diff describes the earlier preparation state, not the current 41 staged files. These historical checks are not GitHub CI or a rerun during documentation correction.

These are separate result categories. The 24 checker tests and seven coverage-tool tests are not application unit coverage. The existing checker suite may create/remove its own temporary Git fixtures; it made no project-repository commit.

## Measured denominator

Backend JaCoCo analyzes all four handwritten production classes. Covered lines are **9/13 = 69.23%**; the four uncovered application entry/bean-configuration lines remain included. No package/class exclusion was added. JaCoCo's normal compiler-generated-record filtering applies.

Frontend V8 explicitly includes authored `src/**/*.{ts,tsx}`, including its uncovered bootstrap. Covered lines are **28/31 = 90.32%**. Only tests/setup/declarations are excluded; no authored production module is excluded.

Unit test inputs exercise process uptime, fresh runtime reads/controller delegation, validated/invalid health payloads, HTTP/network errors and UI loading/success/failure/retry/cancellation/timeout. These are useful scaffold tests, not FR-01–FR-07 tests. There is no combined backend/frontend percentage or integration/E2E coverage claim.

The gate-tool tests demonstrate exactly-50% pass and rejection of below-threshold, missing/empty reports, zero executed tests, reported failures and impossible/malformed counts. Their synthetic fixtures cannot write CI summaries. Native JaCoCo/Vitest unmet-threshold demonstrations from the original foundation remain prior evidence; this integration run used the configured 50% thresholds.

## Actual command details and local evidence

The Windows verifier invokes the imported scripts without changing versions. It selects JDK 21 explicitly, generates an ignored Maven settings file, uses existing ASCII aliases for cache/temp/agent data and restores process environment. This avoids the previously reproduced JDK 21.0.1 Unicode native-agent option failure.

Exact expanded Maven command on this run:

~~~powershell
.\mvnw.cmd --settings '../_local/maven-settings.xml' -B -ntp '-Dstyle.color=never' '-Dunit.coverage.data-file=C:\Users\MERTAL~1\STUDEN~4\repo/backend/target/jacoco-unit.exec' clean verify
~~~

The alias above is evidence for this machine only; use the verifier to discover the appropriate alias rather than hardcoding it elsewhere.

Report locations after verification:

- Backend: `backend/target/site/jacoco/index.html`, `jacoco.xml`, `jacoco.csv`; JUnit XML under `backend/target/surefire-reports`.
- Frontend: `frontend/coverage/unit/index.html`, `coverage-summary.json`, `lcov.info`; `frontend/reports/unit-junit.xml`.
- Logs: `_local/logs/integration-verify-local.log`, `backend-local-verifier.log`, `npm-ci.log`, `frontend-local-build.log`, `frontend-local-tests.log`, `coverage-tool-tests.log`, `backend-coverage-gate.log`, `frontend-coverage-gate.log`, `sprint2-checker-tests.log` and `actionlint.log`.
- Smoke JSON: `_local/smoke-results.json`. Actual ports 61209/61210; observed health `{"status":"UP","service":"sis-foundation","uptimeSeconds":3}`; both servers stopped.
- Local-only review evidence outside the clone: `../evidence` contains baseline/input fingerprints, exact paths/hashes, full candidate patch, static validation and next-authorization instructions.

Generated reports/logs/caches are deliberately excluded from PR source. They are paths as code rather than published Markdown links to excluded files. Future GitHub run/tested merge SHA/artifact links remain [TODO]. Preserve/download actual CI artifacts once an authorized run exists.

## Preservation and integration boundary

Only previously tracked README and .gitignore are intended to change. Original project/course text and ignore rules remain; every other original path, including Sprint 1/2 documentation, API, checker code/tests, templates, contributions and manifest, must match its base fingerprint. Existing history is retained by the full clone.

The Sprint 2 annotated tag object is `b974dea655e3b1e92e0840fd96cc32b3974661bd` and resolves to `409049b69f25596968ae2ba678abd2afbfdd798e`. At the original preparation checkpoint no files were staged. Mert subsequently authorized staging/review of the 41 files and these documentation corrections. No release mutation, tag move, main/develop change, candidate project commit or remote change has occurred.

New attributes apply only to Sprint 3 paths. Thirty-one imported files had Git-reported extra blank EOF lines removed in the new copy; originals were not edited and no application logic or dependency changed. Core Git may warn that LF will become CRLF under the local Windows policy; those warnings are not whitespace-test failures.

## Limits and blockers

- **Approval:** Arda's stack/architecture and Nurefşan's scope decisions remain pending. The candidate is not ready to merge without them and independent review.
- **GitHub:** no workflow/Ubuntu runner/cache/artifact upload execution occurred. Local actionlint and command success are not remote CI evidence; actual run links are [TODO].
- **Platform:** tests ran on Windows with Java 21.0.1, Node 24.13.1, npm 11.8.0 and Python 3.13.14. Linux commands are prepared but not executed. Mockito's dynamic-agent warnings are non-failing.
- **Database:** Docker command unavailable; compose config/startup/PostgreSQL image/volume behavior untested. No DB driver/schema/migrations/fixtures/integration profile exists.
- **Product:** process health/proxy checks do not establish a working SIS MVP, authentication/authorization, academic behavior, deployment, security/NFR acceptance or usability/accessibility conformance.
- **Actions next:** staging/review of the 41 files and documentation corrections are authorized; commit, push, remote Issue/PR and merge/settings/release still require applicable separate Mert authorization. See [candidate decisions](Candidate_Foundation.md) and [next development sequence](Next_Development_Sequence.md).
