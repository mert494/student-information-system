# Student Information System (SIS) — Non-Functional Requirements and Quality Measures

**Version:** Draft 0.2 (revised after Mert's review of `63ca3e8` and Arda's feasibility review in PR #47 §7.1)
**Sprint:** 2
**Status:** Working draft; every target is **Proposed** or **Open**. Nothing here is approved by the Product Owner, the Architecture Lead or the team.
**Prepared by:** Ahmet (QA; S2-05 [#30](https://github.com/mert494/student-information-system/issues/30) and S2-06 [#31](https://github.com/mert494/student-information-system/issues/31), both assigned to `ahmetserdar41`)
**Independent review:** Arda or another member who is not the author — Pending

> This document specifies how the quality of the SIS will be judged and measured. The project is at the documentation/API-contract stage: no backend exists, so **no performance, security or usability test has been run and no result is reported here**. Sections 4–5 are a verification plan, not test results.

## 1. Sources and status rules

| Source | Version used | What this document takes from it |
|---|---|---|
| SRS draft (Nurefşan, PR [#43](https://github.com/mert494/student-information-system/pull/43), not merged) | [`SRS_Draft.md` @ `a9b6b48`](https://github.com/mert494/student-information-system/blob/a9b6b4819ca18146e4e2b72346405283dbdd0c60/docs/sprint2/SRS_Draft.md) | FR-01–FR-07, BR-01–BR-09, OQ-01–OQ-11 and the initial NFR IDs in SRS §8. Existing IDs are kept unchanged so the SRS and backlog links stay valid. |
| Refined backlog draft (PR #43) | [`Refined_Backlog_Draft.md` @ `a9b6b48`](https://github.com/mert494/student-information-system/blob/a9b6b4819ca18146e4e2b72346405283dbdd0c60/docs/sprint2/Refined_Backlog_Draft.md) | PB-01–PB-07 ↔ NFR trace columns |
| OpenAPI draft | [`api/openapi.yaml` @ `98f9b5a`](https://github.com/mert494/student-information-system/blob/98f9b5ac41d24fa1139492c52a043e5773f8a6b4/api/openapi.yaml) | 12 operations, proposed bearer (JWT) security, generic `Error {code, message}` envelope, 400/401/403/404/409 responses |
| Quality model | ISO/IEC 25010 product quality characteristics | Category names in §2 |
| Mert's review of this PR | [Review 5981094098](https://github.com/mert494/student-information-system/pull/45#pullrequestreview-5981094098) on `63ca3e8` (COMMENTED) | MAJOR 1 (operation-level coverage) → §4.0; MAJOR 2 (accessibility scope) → NFR-ACCESS-01 in §3 and §4.4; minors → §1, §3, §4, §7 |
| Arda's architecture draft (PR [#47](https://github.com/mert494/student-information-system/pull/47), not merged) | [`Architecture_Decisions_and_Contract_Mapping.md` @ `a1e6fed`](https://github.com/mert494/student-information-system/blob/a1e6fed85fc8dacd926ee2f5ac38b7ce34e15e4f/docs/sprint2/Architecture_Decisions_and_Contract_Mapping.md) §7.1 | Technical feasibility notes on NFR-SEC-01–05, NFR-DATA-01–02, NFR-PERF-01–02; applied in §4 |

If PR #43 changes an FR, BR or NFR ID before merging, the trace columns below must be rechecked.

**Target status values used in this document**

| Status | Meaning |
|---|---|
| **Proposed** | A candidate target suggested by QA so the requirement is measurable. It is not a commitment until the Product Owner accepts it and Arda confirms it is technically feasible. Any member may replace the value. |
| **Open** | No target is proposed yet, because a decision in the linked OQ is missing. The requirement cannot be accepted unconditionally while it is Open. |
| **Approved** | Accepted by the decision owner, with an evidence link. **No NFR has this status yet.** |

**Measurability.** An NFR is *measurable* only when its target, workload/environment and method are all defined. An NFR with an Open target, or whose method depends on an Open decision, is **not yet measurable and not ready for acceptance**, even if a candidate value is written next to it. Current state:

| Readiness | NFRs |
|---|---|
| Measurable as written (target still Proposed) | NFR-SEC-01 (contract part, §4.0), NFR-SEC-03, NFR-SEC-04, NFR-PRIV-01, NFR-DATA-01, NFR-USE-01, NFR-USE-02, NFR-TEST-01, NFR-MAINT-01, NFR-ACCESS-01 (prototype subset only) |
| Not yet measurable — method depends on an Open decision | NFR-SEC-01 (runtime part: role matrix OQ-01), NFR-SEC-02 (denial outcome OQ-01/OQ-08), NFR-SEC-05 (environments/TLS termination, Arda), NFR-DATA-02 (offering identity and capacity model OQ-05/OQ-06), NFR-PERF-01 and NFR-PERF-02 (workload and environment OQ-10), NFR-ACCESS-01 (full conformance, needs a built UI) |
| Not measurable — target Open | NFR-SEC-06 (OQ-02), NFR-AUD-01 (OQ-09), NFR-AVAIL-01 (OQ-10) |

## 2. Quality attributes in scope

| ISO/IEC 25010 characteristic | Why it matters for the SIS | NFR IDs |
|---|---|---|
| Security (confidentiality, integrity, authenticity, accountability) | Grades and student records are sensitive; several roles see different data | NFR-SEC-01 – NFR-SEC-06, NFR-AUD-01, NFR-PRIV-01 |
| Functional suitability (correctness) / data integrity | Rejected operations must not leave partial data; enrollment capacity must hold | NFR-DATA-01, NFR-DATA-02 |
| Performance efficiency | Enrollment periods create peaks of simultaneous requests | NFR-PERF-01, NFR-PERF-02 |
| Reliability (availability, recoverability) | Academic records must not be lost | NFR-AVAIL-01 |
| Usability and accessibility | Students and staff use the system without training; error states must be clear | NFR-USE-01, NFR-USE-02, NFR-ACCESS-01 |
| Maintainability (testability, modifiability) | The API contract and requirements must stay testable as they change | NFR-TEST-01, NFR-MAINT-01 |

Out of scope for this draft unless the team adds them: portability, multi-language support, mobile-specific behaviour (no separate mobile app, SRS §1.1) and external-system interoperability (no confirmed integrations, SRS §1.2).

## 3. Non-functional requirements

Each requirement is written as a quality scenario: **source/stimulus → environment → expected response**. The measurable part is in §4.

| ID | Requirement (scenario) | Linked FR / BR / PB | Priority (proposal) | Status |
|---|---|---|---|---|
| NFR-SEC-01 | When any client sends a request to a protected operation (11 of the 12 OpenAPI operations; `createSession` is public), including directly to the API without the UI, the server checks authentication and, where the operation is role-restricted, role/record permission before doing anything. Unauthenticated → 401; authenticated but not permitted → 403. The per-operation expectations are in §4.0. | FR-02, BR-08; PB-02 | P1 | Rule from SRS; measures Proposed |
| NFR-SEC-02 | When a Student tries to obtain another student's grades, enrollments or record through any operation that exists in the contract, the response contains no data of the other student. Whether the denial is 403 or a non-disclosing 404 is **Open** (security policy, OQ-01/OQ-08); the pass condition is "no disclosure" in either case. | FR-02, FR-05, FR-07, BR-07; PB-02, PB-05, PB-07 | P1 | Rule from SRS; denial status Open; measures Proposed |
| NFR-SEC-03 | When login fails, the response does not reveal whether the account exists: unknown account and wrong password produce the same status code, the same `code` and the same `message`. | FR-01; PB-01 | P1 | Rule from SRS; measures Proposed |
| NFR-SEC-04 | Passwords are never stored, logged or returned in plain text; only a salted hash produced by an adaptive algorithm (for example bcrypt or Argon2) is stored. | FR-01; User/account data (SRS §6) | P1 | Proposed (algorithm: OQ-02) |
| NFR-SEC-05 | All client–server traffic in shared environments (anything other than a developer's own `localhost`, which the OpenAPI `http://localhost:8080` placeholder represents) uses HTTPS (TLS 1.2 or higher); a token or credential is never placed in a URL. | FR-01, FR-02 | P1 | Proposed (environments and TLS termination: Arda) |
| NFR-SEC-06 | Repeated failed logins for the same account are limited so that password guessing is slowed down. | FR-01; PB-01 | P2 | **Open** — lockout/rate limit is undecided in OQ-02 |
| NFR-AUD-01 | Changes to grades, student records, course records and role assignments are recorded with actor, UTC time, entity, operation and old/new value; the log cannot be edited through the API. | FR-03, FR-04, FR-06, BR-09 | P2 | **Open** — scope, access and retention are OQ-09; candidate content Proposed |
| NFR-PRIV-01 | Test cases, examples, prototypes and documentation use synthetic data only; no real student data appears in the repository. | SRS §4 assumption 3 | P1 | Proposed |
| NFR-DATA-01 | A create/update request that fails validation, uniqueness or permission checks leaves the stored data exactly as it was (no partial write). | FR-03 – FR-06, BR-09 | P1 | Rule from SRS; measures Proposed |
| NFR-DATA-02 | When several students request the last free seat of a course offering at the same moment, the number of active enrollments never exceeds capacity; when the same student sends the same enrollment request several times at once, at most one enrollment is created. | FR-05, BR-03, BR-04; PB-05 | P1 | Proposed (offering identity, capacity/waitlist: OQ-05/OQ-06) |
| NFR-PERF-01 | Under normal load, users get a response quickly enough not to interrupt their work. | All FRs | P2 | Proposed targets in §4 (SRS: OQ-10) |
| NFR-PERF-02 | During the enrollment-period peak, the enrollment and list operations stay responsive and correct. | FR-05; PB-05 | P2 | Proposed targets in §4 (OQ-05, OQ-10) |
| NFR-AVAIL-01 | Academic data survives a server failure, and the service can be restored from backup. | All FRs | P3 | **Open** — SRS marks it "only if required"; OQ-10 |
| NFR-USE-01 | A first-time user can complete the core flows of their role (Student: enroll, view grades; Instructor: enter a grade; Staff: create a student) without help. | FR-03, FR-05 – FR-07 | P2 | Proposed; checkable on the Figma prototype |
| NFR-USE-02 | Every error is shown to the user as a specific message that says what went wrong and what to do; a loading/API error is never shown as an empty list. | FR-05, FR-07; PB-05, PB-07 | P1 | Rule partly from SRS FR-07; measures Proposed |
| NFR-ACCESS-01 | The implemented web interface meets WCAG 2.2 level AA for the core flows. In Sprint 2 only a defined prototype subset can be checked (§4.4); passing that subset is **not** a WCAG conformance claim. | All UI flows | P2 | Proposed (level to be confirmed by team) |
| NFR-TEST-01 | Each approved functional requirement has at least one positive test and, where applicable, negative/alternate-path tests with observable expected outcomes. | FR-01 – FR-07 | P1 | Rule from SRS; measures Proposed |
| NFR-MAINT-01 | The API contract stays valid and in sync with the requirements: every operation is traceable to an FR/PB and every response matches the contract. | All FRs; `api/openapi.yaml` | P2 | Proposed |

Source of each ID: NFR-SEC-01–03, NFR-DATA-01, NFR-TEST-01, NFR-AUD-01, NFR-PERF-01, NFR-AVAIL-01 and NFR-ACCESS-01 come from SRS §8 (wording refined here as scenarios). NFR-SEC-04–06, NFR-PRIV-01, NFR-DATA-02, NFR-PERF-02, NFR-USE-01–02 and NFR-MAINT-01 are new QA proposals and must be added to the SRS/backlog trace by Nurefşan only if accepted.

## 4. Quality measures

For every NFR: what is measured, the proposed target, under which load/environment, how it is measured and when it passes. "Stage" says whether the check can be done now on the Sprint 2 documents (**S2-doc**) or only after implementation (**Impl**).

### 4.0 Operation-level authorization coverage (NFR-SEC-01)

The contract has **12 operations**. **11 are protected** (inherit `bearerAuth`); `createSession` is public (`security: []`). Not every protected operation is role-restricted: logout applies to any authenticated user, so 403 is not expected there. Allowed roles below are taken from the SRS FR actors and are **Proposed** until the role matrix is decided (OQ-01). Source: `api/openapi.yaml` @ `98f9b5a`; SRS @ `a9b6b48`.

| Method and path | operationId | Security in contract | Allowed roles (Proposed, from SRS) | No/invalid token | Authenticated, role not allowed | Record-level rule | 401 / 403 declared in contract |
|---|---|---|---|---|---|---|---|
| POST `/sessions` | createSession | none (public) | anyone | not applicable | not applicable | — | 401 = failed login (NFR-SEC-03) / no 403 — correct |
| DELETE `/sessions/current` | deleteCurrentSession | bearer | any authenticated role | 401 | not applicable | own session only | 401 / no 403 — correct, not role-restricted |
| GET `/students` | listStudents | bearer | Student Affairs Staff (FR-03); Instructor/Administrators Open (OQ-01) | 401 | 403 | — | yes / yes |
| POST `/students` | createStudent | bearer | Student Affairs Staff | 401 | 403 | — | yes / yes |
| PATCH `/students/{studentId}` | updateStudent | bearer | Student Affairs Staff | 401 | 403 | — | yes / yes |
| GET `/courses` | listCourses | bearer | all four roles (a Student must see courses to enroll, FR-05); Open (OQ-01) | 401 | 403 only if a role is excluded by OQ-01 | — | yes / yes |
| POST `/courses` | createCourse | bearer | Student Affairs Staff (FR-04) | 401 | 403 | — | yes / yes |
| PATCH `/courses/{courseId}` | updateCourse | bearer | Student Affairs Staff | 401 | 403 | — | yes / yes |
| GET `/registrations` | listMyRegistrations | bearer | Student (FR-05) | 401 | 403 | returns only the caller's enrollments (NFR-SEC-02) | yes / yes |
| POST `/registrations` | createRegistration | bearer | Student (FR-05) | 401 | 403 | enrolls only the caller | yes / yes |
| PUT `/registrations/{registrationId}/grade` | recordGrade | bearer | Instructor (FR-06) | 401 | 403 | only the instructor assigned to the offering (BR-06) → 403 | yes / yes |
| GET `/grades` | listMyPublishedGrades | bearer | Student (FR-07) | 401 | 403 | only the caller's published grades (NFR-SEC-02, BR-07) | yes / yes |

Contract-level observation (static, at `98f9b5a`): every protected operation declares 401, and every role-restricted operation declares 403. This shows the contract is consistent with the table; it does **not** show that a server enforces it.

### 4.1 Security and privacy

| NFR | Metric / unit | Target (status) | Environment / workload | Method / tool (proposed) | Pass / fail rule | Stage |
|---|---|---|---|---|---|---|
| NFR-SEC-01 | Cells of the §4.0 matrix (operation × role × token state) where the observed outcome differs from the expected one, count | 0 (Proposed) | Test environment; one synthetic account per role, plus no token, expired token and forged token | Contract: compare §4.0 with the OpenAPI. Runtime: automated API tests over every cell (pytest + requests, or Postman/Newman) | Pass if every cell gives the expected 2xx/401/403; any unexpected 2xx is a fail | S2-doc: §4.0 contract check. Impl: runtime test, after OQ-01 fixes the roles |
| NFR-SEC-02 | Requests by Student A that return any data of Student B, count | 0 (Proposed) | Two synthetic Students A and B, each with enrollments and published/unpublished grades | Only operations that exist: call `listMyRegistrations` and `listMyPublishedGrades` as A and check that no B record is returned; call `listStudents` and `updateStudent` on B's record as A and check denial; repeat with a forged token for B | Pass if no response contains B's data. The denial status (403 or a non-disclosing 404) is checked against the policy chosen in OQ-01/OQ-08 | Impl |
| NFR-SEC-03 | Differences between "unknown account" and "wrong password" responses in status, `code`, `message` | 0 differences (Proposed) | Test environment, 20 attempts per case | Compare responses field by field. Response time is recorded and reported only; it is **not** a pass criterion until a timing method and threshold are agreed (Arda, OQ-02) | Pass if status, `code` and `message` are identical | S2-doc: OpenAPI `createSession` has a single 401 response. Impl: test |
| NFR-SEC-04 | Plain-text passwords in database, logs or responses, count | 0 (Proposed) | Test database and application logs after the login test suite | Inspect the stored credential column; search logs and responses for the test passwords | Pass if only hash values are stored and the test passwords appear nowhere | Impl; design review of the data model (S2-doc, with Arda) |
| NFR-SEC-05 | Shared-environment endpoints that accept credentials or tokens over plain HTTP; tokens in URLs, count | 0 and 0 (Proposed) | Shared or deployed environments only; a developer's own `localhost` is excluded | Send a login request over `http://`; review the OpenAPI for credentials in path/query parameters. Where TLS is terminated (proxy or application) is Arda's decision | Pass if plain HTTP is refused, or redirected before any credential is sent, and no parameter carries a token | S2-doc: OpenAPI parameter review. Impl: deployed check |
| NFR-SEC-06 | Failed attempts allowed before limiting; lock duration | **Open** (OQ-02) | — | — | Cannot be accepted until OQ-02 is decided | — |
| NFR-AUD-01 | Audited changes missing a log entry, count; log entries editable via API | 0 and none (Proposed once OQ-09 defines the list of audited events) | Test environment | Perform each audited change, then read the log; try to update/delete a log entry through the API | Pass if every change has one complete entry and modification is impossible | **Open** until OQ-09; then Impl |
| NFR-PRIV-01 | Real personal data found in repository files, count | 0 (Proposed) | Repository at the submission commit | Manual review of examples, fixtures and prototype screenshots; the QA checklist records the check | Pass if all names, numbers and e-mails are clearly synthetic | S2-doc |

### 4.2 Data integrity

| NFR | Metric / unit | Target (status) | Environment / workload | Method / tool (proposed) | Pass / fail rule | Stage |
|---|---|---|---|---|---|---|
| NFR-DATA-01 | Rejected requests that changed stored data, count | 0 (Proposed) | Test database with known synthetic records | For each create/update operation send invalid, duplicate and unauthorized requests; compare a database snapshot before and after | Pass if the snapshot is unchanged after every rejected request | Impl |
| NFR-DATA-02 | (a) Active enrollments above capacity; (b) duplicate enrollments for one student, offering and term, count | 0 and 0 (Proposed) | (a) One offering with capacity 1; 50 parallel requests from 50 synthetic students. (b) One student sends the same request 10 times in parallel to an offering with free seats. Each case repeated 10 times; the database is reset to the same seed before every run | Concurrent requests (k6 or a Python thread pool), then count enrollments in the database | Pass if in every run (a) exactly 1 request succeeds and the others get 409, and (b) exactly 1 enrollment exists | Impl, after the offering identifier and capacity model are fixed (OQ-05/OQ-06): the current `RegistrationInput` has `courseId` and an optional `term`, not an offering ID |

### 4.3 Performance and reliability

The numbers below are QA proposals sized for a single-university course project with an assumed peak of a few hundred simultaneous users. They must be replaced if the Product Owner or Arda gives a different expected load. They are measurable scenarios, **not** demonstrated feasible targets; NFR-PERF-01 and NFR-PERF-02 stay not-ready until the workload (OQ-10) and the test environment are agreed.

Test-run definitions (Proposed, applying to both performance NFRs):

- **Virtual users (VUs) are not the same as concurrent requests.** Each VU runs the request mix below with a 1–3 s random think time between requests; the achieved request rate is reported with the results.
- **Request mix:** NFR-PERF-01 uses 80% reads (`listCourses`, `listMyRegistrations`, `listMyPublishedGrades`, `listStudents`) and 20% writes (`createRegistration`, `updateStudent`, `recordGrade`). NFR-PERF-02 uses 60% `listCourses`, 30% `createRegistration`, 10% `listMyRegistrations`.
- **Warm-up and window:** 1 minute warm-up excluded from the results; p95 computed per operation over the hold phase only.
- **Repetitions:** 3 runs; the target must hold in every run.
- **Error rate:** (5xx responses + timeouts over 10 s + connection errors) ÷ all requests sent. Expected business 4xx (for example 409 for a full course) are not errors.
- **Environment:** CPU, memory and database size are recorded with the results; Arda chooses the environment.

| NFR | Metric / unit | Target (status) | Environment / workload | Method / tool (proposed) | Pass / fail rule | Stage |
|---|---|---|---|---|---|---|
| NFR-PERF-01 | Server response time, 95th percentile (p95), milliseconds | Read operations ≤ 500 ms; create/update ≤ 1000 ms (Proposed) | Test server agreed with Arda; database seeded with 5,000 students, 300 courses, 20,000 enrollments (synthetic); 50 concurrent virtual users for 10 minutes | Load test with k6 (or JMeter); response times measured at the API, not in the browser | Pass if p95 is within target for each operation and the error rate is < 1% | Impl |
| NFR-PERF-02 | p95 response time of `createRegistration` and `listMyRegistrations`; error rate (non-4xx failures) | p95 ≤ 2000 ms; error rate < 1% (Proposed) | Same seed; ramp from 0 to 300 concurrent virtual users in 5 minutes, hold 10 minutes | k6 ramp scenario; database checked afterwards with the NFR-DATA-02 counts | Pass if both targets hold for the whole hold phase and no capacity/duplicate violation appears | Impl |
| NFR-AVAIL-01 | Availability (%), recovery point (RPO), recovery time (RTO) | **Open** (OQ-10). Candidate if the team keeps it in scope: daily backup (RPO ≤ 24 h), restore drill completed in ≤ 4 h (RTO) | Test environment | Restore the latest backup into an empty database and run the read tests | Pass if data up to the last backup is present and the restore finishes within RTO | **Open**; Impl |

### 4.4 Usability and accessibility

| NFR | Metric / unit | Target (status) | Environment / workload | Method / tool (proposed) | Pass / fail rule | Stage |
|---|---|---|---|---|---|---|
| NFR-USE-01 | Task success rate without help, %; number of screens/steps per task | ≥ 80% of at least 5 testers per flow (Proposed); enrollment ≤ 4 steps from the home screen (Proposed) | Clickable Figma prototype; testers are classmates who did not build it, using synthetic data | Short task-based usability test on the prototype; tester completes the task while the observer only records success, errors and steps | Pass if each core flow meets both targets; failing flows are fed back to the prototype owner | S2-doc (prototype) |
| NFR-USE-02 | Error situations in the prototype without a specific message; error shown as empty list, count | 0 and 0 (Proposed) | Figma prototype and user-flow diagrams | Walk through every error branch of FR-05 (inactive, closed period, duplicate, full, prerequisite) and FR-07 (error vs zero results) | Pass if each branch has its own screen/message and FR-07 shows `No published grades are available.` only for a successful empty result | S2-doc (prototype) |
| NFR-ACCESS-01 (a) prototype subset | Failures on core-flow prototype screens in these checks only: text contrast ≥ 4.5:1 (large text ≥ 3:1); non-text contrast of controls ≥ 3:1; information not conveyed by colour alone; every form field has a visible label; error messages identify the field and the problem; focus order annotated | 0 (Proposed) | Figma prototype version named in the result | Contrast: WebAIM contrast checker or a Figma contrast plugin. Others: manual walkthrough with a checklist | Pass means "the prototype passed this subset". It is **not** WCAG 2.2 AA conformance and must not be reported as such | S2-doc (prototype) |
| NFR-ACCESS-01 (b) implemented UI | WCAG 2.2 AA success-criterion failures on core-flow pages, count | 0 (Proposed) | Built web interface in a test environment | Automated scan (axe DevTools) + manual checks: keyboard-only operation and visible focus, screen reader (NVDA on Windows), 200% zoom and 320 px reflow, review of the remaining applicable success criteria | Pass only if automated and manual checks find no failure of an applicable AA criterion. Only this result can support a conformance statement | Impl |

### 4.5 Testability and maintainability

| NFR | Metric / unit | Target (status) | Environment / workload | Method / tool (proposed) | Pass / fail rule | Stage |
|---|---|---|---|---|---|---|
| NFR-TEST-01 | Approved FRs without a positive test case; FRs with error scenarios but no negative test case, count | 0 and 0 (Proposed) | Requirement–test traceability matrix | QA writes test case IDs per FR acceptance criterion and checks coverage both ways | Pass if every approved FR acceptance criterion maps to ≥ 1 test case | S2-doc (test design); Impl (execution) |
| NFR-MAINT-01 | OpenAPI lint errors; operations without an FR/PB reference; responses not matching the schema | 0 errors with Redocly CLI `recommended`; 0 untraced operations (Proposed); 0 schema mismatches later | `api/openapi.yaml` at the submission commit | Redocly CLI lint (used in Sprint 1, QA-06); trace check against SRS §9; later contract tests (e.g. Schemathesis) | Pass if lint has 0 errors and every operation is traced | S2-doc (lint, trace); Impl (contract tests) |

## 5. Verification plan

### 5.1 What can be checked in Sprint 2 (documents and prototype only)

| Check | NFRs | Input artifact | Who (proposed) | Status |
|---|---|---|---|---|
| §4.0 matrix matches the contract: 401 on all 11 protected operations, 403 on all role-restricted ones; `createSession` has one generic 401; no token in path/query | NFR-SEC-01, NFR-SEC-03, NFR-SEC-05 | `api/openapi.yaml` | Ahmet; Arda confirms | Contract part observed for §4.0 at `98f9b5a`; Arda's confirmation Pending |
| OpenAPI lint 0 errors; every operation traced to FR/PB | NFR-MAINT-01 | `api/openapi.yaml`, SRS §9 | Ahmet | Pending |
| Test-case IDs written for each FR acceptance criterion | NFR-TEST-01 | SRS FR-01–FR-07 | Ahmet | Pending |
| Error/empty-state walkthrough and the NFR-ACCESS-01 (a) prototype subset | NFR-USE-02, NFR-ACCESS-01 | Figma prototype and flows (#32, #33) | Ahmet with Azra (prototype owner) | Pending — Figma URL is declared in #32/#33, content not yet reviewed |
| Task-based usability test, ≥ 5 testers per flow | NFR-USE-01 | Clickable Figma prototype | Ahmet organizes; Azra fixes | Pending |
| Synthetic-data review | NFR-PRIV-01 | All Sprint 2 documents and prototype | Ahmet | Pending |
| NFRs reflected in architecture (authorization component, write constraints for capacity and uniqueness, credential storage, backup) | NFR-SEC-01, NFR-SEC-04, NFR-DATA-01, NFR-DATA-02, NFR-AVAIL-01 | Architecture document and C4/UML in PR #47 (#34–#36) | Arda; Ahmet checks consistency | Pending — PR #47 opened, not yet reviewed |

### 5.2 What is planned after implementation

Load tests (NFR-PERF-01, NFR-PERF-02, NFR-DATA-02), the runtime authorization matrix test (NFR-SEC-01, NFR-SEC-02), credential and log inspection (NFR-SEC-04), audit-log tests (NFR-AUD-01), restore drill (NFR-AVAIL-01) and the full accessibility check, NFR-ACCESS-01 (b). These require a running system and are **not** part of the Sprint 2 evidence. Tools named in §4 are proposals; Arda decides the final stack.

### 5.3 Evidence to collect

For every check: date, checked commit or Figma version, tool and version, raw output (or screenshot), result (Pass / Fail / Pending) and the person who checked it. Results go into the Sprint 2 QA report under #38; a failed check becomes a finding with an owner.

## 6. Open decisions

These are needed before the related NFR can move from Proposed/Open to Approved. IDs refer to the SRS decision log; no new decision is assumed here.

| Decision | SRS ref | Affects | Decision owner (from SRS) | Status |
|---|---|---|---|---|
| Expected number of users, peak concurrency and test environment | OQ-10 | NFR-PERF-01, NFR-PERF-02 (all numbers in §4.3) | Ahmet + team; PO confirms; Arda chooses the environment | Open |
| Whether availability/backup is in scope for the course project | OQ-10 | NFR-AVAIL-01 | Team | Open |
| Role-to-operation matrix (fixes the Proposed roles in §4.0) | OQ-01 | NFR-SEC-01, NFR-SEC-02 | Product Owner + Arda + team | Open |
| Denial outcome for cross-student access: 403 or non-disclosing 404 | OQ-01 / OQ-08 | NFR-SEC-02 | Arda + team | Open |
| Authentication method, password hashing, lockout/rate limit, login timing check | OQ-02 | NFR-SEC-03, NFR-SEC-04, NFR-SEC-06 | Arda/team | Open |
| Shared environments and where TLS is terminated | — (architecture; Arda's PR #47 keeps deployment Pending) | NFR-SEC-05 | Arda | Open |
| Which changes are audited, who can read the log, retention | OQ-09 | NFR-AUD-01 | Team/QA | Open |
| Offering identifier, capacity, waitlist and race-condition behaviour | OQ-05 / OQ-06 | NFR-DATA-02 | Product Owner + Arda/team | Open |
| Error-code names and error schema | OQ-08 | NFR-SEC-01, NFR-SEC-03, NFR-USE-02 | Arda | Open |
| Accessibility level (WCAG 2.2 AA proposed) and usability test with classmates | — (new; to be added to the SRS log if accepted) | NFR-ACCESS-01, NFR-USE-01 | Team / Azra (prototype owner) | Open |

## 7. Review and evidence tracker

| Review / decision | Reviewer or decision owner | Required evidence | Status | Evidence link / date |
|---|---|---|---|---|
| Initial review of Draft 0.1 | Mert | PR review | Received (COMMENTED, no approval); findings addressed in Draft 0.2, recheck Pending | [Review 5981094098](https://github.com/mert494/student-information-system/pull/45#pullrequestreview-5981094098), 2026-11-19 |
| Technical feasibility of every Proposed target | Arda | Feasibility notes | Preliminary assessment received (conditional, no target accepted); applied in Draft 0.2; recheck of Draft 0.2 Pending | PR #47 `a1e6fed`, §7.1 |
| Product priority and acceptance of targets | Nurefşan (Product Owner) | PR review or decision-log entry | Pending | [TODO] |
| Independent review of this document (author is not the reviewer) | Arda or another member | PR approval | Pending | [TODO] |
| New NFR IDs added to SRS §8 and backlog trace | Nurefşan | Commit in the SRS/backlog PR | Pending | [TODO] |
| Prototype checks (NFR-USE-01, NFR-USE-02, NFR-ACCESS-01 (a)) | Ahmet with Azra | Check results with Figma version | Pending | [TODO] |
| Assignment of #30 and #31 | Mert (coordination) | Issue assignee | Done: both assigned to `ahmetserdar41` | [#30](https://github.com/mert494/student-information-system/issues/30), [#31](https://github.com/mert494/student-information-system/issues/31) |

## 8. Limitations

- No product exists, so every target is unverified; this document gives no test result.
- The performance numbers are proposals based on an assumed load, not on measurements or a stakeholder statement.
- The SRS used here is an unmerged draft (PR #43 @ `a9b6b48`); IDs or wording may change.
- ISO/IEC 25010 and WCAG 2.2 are used as category and checklist references; no formal conformance claim is made.
- The §4.0 roles come from the SRS FR actors, not from an approved permission matrix.
- Arda's feasibility notes (PR #47 §7.1) were written against Draft 0.1; they are not an approval of Draft 0.2.
