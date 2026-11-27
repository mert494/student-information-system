# Sprint 3 integration candidate

Status: **LOCAL / 41 FILES STAGED / APPROVALS PENDING**. Prepared 25 November 2026 for Mert. Related GitHub Issue: [TODO]. Sprint deadline: 14 December 2026, 23:59 Europe/Istanbul.

## Base and authorization boundary

This candidate is on local branch `feature/sprint3-mvp-ci-foundation` in a separate disposable clone, based on remote develop `5aca26068e2b640f96041f630463d82b73041a4e`. Remote main is `409049b69f25596968ae2ba678abd2afbfdd798e`; both bases contain the same 58 file blobs, with different history. Mert authorized creating this isolated local branch/import, staging and review of the 41 prepared files, and these documentation corrections. The current index has **41 staged changes: 39 additions and 2 modifications**. No candidate commits or remote changes have occurred. Commit, push, Issue/PR creation, merge, settings and release actions still require applicable separate authorization.

Arda's stack/architecture approval and Nurefşan's scope approval remain absent. Local build success supplies technical evidence only. This is a process-health/connectivity scaffold; no FR-01–FR-07 capability or placeholder authentication/security is implemented.

The original dirty checkout, its Git refs/index/worktree registrations and its uncommitted files are protected by before/after fingerprints. All 39 foundation source candidates and the four planning proposals were inspected; their originals remain unchanged. Fetches and the branch creation occurred only in the new clone.

## Reconciliation decisions

| Area | Exact candidate treatment |
| --- | --- |
| README | Preserve the existing project name and BM321 course identification; append repository navigation and candidate setup/status. No original repository identity is replaced. |
| .gitignore | Preserve every existing rule; append build output, dependencies, local evidence/config and Python-cache exclusions. Existing archive/JAR/crash-log exclusions stay intact. |
| .gitattributes | Limit new normalization rules to backend, frontend, scripts, docs/sprint3 and the new workflow. No repository-wide normalization or historical-document conversion. |
| Sprint 1/2 documents and API | Leave all existing paths unchanged, including SRS, backlog, architecture, NFR, contributions, OpenAPI, diagrams and submission manifest. Historical statements remain dated evidence; the new scaffold does not retrospectively approve or rewrite them. |
| Existing workflows/templates | No workflow existed at the base. Add the candidate workflow; preserve existing Issue and PR templates. |
| New source whitespace | Remove only extra blank EOF lines reported by Git on 31 newly imported files. No logic, dependencies or test expectations changed. The original foundation is unchanged. |
| Workflow integration | Retain backend/frontend builds, separate coverage and artifacts; add execution of the existing 24 Sprint 2 checker tests, explicitly outside application coverage. |
| Evidence links | Replace standalone-foundation links to excluded local logs with portable report paths as code and [TODO] CI links. No fake GitHub run or inaccessible log link is published as evidence. |
| Optional PostgreSQL | Retain compose/example files as unverified candidates. Backend has no DB driver, schema or readiness claim. Arda/Barış may omit these files from the eventual PR before approval. |
| Planning documents | Read all four local proposals without copying their entire draft backlog into this first PR. [Issue mapping](First_PR_Issue_Mapping.md) and [next sequence](Next_Development_Sequence.md) state exactly what remains. |
| Branch naming | Use Mert's requested branch name. It is a scoped exception to the draft Issue-number naming convention; no Issue number is invented. |

No previously tracked file is modified except README and .gitignore. Relative to the base, the index contains only the authorized 41-file candidate: 39 staged additions and 2 staged modifications. The earlier preparation checkpoint had an index identical to the base and untracked additions; that is a historical snapshot, not the current state. No candidate commit or remote change exists.

## Approval dependencies

| Owner | Review or decision required |
| --- | --- |
| Arda / `ardaberkkara1` | Java 21 / Spring Boot 4.2.0 / Maven, namespace, module boundaries, local health route, runtime config, frontend proxy and tooling; explicit JUnit 5.14.4 override instead of Boot's default JUnit 6; future Spring integration-test compatibility; future API/security/data contracts. |
| Nurefşan / `nsnkcc` | Accept this limited technical foundation in Sprint 3, confirm MVP priorities and first functional slice; approve product fields, permissions, enrollment and grading/publication behavior before implementation. |
| Barış / `baryyss-001` | Review workflow/cache/artifacts, local setup, optional database configuration and operational limits. No repository Settings change is included. |
| Ahmet / `ahmetserdar41` | Review test value, complete coverage denominator, failure propagation and local evidence; review implementation separately from formal acceptance. |
| Mert / `mert494` | Coordinate decisions/actual Issue linkage; staging/review of these 41 files and documentation corrections are authorized. Commit, push, remote Issue/PR and merge still need applicable separate authorization. Use the actual contributor's identity. |

Suggested independent PR reviewers: **Arda (architecture), Barış (CI), Ahmet (tests)**. No review was requested or approval recorded. Satisfy live rules even if a suggested reviewer is the author/latest pusher.

Active rules observed: develop needs one approval; main two. Both require PRs, stale-approval dismissal, last-push approval and resolved conversations, allow merge commits only, block deletion/force push and have empty bypass lists. Neither currently requires status checks. Select actual observed check contexts only after authorized CI execution and separate settings approval.

## Preserved product decisions

Future implementation must retain JWT `sid` with server-side session revocation on logout; Registration→Student/CourseOffering and CourseOffering→Course/Term; unique `(studentId, courseOfferingId)`; Grade→Registration; a separate authorized Instructor grade GET; and inactive Student login with backend registration rejection (409, no write). Grade multiplicity, exact GET route, security parameters and other open policies are not resolved here.

The provisional OpenAPI still needs token/session mapping, offering references, instructor retrieval, error/PATCH schemas and corrected published-grade examples. The local GET /health route is a technical candidate and is not added to or declared compliant with the shared product contract.

## Validation and limits

Use [Test_Report.md](Test_Report.md) for results from this integration checkout. Coverage percentages concern this tiny scaffold only. The 24 submission-checker tests and seven coverage-tool tests are reported separately from backend/frontend metrics.

Known environment limits: Windows JDK 21.0.1 requires the documented existing ASCII alias for native-agent paths; the verifier keeps cache/temp/data within ignored local output and restores process environment. Mockito may emit non-failing dynamic-agent warnings. Docker/PostgreSQL, Linux execution, GitHub runner/cache/artifact behavior, shared hosting and formal MVP/NFR acceptance remain unverified. No new runtime/dependency version was selected during integration.

Before the first real feature PR: approve relevant slices, reconcile Arda-owned OpenAPI, confirm provisioning and role/record security, attach real test/CI evidence and follow the [next sequence](Next_Development_Sequence.md). No mocked product endpoints or superficial security layer should be introduced to bridge missing decisions.
