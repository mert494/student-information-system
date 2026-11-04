# Azra — Agile Process Coach execution package

Status: Proposal for team approval. Read the [main guide](00_Team_Overview.md) and [RACI](../../RACI_Matrix.md). Related work: S1-06, S1-10, S1-12, S1-14, S1-16.

## A. Purpose of the role

Make team responsibilities and actual process events traceable; prevent meeting, decision, impediment and improvement-action records from being lost. You share the same official role as Mert; the proposed division between you awaits approval.

## B. Sprint 1 responsibilities

1. Clarify the division of work with Mert and RACI assignments with the team.
2. Review the existing RACI; maintain Markdown/CSV parity after approval.
3. Record Sprint Planning, Role Assignment, attendance and decisions using actual information.
4. Track stand-ups, impediments and actions with Mert; keep process records current.
5. Use existing Review/Retrospective sections; add results and improvement actions after meetings occur.

## C. Step-by-step implementation

1. Use Git/a Markdown editor and follow the [shared workflow](00_Team_Overview.md). Read current RACI and process records; do not duplicate them with new Meeting Minutes/RACI templates.
2. Present the proposal to the team: Mert handles board/Issues/planning/workflow/submission; Azra handles RACI/Meeting Minutes/retrospective/report. Record actual approvers, date and scope in the existing Decision Log; leave it proposed if not approved.
3. Check the six members' official roles, implementation responsibilities and one A per row with the team. Being R in the RACI is not evidence of completed contributions. Reconcile changed rows with Mert and the relevant owner.
4. If RACI Markdown changes, update the CSV with the same IDs, tasks and member columns. Verify UTF-8/comma import and Turkish characters; in Excel use Data → From Text/CSV if needed. Do not generate unnecessary XLSX files.
5. Before planning, record date, agenda, participants and goals as “planned”. Once held, fill in attendance, capacity, selected S1 tasks, owners and dependency decisions. Do not fabricate outcomes or attendance if no meeting occurred.
6. For stand-ups, record person, previous progress, next Issue and impediment. For impediments, include owner, impact, opening date, next action and actual closure evidence; reconcile GitHub status with Mert.
7. In the Review, record presented output/commit, acceptance status, feedback and carried-over work. In the Retrospective, record positives, problems, causes and measurable improvement actions. Do not treat template existence as a meeting held.
8. In Action Items, link each action to an owner, date, status and evidence. Unknown information remains `[TODO]`; do not copy personal messages or unnecessary personal data.
9. Check Markdown tables, CSV parity and actual links. Present the diff to Mert/the team; proceed with separate commit/push/PR approvals.

## D. Files to update

| File / format / location | Sections | Requirement status | Completion criterion |
| --- | --- | --- | --- |
| `docs/RACI_Matrix.md` — existing Markdown | Six members/roles, R/A/C/I explanation, task matrix, draft/approval status | Roles/RACI required | One A per task; actual approval recorded or explicitly pending |
| `docs/RACI_Matrix.csv` — existing CSV | ID, task and six member columns | User-requested import equivalent; not a separate course format requirement | Identical to Markdown; Turkish characters preserved |
| `docs/Sprint1_Process_Records.md` — existing Markdown | Goal, Planning, Minutes, Attendance, Stand-up, Progress, Impediments, Decisions, Review, Retrospective, Actions | Process role evidence expected; use the existing single record | Actual/planned distinction, owner/date/evidence clear; no fabricated meetings |

## E. Prompt to paste into Codex

```text
I am Azra, a Scrum Master and Agile Process Coach on the BM321 SIS team.
Inspect README, applicable AGENTS.md files, git status/branch, docs/RACI_Matrix.md
and .csv, docs/Sprint1_Process_Records.md, Git_Workflow, the Projects guide and
docs/team-guides/sprint1/04_Azra_Agile_Process.md.
Use existing RACI and process records; do not create duplicate documents.
Do not treat the division with Mert as final. Check RACI for all six people, one A
per task and consistency between files; submit changes for relevant owners' approval.
Record only actual meeting/attendance/decision information supplied by me.
Distinguish planned from actual events; unknown information remains [TODO].
Use Planning, Role Assignment, stand-up, impediment, decision, review, retrospective
and action sections in the existing file. Include owner/date/evidence fields for each
actual action. Check CSV/Markdown parity and links; do not create unnecessary XLSX/PDF.
Do not delete others' files or modify their uncommitted work. Clarify working boundaries
with Mert in shared files; do not change another person's content without permission.
Show local diff and gaps. Wait for branch/commit approval; obtain separate explicit
approval for push, PR and merge. If develop is missing, ask for the target; do not
force push or commit directly to main/develop.
```

## F. GitHub workflow

Example branch: `docs/azra-sprint1-process-records`; example commit: `docs(process): update RACI and verified sprint records`. State changed RACI rows, actual record sources and remaining TODOs in the PR. Proposed reviewer: Mert; also consult people whose RACI assignments change. Follow the [shared approval sequence](00_Team_Overview.md). Contribute through your own account; do not present Mert's initial preparation as your own completed contribution.

## G. Collaboration

Mert: planning, board and impediment escalation; everyone: actual attendance/responsibility approval; Nurefşan: Review acceptance/feedback; Arda/Barış: technical decision records; Ahmet: record consistency. Use section sharing or sequential PRs rather than editing the shared process file concurrently with Mert.

## H. Submission checklist

- [ ] Proposed/approved status of the Mert–Azra division explicit.
- [ ] RACI and CSV match; six members and one-A rule consistent.
- [ ] Actual meeting/attendance/decision evidence entered; events not held identified.
- [ ] Impediments and actions have owners, dates and statuses.
- [ ] Review/Retrospective templates reused without duplication.
- [ ] Independent review and your own Issue/PR/commit contribution links available.
