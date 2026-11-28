# Sprint 3 foundation — technical validation report

Original local validation: 25 November 2026, Europe/Istanbul. Review update: 28 November 2026. Related Issues: [#53 — S3-02 scaffold/test harness](https://github.com/mert494/student-information-system/issues/53) and [#54 — S3-03 CI/coverage](https://github.com/mert494/student-information-system/issues/54). Architecture/product acceptance remains pending.

[Draft PR #69](https://github.com/mert494/student-information-system/pull/69) was published from commit `11d6291a8c7b134d0f15e8ebf28a33c563b522ac` on 27 November 2026. The reviewed baseline is now `a9f4014c939635773778b8fbb6586e1b94b59c1e`; Arda's follow-up changes only the backend test dependencies to Spring Boot management. This local DevOps correction preserves that change. Architecture/product acceptance and independent review remain pending.

[SIS foundation CI run #1](https://github.com/mert494/student-information-system/actions/runs/46047276557) completed successfully for the original `11d6291a8c7b134d0f15e8ebf28a33c563b522ac` revision. GitHub reports Backend unit, Frontend unit and CI result successful, including both diagnostic-upload steps. This is historical hosted evidence, not a run of the newer baseline or this local patch. Artifact contents/downloads and deliberate hosted failure cases remain unverified.

## Historical pre-publication state

Base: `5aca26068e2b640f96041f630463d82b73041a4e` (remote develop). Local branch: `feature/sprint3-mvp-ci-foundation`. At that checkpoint the local state was **41 files staged: 39 additions and 2 modifications**, with no candidate commits or remote changes; architecture and scope approvals remain pending. See [File_Inventory.md](File_Inventory.md). The build/test results below were obtained from the earlier unstaged preparation snapshot. The earlier pre-publication documentation correction changed status wording and report-link presentation; builds were not rerun at that checkpoint. Fresh checks for this DevOps correction are recorded separately below.

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

**Historical preparation snapshot (before staging):** Static integration checks were **PASS (exit 0)** — tracked/untracked whitespace, 41-path inventory and secret-pattern scan, document links/tables, preserved legacy files/release refs, unchanged original inputs and an empty staged diff were verified locally at that checkpoint. The empty staged diff describes the earlier preparation state, not the published PR or this unstaged correction. These historical checks are not GitHub CI or a rerun during documentation correction.

These are separate result categories. The 24 checker tests and seven coverage-tool tests are not application unit coverage. The existing checker suite may create/remove its own temporary Git fixtures; it made no project-repository commit.

## Measured denominator

Backend JaCoCo analyzes all four handwritten production classes. Covered lines are **9/13 = 69.23%**; the four uncovered application entry/bean-configuration lines remain included. No package/class exclusion was added. JaCoCo's normal compiler-generated-record filtering applies.

Frontend V8 explicitly includes authored `src/**/*.{ts,tsx}`, including its uncovered bootstrap. Covered lines are **28/31 = 90.32%**. Only tests/setup/declarations are excluded; no authored production module is excluded.

Unit test inputs exercise process uptime, fresh runtime reads/controller delegation, validated/invalid health payloads, HTTP/network errors and UI loading/success/failure/retry/cancellation/timeout. These are useful scaffold tests, not FR-01–FR-07 tests. There is no combined backend/frontend percentage or integration/E2E coverage claim.

The gate-tool tests demonstrate exactly-50% pass and rejection of below-threshold, missing/empty reports, zero executed tests, reported failures and impossible/malformed counts. Their synthetic fixtures cannot write CI summaries. Native JaCoCo/Vitest unmet-threshold demonstrations from the original foundation remain prior evidence; this integration run used the configured 50% thresholds.

## Windows troubleshooting (historical environment)

The earlier machine used Oracle JDK 21.0.1 with Java 25 on PATH. Its native-agent options could not preserve `ş` in the user's path. Select JDK 21 explicitly; the verifier uses existing ASCII short-path aliases for Maven cache, temp files and JaCoCo data. It does not move files, map drives or change system settings. If no suitable alias exists, prepare a new isolated ASCII-path checkout or resolve the local JDK path issue. Never move/reset another person's worktree or disable coverage to hide the failure. The old JDK patch should be replaced with a supported JDK 21 patch in a shared environment; this review changes no installed runtime.

Historical Windows invocation:

~~~powershell
.\scripts\verify-local.ps1 -JavaHome 'C:\Program Files\Java\jdk-21'
~~~

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

Generated reports/logs/caches are deliberately excluded from PR source. They are paths as code rather than published Markdown links to excluded files. The original hosted run is linked above. Tested merge-SHA capture and artifact downloads/content checks remain pending; preserve actual artifacts as revision-specific evidence.

## Preservation and integration boundary

Only previously tracked README and .gitignore are intended to change. Original project/course text and ignore rules remain; every other original path, including Sprint 1/2 documentation, API, checker code/tests, templates, contributions and manifest, must match its base fingerprint. Existing history is retained by the full clone.

The Sprint 2 annotated tag object is `b974dea655e3b1e92e0840fd96cc32b3974661bd` and resolves to `409049b69f25596968ae2ba678abd2afbfdd798e`. At the original preparation checkpoint no files were staged. Mert subsequently authorized staging/review of the 41 files and these documentation corrections. No release mutation, tag move, main/develop change, candidate project commit or remote change had occurred at that historical checkpoint. Later publication is recorded above; this DevOps review makes local changes only.

New attributes apply only to Sprint 3 paths. Thirty-one imported files had Git-reported extra blank EOF lines removed in the new copy; originals were not edited and no application logic or dependency changed. Core Git may warn that LF will become CRLF under the local Windows policy; those warnings are not whitespace-test failures.

## Limits and blockers

- **Approval:** Arda's stack/architecture and Nurefşan's scope decisions remain pending. The candidate is not ready to merge without them and independent review.
- **GitHub:** the original hosted run and upload steps passed. Artifact contents/downloads, deliberate hosted failure cases and checks for this local patch remain unverified. Local actionlint is static validation.
- **Platform:** tests ran on Windows with Java 21.0.1, Node 24.13.1, npm 11.8.0 and Python 3.13.14. Linux commands are prepared but not executed. Mockito's dynamic-agent warnings are non-failing.
- **Database:** Docker command unavailable; compose config/startup/PostgreSQL image/volume behavior untested. No DB driver/schema/migrations/fixtures/integration profile exists.
- **Product:** process health/proxy checks do not establish a working SIS MVP, authentication/authorization, academic behavior, deployment, security/NFR acceptance or usability/accessibility conformance.
- **Actions next:** this review authorizes local corrections only. Further staging, commit, push, PR edits/review requests, merge/settings/release actions require applicable separate Mert authorization. See [candidate decisions](Candidate_Foundation.md) and [next development sequence](Next_Development_Sequence.md).

## Additional DevOps assessment (28 November 2026)

These are review recommendations, not implemented changes or owner approvals. Keep the existing independent component gates and fail-closed report checks. Related work remains within #53/#54; no new Issue is created.

| Item | Benefit | Compatibility risk / validation needed | Recommendation for PR #69 |
| --- | --- | --- | --- |
| Single-source coverage thresholds | A shared policy can prevent the Maven `0.50`, Vitest `50` and Python checker default `50.0` from drifting. | Native tools use different units and configuration phases. A shared loader must reject absent/invalid policy, preserve each component's denominator and retain native plus report checks; cross-tool pass/fail cases are needed. | Defer implementation to a focused #54 change. The values already agree; this correction changes no thresholds or gates. |
| Python version pinning | Explicit setup makes checker-runtime selection reproducible across hosted-image updates. [GitHub's Python guidance](https://docs.github.com/en/actions/tutorials/build-and-test-code/python) supports selecting an interpreter with setup-python. | A new SHA-pinned setup action must be maintained in all three jobs. Choose a supported version only after checker tests pass on it; the historical environment and this review use different Python minors. Exact patch pinning also needs a security-update policy. | Defer to #54 after Arda's tooling review. Existing standard-library checks can be validated locally without changing the workflow's Python selection. |
| PostgreSQL image digest pinning | A reviewed digest prevents a mutable `postgres:18.7` tag from changing the selected image. [Docker's pinning guidance](https://docs.docker.com/build/building/best-practices/#pin-base-image-versions) explains this reproducibility benefit. | Verify the real registry digest, multi-platform support, PostgreSQL 18 volume behavior and startup/health. A digest freezes automatic image fixes and needs an update process. Docker execution is unavailable here. | Defer with the optional database candidate until architecture approval and real container validation; do not invent a digest in this patch. |
| Mockito dynamic-agent warning | Explicit instrumentation, if required, can avoid self-attachment warnings and prepare for stricter JVM behavior. [Mockito's Java 21+ guidance](https://github.com/mockito/mockito/blob/main/mockito-core/src/main/java/org/mockito/Mockito.java) documents agent setup. | The candidate explicitly uses `mock-maker-subclass`; first identify why an agent is loaded. A Surefire agent change must preserve JaCoCo's late `argLine`, work with Windows paths and use Boot-managed Mockito. Suppressing the warning alone does not validate compatibility. | Defer to #53. Preserve Arda's managed dependency change; verify actual tests and coverage before deciding whether instrumentation is needed. |
| Artifact upload behavior | `if: always()` attempts to retain available diagnostics after failures; distinct component/run/attempt names and 30-day retention aid investigation. | `if-no-files-found: warn` does not prove an artifact exists; `always()` cannot guarantee upload after hard termination/cancellation or before checkout. Changing to `error` can add a secondary failure when a build produces nothing. [Upload-artifact behavior](https://github.com/actions/upload-artifact) documents missing/hidden-file handling. | Keep current behavior in this correction. Defer changes to #54 until real passing/failing artifact downloads and contents are checked; validators and the aggregate job remain responsible for build/report failure. |

The concurrency correction follows [GitHub's concurrency semantics](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#concurrency): a shared group can replace an older pending run even when cancellation of running work is disabled. PR runs therefore share their PR ref and allow cancellation, while push groups include `github.run_id`. This preserves both running and pending branch-push runs. It does not promise execution ordering. Hosted cancellation behavior for this patch still needs a separately authorized updated PR run.

## Executed DevOps correction validation (28 November 2026)

These checks were executed for the local corrections on detached baseline `a9f4014c939635773778b8fbb6586e1b94b59c1e`. They are separate from the 25 November preparation results and original hosted run. The `11d6291..a9f4014` comparison confirmed one commit changing only `backend/pom.xml`: Arda removed the explicit JUnit 5 override and selected `spring-boot-starter-test`. This patch changes only the POM's Issue description; dependencies, properties and plugin configuration are preserved.

Environment: Windows, Oracle JDK 21.0.1, Node 24.13.1, npm 11.8.0, bundled Python 3.12.14. Existing dependency caches were copied into the isolated checkout; prior reports/results were not copied. A local-only `python.cmd` selects the bundled interpreter because the Windows Store alias is unavailable in the sandbox. The existing verifier was run without changing its build commands or bypassing coverage. Surefire's actual test classpath contains Boot-managed JUnit Jupiter 6.1.3 and Mockito 5.24.0; the former JUnit 5 results above remain historical.

| Executed check | Result |
| --- | --- |
| `scripts/verify-local.ps1 -JavaHome 'C:\Program Files\Java\jdk-21'` | PASS, exit 0; selects the existing ASCII aliases for agent/cache/temp paths. |
| Maven Wrapper `clean verify` through that verifier | PASS; 4 tests, 0 failures/errors/skips; executable package; JaCoCo line gate met. |
| Backend report validator | PASS; 9/13 executable lines = 69.2308%, 4 executed tests, minimum 50%. |
| `npm ci --no-fund --no-audit` | PASS; 88 packages; lockfile unchanged. |
| `npm run build` | PASS; TypeScript and Vite production build. |
| `npm run test:coverage` and frontend report validator | PASS; 13 tests; 28/31 lines = 90.3226%, minimum 50%. |
| `python -B -m unittest discover -s scripts/tests -v` | PASS; 7 coverage-tool safety tests, outside application metrics. |
| `python -X utf8 -B -m unittest discover -s tests -p test_sprint2_submission.py -v` | PASS; 24 existing checker tests, outside application metrics. Temporary test Git fixtures do not create a project commit. |
| `actionlint -shellcheck= -pyflakes= .github/workflows/ci.yml` | PASS with actionlint 1.7.12. ShellCheck/Pyflakes integrations disabled because unavailable. |

Mockito self-attachment/dynamic-agent warnings were observed again; they did not fail the tests or prevent JaCoCo reporting. No agent flags or mock-maker setting were changed. No new Docker, Linux-local, startup/proxy smoke, hosted workflow or artifact-download test is claimed. The earlier smoke and hosted results remain historical evidence.

On Windows, the executable bit is delivered as a Git mode-only hunk (`100644` → `100755`) in the local review patch. A separate verification index is used to check application of the complete patch and inspect `backend/mvnw` at `100755` with its original blob; the checkout's normal index remains at the baseline, with nothing staged. After separately authorized staging, the normal index must also show `100755`; a shell `chmod` in CI is not a substitute for the Git mode correction.

The local review directory outside the candidate contains the complete patch, exact changed-path inventory, patch/content fingerprints, remote provenance observations and static/preservation check results. Generated logs/reports and the verification index are local evidence only and must not be included in the PR.

Static/preservation checks passed: 66 local Markdown links (including anchors), 11 tables, seven concurrency grouping scenarios, full patch application/whitespace checks and `git diff --check`. The nine external documentation/evidence destinations were resolved through official sources or the GitHub connector; the two loopback runtime links were not requested because no fresh runtime smoke was performed. All 86 tracked paths outside the content-change inventory retained their baseline blobs; the wrapper is among these because only its mode changes in the patch. Sprint 1/2 files, OpenAPI, application/test sources, lockfile and all dependency/plugin configuration are unchanged. The original dirty checkout's saved file hashes, index, refs, branch and status also match. PR #68 and all remote resources remain untouched by this review.
