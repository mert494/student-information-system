# Mert QA corrections — Sprint 1

Snapshot: **3 November 2026 (Europe/Istanbul)**. Related QA Issue: [#3](https://github.com/mert494/student-information-system/issues/3). Dedicated Mert correction Issue: [TODO]. Scope: Mert's Sprint 1 documentation and coordination preparation only. Existing corrections b7e8655 and 226d2e8 are committed and pushed; the follow-up changes described here remain local, unstaged and uncommitted. No Issue, Project, review, PR, setting, branch, tag or release was changed remotely in this follow-up.

## Source report and latest evidence

After `git fetch --all --prune`, Ahmet's latest branch is `origin/docs/ahmet-sprint1-quality@8fac0cfa2b89b6deeb51e36a629be58c27cee952`, available through open [PR #2](https://github.com/mert494/student-information-system/pull/2), not main. Read the complete [quality report at that tip](https://github.com/mert494/student-information-system/blob/8fac0cfa2b89b6deeb51e36a629be58c27cee952/docs/Sprint1_Quality_Report.md), [action list](https://github.com/mert494/student-information-system/blob/8fac0cfa2b89b6deeb51e36a629be58c27cee952/docs/Sprint1_Action_Items.md) and [new prompt proposals](https://github.com/mert494/student-information-system/blob/8fac0cfa2b89b6deeb51e36a629be58c27cee952/docs/Sprint1_Codex_Prompts.md). The report itself last changed at 84f8c87; 8fac0cf adds prompts and an action-list link, without changing findings. The prompts are proposals, not team decisions or user authorization. Do not infer develop, approved security choices or corrected user names from their examples.

The report has **26 checks (11 Passed, 11 Failed, 4 Pending)** and **22 original findings**. Priorities below are Ahmet's original values; F-02 has no priority. PR #2's description still contains older counts and must be updated by Ahmet. The task guide 03_Ahmet_QA.md is not a completed QA report.

All eight remote refs were inspected: main@7072b41, docs/sprint1-process@78febb9, docs/sprint1-team-guides@79e3d40, docs/ahmet-sprint1-quality@8fac0cf, docs/arda-sprint1-architecture@e522c95, docs/baris-sprint1-repository@81a66a9, docs/nurefsan-sprint1-requirements@1184b26 and docs/mert-qa-corrections@226d2e8. No develop or approved integration base was found. Main contains only the initial README, LICENSE and .gitignore. The latest Mert-approved documentation base is 226d2e8; this is not a team-approved integrated submission.

Read-only GitHub GETs verified two open Issues (#3 assigned to ahmetserdar41; #5 to baryyss-001), six open PRs (#1/#2/#4/#6/#7/#8), no merged PRs, and zero submitted reviews on all six. PR targets remain #1 to docs/sprint1-process; #2/#6/#7/#8 to docs/sprint1-team-guides; #4 to main. PR #7 is mergeable=false (dirty); #8 is individually mergeable=true, which does not resolve the cross-PR shared-file conflict. No PR exists for Mert's correction branch.

All eight live branch records report protected=false; rulesets=[]; detailed main protection returned 403, so individual settings and plan capability remain Unverified. Releases=[] and live Git tag enumeration is empty. Projects remains Unverified: gh is unavailable and the connector has no Projects read; the earlier web attempt also failed. No board absence or Done status is inferred.

A new live [commit metadata read](https://api.github.com/repos/mert494/student-information-system/commits/e522c959b93ae3b2f8108cc99812bf3c8bef536a) links e522c95 to ardaberkkara1 as author and committer. This verifies the current F-22 account association without changing history. It does not verify future local Git configuration.

## Ownership and all findings

The [RACI at 79e3d40](https://github.com/mert494/student-information-system/blob/79e3d407e304038f1eb159479059e1e79cf5e623/docs/RACI_Matrix.md) and Role Assignment/Decision Log remain approval-pending. Responsibility is provisional. Follow Mert's stated boundaries: A = independently correctable Mert documentation; B = Mert coordinates, but live approval, another owner or a team decision is required; C = another owner corrects. Barış owns administrative configuration, with Mert coordinating/authorizing any action requiring the repository owner's admin capability. Azra owns/co-owns factual records and RACI. This classification changes no RACI assignment.

| ID | Original priority | Category | Finding / affected file or resource | Primary owner; support | Required correction / verified evidence | Current state |
| --- | --- | --- | --- | --- | --- | --- |
| F-01 | P1 | C | Missing Boundary/OpenAPI; docs/System_Vision_and_Boundary.md, api/openapi.yaml | Arda; Nurefşan shared requirements | Drafts exist at e522c95 and combined document at 243195e | Already resolved for existence; QA closed; content findings remain |
| F-02 | — | C | Incorrect access claim; QA report | Ahmet | QA withdrew the incorrect check | Already resolved (withdrawn) |
| F-03 | P1 | B | Missing develop/protection; repository settings | Barış configuration; Mert admin coordination, Arda base, team | Live flags/rulesets confirm gap; choose base and authorize settings before applying | Still open; blocked by team decision and authorization |
| F-04 | P2 | B | Missing deliverable/PB Issues; Issues/Projects | Mert tracking; owners approve scope | Only #3/#5 exist; complete English local drafts now prepared in Projects guide; create/link only after approval | Prepared but awaiting approval; live gap still open |
| F-05 | P2 | C | PB-07 empty state; Initial_Backlog_Draft.md | Nurefşan | Actual 26fc3f4 defines No published grades are available. | Already resolved; QA closed |
| F-06 | P2 | C | Vague PB-02/PB-05 responses; backlog/OpenAPI | Nurefşan; Arda, Ahmet | Current 1184b26 still says appropriate response; owners must agree measurable criteria | Partially resolved; still open |
| F-07 | P3 | A | Old heading count/commit status; Sprint1_Submission_Checklist.md | Mert; members supply evidence, Ahmet rechecks | Actual b7e8655/226d2e8 map all six headings and real contributions; this follow-up records later evidence | Already resolved in Mert's documents; independent QA recheck pending |
| F-08 | P3 | B | All proposed backlog owners were Arda; Initial_Backlog_Draft.md | Nurefşan content; Mert tracks | 26fc3f4 changes later-story owners to team determination; current draft retains proposed status | Already resolved as QA finding; actual assignments still need team decision |
| F-09 | P3 | C | RACI workload information; RACI_Matrix.md/.csv | Azra; team including Mert | Review workload during actual RACI approval | Blocked by team decision; informational finding |
| F-10 | P2 | C | Problem evidence absent; Project_Proposal.md | Nurefşan; Ahmet recheck | c7e9d79 adds preliminary OBS observations with explicit limitations | Partially resolved; QA recheck pending, no fabricated stakeholder validation |
| F-11 | P2 | C | Role names inconsistent; proposal/Vision/backlog/API | Nurefşan; Arda | Current Vision proposes roles but leaves mapping/permission approval open | Partially resolved; blocked by role/scope decisions |
| F-12 | P3 | C | Management need lacks backlog mapping; requirements | Nurefşan | Owner selects story or scope exclusion | Still open; no product edit by Mert |
| F-13 | P3 | C | License rationale/decision; Project_Proposal.md | Nurefşan; Arda | 1184b26 adds suitability rationale; team decision still pending | Partially resolved; QA recheck and decision pending |
| F-14 | P2 | B | Requirements Issue/backlog integration; PR #7 | Nurefşan content/conflict; Mert tracking | Target is corrected; live mergeable=false; source owner must reconcile and approve Issue scope | Partially resolved; blocked by owner/team decision and live authorization |
| F-15 | P2 | B | Overlapping target/scope; PR #4 and #1 | Azra for her PR; Mert integration coordination | Both share 79e3d40; #4 still targets main; agree treatment before retargeting/closure | Still open; blocked by team decision and authorization |
| F-16 | P3 | C | Missing benefit clauses PB-05/06/07; backlog | Nurefşan | Actual source stories still omit so that benefit | Still open; copied faithfully as draft input, not silently repaired |
| F-17 | P3 | C | Stale Issue/PR/access entries; Repository_Setup.md | Barış; Mert supplies evidence | 81a66a9 still has TODO despite #5/#6 and prior permission evidence | Still open; owner update required |
| F-18 | P2 | C | Security/server/license gaps; api/openapi.yaml | Arda; Nurefşan policy, Ahmet validation | e522c95 unchanged; no API/security policy adopted by Mert | Still open |
| F-19 | P3 | C | Examples/tags/data fields; api/openapi.yaml | Arda; Nurefşan | Technical source unchanged; resolve owner decisions and validate | Still open |
| F-20 | P1 | C | Competing Vision/Boundary; PR #7/#8 | Nurefşan shared document; Arda technical/#8 scope | Combined source exists at 243195e, but #8 still adds old shared file | Partially resolved; owner integration required |
| F-21 | P2 | C | External context/permissions; Vision/Boundary | Arda technical; Nurefşan scope | Current combined file leaves decisions TODO; do not invent absence of integrations as a decision | Partially resolved; owner/team decisions required |
| F-22 | P2 | C | Commit identity association; e522c95 | Arda; Ahmet recheck | Live API now associates author and committer with ardaberkkara1 | Already resolved for account association; QA report still stale |

No new severity or original finding was invented. QA-12 (RACI approval) is Azra-led with Mert coordination; QA-21 (release/tag) is Barış-led with Mert support. Submitted review of PR #2/#6, missing correction PR, real sprint facts, board verification and final submission evidence are additional pending coordination tasks, not fabricated F IDs.

## Corrections and prepared actions

Prior published corrections remain intact. This follow-up updates only existing Mert coordination documents:

- [Projects setup](../GitHub_Projects_Setup.md): seven coordination/deliverable Issue descriptions plus seven separate PB drafts copied from Nurefşan's source, including all required fields. Values needing approval remain proposed/[TODO]. Actual Issue #3/#5 retained; no duplicate created. Projects remains Unverified, with a manual verification checklist.
- [Git workflow](../Git_Workflow.md): concrete PR title/body/base candidate and overlap/review gates. Barış's settings ownership and team-approved base requirement retained. No merge order is treated as approved.
- [Submission checklist](../Sprint1_Submission_Checklist.md): latest Ahmet evidence, published 226d2e8, live PR #7 conflict and corrected F-22 association; explicit completion states and outstanding decisions.
- [Overview](../team-guides/sprint1/00_Team_Overview.md) and [Mert guide](../team-guides/sprint1/06_Mert_Scrum_Master_Summary.md): published correction tip/source refreshed without changing assignments or claiming review/merge.
- This existing report: refreshed complete classification; no duplicate audit report created.

The proposed PR base is docs/sprint1-team-guides@79e3d40, pending explicit team/user confirmation. The existing published branch's delta is six Mert documentation files; it preserves Azra's base changes. PR #1 itself includes Azra's process record change as well as Mert's guides; PR #4 overlaps the same head. Neither should be automatically merged/closed. Prepared body and exact paths are in Git_Workflow.md. Any later local commits must be approved and pushed before the PR represents them.

Current duties completed locally: factual documentation correction, Issue-description preparation, PR-description preparation, ownership/dependency mapping and validation. Current duties not completed: live Issues/Projects, review requests/submissions, develop/settings, PR creation/retarget/closure/merge, actual records/approvals, release/tag and course submission. All require actual owner facts or explicit authorization. Missing course date/time zone/team number/channel remain Unverified/[TODO]; Ahmet's reported 5 November deadline is not independently confirmed.

## Preservation and validation

Work remains on the existing isolated docs/mert-qa-corrections worktree at 226d2e8. No new branch, reset, stash or merge was used. The original 12 modified files and untracked translation report, and the separate general-audit drafts, are protected. No Category C file, RACI assignment, PO backlog, API, source, test, template or infrastructure configuration was modified. Edited files are English; inherited untranslated owner documents remain a separate owner-coordination item, not a completed repository translation.

Executed checks passed for all six changed files: 10 Markdown tables, 42 relative links, 37 pinned Git file/commit links, balanced fences, English prose and targeted secret/conflict scans. All 22 original finding IDs and priorities match the finding section of Ahmet's report; all 16 S1 owner assignments and inherited RACI MD/CSV parity/A-R rules are preserved. Each of 14 local Issue drafts has the requested fields, and all seven PB source sections are retained verbatim at the pinned PO revision. The exact six-file scope and git diff --check passed. SHA-256 comparison of 77 files across the original, general-audit and current worktrees found changes only in these six authorized documents; all other files remain unchanged. The diff was reviewed; staging remains empty. No application/API tests or independent GitHub review were performed by this follow-up. Ahmet retains QA finding closure ownership; document preparation is not live-action completion.
