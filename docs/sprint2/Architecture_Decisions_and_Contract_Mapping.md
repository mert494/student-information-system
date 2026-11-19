# Sprint 2 Architecture Decisions and Contract Mapping

**Status:** Draft — proposed architecture analysis; no technology, database, authentication-provider, deployment, or role-permission decision is approved by this document.

**Scope:** Issue [#34](https://github.com/mert494/student-information-system/issues/34) only (planning task S2-09). This is a logical architecture and contract-mapping draft, not an implementation or a new API contract.

**Source baselines:** `develop` at `ee5c64b0730551e8d5a1699a209fdfaef1cb380f`; Nurefşan's PR #43 source branch at `a9b6b4819ca18146e4e2b72346405283dbdd0c60` for `SRS_Draft.md` and `Refined_Backlog_Draft.md` (not present on this `develop` baseline); Ahmet's PR #45 source branch at `63ca3e8c8efc57637185808a6f1981a7561c09d5` for `NFR_Quality_Measures.md` (not present on this `develop` baseline). Live PR metadata could not be retrieved during this review; these are fetched remote branch contents.

## 1. Decision status and evidence rules

| Status | Meaning in this document |
| --- | --- |
| **Proposed** | A candidate model, requirement, or choice appears in a draft source or is presented here for review. It is not an approval. |
| **Pending** | Required owner/team evidence or a decision is absent. Keep dependent mappings provisional. |
| **Approved** | An explicit approval is recorded in an authoritative source with its evidence. No architecture, database, identity-provider, or deployment decision in this document is marked Approved. |

The SRS and refined backlog in PR #43 are Draft 0.3 and remain pending Product Owner/team approval and technical/QA review. Their FR, entity, rule, and NFR labels are used below as **provisional traceability identifiers**, not accepted requirements. Ahmet's NFR and quality-measures draft in PR #45 is also Proposed/Open, with no approved target or test result. `docs/sprint2/Sprint2_Requirements_Traceability.md` and `docs/sprint2/Sprint2_Gap_Analysis.md` are planning evidence; neither approves product behavior.

## 2. Architecture context and scope

The existing System Vision and Boundary describes one conceptual Student Information System (SIS) with four proposed system roles: Student, Instructor, Student Affairs Staff, and Administrators. The final role-to-operation and role-to-data matrix is still open. The Boundary proposes no external systems for Sprint 1 pending team confirmation; PR #43 likewise identifies no confirmed integrations. No external provider or integration is treated here as present.

The existing OpenAPI contract is a provisional document with 12 operations. Its OpenAPI 3.1.0 format is a candidate, `http://localhost:8080` is explicitly a proposed local placeholder, and no live server or deployment is asserted. A root bearer security requirement and JWT format are proposed; the authentication/session policy is pending. `POST /sessions` explicitly has `security: []`.

Issue #34 covers architecture rationale, logical responsibilities, interfaces, data/API mapping, and NFR implications. This document does not specify a backend, deployment topology, framework, database engine, authentication provider, or new endpoint. Logical responsibilities below do not imply separate processes, services, teams, or deployable units.

### 2.1 Candidate logical components

These are responsibility groupings for discussion, not a selected component or deployment architecture.

| Candidate logical responsibility | Proposed responsibilities | Provided interface in current contract | Consumed interface / dependency |
| --- | --- | --- | --- |
| API contract boundary | Describe request/response shapes, operation identifiers, shared errors, and the proposed security declaration. | The 12 OpenAPI operations listed in §4. | Candidate clients; no UI or running API is established. |
| Identity and session responsibility | Authenticate a user, establish a session/token, and support sign-out. | `createSession`, `deleteCurrentSession`. | Credential/account policy and session/token lifecycle are open. |
| Authorization decision responsibility | Evaluate protected operation and record access at the API boundary. | Cross-cutting behavior on protected operations; no dedicated PB-02 operation. | Approved role/record permission matrix; ownership and assignment data. |
| Student information responsibility | Create, list, and update candidate student records. | `listStudents`, `createStudent`, `updateStudent`. | Approved Student fields, source of truth, status, and authorization rules. |
| Course catalog responsibility | List, create, and update candidate course records. | `listCourses`, `createCourse`, `updateCourse`. | Approved Course and term/offering model, uniqueness scope, and permissions. |
| Enrollment responsibility | List the requesting user's registrations and submit enrollment requests. | `listMyRegistrations`, `createRegistration`. | Student status, course offering, term, enrollment period, capacity, prerequisites, and duplicate rules; all require owner confirmation. |
| Grade management and publication responsibility | Record a grade and expose the proposed student published-grade listing. | `recordGrade`, `listMyPublishedGrades`. | Enrollment, instructor assignment, grade scale, publication policy, and role/data permissions. |
| Conceptual data responsibility | Represent candidate account, student, course/offering, registration, and grade information and their constraints. | No data-store interface is defined by the OpenAPI contract. | A selected persistence design is not present; database engine and deployment are undecided. |

### 2.2 Candidate dependencies and boundaries

- Protected API operations depend on authentication; authorization additionally depends on role and record relationships. The SRS says checks must be server/API-side, but its permission matrix is OPEN.
- Candidate enrollment behavior depends on active-student status, an open enrollment period, a course offering, capacity, prerequisites, and duplicate detection. Their owners, values, and failure semantics are not fully settled.
- Candidate grade entry depends on an instructor-to-course-offering assignment and an enrollment relationship. Student visibility depends on publication policy. These relationships and policies remain pending.
- External identity, calendar, payment, and notification systems remain unconfirmed candidates. No integration interface or external dependency is specified.

## 3. Provisional requirement-to-component-to-API mapping

The FR/PB identifiers below come from PR #43's draft SRS and refined backlog. Candidate actors and permissions are also draft inputs. “Pending” means the current OpenAPI text does not establish the actor's permission or the requirement's full behavior.

| Provisional SRS / PB | Draft actor and intent | Candidate logical responsibility | Existing API mapping | Mapping status / discrepancy |
| --- | --- | --- | --- | --- |
| FR-01 / PB-01 | Any user with an assigned role; authenticate and sign out. | Identity/session | `createSession`; `deleteCurrentSession` | Proposed mapping. Credential policy, session/token type, expiry, logout invalidation, and account lifecycle are open. The `SessionResponse.sessionId` and proposed bearer/JWT security leave the token/session relationship unclear. |
| FR-02 / PB-02 | Authenticated user; protect operations and records. | Authorization decision (cross-cutting) | No dedicated operation; root security applies to protected operations; 401/403 responses are declared. | Pending. Bearer authentication and generic 401/403 do not define role permissions, own-record filtering, administrative authority, or record-level enforcement. |
| FR-03 / PB-03 | Authorized Student Affairs Staff; create/list/update students. | Student information | `listStudents`; `createStudent`; `updateStudent` | Proposed mapping. Required fields, identifiers, field formats, archive behavior, and authorization are open. `StudentInput.fullName` has no declared JSON type. |
| FR-04 / PB-04 | Authorized Student Affairs Staff; create/update courses. | Course catalog | `listCourses`; `createCourse`; `updateCourse` | Proposed mapping. Course fields, requiredness, uniqueness scope, term/offering structure, and permissions are open. `title` and `credits` have no declared JSON types. |
| FR-05 / PB-05 | Student; enroll and view own enrollments. | Enrollment | `listMyRegistrations`; `createRegistration` | Proposed mapping. SRS uses course-offering/term concepts; API `RegistrationInput` requires `courseId` and has optional, untyped `term` and `status`. Whether `courseId` identifies a course or offering is unresolved. |
| FR-06 / PB-06 | Instructor assigned to course offering; enter/update and later retrieve grades. | Grade management and publication | `recordGrade` (`PUT /registrations/{registrationId}/grade`) | **Gap:** FR-06 requires a saved grade to be retrievable by an authorized later request, but the API has no instructor grade-read/list operation. `listMyPublishedGrades` is named/described for the student published-grade use case and does not establish instructor retrieval. Do not treat it as satisfying FR-06 or invent a new endpoint. Resolve with Nurefşan before contract changes. |
| FR-07 / PB-07 | Student; view only their own published grades. | Grade publication/read | `listMyPublishedGrades` (`GET /grades`) | Proposed mapping. Own-data filtering and publication rules remain open. The current success example contains `published: false`, which conflicts with the draft's “published grades only” intent and should be corrected or explicitly reconciled by the API owner. |

PB-02 is cross-cutting and is not represented as an extra operation. The mapping is not evidence that any role is authorized to call a listed operation.

## 4. Existing API contract: inputs, outputs, errors, and authorization

Operation details below are transcribed from `api/openapi.yaml` on the stated `develop` baseline. The contract remains provisional. All operations inherit the root proposed `bearerAuth` requirement except `createSession`, which explicitly overrides it with `security: []`. That declaration does not supply role-level authorization rules.

| Method and path | Operation ID | Declared input | Success output | Declared error responses | Authorization mapping |
| --- | --- | --- | --- | --- | --- |
| `POST /sessions` | `createSession` | JSON `SignInRequest` (`username`, `password`; both required) | 200 `SessionResponse` (`sessionId`) | 400, 401, 500 | Explicit `security: []`; generic sign-in actor/credential policy pending. |
| `DELETE /sessions/current` | `deleteCurrentSession` | No body or path parameter declared | 204, no body | 401, 500 | Inherits proposed bearerAuth; how the session is identified/invalidated is pending. |
| `GET /students` | `listStudents` | No request input declared | 200 array of `Student` | 401, 403, 500 | Inherits proposed bearerAuth; role and record visibility pending. |
| `POST /students` | `createStudent` | JSON `StudentInput` | 201 `Student` | 400, 401, 403, 409, 500 | Inherits proposed bearerAuth; Student Affairs permission pending. |
| `PATCH /students/{studentId}` | `updateStudent` | Required path `studentId`; JSON `StudentInput` | 200 `Student` | 400, 401, 403, 404, 500 | Inherits proposed bearerAuth; patch semantics and permission pending. |
| `GET /courses` | `listCourses` | No request input declared | 200 array of `Course` | 401, 403, 500 | Inherits proposed bearerAuth; role and visibility pending. |
| `POST /courses` | `createCourse` | JSON `CourseInput` | 201 `Course` | 400, 401, 403, 409, 500 | Inherits proposed bearerAuth; management permission pending. |
| `PATCH /courses/{courseId}` | `updateCourse` | Required path `courseId`; JSON `CourseInput` | 200 `Course` | 400, 401, 403, 404, 500 | Inherits proposed bearerAuth; patch semantics and permission pending. |
| `GET /registrations` | `listMyRegistrations` | No request input declared | 200 array of `Registration` | 401, 403, 500 | Inherits proposed bearerAuth; identity/own-data rule pending. |
| `POST /registrations` | `createRegistration` | JSON `RegistrationInput` (`courseId` required; candidate `term`/`status` optional and untyped) | 201 `Registration` | 400, 401, 403, 404, 409, 500 | Inherits proposed bearerAuth; Student authorization and business rules pending. |
| `PUT /registrations/{registrationId}/grade` | `recordGrade` | Required path `registrationId`; JSON `GradeInput` (`value` required but untyped) | 200 `Grade` | 400, 401, 403, 404, 500 | Inherits proposed bearerAuth; instructor assignment and grade permissions pending. |
| `GET /grades` | `listMyPublishedGrades` | No request input declared | 200 array of `Grade` | 401, 403, 500 | Inherits proposed bearerAuth; own-student and published-only enforcement pending. |

The reusable `Error` schema currently has `code` and `message`; specific error-code names and per-rule behavior are not defined in the contract. The SRS draft expects distinct 401/403 outcomes, conflict cases for enrollment, and no persistence side effects for rejected changes; those business semantics still need explicit API mapping. A response declaration alone does not prove the behavior is implemented or enforced.

### 4.1 Noted contract questions

1. **FR-06 retrieval:** no instructor read/list operation exists. Confirm whether the SRS requirement changes, an existing operation is extended by an API owner, or a separately reviewed contract change is needed.
2. **Session/token shape:** sign-in returns `sessionId`, while the root proposes bearer JWT. The SRS leaves token/session type and logout semantics open. The contract does not say whether the ID is itself a token, references a server-side session, or relates to bearer credentials.
3. **Grade read example:** `GET /grades` is described as published grades but its synthetic example has `published: false`. Its example and semantics are inconsistent pending owner review.
4. **Data identifiers:** SRS candidate identifiers include `studentNumber`, `courseOfferingId`, `enrollmentId`, and `gradeId`; API uses `studentId`, `courseId`, `registrationId`, and a registration-scoped grade path. Their relationships and sources are not settled.
5. **Error coverage:** SRS describes specific 409 enrollment causes and 400 grade validation, but the OpenAPI contract reuses generic error responses. Error-code catalog and mappings remain pending.
6. **Student/Course field coverage:** The SRS lists candidate Student fields including first name, last name, email, program/department, and status, while `StudentInput` currently lists `studentNumber` and `fullName` (the latter has no JSON type). The SRS lists candidate Course fields including description, department, term/course offering, capacity, and assigned instructor(s), while `CourseInput` currently lists `courseCode`, `title`, and `credits`. These are draft-to-draft coverage differences; confirm the approved fields and requiredness with the requirements owner before changing the contract.

## 5. Technology-neutral conceptual data model

This is a candidate domain view derived from PR #43's SRS §6 and the API schemas. “Key candidate” describes a source field only; it does not declare a primary key, foreign key, database constraint, or approved schema.

| Candidate entity | Key/identifier evidence | Candidate relationships | Draft constraints and unresolved details |
| --- | --- | --- | --- |
| User / Account | SRS candidate `userId` and login identifier; API has `username` in `SignInRequest`. No account identifier contract is approved. | A user has a system role; link to Student/Instructor/administrative records is unspecified. | Account provisioning, identifier uniqueness, lifecycle, credential reference, and role assignment are open. Plaintext password storage is not proposed. |
| Student | SRS candidate `studentNumber` marked unique; API also has `studentId`. Whether one is a business identifier and the other a technical identifier is unresolved. | Student participates in candidate enrollments and has grades through enrollment/course offering. | Student fields, requiredness, source, status values, privacy, retention, and identifier source are open. |
| Course | SRS candidate `courseCode`; API has `courseId`. Code uniqueness scope is open. | Course may have term-specific offerings; relationship and offering identity are not formally modeled in the API. | Required fields, course lifecycle, uniqueness, capacity ownership, and post-enrollment edit rules are open. |
| Course Offering / Term | SRS refers to course offering, term, capacity, and assigned instructor(s); no dedicated API resource or approved key is defined. | Candidate association between Course, term, instructors, enrollments, and grades. Multiplicities are pending. | Offering key, term format, capacity/concurrency, instructor assignment, and lifecycle are open. |
| Enrollment / Registration | SRS candidates `enrollmentId`, `studentNumber`, `courseOfferingId`, `term`; API candidates `registrationId`, `courseId`, `term`, `status`. | Candidate links Student to a Course Offering. Grade may be related through registration or directly through student/offering; exact relationship is open. | SRS BR-03 proposes duplicate student-course-term enrollment prohibition; exact unique key, cancellation, timestamps, waitlist, and status values are open. |
| Grade | SRS candidate `gradeId`, student number, course offering ID, instructor ID, value, publication status; API has `registrationId`, untyped `value` and `status`, plus candidate boolean `published`. | Candidate links to a Student, Course Offering, and Instructor; API path links grade entry to Registration. Exact cardinality/versioning is open. | Scale, precision, grade types, edit lifecycle, audit data, publication trigger, and visibility are open. |

Candidate relationships, with multiplicities left unresolved:

- Student ↔ Enrollment/Registration.
- Course ↔ Course Offering/Term.
- Course Offering ↔ assigned Instructor(s).
- Course Offering ↔ Enrollment/Registration.
- Grade ↔ Student, Instructor, and Course Offering; whether Registration is the canonical grade parent is open.
- User/Account ↔ system role and any corresponding domain record.

Candidate constraints from SRS BR-01–BR-09 include active-student eligibility, enrollment-period enforcement, duplicate prevention, capacity and prerequisite checks, assigned-instructor grade entry, published-only student visibility, server-side authorization, and no unintended persistence on rejected operations. They are draft rules, not approved implementation constraints. Exact keys, nullability, uniqueness scope, cardinalities, and referential behavior require Nurefşan/team decisions.

## 6. Alternatives and rationale (for review; no selection)

| Decision area | Alternatives to evaluate | Evidence-based rationale / trade-off | Status |
| --- | --- | --- | --- |
| Application decomposition | One SIS boundary with internally separated logical responsibilities; versus separately deployed domain services. | Existing sources define one SIS boundary and no independent deployment, scale, or operational NFR. A logical decomposition is sufficient for this documentation draft; separate deployment would add interface, data-consistency, and operations questions without current evidence. This is not a final topology choice. | Proposed analysis; decision Pending. |
| Authentication/session contract | Opaque server-side session reference; bearer token; or a defined combination. No provider is selected. | Current OpenAPI simultaneously returns `sessionId` and proposes bearer JWT. SRS OQ-02 leaves lifecycle and credential controls open. Evaluate logout/revocation, expiry, account-safe failures, and operational implications before choosing. | Pending owner/team decision. |
| Persistence model | A technology-neutral entity/relationship model now; select a persistence representation/engine only when requirements and NFRs support it. | Candidate data has keys, uniqueness, and relationships that must be represented, but neither SRS nor approved NFRs selects an engine, workload, or persistence technology. A conceptual model preserves those constraints without implying a database product. | Conceptual model Proposed; engine Pending. |
| External integrations | Keep external systems outside the current proposed scope; introduce an integration only after an owner confirms the system, boundary, data exchange, and need. | Boundary §5.2 and PR #43 defer/unconfirm external integrations; identity provider, calendar, payment, and notification systems are not confirmed. Excluding them is still pending team confirmation, not an approved Sprint 2 decision. | Proposed exclusion; Pending team confirmation. |

## 7. NFR impacts and trade-offs

PR #43 labels its NFR section as initial proposals pending QA/team confirmation. The fetched PR #45 draft adds measurable security, integrity, performance, usability, accessibility, privacy, and maintainability targets, but labels them Proposed/Open. It reports no measurements or test results. Its assumed workload, performance environment, and architecture-dependent controls require review before any target can be accepted.

| Draft NFR / quality concern | Architecture impact to evaluate | Trade-off / evidence still needed |
| --- | --- | --- |
| NFR-SEC-01: API-side authorization | Authorization must apply to direct API calls, not only a future UI; map decisions to every protected operation. | Role/record matrix, ownership and instructor assignment rules, negative cases, and reviewer evidence are Pending. |
| NFR-SEC-02: own-record protection | Student data and grades require record-level checks, including cross-account requests. | Data relationships and denial behavior (403/error schema) are not fully specified; no runtime test is claimed. |
| NFR-SEC-03: account-safe authentication errors | Sign-in behavior must avoid account enumeration per the draft. | Exact messages, rate/lockout policy, session lifecycle, and test method require owner review. |
| NFR-DATA-01: validation without partial changes | Student/course/enrollment/grade writes need explicit constraints and rejected-operation semantics. | Required fields, uniqueness keys, error mapping, and transaction behavior are pending; no data-store mechanism is selected. |
| NFR-TEST-01: positive and negative coverage | Maintain a trace from approved FRs and error outcomes to verifiable scenarios. | Ahmet's NFR/verification artifact and SRS acceptance are pending; planned checks are not completed tests. |
| NFR-AUD-01: audit (OPEN) | May affect grade/student change records and data lifecycle. | Log fields, access, retention, and privacy/cost trade-offs are open. |
| NFR-PERF-01/02: performance and enrollment concurrency | Enrollment capacity and concurrent requests may affect consistency/throughput choices. | PR #45 proposes p95 and load scenarios, but expected workload, test environment, and feasibility are not approved; see §7.1. |
| NFR-AVAIL-01 (SRS OPEN) / NFR-ACCESS-01 (SRS OPEN; PR #45 proposes WCAG 2.2 AA) | Could affect recovery and accessibility/usability design. | Scope, accessibility level, target, test method, and acceptance owner remain pending; align with UX/Figma inputs. |

### 7.1 Technical feasibility assessment — PR #45 draft

This review compares the fetched PR #45 source branch (`docs/sprint2/NFR_Quality_Measures.md`, head `63ca3e8`) with the current `origin/develop` API contract at `ee5c64b` and the PR #43 SRS source branch at `a9b6b48`. The NFR document is a draft. The findings below are technical review observations, not approvals, test results, or final product requirements. No target has been benchmarked.

| NFR / target | Technical assessment against current evidence | Dependencies and clarification before acceptance |
| --- | --- | --- |
| NFR-SEC-01 — API authorization | The outcome is testable after the role matrix is defined. The proposed document check that every protected operation declares both 401 and 403 does not match the current contract: `DELETE /sessions/current` declares 401 but not 403; `POST /sessions` is explicitly exempt from inherited security. OpenAPI response declarations alone do not prove enforcement. | Define expected outcomes per role, operation, and token state (SRS OQ-01); reconcile the logout 403 expectation with the API owner. Separate contract inspection from runtime authorization testing. |
| NFR-SEC-02 — own-record isolation | Cross-account testing is feasible after permissions and identity are specified. The stated “by ID or by any filter” scope exceeds current read operations: `GET /grades` and `GET /registrations` have no declared filters or identifiers, and there is no `GET /students/{studentId}`. | Map the test cases to actual supported operations and clarify whether 403 is required for every cross-record attempt or whether a non-disclosing not-found outcome is allowed. No policy is chosen here. |
| NFR-SEC-03 — account-safe login | Matching status, error code, and message can be compared; current OpenAPI declares a generic 401 response for `createSession`, but does not prove identical runtime behavior. The proposal to measure response-time differences has no threshold or pass/fail rule. | Define timing method, sample count, acceptable variance/threshold, and noise controls, or keep timing as reported evidence rather than a pass criterion. Credential/session policy remains open (OQ-02). |
| NFR-SEC-04/05 — password handling and transport | Both are plausible security objectives, but they depend on unselected credential storage, hosting, and network boundaries. PR #45 names bcrypt/Argon2 only as examples; neither is approved. Its HTTPS/TLS target conflicts with the OpenAPI's proposed `http://localhost:8080` placeholder only if that placeholder is treated as a shared endpoint; it currently represents local development. | Keep algorithm/provider and deployment undecided. Specify whether the TLS check covers shared environments only, how TLS termination is handled, and whether HTTP must fail or may safely redirect without sending credentials. Reconcile the Boundary's HTTPS proposal with the local-only HTTP placeholder. |
| NFR-DATA-01 — rejected writes leave no changes | Snapshot comparison is a suitable post-implementation verification approach. The target depends on explicit validation rules, authorization outcomes, and persistent state; no persistence implementation exists to test now. | Define the rejected scenarios and initial state per operation, including whether the check covers audit side effects. Keep it as planned verification, not a current pass. Transaction/atomicity design remains open. |
| NFR-DATA-02 — capacity and duplicate enrollment | Capacity-one concurrency is measurable in principle. It is not yet executable against the contract: the SRS uses a course offering, while `RegistrationInput` accepts `courseId` and an untyped optional `term`, with no offering identifier/resource or approved capacity model. Fifty distinct students test the capacity race but do not test the separate same-student duplicate rule. | Confirm offering identity, capacity/waitlist semantics, student eligibility, conflict behavior, and state reset between ten runs (SRS OQ-05/OQ-06). Add a separate repeated-request case for duplicate enrollment. Persistence concurrency mechanism remains unselected. |
| NFR-PERF-01/02 — p95 and load | The 500/1000 ms and 2000 ms p95 targets, 50/300 virtual-user profiles, and proposed synthetic data sizes are measurable scenarios, not demonstrated feasible targets. A 300-VU workload may be reasonable for the stated course-project assumption, but feasibility cannot be established without an agreed server/database environment, resource limits, request mix, pacing, and observed runs. Virtual-user count does not by itself define simultaneous request concurrency. | Product Owner/team must confirm expected workload (SRS OQ-10). Define exact read/write operation sets, request distribution and pacing, warm-up, environment/resource profile, percentile window, repetitions, and error-rate denominator (including timeouts and expected 4xx). Do not claim a target met before implementation and measurement. |
| NFR-SEC-06, NFR-AUD-01, NFR-AVAIL-01 | Correctly remain Open where the SRS decision log has unresolved rate limits, audit scope/retention, or availability scope. Candidate daily backup/RPO/RTO values are not accepted targets. | Resolve OQ-02/OQ-09/OQ-10 and deployment/data-retention boundaries before selecting controls or verification environments. |
| NFR-PRIV-01, NFR-TEST-01, NFR-MAINT-01 | Synthetic-data review, requirement/test trace checks, and lint/contract checks can support Sprint 2 document QA. They do not substitute for runtime security, persistence, or performance tests. | Record source version, tool and result. The PR #45 draft says these checks are Pending; this architecture review does not run them or claim they passed. |
| NFR-USE-01/02, NFR-ACCESS-01 | Prototype walkthroughs and contrast checks are document/prototype-stage activities, but no UX/Figma artifact was found in the fetched PR #43 or the current `develop` tree. Keyboard operation and axe checks require a built interface. | Confirm UX owner, flows, tester protocol, accessibility target, and available prototype. Keep full accessibility verification as post-implementation work where appropriate. |

**Cross-document update:** The latest PR #43 SRS adds explicit Student/Course update requirements (approved mutable-field allowlist, not-found outcome, no changes on rejected requests, and omitted-versus-null/PATCH decisions). Current OpenAPI already uses PATCH and declares 404, but its schemas do not define the field allowlist or null/omitted semantics. This remains an SRS-to-contract decision and is not resolved by this review.

**Review status:** Feasibility review is preliminary and conditional. Numeric performance targets cannot be confirmed as achievable or accepted until the workload, resource profile, and environment are agreed and later measured. Security and data-integrity targets depend on the pending role/data rules and persistence/deployment decisions. No live service, test run, benchmark, or Figma review is claimed.

## 8. Open decisions, questions, and dependencies

| Decision / question | Status | Owner(s) to consult | Dependency / required evidence |
| --- | --- | --- | --- |
| Candidate scope and acceptance of PR #43 FR-01–FR-07 | Pending | Nurefşan / Product Owner / team | Issue #27 input and Issue #28 SRS approval; PR #43 source branch is not in current `develop`, and live PR status could not be verified. |
| Role-to-operation and role-to-data matrix | Pending | Nurefşan / Arda / team | SRS OQ-01; needed for API, component interfaces, and C4/UML behavior. |
| Authentication provider, credential policy, session/token format, expiry, logout | Pending; OpenAPI bearer/JWT is Proposed | Nurefşan / Arda / team | SRS OQ-02; reconcile `sessionId` response and root bearer declaration. |
| Student, Course, Course Offering, Enrollment/Registration, Grade identifiers and constraints | Pending | Nurefşan / team; Arda maps contract | SRS OQ-03–OQ-07 and SRS §6; reconcile SRS entity identifiers with API schema fields before changing API. |
| FR-06 saved-grade retrieval | Pending discrepancy | Nurefşan / Arda / team | Confirm requirement intent and owner-authored contract mapping. No endpoint is invented here. |
| FR-07 published-only example and error mapping | Pending discrepancy | Nurefşan / Arda; Ahmet review | Reconcile `published: false` example, own-data policy, empty state, and generic `Error` responses. |
| External systems and integration boundary | Proposed none for Sprint 1; confirmation Pending | Team / Nurefşan / Arda | Boundary §5.2, SRS §1.2/OQ-11; do not draw an unconfirmed integration as deployed. |
| Database engine and persistence/deployment topology | Pending; no selection in sources | Team / Arda | Need approved requirements and NFR workload/availability before selection. No server/deployment is asserted. |
| OpenAPI 3.1.0 and localhost server metadata | Candidate/proposed, not approved/deployed | Team / Arda | Existing contract marks version candidate and server a local placeholder. |
| NFR targets and verification method | Pending | Ahmet / team; Arda feasibility | Issues #30–#31; architecture trade-offs cannot be accepted against absent targets. |
| Figma user flows / UX consistency | Pending | UX producer [TODO], Nurefşan; Arda consults | Issues #32–#33; no Figma version is included in the reviewed develop tree or PR #43. Relevant to final architecture/UML alignment, not a substitute for SRS decisions. |

### 8.1 Issue dependencies

- **Issue #34:** Issue #27 is the acceptance/input dependency; Issues #28 and #31 are final-alignment inputs. Drafting can proceed, but final alignment waits for the SRS and NFR baselines.
- **Issue #35:** depends on #34's architecture baseline; levels must be agreed, and the views must reflect confirmed boundary/role decisions.
- **Issue #36:** depends on #34 and final UX consistency from #33. Select structure and interaction scenarios from the reviewed SRS and Figma flows rather than inventing them.

## 9. Draft architecture view index — Issues #35 and #36

These editable SVGs are proposed views based on the architecture and requirements drafts. C4 levels and UML types remain subject to team/rubric confirmation. They are not implementation or deployment evidence; no Figma prototype was available for UX alignment.

| View | Editable SVG source | Status / coverage |
| --- | --- | --- |
| C4 Level 1 — System Context | [`docs/diagrams/Sprint2_System_Context.svg`](../diagrams/Sprint2_System_Context.svg) | Proposed actors and conceptual SIS boundary; integration and permission decisions Pending. |
| C4 Level 2 — Container | [`docs/diagrams/Sprint2_Container.svg`](../diagrams/Sprint2_Container.svg) | Logical responsibilities only; no deployable units or technologies selected. |
| C4 Level 3 — Component | [`docs/diagrams/Sprint2_Component.svg`](../diagrams/Sprint2_Component.svg) | Proposed responsibility relationships and operation mappings; not confirmed components/services. |
| UML Domain/Class | [`docs/diagrams/Sprint2_Domain_Class.svg`](../diagrams/Sprint2_Domain_Class.svg) | Candidate entities, fields, and associations; keys and multiplicities Pending. |
| UML Sequence — Enrollment | [`docs/diagrams/Sprint2_Sequence_Enrollment.svg`](../diagrams/Sprint2_Sequence_Enrollment.svg) | FR-05/PB-05 proposal using `POST /registrations` and `GET /registrations`. |
| UML Sequence — Grade Entry | [`docs/diagrams/Sprint2_Sequence_Grade_Entry.svg`](../diagrams/Sprint2_Sequence_Grade_Entry.svg) | FR-06/PB-06 proposal; later instructor retrieval gap shown explicitly. |
| UML Sequence — Published Grades | [`docs/diagrams/Sprint2_Sequence_Published_Grades.svg`](../diagrams/Sprint2_Sequence_Published_Grades.svg) | FR-07/PB-07 proposal using `GET /grades`; publication/own-data rules Pending. |

## 10. Source register

| Source | Use and status |
| --- | --- |
| `api/openapi.yaml` on `develop` `ee5c64b` | Existing provisional operations, schemas, responses, bearer scheme, and server placeholder; unchanged from PR #42 base `98f9b5a`. |
| `docs/System_Vision_and_Boundary.md` on `develop` | Candidate roles, system boundary, Sprint 1 external-systems proposal, and pending role permissions. |
| `docs/Initial_Backlog_Draft.md` on `develop` | PB-01–PB-07 candidate backlog mapping; not treated as approved scope. |
| `docs/sprint2/Sprint2_Requirements_Traceability.md` | Planning crosswalk from PBs to API and expected architecture/UX coverage; some cells were written before the PR #43 SRS draft existed. |
| `docs/sprint2/Sprint2_Gap_Analysis.md` | Planning inventory of contract, SRS, NFR, UX, architecture, and evidence gaps. |
| `docs/sprint2/SRS_Draft.md` and `Refined_Backlog_Draft.md` on PR #43 source branch at `a9b6b48` | Draft-only FR IDs, candidate data model, business rules, NFR statements, and open questions. Not in `develop`; not approved. |
| `docs/sprint2/NFR_Quality_Measures.md` on PR #45 source branch at `63ca3e8` | Draft measurable targets and proposed verification methods, reviewed in §7.1; no target is approved or tested. Not in `develop`. |
| Issues [#34](https://github.com/mert494/student-information-system/issues/34), [#35](https://github.com/mert494/student-information-system/issues/35), [#36](https://github.com/mert494/student-information-system/issues/36) | Acceptance criteria and dependencies for Arda's proposed S2-09, S2-10, and S2-11 responsibilities; assignee, estimates, and member agreement remain pending. |

This draft records the available evidence and discrepancies as of its source baselines. Any later SRS, NFR, UX, or API update requires a fresh traceability review; this document does not approve those updates.
