# Nurefşan — product and requirements execution package

Status: Proposal; not a product scope decision. Based on the [main guide](00_Team_Overview.md), [Product Backlog draft](../../Initial_Backlog_Draft.md) and [RACI](../../RACI_Matrix.md). Related work: S1-01, S1-02, S1-03, S1-04 collaboration, S1-09, S1-14.

## A. Purpose of the role

Explain which problem the SIS solves, for whom and within which boundaries; prioritize the team's stories and clarify acceptance conditions. Mert's example Product Backlog does not transfer requirements ownership away from you.

## B. Sprint 1 responsibilities

1. Write the Project Proposal and Problem Definition with supporting evidence; assess stakeholders, solution and feasibility.
2. Define System Vision, target users, core responsibilities and initial scope; work with Arda on Boundary.
3. Review open-source license selection with Arda/the team; keep the existing MIT file and selection rationale consistent.
4. Assess the example Product Backlog; clarify epic/feature/story, Acceptance Criteria, priorities, estimates and owners.
5. Communicate API needs to Arda; provide Mert with the approved Product Backlog and change information; assess Ahmet's findings.

Detailed SRS and non-functional/quality-measure specifications will be expanded in Sprint 2. Document necessary initial constraints in Sprint 1; do not claim a detailed SRS or implemented product.

## C. Step-by-step implementation

1. Use Git/a Markdown editor and follow the [shared workflow](00_Team_Overview.md). Look for equivalent proposal/vision/Product Backlog files; do not recreate the same document under another name. Verify your account and approved branch base.
2. In the problem definition, distinguish current situation, affected people, problem and impacts. If actual interviews/surveys/data exist, add dates and sources; otherwise label them “assumptions to validate”. Do not fabricate stakeholder interviews or statistics.
3. In a stakeholder table, assess candidates such as students, academic staff and student affairs/administration by need, influence, expectations and validation status. Do not automatically treat them as product roles.
4. Explain the solution and expected outcomes; evaluate technical, time/team and operational feasibility with Arda. Document initial scope, assumptions, risk/impact/mitigation and success measures; do not treat invented measurement targets as agreed.
5. Have the team review the existing MIT license; add selection rationale to the proposal. If needed, clarify the decision with an authorized course/team source; do not guarantee legal suitability or change LICENSE without permission.
6. In the shared Vision/Boundary file, write purpose, users, system responsibilities and core functions. Arda coordinates Boundary. Jointly reconcile in/out of scope, external systems and constraints/assumptions; leave undecided integrations `[TODO]`.
7. Approve/change/reject existing PB-01…PB-07 examples; do not accept them automatically. Make Epic → feature → story relationships visible. Give each story a stable ID, an “As a… I want… so that…” statement and measurable Acceptance Criteria.
8. Write Acceptance Criteria in Given/When/Then or testable conditions: positive, unauthorized/invalid-data and relevant boundary cases. Do not add unnecessary business rules; list open decisions such as grading scale, capacity, prerequisites and term.
9. State priority rationale; have the team estimate story points. Arda's Proposed Owner status in examples is not a confirmed assignment; determine actual implementers based on capacity. Add actual story/Issue links to Dependencies.
10. Update approved/draft status and date/decision record within the Product Backlog; keep the filename at this stage. Map requirement → API `operationId` with Arda and PB → actual GitHub Issue with Mert. Do not commit to feature implementation in Sprint 1.
11. Present the work to Ahmet for review. Resolve requirements contradictions; modify only your own files and agreed shared sections. Follow separate approval steps for diff review, commit, push and PR.

## D. Files to produce or update

| File / format / location | Required sections | Requirement status | Completion criterion |
| --- | --- | --- | --- |
| `docs/Project_Proposal.md` — new Markdown proposal | Problem/evidence, stakeholder analysis, solution/expected outcomes, feasibility/initial scope, assumptions/risks, license selection and rationale | Proposal content required | Sources/assumptions distinguished; all sections reviewed; approval/gaps visible |
| `docs/System_Vision_and_Boundary.md` — shared new Markdown proposal | Purpose/users, responsibilities/functions, context/external interactions, in/out of scope, constraints/assumptions | Vision/Boundary content required | Vision owned by Nurefşan, Boundary by Arda; consistent with proposal/API |
| `docs/Initial_Backlog_Draft.md` — existing Markdown | Epic/feature/story, ID, Acceptance Criteria, priority, team estimate, dependencies, owner, approval/traceability | Initial Product Backlog required | Examples evaluated; approved records explicit; actual assignments and open decisions distinguished |

File names are proposals; Markdown is the editable source format. Prepare PDF/Word separately only if the actual instructions require it.

## E. Prompt to paste into Codex

```text
I am Nurefşan, the BM321 SIS Product Owner and Requirements Engineer.
First inspect README, applicable AGENTS.md files, git status/branch, RACI, Git_Workflow,
Initial_Backlog_Draft, the submission checklist and
docs/team-guides/sprint1/05_Nurefsan_Requirements.md.
If equivalent documents do not exist, create docs/Project_Proposal.md and the Vision
sections of the shared docs/System_Vision_and_Boundary.md.
In the proposal, prepare content for problem/evidence, stakeholder analysis,
solution/outcomes, feasibility/scope, assumptions/risks and selection rationale for
the existing MIT license. Do not fabricate sources or actual stakeholder validation;
use [TODO] and label assumptions. Do not present scope/roles/business rules as approved.
Coordinate Boundary with Arda; do not produce completed OpenAPI on his behalf.
Improve existing docs/Initial_Backlog_Draft.md; do not create a second Product Backlog.
Add epic-feature-story, testable Acceptance Criteria, priority rationale, team estimates,
dependencies and proposed/approved owner distinction. Do not invent points/assignments/
approvals. Preserve PB IDs; clarify API/actual Issue mapping with Arda/Mert.
Separate detailed SRS into Sprint 2; do not assume a PDF/Word requirement.
Do not delete or modify others' files without permission; clarify shared-file boundaries.
Validate local changes and present diff/open decisions. Obtain separate approval for
branch/commit, push, PR and merge; do not push/merge automatically.
If develop is missing, ask for the target.
```

## F. GitHub workflow

Example branch: `docs/nurefsan-sprint1-requirements`; example commit: `docs(requirements): draft proposal vision and initial backlog`. Link actual Issues in the PR. Proposed reviewers: Arda (scope/technical feasibility), Ahmet (testability); Mert tracks progress. Reconcile Boundary changes in the shared file with Arda. Follow the [separate approval sequence](00_Team_Overview.md) and approved PR target.

## G. Collaboration

Arda: domain model, System Boundary, API needs; Ahmet: measurable criteria and quality findings; Mert: priority/sprint/board mapping; Azra: actual scope/priority decision record; Barış: license/repository and technical-environment assumptions. PO priority, team effort estimation and sprint capacity are distinct decisions.

## H. Submission checklist

- [ ] All proposal sections present; evidence and assumptions distinguished.
- [ ] License selection rationale and team review recorded.
- [ ] Vision/Boundary aligned with Arda; in/out of scope explicit.
- [ ] Product Backlog examples actually evaluated; feature relationships and Acceptance Criteria present.
- [ ] Priority, estimates, dependencies, owners and approval statuses clear.
- [ ] Requirement/API/Issue mapping and independent review/commit evidence recorded.
