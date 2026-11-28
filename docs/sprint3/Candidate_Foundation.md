# Sprint 3 integration candidate

Status: **DRAFT PR #69 / APPROVALS PENDING**. Original preparation: 25 November 2026; DevOps review update: 28 November 2026. Related Issues: [#53 — S3-02 scaffold/test harness](https://github.com/mert494/student-information-system/issues/53) and [#54 — S3-03 CI/coverage](https://github.com/mert494/student-information-system/issues/54). Sprint deadline: 14 December 2026, 23:59 Europe/Istanbul.

## Current publication and review boundary

[Draft PR #69](https://github.com/mert494/student-information-system/pull/69) was published from commit `11d6291a8c7b134d0f15e8ebf28a33c563b522ac` on 27 November 2026. The reviewed baseline is now `a9f4014c939635773778b8fbb6586e1b94b59c1e`; Arda's follow-up changes only the backend test dependencies to Spring Boot management. This local DevOps correction preserves that change. Architecture/product acceptance and independent review remain pending.

[SIS foundation CI run #1](https://github.com/mert494/student-information-system/actions/runs/46047276557) completed successfully for the original `11d6291a8c7b134d0f15e8ebf28a33c563b522ac` revision. GitHub reports Backend unit, Frontend unit and CI result successful, including both diagnostic-upload steps. This is historical hosted evidence, not a run of the newer baseline or this local patch. Artifact contents/downloads and deliberate hosted failure cases remain unverified.

## Historical preparation boundary (25 November 2026)

This candidate is on local branch `feature/sprint3-mvp-ci-foundation` in a separate disposable clone, based on remote develop `5aca26068e2b640f96041f630463d82b73041a4e`. Remote main is `409049b69f25596968ae2ba678abd2afbfdd798e`; both bases contain the same 58 file blobs, with different history. Mert authorized creating this isolated local branch/import, staging and review of the 41 prepared files, and these documentation corrections. At that historical checkpoint the index had **41 staged changes: 39 additions and 2 modifications**. No candidate commits or remote changes had occurred at that checkpoint. Commit, push, Issue/PR creation, merge, settings and release actions still require applicable separate authorization.

Arda's stack/architecture approval and Nurefşan's scope approval remain absent. Local build success supplies technical evidence only. This is a process-health/connectivity scaffold; no FR-01–FR-07 capability or placeholder authentication/security is implemented.

The original dirty checkout, its Git refs/index/worktree registrations and its uncommitted files are protected by before/after fingerprints. All 39 foundation source candidates and the four planning proposals were inspected; their originals remain unchanged. Fetches and the branch creation occurred only in the new clone.

## Original reconciliation decisions (historical)

| Area | Exact candidate treatment |
| --- | --- |
| README | Preserve the existing project name and BM321 course identification; append repository navigation and candidate setup/status. No original repository identity is replaced. |
| .gitignore | Preserve every existing rule; append build output, dependencies, local evidence/config and Python-cache exclusions. Existing archive/JAR/crash-log exclusions stay intact. |
| .gitattributes | Limit new normalization rules to backend, frontend, scripts, docs/sprint3 and the new workflow. No repository-wide normalization or historical-document conversion. |
| Sprint 1/2 documents and API | Leave all existing paths unchanged, including SRS, backlog, architecture, NFR, contributions, OpenAPI, diagrams and submission manifest. Historical statements remain dated evidence; the new scaffold does not retrospectively approve or rewrite them. |
| Existing workflows/templates | No workflow existed at the base. Add the candidate workflow; preserve existing Issue and PR templates. |
| New source whitespace | Remove only extra blank EOF lines reported by Git on 31 newly imported files. No logic, dependencies or test expectations changed. The original foundation is unchanged. |
| Workflow integration | Retain backend/frontend builds, separate coverage and artifacts; add execution of the existing 24 Sprint 2 checker tests, explicitly outside application coverage. |
| Evidence links | Replace standalone-foundation links to excluded local logs with portable report paths as code and subsequently verified historical CI links in [Test_Report.md](Test_Report.md). No fake GitHub run or inaccessible log link is published as evidence. |
| Optional PostgreSQL | Retain compose/example files as unverified candidates. Backend has no DB driver, schema or readiness claim. Arda/Barış may omit these files from the eventual PR before approval. |
| Planning documents | Read all four local proposals without copying their entire draft backlog into this first PR. [Issue mapping](First_PR_Issue_Mapping.md) and [next sequence](Next_Development_Sequence.md) state exactly what remains. |
| Branch naming | Use Mert's requested branch name. It is a scoped exception to the draft Issue-number naming convention; no Issue number is invented. |

No previously tracked file is modified except README and .gitignore. The original 41-file publication comprised 39 additions and 2 modifications relative to that base. The earlier preparation checkpoint had an index identical to the base and untracked additions; that is a historical snapshot, not the current state. That statement described pre-publication preparation; see the current publication boundary above.

## Approval dependencies

| Owner | Review or decision required |
| --- | --- |
| Arda / `ardaberkkara1` | Java 21 / Spring Boot 4.2.0 / Maven, namespace, module boundaries, local health route, runtime config, frontend proxy and tooling; Spring Boot managed test dependencies retained from `a9f4014`; future Spring integration-test compatibility; future API/security/data contracts. |
| Nurefşan / `nsnkcc` | Accept this limited technical foundation in Sprint 3, confirm MVP priorities and first functional slice; approve product fields, permissions, enrollment and grading/publication behavior before implementation. |
| Barış / `baryyss-001` | Review workflow/cache/artifacts, local setup, optional database configuration and operational limits. No repository Settings change is included. |
| Ahmet / `ahmetserdar41` | Review test value, complete coverage denominator, failure propagation and local evidence; review implementation separately from formal acceptance. |
| Mert / `mert494` | Coordinate decisions/actual Issue linkage; the original foundation was published as Draft PR #69; this review authorizes local corrections only. Further Git/publication/merge actions need applicable separate authorization. Use the actual contributor's identity. |

Suggested independent PR reviewers: **Arda (architecture), Barış (CI), Ahmet (tests)**. No review was requested or approval recorded. Satisfy live rules even if a suggested reviewer is the author/latest pusher.

Active rules observed: develop needs one approval; main two. Both require PRs, stale-approval dismissal, last-push approval and resolved conversations, allow merge commits only, block deletion/force push and have empty bypass lists. Neither currently requires status checks. Select actual observed check contexts only after authorized CI execution and separate settings approval.

## Preserved product decisions

Future implementation must retain JWT `sid` with server-side session revocation on logout; Registration→Student/CourseOffering and CourseOffering→Course/Term; unique `(studentId, courseOfferingId)`; Grade→Registration; a separate authorized Instructor grade GET; and inactive Student login with backend registration rejection (409, no write). Grade multiplicity, exact GET route, security parameters and other open policies are not resolved here.

The provisional OpenAPI still needs token/session mapping, offering references, instructor retrieval, error/PATCH schemas and corrected published-grade examples. The local GET /health route is a technical candidate and is not added to or declared compliant with the shared product contract.

## Validation and limits

Use [Test_Report.md](Test_Report.md) for results from this integration checkout. Coverage percentages concern this tiny scaffold only. The 24 submission-checker tests and seven coverage-tool tests are reported separately from backend/frontend metrics.

Historical Windows troubleshooting and Mockito warnings are preserved in [Test_Report.md](Test_Report.md#windows-troubleshooting-historical-environment). Hosted Ubuntu execution succeeded for the original revision; artifact contents, hosted failure cases, Docker/PostgreSQL, shared hosting and formal MVP/NFR acceptance remain unverified. This correction selects no new dependency version.

Before the first real feature PR: approve relevant slices, reconcile Arda-owned OpenAPI, confirm provisioning and role/record security, attach real test/CI evidence and follow the [next sequence](Next_Development_Sequence.md). No mocked product endpoints or superficial security layer should be introduced to bridge missing decisions.
