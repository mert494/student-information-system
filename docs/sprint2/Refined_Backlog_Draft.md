# Student Information System (SIS) — Sprint 2 Refined Product Backlog

**Version:** Draft 0.3  
**Status:** Proposed; Product Owner/team approval, estimates, and assignments pending  
**Owner (proposed):** Nurefşan  
**Traceability input:** SRS Draft 0.3

> Sprint 1 backlog history is preserved. This is a proposed Sprint 2 refinement, not a replacement of the Sprint 1 record or an approved Sprint commitment. Story points below are illustrative initial proposals only and must be estimated by the team. No owner or sprint commitment is assigned by this draft.

## Work hierarchy and traceability (proposed; confirm labels/structure with team)

| Epic | Feature | User Story | Supporting Task(s) | SRS | Business Rules / NFRs | Status |
|---|---|---|---|---|---|
| Identity & Access | Login | PB-01 | T-06, T-07 | FR-01 | BR-08; NFR-SEC-01, NFR-SEC-03 | Proposed; pending review |
| Identity & Access | Authorization | PB-02 | T-01, T-07, T-08 | FR-02 | BR-08; NFR-SEC-01, NFR-SEC-02, NFR-TEST-01 | Proposed; pending review |
| Student Affairs | Student Records | PB-03 | T-02, T-07, T-08 | FR-03 | BR-09; NFR-DATA-01, NFR-TEST-01, NFR-AUD-01 (open) | Proposed; pending review |
| Course Catalog | Course Records | PB-04 | T-03, T-07, T-08 | FR-04 | BR-09; NFR-DATA-01, NFR-TEST-01, NFR-AUD-01 (open) | Proposed; pending review |
| Course Enrollment | Enrollment | PB-05 | T-04, T-07, T-08 | FR-05 | BR-01–BR-05, BR-09; NFR-TEST-01 | Proposed; pending review |
| Grade Management | Instructor Grade Entry | PB-06 | T-05, T-07, T-08 | FR-06 | BR-06, BR-09; NFR-DATA-01, NFR-TEST-01, NFR-AUD-01 (open) | Proposed; pending review |
| Grade Management | Published Grade Viewing | PB-07 | T-05, T-07, T-08 | FR-07 | BR-07, BR-08; NFR-SEC-02, NFR-TEST-01 | Proposed; pending review |

**Traceability convention:** Tasks refine/validate the linked story; they are not separate user-value commitments. BR and NFR references identify constraints/quality checks applicable to stories. Confirm any additional hierarchy levels or naming conventions with the team before baselining.

## Refinement rules
- Every story has a clear actor, outcome (`so that`), explicit acceptance criteria, dependencies, and SRS trace links.
- API feasibility review: Arda. QA/testability review: Ahmet.
- Unconfirmed priority, estimate, owner/assignment, and approval are marked Proposed/Pending rather than treated as decisions.
- Feature work remains candidate scope until PO/team approval.

## Backlog summary

| PB | Epic | User story | Priority | SP | SRS trace | BR / NFR trace | Dependency | Owner status |
|---|---|---|---|---|---|---|
| PB-01 | Identity & Access | As a user with an assigned system role, I want to log in with my account so that I can access authorized operations. | P1 Proposed | 5 Proposed | FR-01 | BR-08; NFR-SEC-01, NFR-SEC-03, NFR-TEST-01 | Authentication policy | Owner: TBD (technical reviewer: Arda) |
| PB-02 | Identity & Access | As a user with an assigned system role, I want role-based access restrictions to be enforced so that I can perform only authorized operations and access only permitted data. | P1 Proposed | 5 Proposed | FR-02 | BR-08; NFR-SEC-01, NFR-SEC-02, NFR-TEST-01 | PB-01; permission matrix | Owner: TBD (technical reviewer: Arda) |
| PB-03 | Student Affairs | As authorized Student Affairs Staff, I want to create, list, and update student records so that student information can be maintained accurately. | P1 Proposed | 5 Proposed | FR-03 | BR-09; NFR-DATA-01, NFR-TEST-01, NFR-AUD-01 (open) | PB-02; student data decisions | Owner: TBD |
| PB-04 | Course Catalog | As authorized Student Affairs Staff, I want to create and update course records so that course information can be maintained. | P1 Proposed | 5 Proposed | FR-04 | BR-09; NFR-DATA-01, NFR-TEST-01, NFR-AUD-01 (open) | PB-02; course data decisions | Owner: TBD |
| PB-05 | Enrollment | As a Student, I want to enroll in eligible courses and view my enrollments so that I can plan and track my studies. | P1 Proposed | 8 Proposed | FR-05 | BR-01–BR-05, BR-09; NFR-TEST-01 | PB-03, PB-04; enrollment rules | Owner: TBD (business-rule refinement support: Product Owner) |
| PB-06 | Grade Management | As an Instructor, I want to enter and update grades for students in courses assigned to me so that I can maintain course results. | P2 Proposed | 8 Proposed | FR-06 | BR-06, BR-09; NFR-DATA-01, NFR-TEST-01, NFR-AUD-01 (open) | PB-02, PB-05; instructor/course assignment; grading policy | Owner: TBD (review support: Product Owner/QA) |
| PB-07 | Grade Management | As a Student, I want to view my published grades so that I can monitor my academic progress. | P2 Proposed | 3 Proposed | FR-07 | BR-07, BR-08; NFR-SEC-02, NFR-TEST-01 | PB-06; publication policy | Owner: TBD |


## PB-01 — User Login
**Epic:** Identity and Access  
**Story:** As a user with an assigned system role, I want to log in with my account so that I can access the operations I am authorized to perform.  
**Priority:** P1 (proposed) · **Story Points:** 5 (unestimated; placeholder proposal) · **Owner:** TBD

**Acceptance Criteria:**
1. Valid credentials authenticate the user and establish an approved session/token.
2. Invalid credentials are rejected.
3. The failure response does not reveal whether the account exists.
4. After logout, protected operations require re-authentication.
5. Authentication behavior, expiration and logout policy are documented before implementation.
**Dependencies:** Authentication policy and account provisioning decisions. **Trace:** [SRS FR-01](SRS_Draft_Revision1.md#fr-01--authenticate-user).

## PB-02 — Role-Based Authorization
**Epic:** Identity and Access  
**Story:** As a user with an assigned system role, I want role-based access restrictions to be enforced so that I can perform only authorized operations and access only permitted data.  
**Priority:** P1 (proposed) · **Story Points:** 5 (unestimated; placeholder proposal) · **Owner:** TBD

**Acceptance Criteria:**
1. Operations follow the PO/team-approved role-and-permission matrix.
2. Unauthenticated protected requests return 401 Unauthorized.
3. Authenticated requests without permission return 403 Forbidden with an error code and message.
4. Students cannot access other students' protected academic records through UI or direct API requests.
5. API enforcement is mandatory; UI hiding alone does not satisfy authorization.
6. Permission and data-scope rules are documented and testable.
**Dependencies:** PB-01 and role/permission matrix. **Trace:** [SRS FR-02](SRS_Draft_Revision1.md#fr-02--enforce-role-and-record-authorization).
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
6. Updating a nonexistent student returns a documented not-found outcome and does not create a record.
7. Updates accept only an agreed mutable-field allowlist; immutable/unknown fields and omitted-versus-null semantics are documented and testable.
8. Required fields and validation rules are documented.
**Dependencies:** PB-02; student-field/status decisions. **Trace:** [SRS FR-03](SRS_Draft_Revision1.md#fr-03--create-list-and-update-student-records).
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
6. Updating a nonexistent course returns a documented not-found outcome and does not create a record.
7. Updates accept only an agreed mutable-field allowlist; immutable/unknown fields and omitted-versus-null semantics are documented and testable.
8. Course fields, term/offering model, and uniqueness scope are documented.
**Dependencies:** PB-02; course model/uniqueness decision. **Trace:** [SRS FR-04](SRS_Draft_Revision1.md#fr-04--create-and-update-course-records).
## PB-05 — Course Enrollment
**Epic:** Course Enrollment  
**Story:** As a Student, I want to enroll in eligible courses and view my enrollments so that I can plan and track my studies.  
**Priority:** P1 (proposed) · **Story Points:** 8 (placeholder proposal; team estimate pending) · **Owner:** TBD

**Acceptance Criteria:**
1. Only active students may enroll and only during the configured enrollment period.
2. Duplicate student-course-term enrollment is rejected with 409 Conflict and a defined error code.
3. Enrollment outside the enrollment period is rejected with 409 Conflict and a defined error code.
4. A Student can view only their own enrollment records.
5. Course capacity and applicable prerequisites are checked; a failed condition returns 409 Conflict with a specific code and message identifying the condition.
6. Inactive student status returns 409 Conflict with a specific code and message.
7. Rejected requests create or modify no enrollment record.
8. Successful requests create exactly one enrollment record and it appears in the student's own enrollment list.
**Business Rules:** Active status required; period enforced; capacity and prerequisites checked; duplicate prohibited. University Management stakeholder is responsible for enrollment dates, but role/configuration authority needs team confirmation.  
**Dependencies:** PB-03 and PB-04; enrollment data and rule decisions. **Trace:** [SRS FR-05](SRS_Draft_Revision1.md#fr-05--enroll-in-a-course-and-view-enrollments).
## PB-06 — Instructor Grade Entry
**Epic:** Grade Management  
**Story:** As an Instructor, I want to enter and update grades for students in courses assigned to me so that I can maintain course results.  
**Priority:** P2 (proposed) · **Story Points:** 8 (placeholder proposal; team estimate pending) · **Owner:** TBD

**Acceptance Criteria:**
1. Only an instructor assigned to the course can enter or update grades for it.
2. Grade values outside the approved range are rejected.
3. A grade cannot be entered for a student who is not enrolled in the course.
4. A successfully saved grade can be retrieved later.
5. An authenticated user without permission receives 403 Forbidden.
6. Rejected requests create or modify no grade record.
7. Grading scale, grade editing and publication policy are documented.
**Dependencies:** PB-02, PB-05, instructor/course assignment, grading policy. **Trace:** [SRS FR-06](SRS_Draft_Revision1.md#fr-06--enter-or-update-grades-for-assigned-courses).
## PB-07 — Student Grade Viewing
**Epic:** Grade Management  
**Story:** As a Student, I want to view my published grades so that I can monitor my academic progress.  
**Priority:** P2 (proposed) · **Story Points:** 3 (placeholder proposal; team estimate pending) · **Owner:** TBD

**Acceptance Criteria:**
1. A Student can view only their own published grades.
2. Unpublished grades are not visible to the student.
3. If the authenticated/authorized grade query succeeds and returns zero published grades, display `No published grades are available.` A failed request/loading error must not be treated as an empty collection.
4. Direct API requests for another student's grades return 403 Forbidden with code/message and disclose no protected information.
5. Successful results include only authorized grade information.
6. Publication policy and returned fields are documented.
**Dependencies:** PB-06 and publication policy. **Trace:** [SRS FR-07](SRS_Draft_Revision1.md#fr-07--view-own-published-grades).

## Supporting refinement tasks

| Task | Description | Priority | Estimate | Status |
|---|---|---|---|---|
| T-01 | Confirm role-to-operation and role-to-data matrix | P1 Proposed (priority convention to confirm) | Pending | Open decision; PO/Arda/team |
| T-02 | Approve Student entity fields, status values and validation | P1 Proposed (priority convention to confirm) | Pending | Open decision |
| T-03 | Approve Course fields and code uniqueness scope | P1 Proposed (priority convention to confirm) | Pending | Open decision |
| T-04 | Confirm enrollment dates, capacity, prerequisites, waitlist/withdrawal and error-code mapping | P1 Proposed (priority convention to confirm) | Pending | Open decision |
| T-05 | Confirm grading scale, precision, edit and publication rules | P1 Proposed (priority convention to confirm) | Pending | Open decision |
| T-06 | Define authentication/session policy and account lifecycle | P1 Proposed (priority convention to confirm) | Pending | Open decision |
| T-07 | Arda: review API feasibility and contract consistency | P1 Proposed | Pending | Review requested, not yet evidenced |
| T-08 | Ahmet: review scenario/testability and negative cases | P1 Proposed | Pending | Review requested, not yet evidenced |
| T-09 | Team estimates selected PBs in Story Points and records evidence | P1 Proposed | Pending | Team estimation pending |

## Definition of Ready / Refinement checks
Before a story is selected for implementation, the team should confirm: (a) the actor and outcome are understood; (b) acceptance criteria are observable and testable; (c) dependencies and open business/technical decisions are identified; (d) data and permission impacts are understood; (e) the story is estimated by the team; and (f) an owner is assigned by agreement. These checks are proposed team practice, not an existing approved project rule.

## OpenAPI–SRS alignment decision register (comparison pending)

These are review topics, not confirmed mismatches. Arda should compare the current OpenAPI contract with the SRS and record the exact operation/schema references and outcome.

| Topic | Verify against OpenAPI | Current draft expectation | Status / owner |
|---|---|---|---|
| Authentication | Login endpoint, credential payload, auth scheme/token/session, logout/expiry, error responses | FR-01 authentication and protected operations | Pending — Arda
| Student fields | Student schema required/optional fields, IDs, status enum, formats, update endpoint and method | Section 6 candidate fields; field list/mutability unresolved | Pending — Arda + PO
| Enrollment | Request/response schema, identifiers, duplicate/capacity/prerequisite errors, enrollment-period representation, own-enrollment read | FR-05 and BR-01–BR-05 | Pending — Arda + PO/team
| Grade publishing | Grade schema, instructor/course association, edit method, publication field/operation and student-facing response | FR-06/FR-07; policy undecided | Pending — Arda + academic stakeholder/PO
| Student/course updates | PATCH/PUT method, allowed fields, omitted/null handling, nonexistent target response and error schema | PATCH proposed for confirmation; not-found required; mutable-field allowlist TBD | Pending — Arda

## Traceability and deferred items

### Forward traceability (SRS requirement → backlog)

| SRS requirement | Backlog story | Epic | Feature | BR / NFR coverage | Status |
|---|---|---|---|---|
| FR-01 | PB-01 | Identity & Access | Login | BR-08; NFR-SEC-01, SEC-03, TEST-01 | Proposed; review pending |
| FR-02 | PB-02 | Identity & Access | Authorization | BR-08; NFR-SEC-01, SEC-02, TEST-01 | Proposed; review pending |
| FR-03 | PB-03 | Student Affairs | Student Records | BR-09; NFR-DATA-01, TEST-01, AUD-01 (open) | Proposed; review pending |
| FR-04 | PB-04 | Course Catalog | Course Records | BR-09; NFR-DATA-01, TEST-01, AUD-01 (open) | Proposed; review pending |
| FR-05 | PB-05 | Course Enrollment | Enrollment | BR-01–BR-05, BR-09; NFR-TEST-01 | Proposed; review pending |
| FR-06 | PB-06 | Grade Management | Instructor Grade Entry | BR-06, BR-09; NFR-DATA-01, TEST-01, AUD-01 (open) | Proposed; review pending |
| FR-07 | PB-07 | Grade Management | Published Grade Viewing | BR-07, BR-08; NFR-SEC-02, TEST-01 | Proposed; review pending |

### Reverse traceability (backlog → SRS)

| Backlog story | SRS requirement | Coverage check | Status |
|---|---|---|---|
| PB-01 | FR-01 | Story and AC should be supported by FR-01; no unlinked scope | Pending review |
| PB-02 | FR-02 | Story and AC should be supported by FR-02 | Pending review |
| PB-03 | FR-03 | Story and AC should be supported by FR-03 | Pending review |
| PB-04 | FR-04 | Story and AC should be supported by FR-04 | Pending review |
| PB-05 | FR-05 | Story and AC should be supported by FR-05 | Pending review |
| PB-06 | FR-06 | Story and AC should be supported by FR-06 | Pending review |
| PB-07 | FR-07 | Story and AC should be supported by FR-07 | Pending review |

### Deferred/removed scope rationale

| Item | Disposition | Rationale | Re-entry condition / evidence |
|---|---|---|---|
| Payments and payroll | Deferred | Not included in the current candidate Sprint 2 scope | Reconsider only after approved scope change |
| Full LMS assignments/content | Deferred | Requires separate requirements, design, and backlog | Approved scope change and new backlog items |
| Dedicated University Management dashboard/features | Deferred | Separate features are not part of the current candidate scope; stakeholder remains represented by Administrators mapping | PO/team approval and scope update |
| Separate mobile application | Deferred | No separate mobile deliverable is currently assumed | Approved scope change |
| External integrations | Unconfirmed / not committed | No integration contract or external system is confirmed in draft inputs | Architecture review and explicit scope decision |

### Decision, review, and estimation evidence tracker

| Evidence item | Owner | Evidence expected | Status | Link / date |
|---|---|---|---|---|
| Product Owner scope and backlog approval | Nurefşan / PO | Approval comment or review record | Pending | TBD |
| API feasibility review | Arda | Review comment/notes and API-contract alignment | Pending | TBD |
| QA/testability review | Ahmet | Positive/negative scenario review notes | Pending | TBD |
| Story Point estimation | Team | Recorded team estimate per story; replace placeholders in backlog summary and story headings | Pending | TBD |
| Assignment agreement | Team / sprint coordinator | Agreed owner for each committed item | Pending | TBD |
| Sprint commitment | Team | Confirmed selected scope | Pending | TBD |

## Approval and estimation record
- Product Owner approval: **Pending**.
- Team Story Point estimates: **Pending** (5/5/5/5/8/8/3 are carried forward only as proposed values; re-estimation required).
- Implementation assignments: **Pending** (no owner is assigned by this draft).
- Arda API feasibility review: **Pending evidence**.
- Ahmet QA/testability review: **Pending evidence**.
- Sprint commitment: **Pending team agreement**.
