# Subsequent Sprint 3 branches and PR sequence

Status: proposal, 25 November 2026. Actual Issues/owners/estimates: [TODO] until approved. Deadline: **14 December 2026, 23:59 Europe/Istanbul**. No branch below has been created.

Use the team's approved naming convention with an actual Issue number once available. The `<issue>` strings below are patterns, not GitHub numbers. Keep each PR focused and target the approved current develop. This task authorizes neither future implementation nor remote actions.

| Order | Proposed branch/PR | Dependencies / decisions | Suggested owner and independent review | Acceptance focus |
| --- | --- | --- | --- | --- |
| 1 | `docs/<issue>-sprint3-api-contract` | Arda/PO approval of selected slices; OQ-01/02/03/04/05/06/07/08/12/13 as applicable | Arda owns contract; Nurefşan product decisions; Ahmet testability review | JWT response/`sid`/logout, roles/record mapping, offering identifiers/discovery, Grade→Registration, separate Instructor GET, published-only example and error/PATCH schemas reconciled. Lint passing does not approve semantics. |
| 2 | `feature/<issue>-auth-session` and a focused UI follow-up | Approved FR-01/02 contract, credential/hash/key/expiry/refresh/storage policies, account provisioning and role matrix | Arda proposed backend lead; Azra UI; Ahmet independent security/test review | Login → authorized request → logout → rejected replay; missing/invalid/revoked authentication, role/record denials and inactive login. No client-only logout or cosmetic authorization. |
| 3a | `feature/<issue>-student-management` | Auth, required fields/status authority/identity source and approved OQ-12 PATCH semantics | Nurefşan confirms semantics; developer capacity/assignment [TODO]; Arda + Ahmet review | Staff create/list/update, uniqueness, missing/invalid/unauthorized/no-op/null/omission/repeated update behavior and no unintended writes. |
| 3b | `feature/<issue>-course-management` | Auth, course-code uniqueness scope, Course/Offering/Term and assignment model, OQ-13 | Developer assignment [TODO]; Arda + Ahmet review; PO accepts | Course create/list/update plus approved offering selection/setup. Can run alongside 3a after shared schema/API decisions. Separate UI PRs may consume approved-contract mocks. |
| 4 | `feature/<issue>-course-enrollment` | Student/Offering persistence, identity binding, active-status source, period/timezone/authority, capacity/prerequisites/exceptions and transaction decisions | Arda proposed technical lead; Ahmet concurrency/data-integrity review; PO rules acceptance | Unique `(studentId, courseOfferingId)` and FKs in real PostgreSQL; no oversubscription; inactive/closed/full/duplicate/unmet-prerequisite conflicts; no writes on rejection; own records only. |
| 5a | `feature/<issue>-instructor-grades` | Registration, assignment model, academic scale/precision/types/multiplicity, edit window and exact authorized GET | Developer assignment [TODO]; Arda + Ahmet review; academic/PO approval | Grade references Registration; assigned Instructor saves and later retrieves through a separate GET; invalid/unauthorized/non-enrolled cases rejected without changes. |
| 5b | `feature/<issue>-published-grades` | 5a and approved publication authority/trigger/visibility/fields | Azra proposed UI lead; backend assignment [TODO]; Ahmet and PO review | Only own published grades; unpublished hidden; cross-student denial; distinct loading, successful-empty, non-empty and failed-query states. No inferred publish-on-save. |
| 6 | `feature/<issue>-mvp-integration-demo` with release documentation PR | All accepted vertical slices, real API/DB/UI, deployment applicability, agreed NFR/test environment | Mert coordinates; Barış runtime/CI; Ahmet independent QA; PO acceptance; Arda architecture review | Staff → enrollment → Instructor save/read/publication → Student grade view; repeatable startup, security/integrity checks, full-source unit coverage remeasured, CI artifact evidence and working URL where applicable. |

## Work that can proceed safely while decisions are pending

These are drafting/review activities, not approval to implement unresolved product behavior:

- Arda and Nurefşan prepare decision options, operation/record permission matrices and contract diffs; keep alternatives visibly proposed.
- Ahmet drafts acceptance/test traceability and negative/boundary/concurrency cases, marking unresolved expected outcomes. Review current scaffold tests and coverage tooling.
- Barış reviews wrapper/action pins, runner/cache/artifact behavior and investigates local Docker availability without selecting production hosting or changing repository settings.
- Azra prepares UI flow/error-state/accessibility notes and reviews the technical connection screen; no assumed product API or security grant.
- Mert confirms contributor availability, proposed Issue scopes, review coverage, deadline milestones and submission format; Azra maintains actual decision/process records.
- Recruit usability participants early for the PO's core-flow testing request. Do not record sessions or conformance results before they occur.

After slice approvals, backend and frontend can work concurrently against that approved contract using synthetic mocks for isolated frontend tests. Mock success is not backend/acceptance evidence. Student/Course implementations can proceed in parallel after shared data/permission contracts; enrollment waits for both. Grade UI drafts can proceed after its contract approval while persistence completes.

## Proposed timing / escalation

| Window | Proposed outcome |
| --- | --- |
| 25–30 November | Owner decisions, approved foundation publication/CI when authorized, selected API/security/data contracts and capacity confirmed. |
| 30 November–3 December | Auth vertical slice; Student/Course maintenance and offering lookup in small parallel PRs. |
| 4–7 December | Enrollment with actual DB race tests; Instructor save/read and approved publication. |
| 8–10 December | Student published grades and full product walkthrough; measure coverage across all new production code. |
| 11–13 December | Feature freeze, independent QA, actual usability/accessibility checks, runtime/demo and release evidence. |
| 14 December | Fix release blockers and submit before 23:59; internal target 21:00 is a proposal. Record actual receipt only after submission. |

This schedule depends on confirmed capacity and prompt policy decisions. If critical decisions/capacity remain unresolved on 30 November, Mert convenes PO-led replanning; no meeting is claimed here. Defer optional scope first. Do not silently bypass prerequisites, authorization, grade publication or other required behavior to preserve dates.

Keep the existing PD decisions and inactive-student rule unchanged. Performance targets remain Proposed and availability/recovery Open until their owners agree. The current scaffold's 69.23% / 90.32% results do not establish the expanded MVP's future coverage.

## Publication/integration rules

One independent approval is currently required for develop and two for main; stale reviews/last-push/conversation rules apply. Only merge commits are allowed. Do not force push, alter release tags, introduce a new repository setting or combine push/PR/merge authorizations. Use actual Issue/PR/commit evidence from each contributor's account. Related Issue: [TODO].
