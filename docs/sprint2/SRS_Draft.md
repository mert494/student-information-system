# Student Information System (SIS) — Software Requirements Specification (SRS)

**Version:** Draft 0.3  
**Sprint:** 2  
**Status:** Working draft; pending Product Owner/team approval and technical/QA review  
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

### FR-01 — Authenticate user (trace: PB-01)
**Actor:** Any user with an assigned system role  
**Preconditions:** Account exists and is eligible to authenticate; authentication mechanism configured.  
**Normal scenario:** (1) User submits credentials. (2) System validates credentials. (3) System establishes authenticated session/token. (4) User can access authorized protected operations.  
**Alternate/error scenarios:** Invalid credentials are rejected with a generic message that does not reveal whether the account exists. A logged-out user attempting a protected operation receives 401 Unauthorized.  
**Acceptance criteria:** Valid credentials authenticate; invalid credentials fail; failure message is account-enumeration-safe; after logout, protected operations require re-authentication.  
**Open decisions:** Credential policy, lockout/rate limiting, session/token type, expiration, logout semantics, account activation rules.

### FR-02 — Enforce role and record authorization (trace: PB-02)
**Actor:** Any authenticated user performing a protected operation; authorization rules are administered by an authorized role (to be confirmed)  
**Preconditions:** User authenticated; role/permission matrix approved.  
**Normal scenario:** API evaluates user's role and requested operation/data scope; allowed request proceeds.  
**Alternate/error scenarios:** Unauthenticated request returns 401 Unauthorized; authenticated but unauthorized request returns 403 Forbidden with an error code and message; a Student attempting another student's protected record is denied, including direct API requests.  
**Acceptance criteria:** Authorization is enforced at API level; no unauthorized operation or protected data is exposed; 401 and 403 are distinct outcomes.  
**Open decisions:** Exact permission matrix, role assignment process, administrative permission management, error-code catalog.

### FR-03 — Create, list, and update student records (trace: PB-03)
**Actor:** Authorized Student Affairs Staff  
**Preconditions:** Authenticated staff member has student-record permission; student data schema and required fields approved.  
**Normal scenario:** Staff enters required student fields; system validates; system creates record; authorized listing returns it. Staff requests an update to an existing record using the agreed update operation (PATCH semantics are proposed for confirmation); the system validates only submitted, permitted fields, persists the accepted changes, and subsequent reads reflect the updated values. If the target student record does not exist, the system returns a not-found response and makes no changes.  
**Alternate/error scenarios:** Missing/invalid fields are rejected; duplicate student number is rejected; unauthorized user cannot create/update; failed validation does not create or alter a record.  
**Acceptance criteria:** Required-field validation on creation; student number uniqueness; role authorization; successful update visible in subsequent reads; nonexistent target returns not-found; update fields are restricted to an approved allowlist; invalid requests rejected without persistence.  
**Open decisions:** Student field list, format/validation rules, identifier source, allowed status values, mutable-field allowlist, PATCH vs PUT contract and null/omitted-field semantics, not-found response contract, deletion/archive policy, audit logging.

### FR-04 — Create and update course records (trace: PB-04)
**Actor:** Authorized Student Affairs Staff  
**Preconditions:** Authenticated user has course-management permission; course/term data model and uniqueness scope approved.  
**Normal scenario:** Staff enters course fields; system validates; course is created. Staff requests an update to an existing course using the agreed update operation (PATCH semantics are proposed for confirmation); only permitted submitted fields are validated and saved. If the target course does not exist, the system returns not-found and makes no changes.  
**Alternate/error scenarios:** Missing/invalid creation fields are rejected; duplicate course code within the agreed uniqueness scope is rejected; unauthorized changes are denied; updates to nonexistent courses return not-found; unknown, immutable, or disallowed update fields are rejected or handled according to an approved contract.  
**Acceptance criteria:** Required fields validated on creation; duplicate prevention applies; unauthorized changes denied; new course appears in course list; successful updates are reflected in subsequent reads; nonexistent targets return not-found; updates are limited to an approved field allowlist; invalid requests do not persist.  
**Open decisions:** Course fields, code uniqueness scope, term/offering structure, course status lifecycle, mutable-field allowlist, PATCH vs PUT contract and null/omitted-field semantics, not-found response contract, edit restrictions after enrollment.

### FR-05 — Enroll in a course and view enrollments (trace: PB-05)
**Actor:** Student  
**Preconditions:** Student authenticated and active; enrollment period open; course offering exists; enrollment conditions satisfied.  
**Normal scenario:** Student selects a course offering and submits enrollment; system validates active status, period, duplicate enrollment, capacity, and prerequisites; system creates exactly one enrollment; enrollment appears in student's own enrollment list.  
**Alternate/error scenarios:** Inactive student, closed period, duplicate enrollment, full course, or unmet prerequisite are rejected with 409 Conflict and a specific error code/message. Another student's enrollments are not accessible. Rejected requests create/modify no enrollment.  
**Acceptance criteria:** Only active students enroll; enrollment period enforced; duplicate prevented; own enrollments only; capacity/prerequisites checked; each stated conflict returns 409 plus specific code/message; rejected request has no persistence side effect; success creates exactly one record.  
**Open decisions:** Enrollment start/end timestamps and timezone, authoritative active-status source, capacity semantics/waitlist, prerequisite evaluation and exceptions, term/course offering identifiers, concurrency/race-condition handling, cancellation/withdrawal policy, error-code names/schema. **University Management is identified as the stakeholder responsible for enrollment dates; the Administrators role mapping and configuration authority must be confirmed by the team.**

### FR-06 — Enter or update grades for assigned courses (trace: PB-06)
**Actor:** Instructor  
**Preconditions:** Instructor authenticated; instructor assigned to course offering; student enrolled in course; grading scale and grade-entry window approved.  
**Normal scenario:** Instructor selects an assigned course and enrolled student; enters grade; system validates range and relationship; saves; grade can be retrieved by authorized later request.  
**Alternate/error scenarios:** Out-of-range grade, student not enrolled, instructor not assigned, or unauthorized actor is rejected; rejected request does not create/modify a grade. Authenticated unauthorized actor receives 403.  
**Acceptance criteria:** Only assigned instructor can grade course; grade values within approved scale; only enrolled students can receive course grades; saved grade retrievable; permission enforced with 403; rejected request has no persistence side effect.  
**Open decisions:** Grading scale/range, decimal precision, grade types, assignment model, grade edit deadline, audit trail, publication workflow, error mapping.

### FR-07 — View own published grades (trace: PB-07)
**Actor:** Student  
**Preconditions:** Student is authenticated and authorized to view their own grade collection; the grade-query operation completed successfully. An empty-state is applicable only to a successful query returning zero published grades—not to authentication, authorization, server, or data-loading errors.  
**Normal scenario:** Student opens grades; system returns only that student's published grades and only authorized fields.  
**Alternate/error scenarios:** A successful query returning zero published grades produces the defined empty state. Loading/API failure is presented as an error state, not as an empty collection. Attempt to access another student's grades via direct request returns 403 with code/message and discloses no protected information.  
**Acceptance criteria:** Own grades only; unpublished grades hidden; empty state text is `No published grades are available.` only after a successful zero-results response; errors are not shown as empty state; cross-student access denied with 403; successful response contains only authorized information.  
**Open decisions:** Publication trigger/authority, displayed fields, term/course sorting, grade visibility changes after publication, empty-state wording approval, API mapping.

## 6. Data Requirements and Data Decisions

| Data entity | Draft minimum information/relationships | Decisions still needed |
|---|---|---|
| Student | **Candidate fields:** student number (unique), first name, last name, email, program/department, student status | Confirm required/optional fields, formats, allowed status values, authoritative source, privacy/retention, and whether additional fields are needed. |
| Course | **Candidate fields:** course code, title, description, credits, department, term/course offering, capacity, assigned instructor(s) | Confirm required/optional fields, code uniqueness scope, term/offering model, capacity handling, course lifecycle, and instructor assignment model. |
| Enrollment | **Candidate fields:** enrollment ID, student number, course offering ID, term, enrollment status, created/enrolled timestamp | Confirm status values, timestamp/timezone, withdrawal/cancellation, duplicate key, capacity concurrency, waitlist and prerequisite handling. |
| Grade | **Candidate fields:** grade ID, student number, course offering ID, instructor ID, grade value, publication status, created/updated timestamps | Confirm grade scale/precision/type, edit deadline, audit fields, publication authority/trigger, and visibility policy. |
| User/account | **Candidate fields:** user ID, login identifier, credential reference (not plaintext password), system role, account status | Confirm account provisioning, role assignment, account status values, credential/session controls, and security policy. |


## 7. Business Rules
- BR-01: Only active students may enroll.
- BR-02: Enrollment requests are accepted only during the configured open period.
- BR-03: Duplicate student-course-term enrollment is prohibited.
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

## 9. Traceability Matrix (SRS ↔ Product Backlog)

| SRS ID | Requirement | Backlog item | Priority (proposal) | Story points (proposal) |
|---|---|---|---|---|
| FR-01 | Authentication | PB-01 | P1 | 5 |
| FR-02 | Authorization | PB-02 | P1 | 5 |
| FR-03 | Student records | PB-03 | P1 | 5 |
| FR-04 | Course records | PB-04 | P1 | 5 |
| FR-05 | Enrollment | PB-05 | P1 | 8 |
| FR-06 | Instructor grades | PB-06 | P2 | 8 |
| FR-07 | Published grades for student | PB-07 | P2 | 3 |

## 10. Open Questions / Decision Log

### API contract alignment — comparison required (no mismatch is asserted until Arda verifies the current OpenAPI file)

| Topic | SRS candidate expectation | OpenAPI evidence to inspect | Decision / status | Owner |
|---|---|---|---|---|
| Authentication | Credential submission, session/token behavior, logout and protected-operation outcomes | Actual login endpoint, request/response schemas, auth scheme, error codes, logout/expiry coverage | Pending comparison; do not assume contract supports all SRS statements | Arda + team |
| Student fields | Candidate fields listed in Section 6; requiredness, formats and mutability are undecided | Student schema required/optional properties, formats, IDs, status enum, update endpoint/method | Pending comparison and PO data-field decision | Arda + PO |
| Enrollment | Active student, period, duplicate, capacity and prerequisite rules; successful creation and own-list visibility | Enrollment endpoints, request identifiers, response codes, rule/error schema, collection/read endpoints | Pending comparison; business rules require confirmation | Arda + PO/team |
| Grade entry/publication | Instructor assignment, enrolled student, approved range, saved grade and publication state | Grade endpoints/schema, assignment authorization, update method, publication fields/operation, student grade response | Pending comparison; grading/publication policy unresolved | Arda + academic stakeholder/PO |
| Student/course updates | Not-found handling; allowed mutable fields; update semantics; no unintended changes | PATCH/PUT methods, request schema, required fields, nullable fields, response status/schema | Pending contract review; PATCH semantics are a proposal, not a confirmed API fact | Arda |

Record each confirmed difference in the table above with the exact OpenAPI operation/schema reference, agreed decision, reviewer, date, and evidence link.


The entries below are open proposals, not approved decisions. When an item is closed, record the decision, owner, date, and evidence link (meeting note, issue comment, PR review, policy source, or approved document).

| ID | Question | Owner to consult | Status | Decision / evidence |
|---|---|---|---|---|
| OQ-01 | Final role-to-operation and role-to-data matrix | Product Owner + Arda + team | Open | Pending |
| OQ-02 | Authentication method, session/token policy, credential controls | Arda/team | Open | Pending |
| OQ-03 | Student required fields/status values and authoritative source | Product Owner + team | Open | Pending |
| OQ-04 | Course fields and course-code uniqueness scope | Product Owner + team | Open | Pending |
| OQ-05 | Enrollment period dates/timezone and configuration authority | University policy stakeholder + team | Open | Pending |
| OQ-06 | Capacity, waitlist, prerequisite rules and race-condition behavior | Product Owner + Arda/team | Open | Pending |
| OQ-07 | Grade scale, precision, grade editing and publication policy | Academic stakeholder + team | Open | Pending |
| OQ-08 | API error-code names and error response schema | Arda | Open | Pending |
| OQ-09 | Data ownership, classification, retention and audit trail | Team/QA | Open | Pending |
| OQ-10 | Measurable performance, availability and recovery targets | Ahmet + team | Open | Pending |
| OQ-11 | Confirm external actors/systems/interactions | Arda/team | Open | Pending |

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
