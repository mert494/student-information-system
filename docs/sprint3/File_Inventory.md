# Exact first-PR file inventory

Status: original Draft PR #69 foundation inventory; architecture and product-scope approvals pending. Related Issues: [#53 — S3-02 scaffold/test harness](https://github.com/mert494/student-information-system/issues/53) and [#54 — S3-03 CI/coverage](https://github.com/mert494/student-information-system/issues/54). Base develop: `5aca26068e2b640f96041f630463d82b73041a4e`.

**41 original publication paths: 39 additions and 2 modifications.** All 39 original foundation candidates are represented; two integration-planning documents were added. The table preserves the original preparation index classification relative to develop; it is not the unstaged DevOps correction inventory. [Draft PR #69](https://github.com/mert494/student-information-system/pull/69) was published from commit `11d6291a8c7b134d0f15e8ebf28a33c563b522ac` on 27 November 2026. The reviewed baseline is now `a9f4014c939635773778b8fbb6586e1b94b59c1e`; Arda's follow-up changes only the backend test dependencies to Spring Boot management. This local DevOps correction preserves that change. Architecture/product acceptance and independent review remain pending.

| Staged status relative to base | Exact path |
| --- | --- |
| A (staged addition) | [.env.example](../../.env.example) |
| A (staged addition) | [.gitattributes](../../.gitattributes) |
| A (staged addition) | [.github/workflows/ci.yml](../../.github/workflows/ci.yml) |
| M (staged modification) | [.gitignore](../../.gitignore) |
| M (staged modification) | [README.md](../../README.md) |
| A (staged addition) | [backend/.mvn/wrapper/maven-wrapper.properties](../../backend/.mvn/wrapper/maven-wrapper.properties) |
| A (staged addition) | [backend/mvnw](../../backend/mvnw) |
| A (staged addition) | [backend/mvnw.cmd](../../backend/mvnw.cmd) |
| A (staged addition) | [backend/pom.xml](../../backend/pom.xml) |
| A (staged addition) | [backend/src/main/java/com/example/sis/SisFoundationApplication.java](../../backend/src/main/java/com/example/sis/SisFoundationApplication.java) |
| A (staged addition) | [backend/src/main/java/com/example/sis/health/HealthController.java](../../backend/src/main/java/com/example/sis/health/HealthController.java) |
| A (staged addition) | [backend/src/main/java/com/example/sis/health/HealthResponse.java](../../backend/src/main/java/com/example/sis/health/HealthResponse.java) |
| A (staged addition) | [backend/src/main/java/com/example/sis/health/HealthService.java](../../backend/src/main/java/com/example/sis/health/HealthService.java) |
| A (staged addition) | [backend/src/main/resources/application.properties](../../backend/src/main/resources/application.properties) |
| A (staged addition) | [backend/src/test/java/com/example/sis/health/HealthControllerTest.java](../../backend/src/test/java/com/example/sis/health/HealthControllerTest.java) |
| A (staged addition) | [backend/src/test/java/com/example/sis/health/HealthServiceTest.java](../../backend/src/test/java/com/example/sis/health/HealthServiceTest.java) |
| A (staged addition) | [backend/src/test/resources/mockito-extensions/org.mockito.plugins.MockMaker](../../backend/src/test/resources/mockito-extensions/org.mockito.plugins.MockMaker) |
| A (staged addition) | [compose.yaml](../../compose.yaml) |
| A (staged addition) | [docs/sprint3/Candidate_Foundation.md](../../docs/sprint3/Candidate_Foundation.md) |
| A (staged addition) | [docs/sprint3/File_Inventory.md](../../docs/sprint3/File_Inventory.md) |
| A (staged addition) | [docs/sprint3/First_PR_Issue_Mapping.md](../../docs/sprint3/First_PR_Issue_Mapping.md) |
| A (staged addition) | [docs/sprint3/Next_Development_Sequence.md](../../docs/sprint3/Next_Development_Sequence.md) |
| A (staged addition) | [docs/sprint3/Proposed_Initial_PR.md](../../docs/sprint3/Proposed_Initial_PR.md) |
| A (staged addition) | [docs/sprint3/Test_Report.md](../../docs/sprint3/Test_Report.md) |
| A (staged addition) | [frontend/.env.example](../../frontend/.env.example) |
| A (staged addition) | [frontend/index.html](../../frontend/index.html) |
| A (staged addition) | [frontend/package-lock.json](../../frontend/package-lock.json) |
| A (staged addition) | [frontend/package.json](../../frontend/package.json) |
| A (staged addition) | [frontend/src/App.test.tsx](../../frontend/src/App.test.tsx) |
| A (staged addition) | [frontend/src/App.tsx](../../frontend/src/App.tsx) |
| A (staged addition) | [frontend/src/api/health.test.ts](../../frontend/src/api/health.test.ts) |
| A (staged addition) | [frontend/src/api/health.ts](../../frontend/src/api/health.ts) |
| A (staged addition) | [frontend/src/main.tsx](../../frontend/src/main.tsx) |
| A (staged addition) | [frontend/src/styles.css](../../frontend/src/styles.css) |
| A (staged addition) | [frontend/src/test/setup.ts](../../frontend/src/test/setup.ts) |
| A (staged addition) | [frontend/tsconfig.json](../../frontend/tsconfig.json) |
| A (staged addition) | [frontend/vite.config.ts](../../frontend/vite.config.ts) |
| A (staged addition) | [frontend/vitest.config.ts](../../frontend/vitest.config.ts) |
| A (staged addition) | [scripts/tests/test_verify_coverage.py](../../scripts/tests/test_verify_coverage.py) |
| A (staged addition) | [scripts/verify-local.ps1](../../scripts/verify-local.ps1) |
| A (staged addition) | [scripts/verify_coverage.py](../../scripts/verify_coverage.py) |

## Reconciliation and source provenance

- Modified tracked paths are only `README.md` and `.gitignore`; their original identity/rules remain.
- `.gitattributes` is new and scoped to Sprint 3 paths; `.github/workflows/ci.yml` adds separate legacy checker regression execution.
- Thirty-one new imports had only Git-reported extra EOF blank lines removed. Application behavior, pinned dependencies and expected test outcomes remain the validated foundation.
- Four copied Sprint 3 documents were refreshed for this integration; `First_PR_Issue_Mapping.md` and `Next_Development_Sequence.md` are new.
- Existing `AGENTS.md`, API, Sprint 1/2 documents, checker/tests, templates, contributions, license and release history are unchanged.

## Excluded generated/local-only material

`_local/`, dependency caches/tools, `backend/target/`, `frontend/node_modules/`, `dist/`, `coverage/`, `reports/`, logs and Python cache files are excluded. No real `.env` was created. The two `.env.example` files contain explicit dummy/public configuration only.

The separate local `../evidence` directory contains the exact pathspec, SHA-256 inventory, original-input fingerprints, full candidate patch and authorization instructions. It is outside the clone and is not PR source.

## Approval classification

- Arda reviews all technical stack/package/health/proxy/testing choices; Barış reviews workflow/wrapper/optional infrastructure; Ahmet reviews tests and coverage.
- Nurefşan accepts the limited foundation scope and owns future product decisions. No current file implements unresolved grading, enrollment or authentication behavior.
- Optional `compose.yaml` and root `.env.example` remain unverified; reviewers may defer them before refreshing the final inventory.
- The original staging/publication authorizations are historical. This review permits local corrections only; further staging, commits, pushes, PR edits and merge require applicable separate authorization and required owner decisions; Arda and Nurefşan have not approved the pending decisions.
