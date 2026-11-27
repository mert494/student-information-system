# Sprint 3 Test Strategy and Test Matrix

**Version:** Draft 0.1 (category A preparation: test design only; no test code written or run)
**Owner (suggested):** Ahmet (`ahmetserdar41`), QA / Testing; assignment pending Mert's confirmation
**Related Issues:** [#64](https://github.com/mert494/student-information-system/issues/64) (S3-13), [#67](https://github.com/mert494/student-information-system/issues/67) (S3-16); depends on [#52](https://github.com/mert494/student-information-system/issues/52) (S3-01), [#53](https://github.com/mert494/student-information-system/issues/53) (S3-02), [#54](https://github.com/mert494/student-information-system/issues/54) (S3-03)
**Status:** Draft for team review. Not approved by Arda (technical) or Nurefşan (product). Expected results that depend on an open decision are marked **Blocked** and are not guessed.

## 1. Purpose and sources

This document defines how the Sprint 3 MVP will be tested and which tests prove each requirement. It is written before the code so that features can be built against known checks.

Sources, all at Sprint 2 release `sprint-2` / `main` `409049b`:

| Source | Used for |
| --- | --- |
| [SRS Draft 0.3](https://github.com/mert494/student-information-system/blob/409049b69f25596968ae2ba678abd2afbfdd798e/docs/sprint2/SRS_Draft.md) | FR-01–FR-07 acceptance criteria, BR-01–BR-09, PD-01–PD-04, OQ-01–OQ-13 |
| [NFR and Quality Measures Draft 0.8.4](https://github.com/mert494/student-information-system/blob/409049b69f25596968ae2ba678abd2afbfdd798e/docs/sprint2/NFR_Quality_Measures.md) | NFR IDs and planned verification methods; targets are still Proposed/Open |
| [OpenAPI draft](https://github.com/mert494/student-information-system/blob/409049b69f25596968ae2ba678abd2afbfdd798e/api/openapi.yaml) | The 12 operations; contract gaps (for example `courseId` vs `courseOfferingId`) stay open until Arda reconciles them in S3-01 |
| [#33 Product Owner decision](https://github.com/mert494/student-information-system/issues/33#issuecomment-7113667894) | Inactive students are not blocked at login; enrollment is rejected with 409 and creates no registration |

## 2. Test levels

| Level | What it proves | Tooling (proposal, pending G1) | Counts toward the 50% unit coverage? |
| --- | --- | --- | --- |
| Unit | Business rules and validation in isolation (services, validators, UI components) | JUnit 5 + Mockito; Vitest + Testing Library | **Yes**, the only level that counts |
| Integration (database) | Constraints, transactions and rollback on a real PostgreSQL | Spring Boot Test + Testcontainers, or a CI PostgreSQL service | No; reported separately |
| API / security / contract | HTTP status, body and authorization per role; responses match OpenAPI | Spring MockMvc or REST-assured; an OpenAPI response validator | No; reported separately |
| UI accessibility | Keyboard, focus, labels, errors, contrast on the built UI | axe-core (automated) plus a manual checklist | No |
| Usability | First-time users complete the core flows | Moderated sessions, ≥5 testers per core flow (#67) | No |

Performance tests (NFR-PERF-01/02) run only after the workload and targets in OQ-10 are approved.

## 3. Coverage rules

These rules make sure that the "at least 50% unit test coverage" requirement is measured honestly.

1. **Only real application source counts.** The measured set is backend `src/main` and frontend `src`.
   - Excluded: test files, generated code, build configuration, the Sprint 2 submission checker (`tools/`), and CI or gate scripts.
   - Every exclusion is listed in the build configuration and in the PR, with a reason.
2. **Unit coverage only.** Integration, API and UI test runs are reported separately and are never merged into the unit figure.
3. **Per component and visible.** Backend (JaCoCo) and frontend (Vitest coverage) each publish:
   - covered and total lines and branches;
   - the percentage;
   - the list of exclusions.
   - The reports are uploaded as CI artifacts.
4. **Threshold enforced by CI.** A drop below the agreed threshold (≥50% unless the team agrees a higher one) fails the build. The threshold metric (line or branch) is decided in G1.
5. **Scaffold is not MVP.** Coverage of the initial scaffold (reported locally as 69.23% backend and 90.32% frontend) is not evidence for the MVP. Coverage is re-measured once real SIS features exist.

## 4. CI failure exercises

Before the team relies on CI, these exercises run once on a throwaway branch. Results are recorded with the run link.

| ID | Exercise | Expected result |
| --- | --- | --- |
| CI-01 | A unit test assertion is made to fail | Run is red; the failing test is named in the log |
| CI-02 | Coverage is pushed below the threshold | Run is red with a coverage message |
| CI-03 | The coverage report is not produced | Run is red, not silently green |
| CI-04 | A normal passing change | Run is green; test and coverage reports are downloadable as artifacts |
| CI-05 | An integration test fails against PostgreSQL | Run is red; reported separately from unit results |

## 5. Test environment and data

- **Synthetic data only (NFR-PRIV-01):** one account per role (Student A, Student B, Instructor assigned, Instructor not assigned, Student Affairs Staff, Administrator), plus an inactive student.
- **Fixtures** come from the S3-04 demo seed (#55). Test-only passwords are never real passwords and are never committed as real secrets.
- **Token states for security tests:** none, valid, expired, forged signature, and revoked after logout.
- **Every result records** the commit SHA, tool versions and the CI run link.

## 6. Test matrix

Status values:
- **Ready**: the expected result is fixed by an approved requirement.
- **Blocked**: the result depends on an open decision, named in the last column.

IDs are stable; new cases are added, never renumbered.

### FR-01 — Authenticate user (PB-01)

| ID | Level | Scenario | Expected result | Trace | Status / blocking decision |
| --- | --- | --- | --- | --- | --- |
| T-01-01 | API | Valid credentials | Login succeeds; a token with a `sid` claim is issued | FR-01, PD-01 | Ready (response body mapping: OQ-02) |
| T-01-02 | API | Wrong password for an existing account | Rejected | FR-01 | Ready (status code/schema: OQ-08) |
| T-01-03 | API | Unknown account vs wrong password | Same status, same `code`, same `message` | NFR-SEC-03 | Ready (exact code: OQ-08) |
| T-01-04 | API | Protected call after logout with the old token | 401; session revoked server-side | PD-01, NFR-SEC-01 | Ready |
| T-01-05 | API | Expired and forged tokens | 401 | NFR-SEC-01 | Blocked: expiry policy (OQ-02) |
| T-01-06 | Unit | Password storage | Only an adaptive hash with a per-credential salt is stored; the password is never logged or returned | NFR-SEC-04 | Blocked: algorithm/cost (OQ-02) |
| T-01-07 | API | Inactive student logs in | Login is **not** blocked | #33 decision | Ready |
| T-01-08 | API | Repeated failed logins | Attempts are limited | NFR-SEC-06 | Blocked: lockout/rate limit (OQ-02) |

### FR-02 — Enforce role and record authorization (PB-02)

| ID | Level | Scenario | Expected result | Trace | Status / blocking decision |
| --- | --- | --- | --- | --- | --- |
| T-02-01 | API | Each of the 11 protected operations without a token | 401 | FR-02, NFR-SEC-01 | Ready |
| T-02-02 | API | Each protected operation for each role (operation × role matrix) | Allowed or 403 exactly as the approved matrix says | FR-02, BR-08, NFR-SEC-01 | Blocked: role matrix (OQ-01) |
| T-02-03 | API | Student A requests Student B's registrations, grades or record directly through the API | 403; no data of B in the body | NFR-SEC-02, BR-07 | Ready |
| T-02-04 | API | 401 and 403 cases side by side | 401 and 403 are distinct outcomes | FR-02 | Ready |

### FR-03 — Create, list and update student records (PB-03)

| ID | Level | Scenario | Expected result | Trace | Status / blocking decision |
| --- | --- | --- | --- | --- | --- |
| T-03-01 | API | Staff creates a valid student | Created; appears in the list | FR-03 | Blocked: required fields (OQ-03) |
| T-03-02 | Unit + API | Missing or invalid required field | Rejected; nothing stored | FR-03, BR-09, NFR-DATA-01 | Blocked: required fields (OQ-03) |
| T-03-03 | Integration | Duplicate student number | Rejected by validation and by the unique constraint; nothing stored | FR-03, NFR-DATA-01 | Ready (error code: OQ-08) |
| T-03-04 | API | Non-staff role creates or updates a student | 403; nothing stored | FR-03, BR-08 | Blocked: role matrix (OQ-01) |
| T-03-05 | API | PATCH with omitted, null, immutable and unknown fields | Behaviour as per the approved PATCH policy | FR-03 | Blocked: PATCH policy (OQ-12) |
| T-03-06 | API | PATCH of a non-existent student | 404 | FR-03, OpenAPI `updateStudent` | Ready |

### FR-04 — Create and update course records (PB-04)

| ID | Level | Scenario | Expected result | Trace | Status / blocking decision |
| --- | --- | --- | --- | --- | --- |
| T-04-01 | API | Staff creates a valid course | Created; appears in the course list | FR-04 | Blocked: fields (OQ-04) |
| T-04-02 | Integration | Duplicate course code within the uniqueness scope | Rejected; nothing stored | FR-04, NFR-DATA-01 | Blocked: uniqueness scope (OQ-04) |
| T-04-03 | API | Unauthorized role changes a course | 403; nothing stored | FR-04, BR-08 | Blocked: role matrix (OQ-01) |
| T-04-04 | API | PATCH field policy | As per the approved policy | FR-04 | Blocked: PATCH policy (OQ-13) |

### FR-05 — Enroll in a course and view enrollments (PB-05)

| ID | Level | Scenario | Expected result | Trace | Status / blocking decision |
| --- | --- | --- | --- | --- | --- |
| T-05-01 | API | Eligible student enrolls in an open offering | Exactly one Registration for `(studentId, courseOfferingId)`; visible in own list | FR-05, PD-02 | Blocked: request identifier (`courseId` vs `courseOfferingId`, S3-01) |
| T-05-02 | Integration | Same student enrolls twice in the same offering | Second request rejected with 409; still one Registration | BR-03, PD-03 | Ready (error code: OQ-08) |
| T-05-03 | API | Inactive student enrolls | 409 with a clear message; no Registration created | BR-01, #33 decision | Ready |
| T-05-04 | API | Enrollment outside the open period | 409; nothing created | BR-02 | Blocked: period/timezone (OQ-05) |
| T-05-05 | API | Offering is full | 409; nothing created | BR-04 | Ready |
| T-05-06 | API | Prerequisite not met | 409; nothing created | BR-05 | Blocked: prerequisite rules (OQ-06) |
| T-05-07 | Integration | Several students request the last seat at the same moment | Active registrations never exceed capacity | NFR-DATA-02 | Blocked: concurrency behaviour (OQ-06) |
| T-05-08 | Integration | Same student sends the same request several times at once | At most one Registration | NFR-DATA-02, BR-03 | Ready |
| T-05-09 | API | Student lists registrations | Only their own are returned | FR-05, NFR-SEC-02 | Ready |

### FR-06 — Enter or update grades for assigned courses (PB-06)

| ID | Level | Scenario | Expected result | Trace | Status / blocking decision |
| --- | --- | --- | --- | --- | --- |
| T-06-01 | API | Assigned instructor saves a valid grade for an enrolled student | Saved; retrievable by an authorized request | FR-06, PD-04 | Blocked: grade scale (OQ-07) |
| T-06-02 | API | Instructor not assigned to the offering | 403; nothing stored | BR-06, NFR-SEC-01 | Ready |
| T-06-03 | Unit + API | Grade out of range | Rejected; nothing stored | FR-06, BR-09 | Blocked: scale and precision (OQ-07) |
| T-06-04 | API | Grade for a student not enrolled in the offering | Rejected; nothing stored | FR-06 | Ready (status code: OQ-08) |
| T-06-05 | Integration | Grade references exactly one Registration | Constraint holds | PD-04 | Ready |

### FR-07 — View own published grades (PB-07)

| ID | Level | Scenario | Expected result | Trace | Status / blocking decision |
| --- | --- | --- | --- | --- | --- |
| T-07-01 | API | Student with published grades | Only their own published grades are returned | FR-07, BR-07 | Ready |
| T-07-02 | API | Unpublished grades exist | They are not returned | BR-07 | Blocked: publication trigger (OQ-07) |
| T-07-03 | API | Student requests another student's grades | 403; no data disclosed | NFR-SEC-02 | Ready |
| T-07-04 | UI unit | Successful query with zero results | Shows `No published grades are available.` | FR-07 | Ready |
| T-07-05 | UI unit | Query in progress | Loading state, not the empty message | FR-07, NFR-USE-02 | Ready |
| T-07-06 | UI unit | API failure | Distinct error state, not the empty message | FR-07, NFR-USE-02 | Ready |

### Cross-cutting checks

| ID | Level | Scenario | Expected result | Trace | Status / blocking decision |
| --- | --- | --- | --- | --- | --- |
| T-X-01 | Contract | Every implemented response is validated against `api/openapi.yaml` | No mismatch | NFR-MAINT-01 | Blocked: OpenAPI reconciliation (S3-01) |
| T-X-02 | Integration | Any rejected create/update/enrollment/grade request | Database unchanged (row counts and values before = after) | BR-09, NFR-DATA-01 | Ready |
| T-X-03 | Review | Repository and fixtures | No real personal data; no committed secrets or `.env` files | NFR-PRIV-01 | Ready |
| T-X-04 | Integration | Audit records for grade and record changes | As per the approved audit scope | NFR-AUD-01 | Blocked: audit scope (OQ-09) |

**Matrix summary (Draft 0.1):** 46 cases; 25 Ready, 21 Blocked. The Blocked cases depend on OQ-01–OQ-09, OQ-12/13 and the S3-01 OpenAPI reconciliation.

## 7. Usability and accessibility (#67)

The detailed protocol will be a separate document. It is outlined here so that the UI work knows what will be checked.

- **Core flows:** Student enrollment (FR-05), Student published grades (FR-07), Instructor grade entry (FR-06), Staff student creation (FR-03).
- **Testers:** ≥5 per core flow, as set by the Product Owner. Records are anonymous.
- **Proposed criteria:** ≥80% task success and enrollment in ≤4 steps. These stay **Proposed** until Nurefşan accepts them.
- **Built-UI accessibility (WCAG 2.2 AA target):**
  - an axe-core scan per screen;
  - manual keyboard-only completion of each flow, with visible focus;
  - every input has a visible label and every error is announced;
  - text contrast;
  - loading, empty, error and unauthorized states shown distinctly (NFR-USE-02).
- **Carry-over from the Sprint 2 static prototype check** ([PR #44 review 6029857255](https://github.com/mert494/student-information-system/pull/44#pullrequestreview-6029857255)):
  - focus-order messages that differ from the screens;
  - the inactive-student message styling;
  - grade-entry header fields.
- No session is run and no participant is contacted until the UI is stable and the protocol is accepted.

## 8. Entry and exit criteria

**Entry (per slice):** for each slice:
- the decision for that slice (G1–G5) is recorded;
- the feature PR is open with unit tests;
- CI is green.

**Exit (release candidate):**
- every Ready case has passed on the release-candidate commit, with its run link;
- Blocked cases are either unblocked and run, or listed with the decision owner;
- unit coverage meets the threshold under the rules in §3;
- blocking defects are fixed and retested, or explicitly dispositioned by the correct owner;
- a non-author has reviewed the test changes (Arda technical, Barış CI).

## 9. Open decisions affecting testing

| Decision | Owner | Cases blocked |
| --- | --- | --- |
| G1: test frameworks, PostgreSQL in CI, coverage metric (line or branch) | Arda, with Barış | All integration and contract levels; §3 threshold metric |
| OQ-01 role/operation matrix | Nurefşan + Arda | T-02-02, T-03-04, T-04-03 |
| OQ-02 token expiry, credentials, rate limiting | Arda | T-01-05, T-01-06, T-01-08 |
| OQ-03 / OQ-04 student and course fields, uniqueness | Nurefşan | T-03-01, T-03-02, T-04-01, T-04-02 |
| OQ-05 / OQ-06 period, prerequisites, concurrency | Nurefşan + Arda | T-05-04, T-05-06, T-05-07 |
| OQ-07 grade scale and publication | Nurefşan + Arda | T-06-01, T-06-03, T-07-02 |
| OQ-08 error schema and codes | Arda | Exact codes in many Ready cases (the status is fixed; the `code` value is not) |
| OQ-09 audit scope | Team | T-X-04 |
| OQ-12 / OQ-13 PATCH policy | Arda + Nurefşan | T-03-05, T-04-04 |
| S3-01 OpenAPI reconciliation (`courseOfferingId`) | Arda | T-05-01, T-X-01 |

## 10. Boundaries

- This is a design document. No test has been written or run, and no result is claimed.
- It does not approve any NFR target or decide any open question.
- The tool choices in §2 are proposals for G1.
