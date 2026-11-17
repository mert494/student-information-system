# Sprint 2 task breakdown and GitHub Issue drafts

Status: **Local proposal, 16 November 2026.** No Issues created, no assignees set, no task started or accepted by another member. Related GitHub Issue: [TODO]. Read the [plan](Sprint2_Plan.md) and [submission checklist](Sprint2_Submission_Checklist.md).

## Single task register

Local IDs are not Issue numbers. P0 = early decision/dependency blocker; P1 = mandatory deliverable or submission work. These priorities and all owners/windows are Proposed, subject to PO/team agreement. Estimates for every task: Pending team estimation; no story points or hours inferred. All statuses: Proposed / Not started. Dates use November 2026 and provisional Europe/Istanbul planning time.

| ID | Task | Proposed owner / support | Priority | Dependency | Proposed window |
| --- | --- | --- | --- | --- | --- |
| S2-01 | Confirm scope, capacity and responsibility decisions | Mert (coordination); team decides | P0 | None | 16–17 Nov |
| S2-02 | Define SRS scope, actors and business/data decisions | Nurefşan; Arda consults | P0 | S2-01 | 17–18 Nov |
| S2-03 | Draft detailed SRS requirement scenarios | Nurefşan | P1 | S2-02 | 18–19 Nov |
| S2-04 | Refine backlog and SRS traceability | Nurefşan; Mert tracks only | P1 | S2-03 | 19–21 Nov |
| S2-05 | Specify quality attributes and measurement scenarios | Ahmet (Proposed); Arda/Nurefşan consult | P1 | S2-02 | 18–20 Nov |
| S2-06 | Agree NFR metrics and verification plan | Ahmet (Proposed); Arda feasibility; PO accepts targets | P1 | S2-05 | 20–21 Nov |
| S2-07 | Plan user-flow coverage and Figma access | UX producer [TODO]; Nurefşan validates; Barış access support | P0 | S2-01, S2-02 | 17–19 Nov |
| S2-08 | Produce and review Figma prototypes and flow diagrams | UX producer [TODO]; Nurefşan product review | P1 | S2-07; S2-03 and S2-06 for final alignment | 19–21 Nov |
| S2-09 | Document architecture rationale and contract mapping | Arda | P1 | S2-02; S2-03 and S2-06 for final baseline | 18–21 Nov |
| S2-10 | Create C4 views and architecture consistency checks | Arda | P1 | S2-09 | 19–21 Nov |
| S2-11 | Create UML views for selected structure and interactions | Arda | P1 | S2-09; S2-08 for final UX consistency | 20–21 Nov |
| S2-12 | Record actual decisions, review outcomes and contribution evidence | Azra; Mert tracking support | P1 | S2-01; progressive inputs from S2-02…S2-11 | 16–23 Nov |
| S2-13 | Perform independent cross-deliverable QA and owner rechecks | Ahmet; independent reviewer for Ahmet's own work | P1 | S2-04, S2-06, S2-08, S2-10, S2-11 | 21–23 Nov |
| S2-14 | Prepare protected integration and Sprint 2 release evidence | Barış technical preparation; Mert coordination | P1 | S2-12, S2-13 | 23–24 Nov |
| S2-15 | Validate final package and submit through Teams | Mert; team supplies acceptance evidence | P1 | S2-14 | 24 Nov; target 21:00 |

## Copy-ready Issue drafts — do not publish yet

Each section is the same work item as its register row, not a second task. Actual Issue URL, branch, PR, commit, artifact and approval links: [TODO]. Convert dependency IDs to real Issue links only after authorized creation. Definition of Done for each draft: acceptance criteria checked against an actual version; independent reviewer evidence; unresolved decisions reported; no invented completion; integration only if separately authorized. No automatic closing phrases are supplied.

### S2-01

**Issue title:** [Sprint 2] Confirm scope, capacity and responsibility decisions

**Description:** Collect member availability and facilitate agreement on scope, UX owner, review pairs and milestone feasibility.

**Acceptance criteria:**

- [ ] Record actual owner responses and capacity; flag unanswered decisions Pending.
- [ ] Separate PO, technical and team decisions; link real confirmation or leave [TODO].
- [ ] Do not infer estimates or UX assignment from Sprint 1 roles.

**Proposed owner:** Mert (coordination); team decides. Assignment Pending member/team agreement.

**Priority:** P0 (Proposed). **Estimate:** Pending. **Window:** 16–17 Nov (Proposed).

**Dependencies:** None. Draft inputs may be developed in parallel; final acceptance waits for these dependencies.

**Evidence required:** Actual output version/path or Figma/source/export URL, validation results, independent review and decision links. All [TODO] until they exist.

### S2-02

**Issue title:** [Sprint 2] Define SRS scope, actors and business/data decisions

**Description:** Use PB-01–PB-07 and Boundary gaps as inputs to requirements elicitation, not approved implementation promises.

**Acceptance criteria:**

- [ ] Record actor/permission and scope decisions with owner/evidence; unresolved items explicit.
- [ ] Specify data fields, enrollment/grade/publication rules and external interactions for selected scope.
- [ ] List deferred/rejected scope and impacts on other deliverables.

**Proposed owner:** Nurefşan; Arda consults. Assignment Pending member/team agreement.

**Priority:** P0 (Proposed). **Estimate:** Pending. **Window:** 17–18 Nov (Proposed).

**Dependencies:** S2-01. Draft inputs may be developed in parallel; final acceptance waits for these dependencies.

**Evidence required:** Actual output version/path or Figma/source/export URL, validation results, independent review and decision links. All [TODO] until they exist.

### S2-03

**Issue title:** [Sprint 2] Draft detailed SRS requirement scenarios

**Description:** Write the detailed SRS for selected scope with stable IDs and reviewable scenarios.

**Acceptance criteria:**

- [ ] Each requirement has actor, preconditions, normal/alternate/error outcomes and acceptance criteria.
- [ ] Link rules/data assumptions and identify decision owner for open questions.
- [ ] Arda checks API feasibility; Ahmet checks positive/negative testability.

**Proposed owner:** Nurefşan. Assignment Pending member/team agreement.

**Priority:** P1 (Proposed). **Estimate:** Pending. **Window:** 18–19 Nov (Proposed).

**Dependencies:** S2-02. Draft inputs may be developed in parallel; final acceptance waits for these dependencies.

**Evidence required:** Actual output version/path or Figma/source/export URL, validation results, independent review and decision links. All [TODO] until they exist.

### S2-04

**Issue title:** [Sprint 2] Refine backlog and SRS traceability

**Description:** Refine one authoritative Sprint 2 backlog linked to SRS, preserving Sprint 1 history.

**Acceptance criteria:**

- [ ] Selected items include Epic/Feature/Story/Task, priority, estimate or Pending, dependencies and owner status.
- [ ] Every approved requirement maps to a backlog item; removed/deferred work has rationale.
- [ ] Actual PO approval and team estimation/assignment evidence are distinct from proposals.

**Proposed owner:** Nurefşan; Mert tracks only. Assignment Pending member/team agreement.

**Priority:** P1 (Proposed). **Estimate:** Pending. **Window:** 19–21 Nov (Proposed).

**Dependencies:** S2-03. Draft inputs may be developed in parallel; final acceptance waits for these dependencies.

**Evidence required:** Actual output version/path or Figma/source/export URL, validation results, independent review and decision links. All [TODO] until they exist.

### S2-05

**Issue title:** [Sprint 2] Specify quality attributes and measurement scenarios

**Description:** Propose relevant NFR categories and quality scenarios for the chosen scope.

**Acceptance criteria:**

- [ ] Each NFR has ID, context/stimulus, expected response and linked product requirement.
- [ ] For selected categories consider performance, security, usability/accessibility, reliability and maintainability; choice is owner-approved, not mandatory invented scope.
- [ ] Record stakeholder priority and unresolved targets without inventing numerical thresholds.

**Proposed owner:** Ahmet (Proposed); Arda/Nurefşan consult. Assignment Pending member/team agreement.

**Priority:** P1 (Proposed). **Estimate:** Pending. **Window:** 18–20 Nov (Proposed).

**Dependencies:** S2-02. Draft inputs may be developed in parallel; final acceptance waits for these dependencies.

**Evidence required:** Actual output version/path or Figma/source/export URL, validation results, independent review and decision links. All [TODO] until they exist.

### S2-06

**Issue title:** [Sprint 2] Agree NFR metrics and verification plan

**Description:** Specify how NFRs will be objectively measured without claiming tests on a nonexistent system.

**Acceptance criteria:**

- [ ] Every selected NFR includes metric/unit, target/status, workload/environment, method/tool and pass/fail criterion.
- [ ] Define evidence to collect and limitations; distinguish planned validation from actual results.
- [ ] Arda or another independent reviewer reviews Ahmet's output; target approval recorded or Pending.

**Proposed owner:** Ahmet (Proposed); Arda feasibility; PO accepts targets. Assignment Pending member/team agreement.

**Priority:** P1 (Proposed). **Estimate:** Pending. **Window:** 20–21 Nov (Proposed).

**Dependencies:** S2-05. Draft inputs may be developed in parallel; final acceptance waits for these dependencies.

**Evidence required:** Actual output version/path or Figma/source/export URL, validation results, independent review and decision links. All [TODO] until they exist.

### S2-07

**Issue title:** [Sprint 2] Plan user-flow coverage and Figma access

**Description:** Confirm producer and Figma workspace access, then define selected role-based flows.

**Acceptance criteria:**

- [ ] Record real Figma URL only after creation; reviewer access checked with intended audience.
- [ ] Map each selected flow to SRS/PB and role; include start/end and alternate/error routes.
- [ ] Proposed coverage: login, own enrollment, staff record maintenance and grade entry/viewing; PO confirms final set.

**Proposed owner:** UX producer [TODO]; Nurefşan validates; Barış access support. Assignment Pending member/team agreement.

**Priority:** P0 (Proposed). **Estimate:** Pending. **Window:** 17–19 Nov (Proposed).

**Dependencies:** S2-01, S2-02. Draft inputs may be developed in parallel; final acceptance waits for these dependencies.

**Evidence required:** Actual output version/path or Figma/source/export URL, validation results, independent review and decision links. All [TODO] until they exist.

### S2-08

**Issue title:** [Sprint 2] Produce and review Figma prototypes and flow diagrams

**Description:** The appointed owner builds clickable prototypes and readable user flows in Figma.

**Acceptance criteria:**

- [ ] Selected flows navigate end-to-end with success/error/empty states and consistent role permissions.
- [ ] Supply exact version/page/frame links, readable exports if agreed, and real review feedback.
- [ ] Do not label prototypes as implemented UI or production behavior.

**Proposed owner:** UX producer [TODO]; Nurefşan product review. Assignment Pending member/team agreement.

**Priority:** P1 (Proposed). **Estimate:** Pending. **Window:** 19–21 Nov (Proposed).

**Dependencies:** S2-07; S2-03 and S2-06 for final alignment. Draft inputs may be developed in parallel; final acceptance waits for these dependencies.

**Evidence required:** Actual output version/path or Figma/source/export URL, validation results, independent review and decision links. All [TODO] until they exist.

### S2-09

**Issue title:** [Sprint 2] Document architecture rationale and contract mapping

**Description:** Document architecture decisions, boundaries, responsibilities and SRS/NFR/API traceability.

**Acceptance criteria:**

- [ ] State proposed/approved technology and security decisions with rationale/alternatives and open questions.
- [ ] Map chosen requirements to components/data/API operations, resolving discrepancies with Nurefşan.
- [ ] No fabricated server/deployment; any API change is owner-authored and separately reviewed.

**Proposed owner:** Arda. Assignment Pending member/team agreement.

**Priority:** P1 (Proposed). **Estimate:** Pending. **Window:** 18–21 Nov (Proposed).

**Dependencies:** S2-02; S2-03 and S2-06 for final baseline. Draft inputs may be developed in parallel; final acceptance waits for these dependencies.

**Evidence required:** Actual output version/path or Figma/source/export URL, validation results, independent review and decision links. All [TODO] until they exist.

### S2-10

**Issue title:** [Sprint 2] Create C4 views and architecture consistency checks

**Description:** Create the agreed C4 model levels and exports against the architecture baseline.

**Acceptance criteria:**

- [ ] Team confirms levels; proposed Context/Container minimum is a planning recommendation only.
- [ ] Views show actors, system boundary, containers/responsibilities and labeled relationships; external systems reflect decisions.
- [ ] Keep editable sources/version and readable exports linked to architecture/requirements.

**Proposed owner:** Arda. Assignment Pending member/team agreement.

**Priority:** P1 (Proposed). **Estimate:** Pending. **Window:** 19–21 Nov (Proposed).

**Dependencies:** S2-09. Draft inputs may be developed in parallel; final acceptance waits for these dependencies.

**Evidence required:** Actual output version/path or Figma/source/export URL, validation results, independent review and decision links. All [TODO] until they exist.

### S2-11

**Issue title:** [Sprint 2] Create UML views for selected structure and interactions

**Description:** Create owner-selected UML diagrams for agreed scenarios and domain structure.

**Acceptance criteria:**

- [ ] Agree diagram types; proposed class/domain and sequence set is not an asserted course requirement.
- [ ] Names, multiplicities/relationships, messages and success/error flows are consistent with SRS/API/UX.
- [ ] Include readable exports, editable sources and scenario requirement IDs; unresolved details explicit.

**Proposed owner:** Arda. Assignment Pending member/team agreement.

**Priority:** P1 (Proposed). **Estimate:** Pending. **Window:** 20–21 Nov (Proposed).

**Dependencies:** S2-09; S2-08 for final UX consistency. Draft inputs may be developed in parallel; final acceptance waits for these dependencies.

**Evidence required:** Actual output version/path or Figma/source/export URL, validation results, independent review and decision links. All [TODO] until they exist.

### S2-12

**Issue title:** [Sprint 2] Record actual decisions, review outcomes and contribution evidence

**Description:** Maintain actual Sprint 2 process/contribution records without overwriting Sprint 1 records.

**Acceptance criteria:**

- [ ] Record decisions with actual date, participants/approvers, status and evidence; absent evidence remains Pending.
- [ ] Map each of six members to real Issue/PR/commit/artifact links, without counting assignment as contribution.
- [ ] Reconcile Sprint 2 responsibility proposal with team responses; never auto-close Sprint 1 evidence gaps.

**Proposed owner:** Azra; Mert tracking support. Assignment Pending member/team agreement.

**Priority:** P1 (Proposed). **Estimate:** Pending. **Window:** 16–23 Nov (Proposed).

**Dependencies:** S2-01; progressive inputs from S2-02…S2-11. Draft inputs may be developed in parallel; final acceptance waits for these dependencies.

**Evidence required:** Actual output version/path or Figma/source/export URL, validation results, independent review and decision links. All [TODO] until they exist.

### S2-13

**Issue title:** [Sprint 2] Perform independent cross-deliverable QA and owner rechecks

**Description:** Review the actual four deliverables and their traceability as one package.

**Acceptance criteria:**

- [ ] Matrix lists artifact/version, criterion, method, result, evidence, finding owner and severity.
- [ ] Check SRS/backlog/NFR/Figma/C4/UML consistency, links/access and readable diagrams; missing work is Pending.
- [ ] Owners fix issues; reviewer rechecks actual commits/versions. Passing documentation checks is not running product tests.

**Proposed owner:** Ahmet; independent reviewer for Ahmet's own work. Assignment Pending member/team agreement.

**Priority:** P1 (Proposed). **Estimate:** Pending. **Window:** 21–23 Nov (Proposed).

**Dependencies:** S2-04, S2-06, S2-08, S2-10, S2-11. Draft inputs may be developed in parallel; final acceptance waits for these dependencies.

**Evidence required:** Actual output version/path or Figma/source/export URL, validation results, independent review and decision links. All [TODO] until they exist.

### S2-14

**Issue title:** [Sprint 2] Prepare protected integration and Sprint 2 release evidence

**Description:** Prepare reproducible links/package baseline and later separately authorized release/tag.

**Acceptance criteria:**

- [ ] Verify branch protection, correct target/source SHAs, independent reviews and conversations before merges.
- [ ] After separate authorization, verify new Sprint 2 tag/release points to reviewed commit; do not alter sprint-1.
- [ ] Confirm tool/artifact export/access and preserve individual commit history; no production infrastructure task added.

**Proposed owner:** Barış technical preparation; Mert coordination. Assignment Pending member/team agreement.

**Priority:** P1 (Proposed). **Estimate:** Pending. **Window:** 23–24 Nov (Proposed).

**Dependencies:** S2-12, S2-13. Draft inputs may be developed in parallel; final acceptance waits for these dependencies.

**Evidence required:** Actual output version/path or Figma/source/export URL, validation results, independent review and decision links. All [TODO] until they exist.

### S2-15

**Issue title:** [Sprint 2] Validate final package and submit through Teams

**Description:** Complete the submission checklist and actual Teams submission only after final authorization.

**Acceptance criteria:**

- [ ] All four headings and six member names/responsibilities have accessible versioned links; repository and release/tag included.
- [ ] Record assignment timezone/format/team number; validate package integrity and actual Issue/PR links.
- [ ] Upload through designated assignment before 24 Nov 23:59 (timezone confirmation Pending); retain actual receipt/status.

**Proposed owner:** Mert; team supplies acceptance evidence. Assignment Pending member/team agreement.

**Priority:** P1 (Proposed). **Estimate:** Pending. **Window:** 24 Nov; target 21:00 (Proposed).

**Dependencies:** S2-14. Draft inputs may be developed in parallel; final acceptance waits for these dependencies.

**Evidence required:** Actual output version/path or Figma/source/export URL, validation results, independent review and decision links. All [TODO] until they exist.

## Duplication and scope guard

S2-03 owns SRS content; S2-04 owns refined backlog and mapping, not a duplicate SRS. S2-05 defines quality scenarios; S2-06 defines metrics/verification. S2-07 establishes flow coverage/access; S2-08 produces the prototype/flows. S2-09 owns rationale, S2-10 C4 and S2-11 UML. S2-12 collects real decisions/contributions; S2-13 independently checks outputs; S2-14 prepares integration/release evidence; S2-15 submits. They must share one requirement/decision baseline instead of duplicating decisions.

Sprint 1 Issues #3/#5/#9–#15 remain historical references only. Do not rename them into Sprint 2 work or claim their closure. Implementation, CI coverage, deployment and a working MVP are not introduced as Sprint 2 completion requirements. No colleague's deliverable is authored by this planning task.
