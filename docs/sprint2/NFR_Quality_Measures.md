# Student Information System (SIS) — Non-Functional Requirements and Quality Measures

**Version:** Draft 0.1
**Sprint:** 2
**Status:** Working draft; every target is **Proposed** or **Open**. Nothing here is approved by the Product Owner, the Architecture Lead or the team.
**Prepared by:** Ahmet (QA; proposed owner of S2-05 [#30](https://github.com/mert494/student-information-system/issues/30) and S2-06 [#31](https://github.com/mert494/student-information-system/issues/31); assignment Pending)
**Independent review:** Arda or another member who is not the author — Pending

> This document specifies how the quality of the SIS will be judged and measured. The project is at the documentation/API-contract stage: no backend exists, so **no performance, security or usability test has been run and no result is reported here**. Sections 4–5 are a verification plan, not test results.

## 1. Sources and status rules

| Source | Version used | What this document takes from it |
|---|---|---|
| SRS draft (Nurefşan, PR [#43](https://github.com/mert494/student-information-system/pull/43), not merged) | [`SRS_Draft.md` @ `a9b6b48`](https://github.com/mert494/student-information-system/blob/a9b6b4819ca18146e4e2b72346405283dbdd0c60/docs/sprint2/SRS_Draft.md) | FR-01–FR-07, BR-01–BR-09, OQ-01–OQ-11 and the initial NFR IDs in SRS §8. Existing IDs are kept unchanged so the SRS and backlog links stay valid. |
| Refined backlog draft (PR #43) | [`Refined_Backlog_Draft.md` @ `a9b6b48`](https://github.com/mert494/student-information-system/blob/a9b6b4819ca18146e4e2b72346405283dbdd0c60/docs/sprint2/Refined_Backlog_Draft.md) | PB-01–PB-07 ↔ NFR trace columns |
| OpenAPI draft | [`api/openapi.yaml` @ `98f9b5a`](https://github.com/mert494/student-information-system/blob/98f9b5ac41d24fa1139492c52a043e5773f8a6b4/api/openapi.yaml) | 12 operations, proposed bearer (JWT) security, generic `Error {code, message}` envelope, 400/401/403/404/409 responses |
| Quality model | ISO/IEC 25010 product quality characteristics | Category names in §2 |

If PR #43 changes an FR, BR or NFR ID before merging, the trace columns below must be rechecked.

**Target status values used in this document**

| Status | Meaning |
|---|---|
| **Proposed** | A candidate target suggested by QA so the requirement is measurable. It is not a commitment until the Product Owner accepts it and Arda confirms it is technically feasible. Any member may replace the value. |
| **Open** | No target is proposed yet, because a decision in the linked OQ is missing. The requirement cannot be accepted unconditionally while it is Open. |
| **Approved** | Accepted by the decision owner, with an evidence link. **No NFR has this status yet.** |

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
| NFR-SEC-01 | When any client sends a request to a protected operation, including directly to the API without the UI, the server checks authentication and role/record permission before doing anything. Unauthenticated → 401; authenticated but not permitted → 403. | FR-02, BR-08; PB-02 | P1 | Rule from SRS; measures Proposed |
| NFR-SEC-02 | When a Student requests another student's grades, enrollments or record by ID or by any filter, the system returns 403 and the response body contains no data of the other student. | FR-02, FR-05, FR-07, BR-07; PB-02, PB-05, PB-07 | P1 | Rule from SRS; measures Proposed |
| NFR-SEC-03 | When login fails, the response does not reveal whether the account exists: unknown account and wrong password produce the same status code, the same `code` and the same `message`. | FR-01; PB-01 | P1 | Rule from SRS; measures Proposed |
| NFR-SEC-04 | Passwords are never stored, logged or returned in plain text; only a salted hash produced by an adaptive algorithm (for example bcrypt or Argon2) is stored. | FR-01; User/account data (SRS §6) | P1 | Proposed (algorithm: OQ-02) |
| NFR-SEC-05 | All client–server traffic outside a developer machine uses HTTPS (TLS 1.2 or higher); a token or credential is never placed in a URL. | FR-01, FR-02 | P1 | Proposed (deployment: Arda) |
| NFR-SEC-06 | Repeated failed logins for the same account are limited so that password guessing is slowed down. | FR-01; PB-01 | P2 | **Open** — lockout/rate limit is undecided in OQ-02 |
| NFR-AUD-01 | Changes to grades, student records, course records and role assignments are recorded with actor, UTC time, entity, operation and old/new value; the log cannot be edited through the API. | FR-03, FR-04, FR-06, BR-09 | P2 | **Open** — scope, access and retention are OQ-09; candidate content Proposed |
| NFR-PRIV-01 | Test cases, examples, prototypes and documentation use synthetic data only; no real student data appears in the repository. | SRS §4 assumption 3 | P1 | Proposed |
| NFR-DATA-01 | A create/update request that fails validation, uniqueness or permission checks leaves the stored data exactly as it was (no partial write). | FR-03 – FR-06, BR-09 | P1 | Rule from SRS; measures Proposed |
| NFR-DATA-02 | When several students request the last free seat of a course offering at the same moment, the number of active enrollments never exceeds capacity and each student has at most one enrollment per offering and term. | FR-05, BR-03, BR-04; PB-05 | P1 | Proposed (waitlist/race behaviour: OQ-06) |
| NFR-PERF-01 | Under normal load, users get a response quickly enough not to interrupt their work. | All FRs | P2 | Proposed targets in §4 (SRS: OQ-10) |
| NFR-PERF-02 | During the enrollment-period peak, the enrollment and list operations stay responsive and correct. | FR-05; PB-05 | P2 | Proposed targets in §4 (OQ-05, OQ-10) |
| NFR-AVAIL-01 | Academic data survives a server failure, and the service can be restored from backup. | All FRs | P3 | **Open** — SRS marks it "only if required"; OQ-10 |
| NFR-USE-01 | A first-time user can complete the core flows of their role (Student: enroll, view grades; Instructor: enter a grade; Staff: create a student) without help. | FR-03, FR-05 – FR-07 | P2 | Proposed; checkable on the Figma prototype |
| NFR-USE-02 | Every error is shown to the user as a specific message that says what went wrong and what to do; a loading/API error is never shown as an empty list. | FR-05, FR-07; PB-05, PB-07 | P1 | Rule partly from SRS FR-07; measures Proposed |
| NFR-ACCESS-01 | The web interface meets WCAG 2.2 level AA for the core flows. | All UI flows | P2 | Proposed (level to be confirmed by team) |
| NFR-TEST-01 | Each approved functional requirement has at least one positive test and, where applicable, negative/alternate-path tests with observable expected outcomes. | FR-01 – FR-07 | P1 | Rule from SRS; measures Proposed |
| NFR-MAINT-01 | The API contract stays valid and in sync with the requirements: every operation is traceable to an FR/PB and every response matches the contract. | All FRs; `api/openapi.yaml` | P2 | Proposed |

Source of each ID: NFR-SEC-01–03, NFR-DATA-01, NFR-TEST-01, NFR-AUD-01, NFR-PERF-01, NFR-AVAIL-01 and NFR-ACCESS-01 come from SRS §8 (wording refined here as scenarios). NFR-SEC-04–06, NFR-PRIV-01, NFR-DATA-02, NFR-PERF-02, NFR-USE-01–02 and NFR-MAINT-01 are new QA proposals and must be added to the SRS/backlog trace by Nurefşan only if accepted.

## 4. Quality measures

For every NFR: what is measured, the proposed target, under which load/environment, how it is measured and when it passes. "Stage" says whether the check can be done now on the Sprint 2 documents (**S2-doc**) or only after implementation (**Impl**).

### 4.1 Security and privacy

| NFR | Metric / unit | Target (status) | Environment / workload | Method / tool (proposed) | Pass / fail rule | Stage |
|---|---|---|---|---|---|---|
| NFR-SEC-01 | Protected operations without a correct 401/403 check, count | 0 of 12 operations (Proposed) | Test environment; one synthetic account per role plus no token, expired token and forged token | Authorization matrix test: every operation × every role × token state, automated API tests (pytest + requests, or Postman/Newman) | Pass if every cell gives the expected 2xx/401/403; any unexpected 2xx is a fail | S2-doc: every protected operation in OpenAPI declares 401 and 403 responses. Impl: test run |
| NFR-SEC-02 | Cross-student requests returning another student's data, count | 0 (Proposed) | Two synthetic Students A and B with grades and enrollments | Request B's resources with A's token by ID and by list/filter parameters; inspect status and body | Pass if every attempt returns 403 and the body has only `code`/`message` | Impl |
| NFR-SEC-03 | Observable difference between "unknown account" and "wrong password" responses | No difference in status, `code`, `message` (Proposed); response-time difference measured and reported | Test environment, 20 attempts per case | Compare responses field by field; record the median response time of each case | Pass if status, `code` and `message` are identical | S2-doc: OpenAPI `createSession` has a single 401 response. Impl: test |
| NFR-SEC-04 | Plain-text passwords in database, logs or responses, count | 0 (Proposed) | Test database and application logs after the login test suite | Inspect the stored credential column; search logs and responses for the test passwords | Pass if only hash values are stored and the test passwords appear nowhere | Impl; design review of the data model (S2-doc, with Arda) |
| NFR-SEC-05 | Non-HTTPS endpoints reachable outside localhost; tokens in URLs, count | 0 and 0 (Proposed) | Any shared or deployed environment | Request over `http://`; review the OpenAPI for credentials in path/query parameters | Pass if HTTP is refused or redirected and no parameter carries a token | S2-doc: OpenAPI parameter review. Impl: deployed check |
| NFR-SEC-06 | Failed attempts allowed before limiting; lock duration | **Open** (OQ-02) | — | — | Cannot be accepted until OQ-02 is decided | — |
| NFR-AUD-01 | Audited changes missing a log entry, count; log entries editable via API | 0 and none (Proposed once OQ-09 defines the list of audited events) | Test environment | Perform each audited change, then read the log; try to update/delete a log entry through the API | Pass if every change has one complete entry and modification is impossible | **Open** until OQ-09; then Impl |
| NFR-PRIV-01 | Real personal data found in repository files, count | 0 (Proposed) | Repository at the submission commit | Manual review of examples, fixtures and prototype screenshots; the QA checklist records the check | Pass if all names, numbers and e-mails are clearly synthetic | S2-doc |

### 4.2 Data integrity

| NFR | Metric / unit | Target (status) | Environment / workload | Method / tool (proposed) | Pass / fail rule | Stage |
|---|---|---|---|---|---|---|
| NFR-DATA-01 | Rejected requests that changed stored data, count | 0 (Proposed) | Test database with known synthetic records | For each create/update operation send invalid, duplicate and unauthorized requests; compare a database snapshot before and after | Pass if the snapshot is unchanged after every rejected request | Impl |
| NFR-DATA-02 | Active enrollments above capacity; duplicate enrollments per student-offering-term, count | 0 and 0 (Proposed) | One offering with capacity 1; 50 parallel enrollment requests from 50 synthetic students; test repeated 10 times | Concurrent requests (k6 or a Python thread pool), then count enrollments in the database | Pass if, in all 10 runs, exactly 1 request succeeds and the rest get 409 | Impl |

### 4.3 Performance and reliability

The numbers below are QA proposals sized for a single-university course project with an assumed peak of a few hundred simultaneous users. They must be replaced if the Product Owner or Arda gives a different expected load.

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
| NFR-ACCESS-01 | WCAG 2.2 AA violations on core-flow screens, count | 0 critical; text contrast ≥ 4.5:1 (large text ≥ 3:1); all actions reachable by keyboard (Proposed) | Figma screens now; built pages later | Now: contrast check on Figma colours (WebAIM contrast checker or a Figma contrast plugin). Later: axe DevTools + manual keyboard test | Pass if no contrast failure and no axe "critical/serious" violation on core flows | S2-doc (contrast); Impl (full) |

### 4.5 Testability and maintainability

| NFR | Metric / unit | Target (status) | Environment / workload | Method / tool (proposed) | Pass / fail rule | Stage |
|---|---|---|---|---|---|---|
| NFR-TEST-01 | Approved FRs without a positive test case; FRs with error scenarios but no negative test case, count | 0 and 0 (Proposed) | Requirement–test traceability matrix | QA writes test case IDs per FR acceptance criterion and checks coverage both ways | Pass if every approved FR acceptance criterion maps to ≥ 1 test case | S2-doc (test design); Impl (execution) |
| NFR-MAINT-01 | OpenAPI lint errors; operations without an FR/PB reference; responses not matching the schema | 0 errors with Redocly CLI `recommended`; 0 untraced operations (Proposed); 0 schema mismatches later | `api/openapi.yaml` at the submission commit | Redocly CLI lint (used in Sprint 1, QA-06); trace check against SRS §9; later contract tests (e.g. Schemathesis) | Pass if lint has 0 errors and every operation is traced | S2-doc (lint, trace); Impl (contract tests) |

## 5. Verification plan

### 5.1 What can be checked in Sprint 2 (documents and prototype only)

| Check | NFRs | Input artifact | Who (proposed) | Status |
|---|---|---|---|---|
| Every protected OpenAPI operation declares 401 and 403; `createSession` has one generic 401; no token in path/query | SEC-01, SEC-03, SEC-05 | `api/openapi.yaml` | Ahmet; Arda confirms | Pending |
| OpenAPI lint 0 errors; every operation traced to FR/PB | MAINT-01 | `api/openapi.yaml`, SRS §9 | Ahmet | Pending |
| Test-case IDs written for each FR acceptance criterion | TEST-01 | SRS FR-01–FR-07 | Ahmet | Pending |
| Error/empty-state walkthrough and contrast check | USE-02, ACCESS-01 | Figma prototype and flows (#32, #33) | Ahmet with the prototype owner | Pending — prototype not available yet |
| Task-based usability test, ≥ 5 testers per flow | USE-01 | Clickable Figma prototype | Ahmet organizes; prototype owner fixes | Pending — prototype not available yet |
| Synthetic-data review | PRIV-01 | All Sprint 2 documents and prototype | Ahmet | Pending |
| NFRs reflected in architecture (security layer, database transactions/constraints for capacity, backup) | SEC-01, SEC-04, DATA-01, DATA-02, AVAIL-01 | C4/UML documents (#34–#36) | Arda; Ahmet checks consistency | Pending — architecture not available yet |

### 5.2 What is planned after implementation

Load tests (PERF-01, PERF-02, DATA-02), the authorization matrix test (SEC-01, SEC-02), credential and log inspection (SEC-04), audit-log tests (AUD-01), restore drill (AVAIL-01) and the automated accessibility scan (ACCESS-01). These require a running system and are **not** part of the Sprint 2 evidence. Tools named in §4 are proposals; Arda decides the final stack.

### 5.3 Evidence to collect

For every check: date, checked commit or Figma version, tool and version, raw output (or screenshot), result (Pass / Fail / Pending) and the person who checked it. Results go into the Sprint 2 QA report under #38; a failed check becomes a finding with an owner.

## 6. Open decisions

These are needed before the related NFR can move from Proposed/Open to Approved. IDs refer to the SRS decision log; no new decision is assumed here.

| Decision | SRS ref | Affects | Decision owner (from SRS) | Status |
|---|---|---|---|---|
| Expected number of users and peak concurrency during enrollment | OQ-10 | PERF-01, PERF-02 (all numbers in §4.3) | Ahmet + team; PO confirms | Open |
| Whether availability/backup is in scope for the course project | OQ-10 | AVAIL-01 | Team | Open |
| Authentication method, password hashing, lockout/rate limit | OQ-02 | SEC-04, SEC-06 | Arda/team | Open |
| Which changes are audited, who can read the log, retention | OQ-09 | AUD-01 | Team/QA | Open |
| Capacity, waitlist and race-condition behaviour | OQ-06 | DATA-02 | Product Owner + Arda/team | Open |
| Error-code names and error schema | OQ-08 | SEC-01, SEC-03, USE-02 | Arda | Open |
| Accessibility level (WCAG 2.2 AA proposed) and usability test with classmates | — (new; to be added to the SRS log if accepted) | ACCESS-01, USE-01 | Team / prototype owner | Open |

## 7. Review and evidence tracker

| Review / decision | Reviewer or decision owner | Required evidence | Status | Evidence link / date |
|---|---|---|---|---|
| Technical feasibility of every Proposed target | Arda | PR review comments | Pending | [TODO] |
| Product priority and acceptance of targets | Nurefşan (Product Owner) | PR review or decision-log entry | Pending | [TODO] |
| Independent review of this document (author is not the reviewer) | Arda or another member | PR approval | Pending | [TODO] |
| New NFR IDs added to SRS §8 and backlog trace | Nurefşan | Commit in the SRS/backlog PR | Pending | [TODO] |
| Assignment of #30 and #31 | Mert (coordination) / team | Issue assignee | Pending | [TODO] |

## 8. Limitations

- No product exists, so every target is unverified; this document gives no test result.
- The performance numbers are proposals based on an assumed load, not on measurements or a stakeholder statement.
- The SRS used here is an unmerged draft (PR #43 @ `a9b6b48`); IDs or wording may change.
- ISO/IEC 25010 and WCAG 2.2 are used as category and checklist references; no formal conformance claim is made.
