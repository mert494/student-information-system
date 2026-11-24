# Sprint 2 plan — Requirements and Architecture

Status: **Local Scrum Master planning proposal, 16 November 2026.** Prepared by Mert; no team member's Sprint 2 deliverable, acceptance, estimate, assignment or meeting is recorded as complete. Actual Sprint 2 Issue/PR: [TODO]. See [task breakdown and Issue drafts](Sprint2_Task_Breakdown.md) and [submission checklist](Sprint2_Submission_Checklist.md).

## Mandate and evidence boundary

The Sprint 2 announcement supplied by Mert requires four deliverables: detailed SRS and refined Product Backlog; non-functional requirements and quality-measure specifications; Figma UI/UX prototypes including user-flow diagrams; architecture documentation including C4 and UML. Deadline: **24 November 2026, 23:59**, as reported from the Teams screen. Grade weight: **20%**. Timezone confirmation from the actual assignment: [TODO]; operational planning uses Europe/Istanbul pending confirmation. Announcement permalink and detailed format/rubric: [TODO]. These requirements are supplied by the user; no Teams inspection is claimed.

Teams also requires team information, repository URL, release/tag information, all six names/responsibilities, and real links to Issues, PRs, technical documents, diagrams and other outputs. No format, diagram level or diagram type beyond the supplied announcement is asserted as an official requirement.

## Read-only repository assessment

GitHub checked on 16 November 2026:
- Main: https://github.com/mert494/student-information-system/commit/c6af2af9840d7166912370d645e002eb69649efb.
- Develop: https://github.com/mert494/student-information-system/commit/61aff1102ce5210db0ed87c7c84a6f8f5c608c62.
- Main is historically ahead of develop, with no file differences in the GitHub comparison. This does not authorize history rewriting or synchronization.
- No Sprint 2 directory in the remote develop tree; no open PRs. Open Issues #3, #5 and #9–#15 are Sprint 1 records, not Sprint 2 task acceptance.
- Existing sprint-1 tag points to d64b7f33119d9ccccb20200aaed38ea6b54b1e16; release exists. It predates the final four-file supplement and is not the Sprint 2 baseline or release.
- Local checkout is docs/sprint1-team-guides with pre-existing modified templates, AGENTS and Sprint 1 documents, plus an untracked translation report. Those changes are outside this task. These three new files are local proposals on the existing checkout, not a Sprint 2 feature branch or published work.
- Repository rules and README were read; no nested AGENTS.md exists in the remote tree or local scanned tree.

Immutable remote sources below avoid confusing the older dirty local copies with the latest integrated baseline.

| Input reviewed | Reusable content | Decisions or limitations to carry forward |
| --- | --- | --- |
| [docs/System_Vision_and_Boundary.md](https://github.com/mert494/student-information-system/blob/61aff1102ce5210db0ed87c7c84a6f8f5c608c62/docs/System_Vision_and_Boundary.md) | Four named roles, candidate capabilities, actor interactions and existing context SVG | Scope/actors/permissions, external-system exclusion, data ownership/trust boundaries and final Boundary approval remain pending; candidate roles are not a permission matrix |
| [docs/Initial_Backlog_Draft.md](https://github.com/mert494/student-information-system/blob/61aff1102ce5210db0ed87c7c84a6f8f5c608c62/docs/Initial_Backlog_Draft.md) | PB-01–PB-07 stories, proposed priorities/points, dependencies, measurable 401/403/409 scenarios and proposed Feature/Task supplement | PO approval, estimates, implementers, student/course fields, uniqueness scope, grade/publication policies and error mapping require owners; PB-05 enrollment-date authority and role naming need clarification |
| [api/openapi.yaml](https://github.com/mert494/student-information-system/blob/61aff1102ce5210db0ed87c7c84a6f8f5c608c62/api/openapi.yaml) | OpenAPI 3.1.0 provisional contract, 12 operations, PB references, proposed bearer security, synthetic examples | Version/tool/security/data decisions not team-approved; localhost is a placeholder, not deployment; missing term/status and data/policy decisions belong to Arda with PO input |
| [docs/RACI_Matrix.md](https://github.com/mert494/student-information-system/blob/61aff1102ce5210db0ed87c7c84a6f8f5c608c62/docs/RACI_Matrix.md) | Six role labels and division of product, architecture, QA, DevOps and process concerns | Matrix is Sprint 1-specific; D-01/D-02 are team-reported. Use role expertise to propose Sprint 2 ownership, not silently extend S1 assignments or claim fresh approval |
| [CONTRIBUTIONS.md](https://github.com/mert494/student-information-system/blob/61aff1102ce5210db0ed87c7c84a6f8f5c608c62/CONTRIBUTIONS.md) | Names/accounts and historical Issue/PR/commit evidence | Student details come from Mert's supplied roster; F-25 early nsankcc/nsnkcc account association gap remains explicit; no Sprint 2 contributions yet |
| [docs/Sprint1_Quality_Report.md](https://github.com/mert494/student-information-system/blob/61aff1102ce5210db0ed87c7c84a6f8f5c608c62/docs/Sprint1_Quality_Report.md) | Review method and unresolved evidence inventory | Historical 28 checks = 21 Passed, 3 Failed, 4 Pending. Do not copy this score as Sprint 2 results; open/partial findings require new owner rechecks |

Sprint 1 records and release stay unchanged. Scope/permission/backlog gaps that affect SRS are dependency decisions, not a second Sprint 1 deliverable. Historical license/account/RACI evidence gaps remain visible and do not become fictional Sprint 2 achievements.

## Four deliverables and proposed acceptance gates

| Official heading | Proposed measurable completion criteria | Proposed lead / independent review | Evidence still absent |
| --- | --- | --- | --- |
| Detailed SRS and refined Product Backlog | Every selected feature has stable requirement IDs, actor, preconditions, normal/alternate/error flows, business/data rules and testable acceptance criteria; each approved requirement maps to a backlog item with Epic/Feature/Story/Task, priority, estimate status, dependency and owner status; rejected/deferred scope is explicit | Nurefşan; Arda consults, Ahmet reviews testability | SRS, refined baseline and PO/team decision links [TODO] |
| NFR and quality measures | Every selected quality attribute has ID, scenario, metric/unit, numerical target or explicit unresolved decision, environment/workload, measurement method, pass/fail rule and owner; unapproved thresholds remain Proposed; unresolved mandatory target blocks unconditional acceptance | Ahmet proposes measurement work with Arda technical consultation and Nurefşan priority approval | NFR specification and target approvals [TODO] |
| Figma prototypes and user flows | Every selected primary flow maps to SRS/PB IDs, entry/exit, role and success/error/empty states; prototype navigation works in Figma, flows are readable and consistent with permissions; reviewer can open the exact shared version; include export evidence if agreed | UI/UX producer [TODO] — team decision required; Nurefşan product validation, Arda technical consultation, Ahmet QA | Figma URL/version/access and flow diagrams [TODO] |
| Architecture including C4 and UML | Versioned architecture rationale references SRS/NFR IDs; C4 and UML sources plus readable exports have consistent names/boundaries/relationships and match API/data/flows; chosen levels/types and unresolved decisions are explicit | Arda; Ahmet consistency review, Nurefşan scope review | C4/UML artifacts, level/type decisions, architecture record [TODO] |

Proposed minimum discussion set: C4 System Context and Container views; UML domain/class view plus sequence views for selected cross-component flows. This is a team planning recommendation, not an invented course rubric. Arda/team decide whether Component, deployment, state or additional views are required by the real rubric and chosen design.

## People and ownership proposal

| Member / account | Existing role | Sprint 2 proposed responsibility / approval boundary |
| --- | --- | --- |
| Mert Altan Coşkun / mert494 | Scrum Master and Agile Process Coach | Planning, dependency/Issue coordination, review gates, contribution and Teams evidence; no PO or technical decision on others' behalf |
| Nurefsan Koç / nsnkcc | Product Owner and Requirements Engineer | SRS/refined backlog and product priorities/acceptance; confirms scope and UX acceptance |
| Arda Berk Kara / ardaberkkara1 | Lead Software Architect and Technical Lead | Architecture, C4/UML, contract alignment and technical NFR feasibility; does not invent PO decisions |
| Ahmet Serdar Erünsal / ahmetserdar41 | Quality Assurance and Test Automation Engineer | Proposed NFR measurement specification and independent cross-deliverable QA; another reviewer checks Ahmet's own output |
| Alim Barış Sevindik / baryyss-001 | DevOps and CI/CD Infrastructure Engineer | Tool/access prerequisites, artifact/release reproducibility and tag verification; no production infrastructure work implied |
| Azra Yağmur Öztegil / azrayy | Scrum Master and Agile Process Coach | Actual decision/meeting evidence, responsibility coordination and contribution records; no fabricated attendance/approvals |

All new assignments, capacity, estimates and the Mert–Azra split require member/team agreement. UI/UX ownership is unassigned; do not assign it by guessing from a role name.

## Proposed calendar and capacity control

No member capacity is known. Each owner supplies availability, estimates and impediments on 16–17 November; date windows are a proposal, not assigned effort or a promise. Freeze optional scope before reducing any of the four mandatory headings.

| Window (November 2026) | Proposed work / gate | Dependency and fallback |
| --- | --- | --- |
| 16–17 | Mert coordinates kickoff/capacity and decision inventory; team selects scope, UX producer, artifact locations and review pairs | Log actual decisions only; escalate missing UX owner or PO scope by 17 November |
| 17–19 | Nurefşan drafts SRS/backlog; Ahmet/Arda draft measurable NFR approach; UI producer begins agreed flows; Arda sketches architecture against agreed scope | Parallel drafts may carry explicit assumptions; unresolved policy is not an approved baseline |
| 19–21 | Owners refine prototypes, C4/UML and API mapping against requirement/NFR IDs | Review shared role/data/flow decisions once, reuse them across outputs |
| 21–22 | Independent reviews and cross-artifact QA; owners fix findings | Prioritize mandatory acceptance gaps; no author approves their own output |
| 23 | Proposed content freeze and reviewed integration; Barış/Mert rehearse artifact access and release/package evidence | If blocked, notify team, identify owner and agree recovery; do not hide gaps |
| 24, before 18:00 | Proposed buffer for final fixes, re-review and protected release integration | Recheck SHA/reviews after any new commit; timing subject to owner availability |
| 24, target 21:00 | Mert performs Teams upload/confirmation after separate authorization; retain receipt | Buffer before official 23:59 deadline; no submission is claimed now |

## Decisions, risks and escalation

| Pending decision / risk | Proposed decision owner | Needed by / affected work |
| --- | --- | --- |
| Confirm assignment timezone, team number, announcement URL, mandatory formats and diagram depth | Mert with course source/team | 17 November; submission plan |
| Scope, role–permission matrix, business/data/publication rules | Nurefşan with Arda/team | Initial baseline 18 November; all artifacts |
| UX producer, Figma access and exact flow coverage | Team / Nurefşan | 17 November; prototypes cannot proceed as assigned until confirmed |
| NFR categories, target values/workload and measurement feasibility | Nurefşan / Arda / Ahmet | 19 November; quality and architecture |
| C4 levels, UML types, technologies and contract changes | Arda with team | 19 November; architecture |
| Capacity, estimates, review pairs and Sprint 2 workflow | All members; Mert coordinates | 17 November; schedule |
| Final acceptance of disclosed gaps and release/tag naming | PO/team; Barış/Mert execute only after authorization | Before release; never reuse/move sprint-1 |

Mert records blocker, impact, owner, required decision, target date and escalation outcome in these planning/task updates or an agreed existing tool after authorization. Meetings/reviews/decisions are Pending until actual evidence is supplied.

## Workflow and next authorization

Task IDs S2-01…S2-15 are local planning IDs, not GitHub Issue numbers. See the single task register and reusable Issue drafts in [Task Breakdown](Sprint2_Task_Breakdown.md). Do not create duplicate tasks for the same output.

Next proposed approval: team confirms assignments/scope/capacity; Mert then requests authorization for a current-develop planning branch and a focused batch of actual Sprint 2 Issues derived from accepted drafts. No branch, Issue, PR, commit, push or remote mutation is performed in this phase. Recheck base SHA and preserve dirty work before any later branch operation.

Later owner-authored PRs target the agreed integration branch, with actual Issue links, validation and independent review. Existing protection must be checked at execution time; draft policy is not team approval. Each commit/push/PR/merge needs the applicable user authorization. Main integration and a new Sprint 2 release/tag occur only after review and separate permission; sprint-1 remains immutable. Use the [submission checklist](Sprint2_Submission_Checklist.md) for final evidence.
