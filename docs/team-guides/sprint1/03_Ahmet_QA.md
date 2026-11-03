# Ahmet — quality assurance execution package

Status: Proposal; not a record of performed tests or reviews. Consistent with the [main guide](00_Team_Overview.md) and [RACI](../../RACI_Matrix.md). Related work: S1-05 consultation, S1-09 Acceptance Criteria, S1-13 quality ownership, S1-14 contribution evidence.

## A. Purpose of the role

Independently review Sprint 1 documents for existence, content completeness, mutual consistency and verifiable evidence. Make unfinished work visible without making requirements or API decisions on behalf of the author.

## B. Sprint 1 responsibilities

1. Prepare check criteria for all six deliverable headings; mark missing files as “Pending”.
2. Review proposal and Vision/Boundary scope, evidence and mutual consistency.
3. Check Arda's OpenAPI YAML against the selected version/tool; record results.
4. Assess whether Product Backlog Acceptance Criteria are testable and review RACI/Git-Flow consistency.
5. Prepare a quality report, send findings to owners, support Mert in opening Issues and recheck fixes.

Sprint 3's target of at least 50% unit-test coverage is not a Sprint 1 acceptance condition. Without a working product, do not claim that unit/integration/E2E tests passed or coverage was achieved. A draft test strategy is optional preparation for later sprints.

## C. Step-by-step implementation

1. Inspect/update the repository through the [shared workflow](00_Team_Overview.md); do not switch branches until the working tree is clean and the base approved. Read the existing submission checklist and authors' files.
2. Create a check table: check ID, deliverable, file+commit, expected criterion, method, result, evidence, finding owner and recheck date. Results may be `Passed`, `Failed`, `Pending`, `Not applicable (with rationale)`.
3. In the proposal, look for problem/evidence, stakeholder analysis, proposed solution/benefit, feasibility/scope, assumptions/risks and license rationale. Do not accept unsourced survey/interview counts as actual evidence.
4. In Vision/Boundary, check purpose/target users, system responsibilities, external interactions, in/out of scope and constraints/assumptions. Report contradictions when work appears in the proposal/Product Backlog but is excluded by the boundary.
5. For OpenAPI, use Arda's selected version and validator. Review YAML parsing, references, types/required fields, path parameters, operation IDs, requests/responses and examples. Map relevant authorization/error scenarios to stories. Explicitly state that you validated only the contract, not a live API.
6. Identify unmeasurable Product Backlog wording such as “easy, fast, proper”. Check for positive/negative conditions, priority, team estimates, dependencies and proposed/approved owner distinction in each story. Suggest gaps to Nurefşan; do not rewrite criteria without permission.
7. In RACI, check all six people, one A per row, an R in every row and CSV consistency. In Git-Flow, compare branch target/review/merge rules and access/protection evidence against written rules.
8. Prepare local finding drafts using `.github/ISSUE_TEMPLATE/documentation.md` or the bug template for an actual product defect. Include priority, owner, reproduction/validation steps and evidence. Creating an actual Issue requires separate permission; do not invent numbers.
9. After a fix PR/commit arrives, rerun only affected checks and record closure evidence. Present the report to an independent reviewer; obtain separate commit/push/PR approvals.

Tools: Git diff, Markdown editor/preview, an existing CSV reader and the selected OpenAPI validator. If Redocly CLI is installed, `redocly lint api/openapi.yaml` is an example; verify file path and version. If unavailable, request installation permission and mark the check `Pending`. Use the [official Redocly command guide](https://redocly.com/docs/cli/commands/lint).

## D. Files to produce

| File / format / location | Required sections | Requirement status | Completion criterion |
| --- | --- | --- | --- |
| `docs/Sprint1_Quality_Report.md` — new Markdown proposal | Scope/source versions, method/tool, check matrix, OpenAPI results, findings, rechecks, open risks | Expected in this package as a QA role output; not an additional official course requirement beyond the six deliverables | Based on actual review; file/commit/result/evidence mapped and open gaps listed |
| `docs/Sprint1_Submission_Checklist.md` — existing Markdown | Targeted proposed update for Mert with quality results | Submission tracking required; do not create another checklist | Coordinated with Mert; not marked complete merely because files exist |

## E. Prompt to paste into Codex

```text
I am Ahmet, the BM321 SIS Quality Assurance and Test Automation Engineer.
First inspect README, applicable AGENTS.md files, git status/branch, all Sprint 1 files,
Issue/PR templates and docs/team-guides/sprint1/03_Ahmet_QA.md.
Use an existing QA report if present; otherwise create docs/Sprint1_Quality_Report.md.
Create a check matrix for proposal, Vision/Boundary, OpenAPI, RACI, Git-Flow and
Product Backlog. For every result include the checked file/commit, method, actual
result, evidence and finding owner. Do not mark nonexistent files or unrun tests Passed;
mark gaps [TODO]/Pending. Check OpenAPI with Arda's selected version and an installed
validator; do not install new dependencies without permission. Distinguish YAML validation
from live API testing. Check criterion measurability, scope consistency and RACI CSV parity.
Separate the 50% unit-test coverage target into Sprint 3; do not fabricate application
tests for Sprint 1. Report findings without modifying authors' documents without
permission; propose Issue drafts and do not create actual Issues without permission.
Do not delete or overwrite another team member's files. Prepare local changes only,
then present diff/checks/open decisions to the user. Obtain separate approval for
branch/commit, push, PR and merge; do not push/merge automatically. If develop is missing,
ask for the base/target; do not commit directly to main/develop or force push.
```

## F. GitHub workflow

Example branch: `docs/ahmet-sprint1-quality`; example commit: `docs(qa): record sprint 1 validation findings`. Link the actual quality Issue. Include validation command/tool version, checked commit and open findings in the PR. Proposed reviewer: Mert; consult Arda on technical findings and Nurefşan on requirements findings. Follow the [separate approval sequence](00_Team_Overview.md); the user clarifies the target branch.

## G. Collaboration

Nurefşan: problem evidence/scope/criteria; Arda: OpenAPI and technical findings; Barış: actual access/rules/PR evidence; Azra: RACI and process accuracy; Mert: Issue priority and submission impediments. Record authors' fixes and QA revalidation separately.

## H. Submission checklist

- [ ] All six deliverable headings covered in the check matrix.
- [ ] Actual file/commit and result evidence recorded; pending work explicit.
- [ ] OpenAPI contract checks distinguished from working-product tests.
- [ ] Product Backlog, RACI/CSV and workflow consistency reviewed.
- [ ] Finding owners and recheck results documented.
- [ ] Report independently reviewed; actual Issue/PR/commit links sent to Mert.
