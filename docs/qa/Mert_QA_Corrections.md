# Mert QA corrections

Status: Local corrections prepared for review; not committed, pushed, merged or submitted. Date: 3 November 2026 (Europe/Istanbul). Related QA tracking: [Issue #3](https://github.com/mert494/student-information-system/issues/3). Dedicated correction Issue: [TODO]; no remote resource was created.

## QA report and repository evidence

The source is Ahmet Serdar Erunsal's complete [Sprint1_Quality_Report.md](https://github.com/mert494/student-information-system/blob/84f8c871ae4eedcc009ed45b31ce6feafb6760ef/docs/Sprint1_Quality_Report.md), read using `git show origin/docs/ahmet-sprint1-quality:docs/Sprint1_Quality_Report.md`. The latest report commit is `84f8c871ae4eedcc009ed45b31ce6feafb6760ef` (3 November 2026). Its companion [Sprint1_Action_Items.md](https://github.com/mert494/student-information-system/blob/84f8c871ae4eedcc009ed45b31ce6feafb6760ef/docs/Sprint1_Action_Items.md) was also read. These are actual QA outputs; `docs/team-guides/sprint1/03_Ahmet_QA.md` is a task guide.

The report contains **26 checks: 11 Passed, 11 Failed, 4 Pending**, and **22 findings F-01–F-22**. Its priorities P1/P2/P3 are preserved below; they are not newly assigned severity levels. F-02 has no priority. The report remains an interim report awaiting independent review. PR #2's older description says 21 checks and nine findings; use the source file at the pinned commit. Some report risk paragraphs retain old PR #7 target information; current PR metadata takes precedence for present status.

`git remote -v`, `git status`, `git fetch origin --prune`, `git branch -a`, remote histories, file trees and Markdown content searches were inspected. The first sandboxed fetch could not write FETCH_HEAD; the authorized retry succeeded. Remote refs inspected:

| Remote branch | Fetched tip | Relevant content |
| --- | --- | --- |
| origin/main | 7072b41 | README, LICENSE and .gitignore only |
| origin/docs/sprint1-process | 78febb9 | Initial process documents/templates |
| origin/docs/sprint1-team-guides | 79e3d40 | Team guides and Azra's Role Assignment section |
| origin/docs/ahmet-sprint1-quality | 84f8c87 | QA report and action list; only completed QA-report candidate found |
| origin/docs/arda-sprint1-architecture | e522c95 | Boundary and OpenAPI drafts |
| origin/docs/baris-sprint1-repository | 81a66a9 | Repository setup evidence |
| origin/docs/nurefsan-sprint1-requirements | 1184b26 | Requirements and later proposal evidence/license updates |

GitHub CLI was unavailable locally. The GitHub connector inspected all six accessible PRs returned by the repository search. All were open and unmerged at inspection:

| PR | Head | Target | Observed condition |
| --- | --- | --- | --- |
| [#1](https://github.com/mert494/student-information-system/pull/1) | docs/sprint1-team-guides | docs/sprint1-process | mergeable=true; includes latest head 79e3d40 |
| [#2](https://github.com/mert494/student-information-system/pull/2) | docs/ahmet-sprint1-quality | docs/sprint1-team-guides | Draft; Mert requested as reviewer; report head 84f8c87 |
| [#4](https://github.com/mert494/student-information-system/pull/4) | docs/sprint1-team-guides | main | Same head as PR #1; integration decision pending |
| [#6](https://github.com/mert494/student-information-system/pull/6) | docs/baris-sprint1-repository | docs/sprint1-team-guides | mergeable=true; Mert/Arda requested as reviewers |
| [#7](https://github.com/mert494/student-information-system/pull/7) | docs/nurefsan-sprint1-requirements | docs/sprint1-team-guides | mergeable=false; current head 1184b26 |
| [#8](https://github.com/mert494/student-information-system/pull/8) | docs/arda-sprint1-architecture | docs/sprint1-team-guides | mergeable=true individually; competing Vision/Boundary remains |

Mergeability is not approval. No review was submitted, reviewer assigned, PR retargeted/closed or merge performed in this task. Current protection settings, full Issue inventory, Projects, tags and releases were not independently queried; relevant claims below are attributed to Ahmet's report rather than treated as newly verified settings.

## Responsibility classification

No approved RACI was found. The [RACI at 79e3d40](https://github.com/mert494/student-information-system/blob/79e3d407e304038f1eb159479059e1e79cf5e623/docs/RACI_Matrix.md) explicitly remains a draft; approval date/decision and Mert–Azra division are [TODO]. The table uses Ahmet's named owners, the existing draft and Mert's stated role scope. It does not approve assignments. Shared-owner ordering is an operational interpretation; final assignment approval is **Needs Team Decision**. RACI content and PO-owned backlog were not changed.

| Finding ID | Description | Original priority | Affected file / resource | Primary owner; support | Required correction | Current status |
| --- | --- | --- | --- | --- | --- | --- |
| F-01 | Boundary and OpenAPI were absent | P1 | docs/System_Vision_and_Boundary.md; api/openapi.yaml | Arda | Supply drafts | Closed by QA at e522c95; no change here |
| F-02 | Incorrect claim of missing write access | — | QA report / GitHub access | Ahmet | Withdraw incorrect finding | Withdrawn by QA; no change here |
| F-03 | develop and protection absent | P1 | GitHub branches/settings; docs/Git_Workflow.md | Mert as admin; Barış technical guidance/evidence | Approve base and settings, then apply and verify | Open; local action plan only |
| F-04 | Deliverable and PB Issues missing | P2 | GitHub Issues/Projects; docs/GitHub_Projects_Setup.md | Mert; Nurefşan scope approval, Azra planning support | Inventory, draft/map and create approved Issues | Open; local mapping plan only |
| F-05 | PB-07 empty-state criterion unclear | P2 | docs/Initial_Backlog_Draft.md | Nurefşan | Define concrete message | Closed by QA at 26fc3f4 |
| F-06 | PB-02/PB-05 response criteria unclear | P2 | docs/Initial_Backlog_Draft.md; api/openapi.yaml | Nurefşan; Arda | Agree measurable responses and contract mapping | Partially resolved per QA; untouched |
| F-07 | Checklist has old heading count and commit status | P3 | docs/Sprint1_Submission_Checklist.md | Mert; all members supply evidence | Map six headings, refresh status and actual links | Corrected and locally checked; Ahmet recheck pending |
| F-08 | All proposed backlog owners were Arda | P3 | docs/Initial_Backlog_Draft.md | Nurefşan; Mert | Clarify proposed assignments | Closed by QA at 26fc3f4; no reassignment here |
| F-09 | RACI workload imbalance information | P3 | docs/RACI_Matrix.md and .csv | Azra; team including Mert | Discuss workload during approval | Open informational item; Needs Team Decision |
| F-10 | Proposal lacks supporting problem evidence | P2 | docs/Project_Proposal.md | Nurefşan | Add genuine evidence | QA says new; c7e9d79 adds preliminary observations; Ahmet recheck pending |
| F-11 | Role names differ across documents | P2 | Proposal; Vision/Boundary; backlog; OpenAPI | Nurefşan; Arda | Agree and map roles consistently | Partially resolved; Needs Team Decision |
| F-12 | Management need has no backlog mapping | P3 | Proposal; Vision/Boundary; backlog | Nurefşan | Add approved story or scope exclusion | New per QA; untouched |
| F-13 | License rationale lacks project context | P3 | docs/Project_Proposal.md | Nurefşan; Arda | Add rationale and decision | QA says new; 1184b26 adds rationale; decision/recheck pending |
| F-14 | Requirements PR lacks Issue and conflicts on backlog | P2 | PR #7; docs/Initial_Backlog_Draft.md | Nurefşan for content/conflict; Mert for coordination/Issue mapping | Agree authoritative version, resolve with owner and link Issue | Partially resolved; target corrected, mergeable=false; Needs Team Decision |
| F-15 | PR #4 target/scope/description inconsistent | P2 | PR #4; process change description | Azra for PR description; Mert for integration coordination | Agree target/order; accurately describe actual change | Partially resolved per QA; #4 still targets main; Needs Team Decision |
| F-16 | Three stories lack benefit clause | P3 | docs/Initial_Backlog_Draft.md | Nurefşan | Add benefit to PB-05/PB-06/PB-07 | New per QA; untouched |
| F-17 | Setup evidence links/access table outdated | P3 | docs/Repository_Setup.md | Barış | Refresh #5/#6 and verified access entries | New per QA; untouched |
| F-18 | Security/server/license contract gaps | P2 | api/openapi.yaml | Arda | Resolve technical policy and validate contract | New per QA; untouched |
| F-19 | Contract examples/tags/data fields missing | P3 | api/openapi.yaml | Arda; Nurefşan data decisions | Add dummy examples and agreed fields | New per QA; untouched |
| F-20 | Competing Vision/Boundary files | P1 | PR #7/#8; docs/System_Vision_and_Boundary.md | Arda for #8 scope; Nurefşan shared content | Agree common document and reconcile PR scope | Partially resolved; combined file exists in #7; untouched |
| F-21 | Boundary external-system/permission decisions missing | P2 | docs/System_Vision_and_Boundary.md | Arda; Nurefşan roles/scope | Define context and approved permissions | Partially resolved; untouched |
| F-22 | Architecture commit uses different GitHub account | P2 | Commit e522c95; author account settings | Arda | Resolve own account/email association without rewriting history | New per QA; untouched |

Mert's primary open findings are F-03, F-04 and F-07. Mert supports F-14/F-15 and the already closed F-08. QA-12 (RACI approval) is Azra-led with Mert coordination; QA-21 (release/tag) is Barış-led with Mert support. Neither is an additional F finding.

## Files corrected and preservation

Only these two files belong to this correction:

- `docs/Sprint1_Submission_Checklist.md`: retained the checklist, contribution table and final-check structure, expressed the edited document in English, explained six Teams headings without removing license or Vision/Boundary requirements, replaced absent-file/uncommitted claims with pinned remote evidence, and populated observed account/Issue/PR/commit links. Review, team approvals, missing Issues, F-22, tags and submission remain pending. The reported deadline is attributed to Ahmet; course-source and time-zone confirmation remain [TODO].
- `docs/qa/Mert_QA_Corrections.md`: this English report records all findings, ownership, actual scope, validation and pending actions. It does not replace or modify Ahmet's report.

F-07 is locally corrected; this does not close the Sprint or certify acceptance. F-03/F-04/F-14/F-15 remain open because external operations or owner decisions have not occurred. The Projects setup and workflow drafts are not newly approved or rewritten by this task; use this dated report/checklist for the inspected evidence snapshot.

The original working tree had 12 modified tracked files (.github's three Issue templates and PR template; AGENTS.md; Projects setup, Git workflow, backlog, RACI Markdown/CSV, process records and submission checklist) and one untracked translation report. Their contents were left in place. Work uses a separate worktree and local `docs/mert-qa-corrections` branch from `origin/docs/sprint1-team-guides@79e3d40`. The original tree remains on `docs/sprint1-team-guides` at 2987dc0. No stash, reset, checkout over local work or remote merge was used. This review base contains Azra's latest process change but is not an approved integration/release base; main still contains only the initial files. Final PR target: [TODO], to be agreed before PR creation. The branch initially tracks origin/docs/sprint1-team-guides; a future push must explicitly name docs/mert-qa-corrections and requires approval.

The original English translation work was not staged or moved. This branch's checklist is English; inherited, untouched process documents and Ahmet's remote report still contain Turkish. A repository-wide English conversion is not claimed and must be integrated with the existing translation work separately.

## Remaining action items

1. **F-03 — Mert, supported by Barış:** obtain the team decision on the exact develop base SHA and workflow; separately authorize remote branch/settings operations. Apply PR-only changes and at least one independent approval on main/develop, verify actual plan/settings support, and record live evidence with Barış. Do not invent CI status checks or claim protection is enabled.
2. **F-04 — Mert:** inspect the complete current Issue/Project inventory before creating anything. Local mapping targets are the six headings below plus PB-01–PB-07. Use the existing documentation/feature templates with title, owner approval, acceptance criteria, source, priority and dependency/evidence fields. Preserve original PB IDs; they are not Issue numbers. New Issue/Project creation requires explicit approval. Suggested assignees remain proposals until confirmed.

| Local mapping target | Existing task IDs / owner proposals | Actual Issue / acceptance needed |
| --- | --- | --- |
| Project Proposal and Problem Definition, including license | S1-01/S1-02; Nurefşan, Arda license consultation | [TODO]; proposal content, real evidence, rationale and review |
| System Vision and Boundary | S1-03/S1-04; Nurefşan and Arda | [TODO]; one shared scope-consistent document |
| OpenAPI Draft | S1-05; Arda | [TODO]; agreed contract/version, validation and backlog mapping |
| Team Roles and RACI | S1-06; Azra, Mert support | [TODO]; six people, MD/CSV parity and recorded approval |
| GitHub Repository and Git-Flow | S1-07/S1-08; Barış and Mert | Existing DevOps [#5](https://github.com/mert494/student-information-system/issues/5); additional workflow mapping [TODO]; reuse relevant Issues, verify access/rules |
| Initial Product Backlog | S1-09; Nurefşan, Mert tracking | [TODO]; PO-approved content/priority and team estimates/owners |
| PB-01, PB-02, PB-03, PB-04, PB-05, PB-06, PB-07 | PO-owned stories; actual implementers [TODO] | Seven actual Issue URLs [TODO]; retain each approved story and criteria verbatim, with PO/team decisions; no implementation commitment inferred |

3. **F-14 — Nurefşan and Mert:** use the newer English requirements branch as a candidate, not an automatically approved replacement. Confirm the authoritative backlog with Nurefşan. The owner resolves the conflict on the requirements branch, preserves intended content and supplies an actual Issue link. Do not overwrite the original local translation or merge another person's PR here.
4. **F-15 — Azra and Mert:** agree how overlapping PR #1/#4 and a future develop branch are integrated. Azra updates her PR description to distinguish RACI checks from actual file changes. Retargeting or closing a PR and merging require separate approval; do not rewrite the existing commit message/history.
5. **Proposed integration order, Needs Team Decision:** settle base and overlapping process PRs first; coordinate PR #7/#8 so only one combined Vision/Boundary is integrated; resolve backlog conflicts with its owner; review technical/setup/requirements outputs; Ahmet rechecks fixes; then finalize QA integration and the approved release path. Ahmet's numbered merge order is a proposal, not permission. No merge performed.
6. **Azra/team:** approve RACI, workload and actual assignments; record only real decisions/meetings. **Ahmet:** recheck F-07 and later F-10/F-13 commits, refresh stale PR #2 summary/risk notes and retain independent QA closure evidence. **All members:** verify contribution accounts, missing Issue/review links and their own document language. **Barış/Mert:** verify tag/release on the final approved SHA. **Mert:** confirm Teams requirements, deadline/time zone, team number and receipt evidence before final submission.

## Validation results

Validation is limited to this documentation correction. Executed PowerShell checks passed for 2 documents, 6 Markdown tables, 9 relative links, 9 pinned GitHub blob links and referenced commit objects. The classification contains all 22 unique original finding IDs. All 16 inherited RACI rows match the CSV and satisfy one A and at least one R; ownership in the checklist remains consistent with these proposed assignments. SHA-256 comparison confirmed all 25 files in the original working-tree snapshot were unchanged. Git diff --check and the new report no-index whitespace check passed; conflict-marker and targeted secret scans were clean. Manual review confirmed English prose in both changed documents and no application/API/configuration edits. The initial Python check could not start because the Windows Python alias was unavailable; equivalent checks were executed successfully in PowerShell. No application or OpenAPI tests were run: neither application nor contract is changed, and Ahmet's reported validator results are cited as his evidence only. External Markdown links are pinned to inspected Git objects or observed PR/Issue references where possible; general website availability, Projects/protection settings and course-source correctness require separate checks.

Unresolved release risks: no approved RACI/integration target; external actions F-03/F-04 pending; shared-owner conflicts F-14/F-15/F-20; API/requirements findings; account F-22; English translation integration; final course confirmation, independent reviews, release and receipt evidence. No unresolved finding was marked resolved merely because this report exists.
