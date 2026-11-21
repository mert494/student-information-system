# Student Information System (SIS) — Software Requirements Specification (SRS)

**Version:** Draft 0.3  
**Sprint:** 2  
**Status:** Working draft; four architecture/product decisions approved by Product Owner; OpenAPI implementation, remaining product decisions, and technical/QA review pending  
**Prepared by:** Nurefşan (proposed owner; assignment confirmation pending)  
**Inputs:** Sprint 1 PB-01–PB-07, System Vision and Boundary, Sprint 2 refinement draft

> This document refines candidate requirements for review. It is not an implementation commitment. Decisions marked **OPEN** must be confirmed before the relevant requirement is baselined.

## 1. Purpose and Scope

The Student Information System (SIS) is intended to centralize essential academic information and support student, instructor, and authorized administrative workflows. The candidate Sprint 2 scope includes authentication, role-based authorization, student record management, course management, course enrollment, instructor grade entry, and student viewing of published grades. These features remain proposed until reviewed and approved by the Product Owner and team.

Out of scope unless explicitly approved: payment processing, payroll, full LMS content/assignment features, a separate mobile app, and unconfirmed integrations with external university systems.

### 1.1 Deferred scope and impact

| Deferred/rejected candidate | Scope decision | Impact / follow-up deliverable |
|---|---|---|
| Payment processing and payroll | Deferred; not part of current candidate scope | No payment/payroll data model, workflows, API endpoints, or acceptance criteria are included in Sprint 2 requirements. Revisit only through an approved scope change. |
| Full LMS content, assignments, and learning materials | Deferred | No content/assignment workflows are specified; if approved later, they require separate backlog items, requirements, and design. |
| Dedicated University Management dashboard/features | Deferred from Sprint 1 and not included as a separate Sprint 2 feature in this draft | University Management remains a stakeholder mapped to Administrators; any dedicated management features require separate backlog and scope approval. |
| Separate mobile application | Deferred | Current requirements assume no separate mobile app deliverable; UI/platform decisions are not specified here. |
| External integrations (identity provider, academic calendar, payments, notifications, etc.) | Unconfirmed; none included as committed integration | Integration contracts, dependencies, data exchange, and system boundaries must be defined only if an integration is selected. |

### 1.2 External interactions (draft boundary)

- **Students:** interact with the SIS to access their own academic information, submit enrollment requests, and view published grades.
- **Academic Staff / Instructors:** interact with the SIS to access permitted course/student information and manage grades for assigned course offerings.
- **Student Affairs Personnel / Student Affairs Staff:** interact with the SIS to maintain authorized student/course/enrollment-related records.
- **University Management / Administrators:** potential administrative interactions are limited to approved system-level operations; dedicated University Management features remain deferred.
- **External systems:** no confirmed external systems or integrations are identified in the current inputs. Identity providers, academic calendars, payment services, notification services, and other integrations are not assumed to exist in scope.
- **Decision owner:** Arda (Architecture Lead) and the team should validate technical boundary and integration feasibility; Product Owner/team must confirm selected scope. Evidence remains pending review. This section does not replace the Sprint 1 Vision/Boundary document's reserved external-interactions TODO.

## 2. Stakeholders and System Roles

**Terminology convention:** Use **Course Enrollment** for the user-facing business capability/feature; use **Registration** for the individual persisted enrollment record and `CourseOffering` for the specific course section/branch. Use these entity names consistently in SRS data relationships and API mapping. The current API path `/registrations` is retained as an API-contract name pending Arda's alignment; do not use `Enrollment` and `Registration` interchangeably for the same entity.

**Naming convention:** Stakeholder labels describe groups outside/around the system; system-role labels are the role names used for authorization. Use the system-role names consistently in requirements and permissions: `Student`, `Instructor`, `Student Affairs Staff`, and `Administrators`.

### 2.1 Stakeholder-to-role mapping

| Stakeholder group | System role | Draft access purpose |
|---|---|---|
| Student | Student | View own academic information, enrollments, and published grades; submit eligible enrollment requests. |
| Academic Staff | Instructor | View relevant course/student information and manage grades for assigned courses. |
| Student Affairs Personnel | Student Affairs Staff | Maintain authorized student and enrollment-related records and perform permitted administrative actions. |
| University Management | Administrators | Perform system-level administrative operations within approved scope. Dedicated University Management functions are deferred from Sprint 1 and are not specified as separate features here. |


### 2.2 Role and permission principles
- All protected operations require authentication.
- Permission checks must be enforced server/API-side, not only by UI visibility.
- Users may access only records and operations permitted by their role and record-level relationship.
- The final role-to-operation and role-to-data matrix is **OPEN** for Architecture Lead/team validation.

## 3. Definitions
- **Active student:** A student whose institutional status permits enrollment. Exact status values and source are **OPEN**.
- **Enrollment period:** Configured time window during which enrollment requests are allowed. Dates and authorized configurator are **OPEN**.
- **Published grade:** A grade explicitly made visible to the student under an approved publication rule. Publication workflow is **OPEN**.
- **Prerequisite:** A course or academic condition that must be met before enrollment. Rule representation and grade threshold are **OPEN**.
- **Capacity:** Maximum enrollment count for a course offering/term. Data ownership and concurrency handling are **OPEN**.

## 4. Assumptions and Constraints
1. The project is a documentation/API-contract stage; this SRS does not imply that a functioning backend exists.
2. PB-01–PB-07 are the current candidate requirements and require PO/team confirmation.
3. Academic records are sensitive; test examples must use synthetic data only.
4. HTTP response codes (401, 403, 409) are draft expectations only; Arda/team must verify their consistency with the API contract. Detailed error-code names and response schema remain open.
5. Story Point estimates remain proposed until the team estimates them.

## 5. Functional Requirements and Scenarios

<a id="fr-01-authenticate-user"></a>
### FR-01 — Authenticate user (trace: PB-01)
**Actor:** Any user with an assigned system role  
**Preconditions:** Account exists and is eligible to authenticate; authentication mechanism configured.  
**Normal scenario:** (1) User submits credentials. (2) System validates credentials. (3) System establishes authenticated session/token. (4) User can access authorized protected operations.  
**Alternate/error scenarios:** Invalid credentials are rejected with a generic message that does not reveal whether the account exists. A logged-out user attempting a protected operation receives 401 Unauthorized.  
**Acceptance criteria:** Valid credentials authenticate; invalid credentials fail; failure message is account-enumeration-safe; after logout, protected operations require re-authentication.  
**Approved session decision:** The JWT shall carry a `sid` (sessionId) claim. Logout shall revoke the corresponding server-side session; a revoked session must no longer authorize protected requests.
**Open decisions:** Credential policy, lockout/rate limiting, token expiration/refresh policy, account activation rules, and the exact API request/response contract. The approved session model does not by itself settle these remaining details.

<a id="fr-02-enforce-role-and-record-authorization"></a>
### FR-02 — Enforce role and record authorization (trace: PB-02)
**Actor:** Any authenticated user performing a protected operation; authorization rules are administered by an authorized role (to be confirmed)  
**Preconditions:** User authenticated; role/permission matrix approved.  
**Normal scenario:** API evaluates user's role and requested operation/data scope; allowed request proceeds.  
**Alternate/error scenarios:** Unauthenticated request returns 401 Unauthorized; authenticated but unauthorized request returns 403 Forbidden with an error code and message; a Student attempting another student's protected record is denied, including direct API requests.  
**Acceptance criteria:** Authorization is enforced at API level; no unauthorized operation or protected data is exposed; 401 and 403 are distinct outcomes.  
**Open decisions:** Exact permission matrix, role assignment process, administrative permission management, error-code catalog, and Instructor grade-read scope.

<a id="fr-03-create-list-and-update-student-records"></a>
### FR-03 — Create, list, and update student records (trace: PB-03)
**Actor:** Authorized Student Affairs Staff  
**Preconditions:** Authenticated staff member has student-record permission; student data schema and required fields approved.  
**Normal scenario:** Staff enters required student fields; system validates; system creates record; authorized listing returns it. Staff updates an existing record; system validates and persists; updated values are reflected in subsequent reads.  
**Alternate/error scenarios:** Missing/invalid fields are rejected; duplicate student number is rejected; unauthorized user cannot create/update; failed validation does not create or alter a record.  
**Acceptance criteria:** Required-field validation; student number uniqueness; role authorization; successful update visible in list; invalid requests rejected without persistence.  
**Open decisions:** Student field list, format/validation rules, identifier source, allowed status values, deletion/archive policy, audit logging.

<a id="fr-04-create-and-update-course-records"></a>
### FR-04 — Create and update course records (trace: PB-04)
**Actor:** Authorized Student Affairs Staff  
**Preconditions:** Authenticated user has course-management permission; course/term data model and uniqueness scope approved.  
**Normal scenario:** Staff enters course fields; system validates; course is created. Staff edits an existing course; system validates and saves changes.  
**Alternate/error scenarios:** Missing/invalid fields are rejected; duplicate course code within the agreed uniqueness scope is rejected; unauthorized changes are denied.  
**Acceptance criteria:** Required fields validated; duplicate prevention applies; unauthorized changes denied; new course appears in course list; invalid requests do not persist.  
**Open decisions:** Course fields, code uniqueness scope, term/offering structure, course status lifecycle, edit restrictions after enrollment.

<a id="fr-05-enroll-in-a-course-and-view-enrollments"></a>
### FR-05 — Enroll in a course and view enrollments (trace: PB-05)
**Actor:** Student  
**Preconditions:** Student authenticated and active; enrollment period open; course offering exists; enrollment conditions satisfied.  
**Normal scenario:** Student selects a course offering and submits enrollment; system validates active status, period, duplicate enrollment, capacity, and prerequisites; system creates exactly one Registration; the Registration appears in the student's own registration list.  
**Alternate/error scenarios:** Inactive student, closed period, duplicate enrollment, full course, or unmet prerequisite are rejected with 409 Conflict and a specific error code/message. Another student's registrations are not accessible. Rejected requests create/modify no enrollment.  
**Acceptance criteria:** Only active students register; enrollment period enforced; duplicate `(studentId, courseOfferingId)` prevented; students can access only their own registrations; capacity/prerequisites checked; each stated conflict returns 409 plus specific code/message; rejected request has no persistence side effect; success creates exactly one Registration.  
**Approved data-model decision:** A `Registration` belongs to exactly one `Student` and one `CourseOffering`. A `CourseOffering` belongs to one `Course` and one `Term`. The pair `(studentId, courseOfferingId)` shall be unique, preventing a student from registering more than once for the same offering.
**Open decisions:** Enrollment start/end timestamps and timezone, authoritative active-status source, capacity semantics/waitlist, prerequisite evaluation and exceptions, concurrency/race-condition handling, cancellation/withdrawal policy, error-code names/schema, and final API field naming/contract. **University Management is identified as the stakeholder responsible for enrollment dates; the Administrators role mapping and configuration authority must be confirmed by the team.**

<a id="fr-06-enter-or-update-grades-for-assigned-courses"></a>
### FR-06 — Enter or update grades for assigned courses (trace: PB-06)
**Actor:** Instructor  
**Preconditions:** Instructor authenticated; instructor assigned to course offering; student enrolled in course; grading scale and grade-entry window approved.  
**Normal scenario:** Instructor selects an assigned course and enrolled student; enters grade; system validates range and relationship; saves; grade can be retrieved by authorized later request.  
**Alternate/error scenarios:** Out-of-range grade, student not enrolled, instructor not assigned, or unauthorized actor is rejected; rejected request does not create/modify a grade. Authenticated unauthorized actor receives 403.  
**Acceptance criteria:** Only assigned instructor can grade course; grade values within approved scale; only enrolled students can receive course grades; saved grade retrievable; permission enforced with 403; rejected request has no persistence side effect.  
**Approved data/API decision:** A `Grade` shall be associated with a `Registration`. A separate GET operation shall allow an authorized Instructor to retrieve grades for the relevant course offering/registrations. The exact route, response schema, and instructor authorization scope must be specified in the OpenAPI contract.
**Open decisions:** Grading scale/range, decimal precision, grade types, grade edit deadline, audit trail, publication workflow, error mapping, and exact GET operation contract.

<a id="fr-07-view-own-published-grades"></a>
### FR-07 — View own published grades (trace: PB-07)
**Actor:** Student  
**Preconditions:** Student is authenticated and authorized to view their own grades; the grades query has completed successfully. The query may return zero records.  
**Normal scenario:** Student opens the grades view; the system completes the query and returns only that student's published grades and authorized fields.  
**Successful empty-result scenario:** If the query completes successfully and returns zero published grades, the system presents the empty state `No published grades are available.` This is a successful result, not a loading state or an error.  
**Loading state:** While the query is still in progress, the UI presents a loading state and does not present the successful-empty message.  
**Error scenarios:** If the API/query fails, the system presents a distinct error state and does not present the successful-empty message. An attempt to access another student's grades through a direct request is denied with 403 and does not disclose protected information.  
**Acceptance criteria:** (1) A successful query with one or more published grades displays only the student's own authorized grades. (2) A successful query returning zero published grades displays `No published grades are available.` (3) An in-progress query displays a loading state, not the empty state. (4) A failed API/query displays a distinct error state, not the empty state. (5) Unpublished grades remain hidden. (6) Cross-student access is denied with 403.  
**Open decisions:** Publication trigger/authority, displayed fields, term/course sorting, grade visibility changes after publication, empty-state wording approval, exact loading/error presentation and API mapping.

## 6. Data Requirements and Data Decisions

| Data entity | Draft minimum information/relationships | Decisions still needed |
|---|---|---|
| Student | **Candidate fields:** student number (unique), first name, last name, email, program/department, student status | Confirm required/optional fields, formats, allowed status values, authoritative source, privacy/retention, and whether additional fields are needed. |
| Course | **Candidate fields:** course code, title, description, credits, department, term/course offering, capacity, assigned instructor(s) | Confirm required/optional fields, code uniqueness scope, term/offering model, capacity handling, course lifecycle, and instructor assignment model. |
| Course Offering | **Approved relationship:** each Course Offering belongs to one Course and one Term. | Confirm offering identifier, section/instructor assignment, capacity, lifecycle and required fields. |
| Registration | **Approved relationship:** each Registration belongs to one Student and one Course Offering; `(studentId, courseOfferingId)` is unique. Candidate fields: registration ID, student ID, course offering ID, status, created/enrolled timestamp. | Confirm status values, timestamp/timezone, withdrawal/cancellation, capacity concurrency, waitlist and prerequisite handling; align API naming (`Registration` vs `Enrollment`). |
| Grade | **Approved relationship:** each Grade is associated with one Registration. Candidate fields: grade ID, registration ID, grade value, publication status, created/updated timestamps. | Confirm grade scale/precision/type, edit deadline, audit fields, publication authority/trigger, visibility policy, and Instructor GET scope/contract. |
| User/account | **Candidate fields:** user ID, login identifier, credential reference (not plaintext password), system role, account status | Confirm account provisioning, role assignment, account status values, credential/session controls, and security policy. |


## 7. Business Rules
- BR-01: Only active students may enroll.
- BR-02: Enrollment requests are accepted only during the configured open period.
- BR-03: A student must not have more than one Registration for the same Course Offering (the specific course section/branch). The pair `(studentId, courseOfferingId)` must be unique. A repeated attempt for the same student and Course Offering must be rejected. The exact API error response remains subject to OpenAPI alignment.
- BR-04: Course capacity is enforced.
- BR-05: Prerequisites are enforced where applicable.
- BR-06: Only an instructor assigned to the course offering may enter its grades.
- BR-07: Grades are visible to students only after publication and only for the requesting student.
- BR-08: Authorization is enforced server-side.
- BR-09: Rejected create/update/enrollment/grade operations must not persist partial or unintended changes.

## 8. Non-Functional Requirements (initial proposals; pending QA/team confirmation)
These are candidate quality requirements, not approved targets. Ahmet and the team should confirm measurable thresholds, test methods, and feasibility before baselining.

- NFR-SEC-01: Authorization shall be enforced by the server/API for every protected operation, including requests sent directly to the API. **Verification:** positive and negative authorization tests.
- NFR-SEC-02: A student shall not retrieve another student's protected academic records. **Verification:** cross-account access tests using synthetic accounts.
- NFR-SEC-03: Authentication failures shall not disclose whether a username/account exists. **Verification:** compare responses for unknown account and incorrect credential cases.
- NFR-DATA-01: Required-field, format, and uniqueness validation shall reject invalid data without persisting partial changes. **Verification:** invalid-input and duplicate tests.
- NFR-TEST-01: Each approved functional requirement shall have at least one positive test and, where applicable, negative/alternate-path tests with observable expected outcomes.
- NFR-AUD-01 (**OPEN**): Define which record changes must be logged, the fields captured, access to logs, and retention.
- NFR-PERF-01 (**OPEN**): Agree measurable response-time and concurrency targets and the test conditions before implementation/verification.
- NFR-AVAIL-01 (**OPEN**): Define availability, backup, and recovery expectations only if required for this project scope.
- NFR-ACCESS-01 (**OPEN**): Confirm accessibility/usability requirements and test criteria, if applicable to the course scope.


## 8.1 Approved architecture and data-model decisions — Product Owner record for PR #43

The following four product decisions are **APPROVED (PO approval)**. This section is the explicit repository record requested in the review. Approval of a product decision does not mean that Arda has completed its OpenAPI representation or implementation.

| Decision | Approved product decision | Related SRS trace | Implementation / contract status |
|---|---|---|---|
| PD-01 — JWT/session lifecycle | JWT includes a `sid` (`sessionId`) claim. Logout revokes the corresponding server-side session; a revoked session must not authorize subsequent protected requests. | FR-01 / PB-01 | **TODO — Arda:** update and verify OpenAPI token/session/logout contract. Expiry/refresh policy remains **Pending**. |
| PD-02 — Registration relationships | Each `Registration` references exactly one `Student` and one `CourseOffering`. Each `CourseOffering` references one `Course` and one `Term`. | FR-05 / PB-05 | **TODO — Arda:** map approved relationships into OpenAPI schemas and operations; align `Registration` / `Enrollment` naming. |
| PD-03 — Duplicate registration per course section | A student must not register more than once for the same `CourseOffering` (the particular course section/branch). The unique pair is `(studentId, courseOfferingId)`. This is the approved rule recorded as **BR-03**. | BR-03; FR-05 / PB-05 | Product rule **Approved**. **TODO — Arda:** represent the constraint and conflict behavior consistently in the API/data contract. Exact HTTP error schema remains **Pending**. |
| PD-04 — Grade relationship | Each `Grade` references exactly one `Registration`. | FR-06 / PB-06 | Product relationship **Approved**. **TODO — Arda:** reflect it in OpenAPI and define the separate Instructor grade-retrieval GET route, response schema and authorization scope. |

These approvals do not decide credential policy, token expiry/refresh, enrollment dates/capacity/prerequisite/waitlist/withdrawal rules, grading scale/editing/publication policy, or unspecified endpoint details. Those remain **Pending** with the relevant decision owners.

## 8.2 Cross-check against Arda's Sprint 2 architecture proposal (PR #47)

This is a documentation cross-check against the diagrams visible in the open PR #47. The diagrams are proposed architecture evidence; they do not establish that the OpenAPI contract or implementation has been updated, and PR #47 is not treated as merged or approved as a whole.

| PR #47 artifact | What the visible proposal depicts | SRS alignment / remaining boundary |
|---|---|---|
| `Sprint2_Domain_Class.svg` | Student, Course, CourseOffering, Term, Registration/Enrollment, Grade and account/role concepts; Registration connects Student and CourseOffering; CourseOffering connects Course and Term; Grade connects to Registration. | Matches PD-02 and PD-04. Treat class diagram as a proposed logical model, not a physical schema or OpenAPI implementation. |
| `Sprint2_Sequence_Enrollment.svg` | Student submits a registration request; validation and authorization occur; success and conflict branches are shown. | Matches the Course Enrollment flow and PD-02/PD-03. Specific conflict codes/messages, identity source and API schema remain TODO/Pending. |
| `Sprint2_Sequence_Grade_Entry.svg` | Instructor grade-entry flow references Registration; grade validation and authorization are shown. | Matches Grade → Registration. Instructor retrieval is not finalized by this entry flow; separate GET route/schema/scope remain TODO — Arda. |
| `Sprint2_Sequence_Published_Grades.svg` | Student requests published grades; successful response branches include records and an empty collection. | Supports FR-07 successful-empty distinction. API/query failure and loading remain separate UI states under FR-07; exact response contract remains to be aligned. |
| `Sprint2_Sequence_Session_Lifecycle.svg` | JWT bearer/session reference, server-side session validation, logout revocation and replay rejection are depicted. | Matches PD-01 at logical level. The diagram itself notes a contract mismatch; `sid`, logout route/response and protected-operation security still require OpenAPI alignment. |
| `Sprint2_Container.svg` and `Sprint2_Component.svg` | Proposed frontend/API/backend and logical component responsibilities; deployment/implementation choices remain pending. | Consistent with this SRS being a requirements draft. Do not infer a selected technology, deployed service or completed backend. |

**Scope of PO approval:** PD-01 to PD-04 in Section 8.1 are the only decisions recorded as approved here. This does not approve the entire architecture, role/record authorization matrix, token expiry/refresh, enrollment eligibility policies, grading/publication policies, PATCH policies, OpenAPI alignment, or the SRS/backlog as a whole.

## 9. OpenAPI contract comparison (repository `develop`)

**Evidence source:** [`api/openapi.yaml`](https://github.com/mert494/student-information-system/blob/develop/api/openapi.yaml), OpenAPI 3.1.0, draft `0.1.0-draft`. This is a repository snapshot; reviewers should compare against the current `develop` version before baselining. The source explicitly says it is proposed and not ready for consumption. The four architecture/data-model decisions below are approved by the Product Owner and explicitly recorded for PR #43 review. The current OpenAPI draft has not yet been updated to evidence them; concrete contract changes are **TODO — Arda**. Remaining policy questions are separately marked **Pending**.

**Implementation status (do not confuse with decision status):**
- [ ] **TODO — Arda:** add `sid` to the session/token contract and define logout revocation behavior; verify protected-operation security.
- [ ] **TODO — Arda:** map Registration to Student + CourseOffering, CourseOffering to Course + Term, and represent the unique `(studentId, courseOfferingId)` constraint in the contract/data model.
- [ ] **TODO — Arda:** represent Grade → Registration and add a separate Instructor grade-retrieval GET operation with route, response schema, and authorization scope.
- **Pending:** credential expiry/refresh, enrollment policies, grading/publication policies, exact field naming and unresolved authorization/error details.

| OQ | SRS/PB | Exact OpenAPI evidence | Difference requiring decision | Decision owner | Status |
|---|---|---|---|---|---|
| OQ-02 | FR-01 / PB-01 | `POST /sessions`, `createSession`, `SignInRequest`, `SessionResponse.sessionId` (lines 44–76, 472–494); global `bearerAuth` JWT (41–42, 439–445); operation has `security: []` | Approved: JWT contains `sid` and logout revokes the server-side session. Arda must align token/session schemas and protected-operation security with this decision; credential policy, expiry and refresh remain open. | Arda + team; PO decision recorded | Product decision approved; OpenAPI update TODO — Arda |
| OQ-03 | FR-03 / PB-03 | `POST /students`, `createStudent`; `StudentInput.studentNumber`, `StudentInput.fullName` (121–156, 495–517) | SRS candidate data lists firstName/lastName; OpenAPI has fullName and no firstName/lastName. Decide canonical fields, requiredness and studentNumber mutability. | PO + Arda + team | Pending |
| OQ-05 | FR-05 / PB-05 | `POST /registrations`, `createRegistration`; `RegistrationInput.courseId`, `term`, `status`; only `courseId` required (329–366, 544–570) | PD-02 and PD-03 approved: Registration → Student + CourseOffering; CourseOffering → Course + Term; BR-03 prohibits duplicate registration for the same student and CourseOffering using unique `(studentId, courseOfferingId)`. Arda must map the approved model to request/response schemas and resolve whether student identity is derived from the authenticated principal; Enrollment vs Registration terminology must be consistent. | PO + Arda + team | Product decision approved; OpenAPI mapping TODO — Arda |
| OQ-07 | FR-06/FR-07; PB-06/PB-07 | `PUT /registrations/{registrationId}/grade`, `recordGrade`; `GET /grades`, `listMyPublishedGrades`; `Grade.published` (367–438, 571–600) | Approved: Grade → Registration and a separate GET operation shall support authorized Instructor grade retrieval. Arda must define the route, response schema and instructor assignment scope. The existing student published-grade GET remains distinct; its example has `published: false` and still needs correction/clarification. | Arda + academic stakeholder + team | Product decision approved; OpenAPI mapping TODO — Arda |
| OQ-12 | FR-03 / PB-03 | `PATCH /students/{studentId}`, `updateStudent`; body `$ref: StudentInput`; responses include 404 (157–195) | Define mutable fields, requiredness, omission/null behavior, unknown/immutable field handling and no-op behavior. | Arda + PO + team | Pending |
| OQ-13 | FR-04 / PB-04 | `PATCH /courses/{courseId}`, `updateCourse`; body `$ref: CourseInput`; responses include 404 (261–299) | Define mutable fields, requiredness, omission/null behavior, unknown/immutable field handling and no-op behavior. | Arda + PO + team | Pending |

### PATCH scenario matrix — policies remain Pending where owner decision is required

The OpenAPI draft defines PATCH routes but does not define dedicated patch schemas or omission/null semantics. These are distinct scenarios; listing them does not pre-approve a response policy.

| Case | Student PATCH scenario | Course PATCH scenario | Policy / expected result |
|---|---|---|---|
| Missing target | PATCH an unknown `studentId` | PATCH an unknown `courseId` | OpenAPI lists 404 NotFound. Confirm error envelope/code and ensure no record is created. Pending OQ-08. |
| Unique-value collision | Change `studentNumber` to a value already used by another student (if mutable) | Change a unique course field (for example `courseCode`, if unique at the approved scope) to a value already used by another course | Must be distinguished from a repeated request. Decide conflict response/code and field-level message; reject without overwriting the other record. Pending OQ-12/OQ-13 and uniqueness-scope decisions. |
| Omitted field | Send only one mutable candidate field; omit another existing field | Same | Decide whether omitted fields remain unchanged. Pending OQ-12/OQ-13. |
| Explicit null | Send a candidate field explicitly as `null` | Same | Decide per-field whether null clears a nullable value or is rejected; do not treat null as omission without an explicit rule. Pending. |
| Immutable field | Include an identifier or field declared immutable | Same | Decide whether request is rejected or field ignored; define validation/error mapping. Pending. |
| Unknown field | Include an undeclared property | Same | Decide reject vs ignore; current input schemas do not set `additionalProperties: false`. Pending. |
| Same-value no-op | Set a field to its current value | Same | Decide whether accepted as a successful no-op and whether `updatedAt`/audit data changes. This is not the same as a repeated state-changing request. Pending. |
| Repeated state-changing submission | Submit the same state-changing PATCH request again after the first submission changed the resource | Same | Keep distinct from a same-value no-op: decide whether the repeated request is idempotent, whether side effects/audit events repeat, and whether an idempotency mechanism is required. Pending. |
| Invalid value | Submit an invalid candidate value | Same | Reject without partial unintended persistence; exact validation/error mapping pending. |
| Unauthorized caller | Unauthenticated / insufficient role | Unauthenticated / insufficient role | OpenAPI lists 401/403; confirm role matrix and response contract. Pending OQ-01/OQ-08. |

## 10. Traceability Matrix (SRS ↔ Product Backlog)

| SRS ID | Requirement | Backlog item | Priority (proposal) | Story points (proposal) |
|---|---|---|---|---|
| FR-01 | Authentication | PB-01 | P1 | 5 |
| FR-02 | Authorization | PB-02 | P1 | 5 |
| FR-03 | Student records | PB-03 | P1 | 5 |
| FR-04 | Course records | PB-04 | P1 | 5 |
| FR-05 | Course Enrollment | PB-05 | P1 | 8 |
| FR-06 | Instructor grades | PB-06 | P2 | 8 |
| FR-07 | Published grades for student | PB-07 | P2 | 3 |

## 11. Open Questions / Decision Log

The entries below are open proposals, not approved decisions. When an item is closed, record the decision, owner, date, and evidence link (meeting note, issue comment, PR review, policy source, or approved document).

| ID | Question | Owner to consult | Status | Decision / evidence |
|---|---|---|---|---|
| OQ-01 | Final role-to-operation and role-to-data matrix | Product Owner + Arda + team | Open | Pending |
| OQ-02 | Authentication method, session/token policy, credential controls | Arda / Architecture Lead; Product Owner for product policy | Partially decided | **Approved by PO:** JWT carries `sid`; logout revokes the corresponding server-side session. **TODO — Arda:** align token/session/logout schema, route and protected-operation security in OpenAPI. Credential policy, expiry/refresh, exact route and response remain **Pending**. Evidence: PR #47 session-lifecycle proposal; contract mismatch remains explicitly noted. |
| OQ-03 | Student required fields/status values and authoritative source | Product Owner + team | Open | Pending |
| OQ-04 | Course fields and course-code uniqueness scope | Product Owner + team | Open | Pending |
| OQ-05 | Enrollment period dates/timezone and configuration authority; Registration/CourseOffering mapping | Product Owner; University policy stakeholder; Arda / team for API mapping | Partially decided | **Approved by PO:** Registration → Student + CourseOffering; CourseOffering → Course + Term; BR-03 prohibits duplicate Registration for the same student and CourseOffering using unique `(studentId, courseOfferingId)`. **TODO — Arda:** map to OpenAPI schemas/operations and resolve authenticated-student identity source. Enrollment dates/timezone, configuration authority, capacity, prerequisites, waitlist, withdrawal and error contract remain **Pending**. Evidence: PR #47 class/enrollment sequence proposals. |
| OQ-06 | Capacity, waitlist, prerequisite rules and race-condition behavior | Product Owner + Arda/team | Open | Pending |
| OQ-07 | Grade scale, precision, grade editing and publication policy; Grade relationship and Instructor read operation | Product Owner; academic stakeholder; Arda / team for API mapping | Partially decided | **Approved by PO:** Grade → Registration. **TODO — Arda:** define a separate Instructor grade-retrieval GET route, response schema and authorization scope in OpenAPI. Grading scale, precision, editing, publication authority, student published-grade query contract and Instructor access scope remain **Pending**. Evidence: PR #47 grade-entry/published-grade sequence proposals. |
| OQ-08 | API error-code names and error response schema | Arda | Open | Pending |
| OQ-09 | Data ownership, classification, retention and audit trail | Team/QA | Open | Pending |
| OQ-10 | Measurable performance, availability and recovery targets | Ahmet + team | Open | Pending |
| OQ-11 | Confirm external actors/systems/interactions | Arda/team | Open | Pending |
| OQ-12 | Student PATCH: unique-value collision, repeated state-changing submission, same-value no-op, omitted/null/immutable/unknown fields | Arda + PO + team | Open | Pending |
| OQ-13 | Course PATCH: unique-value collision, repeated state-changing submission, same-value no-op, omitted/null/immutable/unknown fields | Arda + PO + team | Open | Pending |

## 12. Review and Evidence Tracker

| Review / decision | Reviewer or decision owner | Required evidence | Status | Evidence link / date |
|---|---|---|---|---|
| Scope, stakeholders, business rules approval | Product Owner + team | Explicit approval comment or meeting record | Pending | TBD |
| Role/permission and API feasibility | Arda + team | Review comments, API mapping/contract evidence | Pending | TBD |
| Requirement scenario/testability review | Ahmet | Positive/negative testability review notes | Pending | TBD |
| Data and enrollment decisions | Product Owner + team | Decision-log entries with rationale | Pending | TBD |
| Grade and publication decisions | Academic stakeholder/team | Approved rule/source and decision log | Pending | TBD |
| Priority and estimates | Product Owner/team | PO priority confirmation and team estimation record | Pending | TBD |
| Sprint commitment | Team | Agreed sprint scope/commitment record | Pending | TBD |

## 13. Review Checklist
- [ ] Product Owner confirms candidate scope, stakeholder-role mapping, and business rules.
- [ ] Team confirms which assumptions become requirements and which remain out of scope.
- [ ] Arda reviews API feasibility, boundary, data model, permissions, and response-code consistency.
- [ ] Ahmet reviews testability, negative/alternate scenarios, and measurable NFR targets.
- [ ] Team confirms data fields, status values, enrollment/grading policies, priorities, and estimates.
- [ ] Assign owners only after team agreement; record approval evidence/decision links.
- [ ] Update version and review status; keep unresolved decisions marked OPEN.


## Cross-reference index (FR → BR/NFR)

| FR | Related BR | Related NFR | Backlog |
|---|---|---|---|
| FR-01 | — | NFR-SEC-03 | PB-01 |
| FR-02 | BR-08 | NFR-SEC-01, NFR-SEC-02 | PB-02 |
| FR-03 | BR-09 | NFR-DATA-01, NFR-AUD-01 (OPEN) | PB-03 |
| FR-04 | BR-09 | NFR-DATA-01, NFR-AUD-01 (OPEN) | PB-04 |
| FR-05 | BR-01–BR-05, BR-09 | NFR-DATA-01, NFR-PERF-01 (OPEN) | PB-05 |
| FR-06 | BR-06, BR-09 | NFR-SEC-01, NFR-AUD-01 (OPEN) | PB-06 |
| FR-07 | BR-07 | NFR-SEC-02 | PB-07 |
