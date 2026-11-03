# Mert — Scrum Master task summary and execution package

Status: Proposed division of work; read with the [RACI](../../RACI_Matrix.md) and [main guide](00_Team_Overview.md). Related work: S1-08, S1-10, S1-11, S1-13 support, S1-14, S1-16.

## A. Purpose of the role

Make team work visible and traceable; coordinate planning, dependencies, impediments and submission evidence. Track owners' progress rather than completing other roles' documents on their behalf.

## B. Sprint 1 responsibilities

1. Share guides with owners; track team approval of the Mert–Azra division, RACI and sprint goal.
2. Clarify `develop`, Git-Flow and access decisions with Barış; coordinate task Issue/PR links.
3. Transfer Nurefşan's approved Product Backlog into Projects; track priorities, owners, status, estimates and dependencies.
4. Facilitate planning/stand-ups and impediment resolution with Azra; preserve actual records.
5. Track closure of Ahmet's findings, individual contribution evidence and Barış's release/tag preparation; check final submission.

Ready items: Process 78febb9, guides 2987dc0 and Azra's 79e3d40 contribution were integrated into develop through PR #1 at 1f6c6ddca7bc1ced42db14ea527b8fa845397ac7, preserving individual commits. Ahmet, Barış and Arda approved that source. Corrections through c2d6d39 are published separately without a PR; the current six-file refresh is local only. Issues #9–#15 exist, are open and unassigned. These facts do not establish approved RACI, actual meetings, a live board or completed Sprint 1. See the [submission checklist](../../Sprint1_Submission_Checklist.md) for evidence.

## C. Step-by-step implementation

1. Check current status through the [shared workflow](00_Team_Overview.md). The old preparation-uncommitted statement was corrected in b7e8655. Keep actual Issue/PR/commit/review evidence current in the existing checklist; do not mark [TODO] fields complete in bulk.
2. Send everyone `00_Team_Overview.md` and their individual guide. These documents are sharing material; sending messages through Codex requires separate explicit authorization.
3. Agree on sprint goal, actual end date/time zone, capacity, RACI and Mert–Azra division with the team; record them in the Decision Log with Azra.
4. Use verified develop as the planned correction PR base; recheck its SHA before synchronization. Preserve correction history. Local merge-commit synchronization is pending clarification of the current no-commit/no-merge limit. Keep PR #4 open until Azra approves closure.
5. Reuse #3/#5 and #9–#15 in the [Projects guide](../../GitHub_Projects_Setup.md); do not duplicate them. Verify Projects separately. Obtain actual owner/priority/estimate decisions; PB Issues await Nurefşan and separate creation approval.
6. Nurefşan approves the product backlog; the team clarifies estimates. Proposed board statuses: Backlog → To Do → In Progress → In Review → Done. Keep impediments separately visible; check for incorrect Done transitions caused by early Issue closure.
7. Conduct regular progress/impediment checks; Azra records actual Meeting Minutes. Return QA findings to owners and obtain recheck evidence from Ahmet.
8. Map each member's Issue/commit/PR/review contributions from their own account in the checklist. With squash merges, preserve original commit/review traces through the PR; do not count assignment as contribution evidence.
9. Compare the final deliverables guide with the actual course instructions in Teams Files. Barış links release/tag to the approved submission commit. Record the final submission link and receipt evidence; perform only approved actions.

Tools: Git CLI, GitHub web/`gh` if available, Markdown editor and existing check tables. If remote status cannot be verified, state that explicitly; do not fill gaps with assumptions.

## D. Files to update

| File / format / location | Sections / scope | Requirement status | Completion criterion |
| --- | --- | --- | --- |
| `docs/GitHub_Projects_Setup.md` — existing Markdown | Board/Issue mapping, fields/statuses, acceptance and tracking rules | Board/Product Backlog tracking is a role responsibility; a guide alone is not implementation | Actual URLs/assignees/statuses verified or identified as gaps |
| `docs/Sprint1_Submission_Checklist.md` — existing Markdown | Deliverable statuses, accounts, Issue/PR/commit, release/tag, final links | Submission evidence required | Current, actual evidence; gaps explicit |
| `docs/Git_Workflow.md` — existing Markdown | Approved branch/review/merge decisions and remaining proposals | Git-Flow content required | Aligned with Barış/team decisions; applied-setting claims supported by evidence |
| `docs/Sprint1_Process_Records.md` — existing Markdown | Planning/progress/impediment contributions | Process role evidence | Section sharing with Azra; actual records and owners |

These nine guides provide work support; they do not replace the six required deliverables. Completing the initial 12-file package or these guides alone does not close Sprint 1.

## E. Prompt to paste into Codex

```text
I am Mert, a Scrum Master and Agile Process Coach on the BM321 SIS team.
First inspect git status/branch/log, README, applicable AGENTS.md files, process documents
under docs and docs/team-guides/sprint1/06_Mert_Scrum_Master_Summary.md.
Use existing RACI/Product Backlog/Meeting Minutes/submission files; do not duplicate records.
Verify evidence for prior process commit 78febb9 and prepare targeted updates to outdated
status statements. Distinguish completed documents from implemented processes/approvals.
Missing information remains [TODO]. Track owners/dependencies/evidence without completing
Arda's OpenAPI or Nurefşan's requirements on their behalf. The division with Azra is still
a proposal. Do not fabricate planning, impediments, decisions or meeting records.
Inspect Projects/Issues read-only if tools are available; state explicitly if inaccessible.
Do not create/change Issues/Projects/releases/settings or send messages without permission.
Prepare local files only; perform relevant checks and show the diff and pending decisions.
Wait for approval to create/switch branches or commit. Obtain separate explicit approval
for push, PR and merge. If develop is missing, ask for the target/base. Do not delete other
members' files or modify their uncommitted work; do not commit directly to main/develop
or force push.
```

## F. GitHub workflow

The original guides and Azra's process-record contribution were merged through PR #1. The separate correction head is c2d6d39; its planned PR base is develop at 1f6c6ddca7bc1ced42db14ea527b8fa845397ac7. Only the six Mert documents may change; no correction PR or local synchronization merge has been performed. PR #1 approvals do not cover new corrections. Proposed correction reviewers remain Azra and Ahmet, pending actual requests. Obtain separate commit, push, PR and merge approvals.

## G. Collaboration

Azra: records/RACI; Barış: access/workflow/release; Nurefşan: scope/priorities/Product Backlog; Arda: API/technical dependencies; Ahmet: quality/closure evidence. For submission impediments, clarify the relevant owner's action and target date; do not silently take over the task.

## H. Submission checklist

- [ ] Guides and proposed roles/responsibilities shared with the team; approval status recorded.
- [ ] Sprint goal, capacity and exact schedule established.
- [ ] Board/Issues and PR target verified; Product Backlog subject to PO approval.
- [ ] Actual process records and contribution links current.
- [ ] QA findings closed or reported as open submission risks.
- [ ] Release/tag and final submission links checked.
