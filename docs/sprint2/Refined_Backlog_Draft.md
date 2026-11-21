# Student Information System (SIS) — Sprint 2 Refined Product Backlog

**Version:** Draft 0.3  
**Status:** Proposed; Product Owner/team approval, estimates, and assignments pending  
**Owner (proposed):** Nurefşan  
**Traceability input:** SRS Draft 0.3

> Sprint 1 backlog history is preserved. This is a proposed Sprint 2 refinement, not a replacement of the Sprint 1 record or an approved Sprint commitment. Story points below are illustrative initial proposals only and must be estimated by the team. No owner or sprint commitment is assigned by this draft.

## Hierarchy and end-to-end traceability (proposed; approval pending)

| Epic | Feature | User Story | Supporting tasks | SRS / BR / NFR / OQ | Status |
|---|---|---|---|---|---|
| Identity & Access | Authentication/session lifecycle | PB-01 | T-06, T-07, T-09 | [FR-01](SRS_Draft.md#fr-01-authenticate-user); NFR-SEC-03; OQ-02 | Proposed/Pending |
| Identity & Access | Role and record authorization | PB-02 | T-01, T-07, T-08, T-09 | [FR-02](SRS_Draft.md#fr-02-enforce-role-and-record-authorization); BR-08; NFR-SEC-01/02; OQ-01 | Proposed/Pending |
| Student Affairs | Student record lifecycle | PB-03 | T-02, T-07, T-08, T-09 | [FR-03](SRS_Draft.md#fr-03-create-list-and-update-student-records); BR-09; NFR-DATA-01; OQ-03/12 | Proposed/Pending |
| Course Catalog | Course record lifecycle | PB-04 | T-03, T-07, T-08, T-09 | [FR-04](SRS_Draft.md#fr-04-create-and-update-course-records); BR-09; NFR-DATA-01; OQ-04/13 | Proposed/Pending |
| Course Enrollment | Registration and eligibility | PB-05 | T-04, T-07, T-08, T-09 | [FR-05](SRS_Draft.md#fr-05-enroll-in-a-course-and-view-enrollments); BR-01–05/09; NFR-DATA-01; OQ-05/06/08 | Proposed/Pending |
| Grade Management | Instructor grade entry | PB-06 | T-05, T-07, T-08, T-09 | [FR-06](SRS_Draft.md#fr-06-enter-or-update-grades-for-assigned-courses); BR-06/09; NFR-SEC-01; OQ-07 | Proposed/Pending |
| Grade Management | Student published-grade viewing | PB-07 | T-05, T-07, T-08, T-09 | [FR-07](SRS_Draft.md#fr-07-view-own-published-grades); BR-07; NFR-SEC-02; OQ-07 | Proposed/Pending |

Hierarchy convention: Epic → Feature → PB user story → supporting task. Tasks may support multiple stories; each parent is listed. This is a proposal, not an approved sprint commitment.

## Refinement rules
- Every story has a clear actor, outcome (`so that`), explicit acceptance criteria, dependencies, and SRS trace links.
- API feasibility review: Arda. QA/testability review: Ahmet.
- Unconfirmed priority, estimate, owner/assignment, and approval are marked Proposed/Pending rather than treated as decisions.
- Feature work remains candidate scope until PO/team approval.
- **Status convention:** `Approved` = product decision confirmed; `TODO — owner` = a concrete deliverable not yet completed; `Pending` = a decision, policy, review, estimate, or evidence still awaited. Do not mark an approved decision as Pending merely because its API implementation is outstanding.

## Approved architecture decisions to implement

The Product Owner has approved the Architecture Lead's three proposals. They are recorded in the story acceptance criteria below. Product-decision status is **Approved**; implementation of the corresponding OpenAPI contract changes is **TODO — Arda** and must not be represented as complete until committed and reviewed.

- **PB-01:** JWT carries `sid`; logout revokes the corresponding server-side session.
- **PB-05:** Registration references Student and CourseOffering; CourseOffering references Course and Term; `(studentId, courseOfferingId)` is unique.
- **PB-06:** Grade references Registration; a separate GET operation supports authorized Instructor grade retrieval. Arda must specify the route, response schema and authorization scope in OpenAPI.

## Backlog summary

| PB | Epic | User story | Priority | SP | SRS trace | Dependency | Owner status |
|---|---|---|---|---|---|---|---|
| PB-01 | Identity & Access | As a user with an assigned system role, I want to log in with my account so that I can access authorized operations. | P1 Proposed | 5 Proposed | [FR-01](SRS_Draft.md#fr-01-authenticate-user) | Authentication policy | Owner: TBD (technical reviewer: Arda) |
| PB-02 | Identity & Access | As Student Affairs Staff, I want role-based access restrictions to be enforced so that each user can perform only authorized operations and access permitted data. | P1 Proposed | 5 Proposed | [FR-02](SRS_Draft.md#fr-02-enforce-role-and-record-authorization) | PB-01; permission matrix | Owner: TBD (technical reviewer: Arda) |
| PB-03 | Student Affairs | As authorized Student Affairs Staff, I want to create, list, and update student records so that student information can be maintained accurately. | P1 Proposed | 5 Proposed | [FR-03](SRS_Draft.md#fr-03-create-list-and-update-student-records) | PB-02; student data decisions | Owner: TBD |
| PB-04 | Course Catalog | As authorized Student Affairs Staff, I want to create and update course records so that course information can be maintained. | P1 Proposed | 5 Proposed | [FR-04](SRS_Draft.md#fr-04-create-and-update-course-records) | PB-02; course data decisions | Owner: TBD |
| PB-05 | Enrollment | As a Student, I want to enroll in eligible courses and view my enrollments so that I can plan and track my studies. | P1 Proposed | 8 Proposed | [FR-05](SRS_Draft.md#fr-05-enroll-in-a-course-and-view-enrollments) | PB-03, PB-04; enrollment rules | Owner: TBD (business-rule refinement support: Product Owner) |
| PB-06 | Grade Management | As an Instructor, I want to enter and update grades for students in courses assigned to me so that I can maintain course results. | P2 Proposed | 8 Proposed | [FR-06](SRS_Draft.md#fr-06-enter-or-update-grades-for-assigned-courses) | PB-02, PB-05; instructor/course assignment; grading policy | Owner: TBD (review support: Product Owner/QA) |
| PB-07 | Grade Management | As a Student, I want to view my published grades so that I can monitor my academic progress. | P2 Proposed | 3 Proposed | [FR-07](SRS_Draft.md#fr-07-view-own-published-grades) | PB-06; publication policy | Owner: TBD |


## PB-01 — User Login
**Epic:** Identity and Access  
**Story:** As a user with an assigned system role, I want to log in with my account so that I can access the operations I am authorized to perform.  
**Priority:** P1 (proposed) · **Story Points:** 5 (unestimated; placeholder proposal) · **Owner:** TBD

**Acceptance Criteria:**
1. Valid credentials authenticate the user and establish an approved session/token.
2. Invalid credentials are rejected.
3. The failure response does not reveal whether the account exists.
4. After logout, protected operations require re-authentication.
5. JWT contains the approved `sid` (sessionId) claim; logout revokes the corresponding server-side session. A revoked session cannot authorize subsequent protected requests.
6. Arda updates the OpenAPI session/token and logout contract to reflect this approved behavior (**TODO — Arda**).
7. Token expiration/refresh and account lifecycle policies remain **Pending**.
**Dependencies:** Authentication policy and account provisioning decisions. **Trace:** FR-01.

## PB-02 — Role-Based Authorization
**Epic:** Identity and Access  
**Story:** As Student Affairs Staff, I want role-based access restrictions to be enforced so that each user can perform only authorized operations and access permitted data.  
**Priority:** P1 (proposed) · **Story Points:** 5 (unestimated; placeholder proposal) · **Owner:** TBD

**Acceptance Criteria:**
1. Operations follow the PO/team-approved role-and-permission matrix.
2. Unauthenticated protected requests return 401 Unauthorized.
3. Authenticated requests without permission return 403 Forbidden with an error code and message.
4. Students cannot access other students' protected academic records through UI or direct API requests.
5. API enforcement is mandatory; UI hiding alone does not satisfy authorization.
6. Permission and data-scope rules are documented and testable.
**Dependencies:** PB-01 and role/permission matrix. **Trace:** FR-02.
## PB-03 — Student Management
**Epic:** Student Affairs  
**Story:** As authorized Student Affairs Staff, I want to create, list, and update student records so that student information can be maintained accurately.  
**Priority:** P1 (proposed) · **Story Points:** 5 (placeholder proposal; team estimate pending) · **Owner:** TBD

**Acceptance Criteria:**
1. Required student fields are validated on creation.
2. Duplicate student number is rejected.
3. Unauthorized users cannot create or update student records.
4. Successful updates are reflected in subsequent list/read results.
5. Missing or invalid data is rejected without creating or changing a record.
6. Required fields and validation rules are documented.
7. Unknown `studentId` follows the OpenAPI 404 NotFound response; error code/envelope is subject to OQ-08.
8. Tests cover omitted field, explicit null, unknown field, immutable field, same-value no-op, validation failure and unauthorized caller; expected behavior remains Pending OQ-12/OQ-01/OQ-08.
9. Rejected update causes no partial or unintended persisted change.
**Dependencies:** PB-02; student-field/status decisions. **Trace:** [FR-03](SRS_Draft.md#fr-03-create-list-and-update-student-records); BR-09; NFR-DATA-01; OQ-03/OQ-12.
## PB-04 — Course Management
**Epic:** Course Catalog  
**Story:** As authorized Student Affairs Staff, I want to create and update course records so that course information can be maintained.  
**Priority:** P1 (proposed) · **Story Points:** 5 (placeholder proposal; team estimate pending) · **Owner:** TBD

**Acceptance Criteria:**
1. Required course fields are validated on creation.
2. Duplicate course code is rejected within the team-approved uniqueness scope.
3. Unauthorized users cannot create or update course records.
4. Successfully created courses appear in the course list.
5. Missing or invalid data is rejected without persisting a record.
6. Course fields, term/offering model, and uniqueness scope are documented.
7. Unknown `courseId` follows the OpenAPI 404 NotFound response; error code/envelope is subject to OQ-08.
8. Tests cover omitted field, explicit null, unknown field, immutable field, same-value no-op, validation failure and unauthorized caller; expected behavior remains Pending OQ-13/OQ-01/OQ-08.
9. Rejected update causes no partial or unintended persisted change.
**Dependencies:** PB-02; course model/uniqueness decision. **Trace:** [FR-04](SRS_Draft.md#fr-04-create-and-update-course-records); BR-09; NFR-DATA-01; OQ-04/OQ-13.
## PB-05 — Course Enrollment
**Epic:** Course Enrollment  
**Story:** As a Student, I want to enroll in eligible courses and view my enrollments so that I can plan and track my studies.  
**Priority:** P1 (proposed) · **Story Points:** 8 (placeholder proposal; team estimate pending) · **Owner:** TBD

**Acceptance Criteria:**
1. Only active students may enroll and only during the configured enrollment period.
2. Each Registration references one Student and one CourseOffering; each CourseOffering references one Course and one Term.
3. `(studentId, courseOfferingId)` is unique; a duplicate registration is rejected with 409 Conflict and a defined error code.
4. Enrollment outside the enrollment period is rejected with 409 Conflict and a defined error code.
5. A Student can view only their own registration records.
6. Course capacity and applicable prerequisites are checked; a failed condition returns 409 Conflict with a specific code and message identifying the condition.
7. Inactive student status returns 409 Conflict with a specific code and message.
8. Rejected requests create or modify no registration record.
9. Successful requests create exactly one Registration and it appears in the student's own registration list.
10. Arda updates the OpenAPI schemas/operations to represent the approved relationships and unique pair (**TODO — Arda**); API mapping is not complete until reviewed.
**Business Rules:** Active status required; period enforced; capacity and prerequisites checked; duplicate `(studentId, courseOfferingId)` prohibited. Registration → Student + CourseOffering; CourseOffering → Course + Term. University Management stakeholder is responsible for enrollment dates, but role/configuration authority needs team confirmation.  
**Dependencies:** PB-03 and PB-04; enrollment data and rule decisions. **Trace:** FR-05.
## PB-06 — Instructor Grade Entry
**Epic:** Grade Management  
**Story:** As an Instructor, I want to enter and update grades for students in courses assigned to me so that I can maintain course results.  
**Priority:** P2 (proposed) · **Story Points:** 8 (placeholder proposal; team estimate pending) · **Owner:** TBD

**Acceptance Criteria:**
1. Only an instructor assigned to the course can enter or update grades for it.
2. Grade values outside the approved range are rejected.
3. A grade cannot be entered for a student who is not enrolled in the course.
4. Each Grade is associated with one Registration.
5. An authorized Instructor can retrieve grades through a separate GET operation for the relevant assigned course offering/registrations; exact route, response schema and scope are defined in the OpenAPI contract.
6. A successfully saved grade can be retrieved later.
7. An authenticated user without permission receives 403 Forbidden.
8. Rejected requests create or modify no grade record.
9. Grading scale, grade editing and publication policy are documented.
**Dependencies:** PB-02, PB-05, instructor/course assignment, grading policy, OpenAPI Instructor GET operation. **Trace:** FR-06.
## PB-07 — Student Grade Viewing
**Epic:** Grade Management  
**Story:** As a Student, I want to view my published grades so that I can monitor my academic progress.  
**Priority:** P2 (proposed) · **Story Points:** 3 (placeholder proposal; team estimate pending) · **Owner:** TBD

**Acceptance Criteria:**
1. A Student can view only their own published grades.
2. Unpublished grades are not visible to the student.
3. If there are no published grades, display `No published grades are available.`
4. Direct API requests for another student's grades return 403 Forbidden with code/message and disclose no protected information.
5. Successful results include only authorized grade information.
6. Publication policy and returned fields are documented.
**Dependencies:** PB-06 and publication policy. **Trace:** FR-07.

## Supporting refinement tasks and parent links

| Task | Parent Epic / Feature | Parent PB / FR | Deliverable | Dependencies | Related OQ | BR / NFR | Owner / Status |
|---|---|---|---|---|---|---|---|
| T-01 | Identity & Access / Role authorization | PB-02 / FR-02 | Confirm role-to-operation and role-to-data matrix | T-06; team role model | OQ-01 | BR-08; NFR-SEC-01/02 | PO/Arda/team; Pending |
| T-02 | Student Affairs / Student lifecycle | PB-03 / FR-03 | Approve Student fields, statuses and validation | T-07 API review | OQ-03/OQ-12 | BR-09; NFR-DATA-01 | PO/team; Pending |
| T-03 | Course Catalog / Course lifecycle | PB-04 / FR-04 | Approve Course fields and uniqueness scope | T-07 API review | OQ-04/OQ-13 | BR-09; NFR-DATA-01 | PO/team; Pending |
| T-04 | Course Enrollment / Eligibility | PB-05 / FR-05 | Implement approved Registration–Student/CourseOffering and CourseOffering–Course/Term relationships and unique pair; confirm dates, capacity, prerequisites, waitlist/withdrawal and error mapping | T-02, T-03, T-07 | OQ-05/OQ-06/OQ-08 | BR-01–05/09; NFR-DATA-01 | Arda: OpenAPI mapping TODO; PO-approved data model; remaining policy Pending |
| T-05 | Grade Management / Entry and publication | PB-06/PB-07 / FR-06/FR-07 | Implement Grade–Registration relationship and separate Instructor grade GET operation; confirm grading scale, precision, editing and publication rules | T-04, T-07 | OQ-07 | BR-06/07/09; NFR-AUD-01 (OPEN) | Arda: Instructor GET/OpenAPI mapping TODO; PO-approved relationship; grading policy Pending |
| T-06 | Identity & Access / Authentication | PB-01 / FR-01 | Implement approved JWT `sid` claim and server-side session revocation on logout; confirm expiry/refresh and account lifecycle | OpenAPI contract review | OQ-02 | NFR-SEC-03 | Arda: OpenAPI sid/logout mapping TODO; expiry/refresh Pending |
| T-07 | Cross-cutting / API contract alignment | PB-01–PB-07 / FR-01–FR-07 | Arda reviews operation/schema/requirement consistency | SRS/API draft available | OQ-02/05/07 (product decisions approved; OpenAPI mapping TODO), remaining OQs pending | Applicable BR/NFR per story | Arda; TODO — update OpenAPI and provide contract evidence |
| T-08 | Cross-cutting / QA and testability | PB-01–PB-07 / FR-01–FR-07 | Ahmet reviews positive/negative cases, PATCH matrix and measurable NFRs | T-07; decision outcomes as available | OQ-01–13 | Applicable BR/NFR per story | Ahmet; Pending |
| T-09 | Cross-cutting / Estimation and commitment | PB-01–PB-07 / FR-01–FR-07 | Team estimates stories and records owner/commitment evidence | T-01–T-08 refinement inputs | All applicable OQs | All applicable BR/NFR | Team; Pending |

## Definition of Ready / Refinement checks
Before a story is selected for implementation, the team should confirm: (a) the actor and outcome are understood; (b) acceptance criteria are observable and testable; (c) dependencies and open business/technical decisions are identified; (d) data and permission impacts are understood; (e) the story is estimated by the team; and (f) an owner is assigned by agreement. These checks are proposed team practice, not an existing approved project rule.

## Traceability and deferred items

### Forward traceability (SRS requirement → backlog)

| SRS requirement | Backlog story | Linkage | Status |
|---|---|---|---|
| [FR-01](SRS_Draft.md#fr-01-authenticate-user) | PB-01 | Authentication story covers the requirement | Proposed; review pending |
| [FR-02](SRS_Draft.md#fr-02-enforce-role-and-record-authorization) | PB-02 | Authorization story covers the requirement | Proposed; review pending |
| [FR-03](SRS_Draft.md#fr-03-create-list-and-update-student-records) | PB-03 | Student record management story covers the requirement | Proposed; review pending |
| [FR-04](SRS_Draft.md#fr-04-create-and-update-course-records) | PB-04 | Course record management story covers the requirement | Proposed; review pending |
| [FR-05](SRS_Draft.md#fr-05-enroll-in-a-course-and-view-enrollments) | PB-05 | Enrollment story covers the requirement | Proposed; review pending |
| [FR-06](SRS_Draft.md#fr-06-enter-or-update-grades-for-assigned-courses) | PB-06 | Instructor grade-entry story covers the requirement | Proposed; review pending |
| [FR-07](SRS_Draft.md#fr-07-view-own-published-grades) | PB-07 | Student published-grade viewing story covers the requirement | Proposed; review pending |

### Reverse traceability (backlog → SRS)

| Backlog story | SRS requirement | Coverage check | Status |
|---|---|---|---|
| PB-01 | [FR-01](SRS_Draft.md#fr-01-authenticate-user) | Story and AC should be supported by FR-01; no unlinked scope | Pending review |
| PB-02 | [FR-02](SRS_Draft.md#fr-02-enforce-role-and-record-authorization) | Story and AC should be supported by FR-02 | Pending review |
| PB-03 | [FR-03](SRS_Draft.md#fr-03-create-list-and-update-student-records) | Story and AC should be supported by FR-03 | Pending review |
| PB-04 | [FR-04](SRS_Draft.md#fr-04-create-and-update-course-records) | Story and AC should be supported by FR-04 | Pending review |
| PB-05 | [FR-05](SRS_Draft.md#fr-05-enroll-in-a-course-and-view-enrollments) | Story and AC should be supported by FR-05 | Pending review |
| PB-06 | [FR-06](SRS_Draft.md#fr-06-enter-or-update-grades-for-assigned-courses) | Story and AC should be supported by FR-06 | Pending review |
| PB-07 | [FR-07](SRS_Draft.md#fr-07-view-own-published-grades) | Story and AC should be supported by FR-07 | Pending review |

### Deferred/removed scope rationale

| Item | Disposition | Rationale | Re-entry condition / evidence |
|---|---|---|---|
| Payments and payroll | Deferred | Not included in the current candidate Sprint 2 scope | Reconsider only after approved scope change |
| Full LMS assignments/content | Deferred | Requires separate requirements, design, and backlog | Approved scope change and new backlog items |
| Dedicated University Management dashboard/features | Deferred | Separate features are not part of the current candidate scope; stakeholder remains represented by Administrators mapping | PO/team approval and scope update |
| Separate mobile application | Deferred | No separate mobile deliverable is currently assumed | Approved scope change |
| External integrations | Unconfirmed / not committed | No integration contract or external system is confirmed in draft inputs | Architecture review and explicit scope decision |

### Approved decisions vs. outstanding implementation

| Item | Product decision | Outstanding work | Status |
|---|---|---|---|
| Session model (PB-01) | JWT `sid`; logout revokes server-side session | Arda updates and verifies OpenAPI token/session/logout contract | Approved / TODO — Arda |
| Registration model (PB-05) | Registration → Student + CourseOffering; CourseOffering → Course + Term; unique `(studentId, courseOfferingId)` | Arda maps relationships and uniqueness into OpenAPI schemas/operations; student identity source still needs contract confirmation | Approved / TODO — Arda; identity mapping Pending |
| Grade model (PB-06) | Grade → Registration; separate Instructor grade GET | Arda defines route, response schema and instructor authorization scope | Approved / TODO — Arda |
| Other enrollment/grading/authorization/PATCH policies | Not decided by these three approvals | Obtain relevant PO/team/academic/QA decisions | Pending |

## Decision, review, and estimation evidence tracker

| Evidence item | Owner | Evidence expected | Status | Link / date |
|---|---|---|---|---|
| Product Owner scope and backlog approval | Nurefşan / PO | Approval comment or review record | Pending | TBD |
| API feasibility review | Arda | Review comment/notes and API-contract alignment | Pending | TBD |
| QA/testability review | Ahmet | Positive/negative scenario review notes | Pending | TBD |
| Story Point estimation | Team | Recorded team estimate per story; replace placeholders in backlog summary and story headings | Pending | TBD |
| Assignment agreement | Team / sprint coordinator | Agreed owner for each committed item | Pending | TBD |
| Sprint commitment | Team | Confirmed selected scope | Pending | TBD |

## Approval and estimation record
- Product Owner approval of the three architecture decisions (PB-01, PB-05, PB-06): **Approved**. Overall backlog/sprint-scope approval: **Pending**.
- Team Story Point estimates: **Pending** (5/5/5/5/8/8/3 are carried forward only as proposed values; re-estimation required).
- Implementation assignments: **Pending** (no owner is assigned by this draft).
- Arda API feasibility review: **Pending evidence**.
- Ahmet QA/testability review: **Pending evidence**.
- Sprint commitment: **Pending team agreement**.

## Explicit BR / NFR traceability

| PB | SRS requirement | BR | NFR | Open decisions |
|---|---|---|---|---|
| PB-01 | [FR-01](SRS_Draft.md#fr-01-authenticate-user) | — | NFR-SEC-03 | OQ-02 (sid/revocation approved; API mapping pending) |
| PB-02 | [FR-02](SRS_Draft.md#fr-02-enforce-role-and-record-authorization) | BR-08 | NFR-SEC-01/02 | OQ-01/OQ-08 |
| PB-03 | [FR-03](SRS_Draft.md#fr-03-create-list-and-update-student-records) | BR-09 | NFR-DATA-01; NFR-AUD-01 OPEN | OQ-03/OQ-12 |
| PB-04 | [FR-04](SRS_Draft.md#fr-04-create-and-update-course-records) | BR-09 | NFR-DATA-01; NFR-AUD-01 OPEN | OQ-04/OQ-13 |
| PB-05 | [FR-05](SRS_Draft.md#fr-05-enroll-in-a-course-and-view-enrollments) | BR-01–05/09 | NFR-DATA-01; NFR-PERF-01 OPEN | OQ-05 (data model approved; API mapping pending)/OQ-06/OQ-08 |
| PB-06 | [FR-06](SRS_Draft.md#fr-06-enter-or-update-grades-for-assigned-courses) | BR-06/09 | NFR-SEC-01; NFR-AUD-01 OPEN | OQ-07 (relationship/Instructor GET approved; API mapping pending)/OQ-08 |
| PB-07 | [FR-07](SRS_Draft.md#fr-07-view-own-published-grades) | BR-07 | NFR-SEC-02 | OQ-07 |

## API evidence and decision log

Operation-level evidence is recorded in the SRS OpenAPI comparison table, including method/path, operationId, schema/field, requirement, decision owner and Pending status. Source: [api/openapi.yaml on develop](https://github.com/mert494/student-information-system/blob/develop/api/openapi.yaml). The API file is a provisional draft, not an approved contract.

## Document links

- [Sprint 2 SRS](SRS_Draft.md)
- [OpenAPI draft](../../api/openapi.yaml)
- [SRS Open Questions / Decision Log](SRS_Draft.md#11-open-questions--decision-log)

The relative links above assume both Sprint 2 Markdown files are in `docs/sprint2`; verify rendered links in GitHub after replacing the files.

Terminology note: SRS uses Enrollment for the business concept while the current API draft uses `/registrations`, `Registration` and `RegistrationInput`. This naming difference remains Pending OQ-05.
