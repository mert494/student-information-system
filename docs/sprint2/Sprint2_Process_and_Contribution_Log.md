# Sprint 2 Process, Decisions & Contribution Evidence (S2-12 / Issue #37)

- **Snapshot Date:** 2026-11-20 (`UTC+3` / `Europe/Istanbul`)
- **Timezone Note:** All event dates and timestamps in this log are recorded in `UTC+3` (`Europe/Istanbul`) unless explicitly marked as `Pending`.
- **Tracking Issue:** [Issue #37](https://github.com/mert494/student-information-system/issues/37)
- **Tracking PR:** [PR #44](https://github.com/mert494/student-information-system/pull/44) (Prior Reviewed HEAD: `fbc2b44`; Follow-up Reviewed HEAD: `269b489` / `479e68b`)
- **System Name Note:** `SIS` (Student Information System) is used consistently across this log.

> **Note:** Sprint 1 records are preserved untouched. Open PRs, unverified artifacts, and items awaiting reviewer approval remain explicitly marked as `Draft / Open`, `Under Review`, `Unverified`, or `Pending`. Dismissed approvals (`DISMISSED`) are recorded only as historical review evidence and never counted as currently valid approvals; proposed reviewers are never counted as having completed a review.

---

## 1. Decisions & Review History Log

| Date (`UTC+3`) | Decision / Review Event | Participants / Approvers | Outcome / State | Evidence Link |
| :--- | :--- | :--- | :--- | :--- |
| 2026-11-17 20:31 | Sprint 2 planning / tracking PR merged into `develop` (Merge SHA: `eb6e7a0`) | Mert (Author & Merger: `mert494`); Ahmet (`APPROVED` at `c6a1aa9`); Azra (`APPROVED` review link recorded) | `MERGED` (`eb6e7a0`) | [PR #24](https://github.com/mert494/student-information-system/pull/24) · Ahmet: https://github.com/mert494/student-information-system/pull/24#pullrequestreview-5937084529 · Azra: https://github.com/mert494/student-information-system/pull/24#pullrequestreview-5924357973 |
| 2026-11-17 21:07 | Sprint 2 planning / tracking PR merged into `develop` (Merge SHA: `2945b81`) | Mert (Author & Merger: `mert494`); Ahmet (First approval `DISMISSED` after base change; re-`APPROVED` at `54c1e0a`); Azra (`APPROVED` review link recorded) | `MERGED` (`2945b81`) | [PR #25](https://github.com/mert494/student-information-system/pull/25) · Ahmet: https://github.com/mert494/student-information-system/pull/25#pullrequestreview-5943542094 · Azra: https://github.com/mert494/student-information-system/pull/25#pullrequestreview-5943656924 |
| 2026-11-18 22:51 | Sprint 2 release/integration evidence PR opened | Barış (Author / Reviser); Mert (`mert494`, Reviewer) | `OPEN` (Submitted `2026-11-18 22:51:36 UTC+3`) | [PR #42](https://github.com/mert494/student-information-system/pull/42) |
| 2026-11-19 00:47 | Sprint 2 release/integration evidence PR merged into `develop` (Merge SHA: `98f9b5a`, `2026-11-18 21:47 UTC`) | Barış (Author / Reviser); Mert (`mert494`, Merger; review recorded); Azra (Historical `DISMISSED` approval) | `MERGED` (`98f9b5a` at `2026-11-19 00:47:44 UTC+3`; Azra: `DISMISSED` historical record only) | [PR #42](https://github.com/mert494/student-information-system/pull/42) · Mert: https://github.com/mert494/student-information-system/pull/42#pullrequestreview-5965667751 · Azra (`DISMISSED`): https://github.com/mert494/student-information-system/pull/42#event-36581772978 |
| 2026-11-19 21:56 | Sprint 2 planning / tracking PR merged into `develop` (Merge SHA: `ee5c64b`) | Mert (Author & Merger: `mert494`); Ahmet (`APPROVED` at `f4d49c1`); Azra (`APPROVED` review link recorded) | `MERGED` (`ee5c64b`) | [PR #41](https://github.com/mert494/student-information-system/pull/41) · Ahmet: https://github.com/mert494/student-information-system/pull/41#pullrequestreview-5970428075 · Azra: https://github.com/mert494/student-information-system/pull/41#pullrequestreview-5960127871 |
| 2026-11-19 23:46 | Sprint 2 architecture PR opened (`Docs/arda sprint2 architecture`) and reviewed | Arda (`ardaberkkara1`, Author); Ahmet (Reviewer: `COMMENTED`); Final approval (`Pending`) | `Draft / Open` (Opened `2026-11-19 23:46:54 UTC+3`; final acceptance `Pending`) | [PR #47](https://github.com/mert494/student-information-system/pull/47) · Review: https://github.com/mert494/student-information-system/pull/47#pullrequestreview-5992352880 |
| 2026-11-19 | Sprint 2 responsibility acceptance and initial Figma user-flow & prototype sharing for SIS (#32, #33) | Azra (Owner / Author) | `Recorded` (Issue comments; not formal PR reviews) | #32 initial: https://github.com/mert494/student-information-system/issues/32#issuecomment-6992432115 · #33 initial: https://github.com/mert494/student-information-system/issues/33#issuecomment-6996146017 |
| 2026-11-19 | Sprint 2 requirements / SRS traceability PR submitted and reviewed | Nurefşan (Author); Mert (Reviewer: `COMMENTED`) | `COMMENTED` / `Under Review` | [PR #43](https://github.com/mert494/student-information-system/pull/43) · Mert: https://github.com/mert494/student-information-system/pull/43#pullrequestreview-5965776469 |
| 2026-11-20 | Sprint 2 QA / quality attributes PR revised (`4502c7e`) and reviewed | Ahmet (Author); Mert (Reviewer) | `Under Review` (`4502c7e` on `2026-11-20 UTC+3`) | [PR #45](https://github.com/mert494/student-information-system/pull/45) · Review: https://github.com/mert494/student-information-system/pull/45#pullrequestreview-5998972154 |
| 2026-11-20 | QA matrix recheck (`0f0d2fb`) and Ahmet's prototype QA walkthrough on #33 | Ahmet (Reviewer: `COMMENTED` on #46 on `2026-11-20 UTC+3`; static QA walkthrough comment on #33 on `2026-11-20`) | `COMMENTED` (`0f0d2fb` on `2026-11-20 UTC+3`) | [PR #46](https://github.com/mert494/student-information-system/pull/46) · Ahmet #46: https://github.com/mert494/student-information-system/pull/46#pullrequestreview-5998727032 · Ahmet #33 walkthrough: https://github.com/mert494/student-information-system/issues/33#issuecomment-7039054965 |
| 2026-11-20 | Sprint 2 process & contribution log (`PR #44`, HEAD `269b489` / `479e68b`) & Figma recheck (`v1.2-sprint2-recheck`) | Azra (Author); Mert (Reviewer: `COMMENTED`); Ahmet (Reviewer: `COMMENTED`) | `Under Review` / Recheck updated (`v1.2-sprint2-recheck` on #32, #33) | [PR #44](https://github.com/mert494/student-information-system/pull/44) · Mert: https://github.com/mert494/student-information-system/pull/44#pullrequestreview-5981606023 · Ahmet: https://github.com/mert494/student-information-system/pull/44#pullrequestreview-5992353101 · #32 update: https://github.com/mert494/student-information-system/issues/32#issuecomment-7050134256 · #33 update: https://github.com/mert494/student-information-system/issues/33#issuecomment-7050129787 |
| Pending | Final PR/log approvals and remaining peer-assessment records | All Team Members | `Pending` | Pending verification |

---

## 2. Member Contribution Evidence (Sprint 2 Only)

> *Assignment alone is not counted as contribution. Open PRs represent draft/in-review work, not accepted delivery.*

- **Azra:**
  - **Process & Contribution Log (`Draft / Open`):** Authored and revised Sprint 2 process and contribution log in [PR #44](https://github.com/mert494/student-information-system/pull/44) (linked to [Issue #37](https://github.com/mert494/student-information-system/issues/37)).
  - **UI/UX Design & Prototype (`v1.2-sprint2-recheck` — Recheck Updated):** Accepted responsibility and shared initial Figma design & prototype links via comments in [Issue #32](https://github.com/mert494/student-information-system/issues/32#issuecomment-6992432115) and [Issue #33](https://github.com/mert494/student-information-system/issues/33#issuecomment-6996146017); subsequently frozen version `v1.2-sprint2-recheck` with `409 Conflict Error` screen, `Grades - Empty State` screen, `User Flow` page (Student, Faculty, Student Affairs), and public view access (`Anyone: can view`) and posted recheck updates on [#32](https://github.com/mert494/student-information-system/issues/32#issuecomment-7050134256) and [#33](https://github.com/mert494/student-information-system/issues/33#issuecomment-7050129787).
  - **Sprint 2 PR Reviews:**
    - [PR #24](https://github.com/mert494/student-information-system/pull/24): `APPROVED` (https://github.com/mert494/student-information-system/pull/24#pullrequestreview-5924357973).
    - [PR #25](https://github.com/mert494/student-information-system/pull/25): `APPROVED` (https://github.com/mert494/student-information-system/pull/25#pullrequestreview-5943656924).
    - [PR #41](https://github.com/mert494/student-information-system/pull/41): `APPROVED` (https://github.com/mert494/student-information-system/pull/41#pullrequestreview-5960127871).
    - [PR #42](https://github.com/mert494/student-information-system/pull/42): Prior approval recorded as `DISMISSED` (https://github.com/mert494/student-information-system/pull/42#event-36581772978; historical review evidence only, not a valid current approval).
- **Mert:**
  - **Planning, Coordination & Setup (`Merged / Active`):** Authored Sprint 2 planning and repository tracking updates in [PR #24](https://github.com/mert494/student-information-system/pull/24) (merged `2026-11-17 20:31` `UTC+3`, SHA `eb6e7a0`), [PR #25](https://github.com/mert494/student-information-system/pull/25) (merged `2026-11-17 21:07` `UTC+3`, SHA `2945b81`), and [PR #41](https://github.com/mert494/student-information-system/pull/41) (merged `2026-11-19 21:56` `UTC+3`, SHA `ee5c64b`), all merged by `mert494`.
  - **Reviews & Merges (`Active`):** Merged [PR #42](https://github.com/mert494/student-information-system/pull/42) (`mert494`, opened `2026-11-18 22:51:36 UTC+3`, merged `2026-11-19 00:47:44 UTC+3` / `2026-11-18 21:47 UTC`, SHA `98f9b5a`); recorded review on [PR #42](https://github.com/mert494/student-information-system/pull/42) (https://github.com/mert494/student-information-system/pull/42#pullrequestreview-5965667751); recorded `COMMENTED` reviews on [PR #43](https://github.com/mert494/student-information-system/pull/43) (https://github.com/mert494/student-information-system/pull/43#pullrequestreview-5965776469), [PR #44](https://github.com/mert494/student-information-system/pull/44) (https://github.com/mert494/student-information-system/pull/44#pullrequestreview-5981606023), and [PR #45](https://github.com/mert494/student-information-system/pull/45) (https://github.com/mert494/student-information-system/pull/45#pullrequestreview-5998972154).
- **Ahmet:**
  - **QA & NFR Documentation (`Under Review`):** Authored Sprint 2 quality/NFR deliverable in [PR #45](https://github.com/mert494/student-information-system/pull/45), revised at `4502c7e` on `2026-11-20` (`UTC+3`) after Mert's review (`Under Review`), and published a static prototype QA walkthrough comment on [Issue #33](https://github.com/mert494/student-information-system/issues/33) on `2026-11-20` (https://github.com/mert494/student-information-system/issues/33#issuecomment-7039054965).
  - **Sprint 2 PR Reviews (GitHub API verified `2026-11-20`, `UTC+3`):**
    - [PR #24](https://github.com/mert494/student-information-system/pull/24): `APPROVED` at `c6a1aa9` (https://github.com/mert494/student-information-system/pull/24#pullrequestreview-5937084529).
    - [PR #25](https://github.com/mert494/student-information-system/pull/25): First approval `DISMISSED` after base change; re-`APPROVED` at `54c1e0a` (https://github.com/mert494/student-information-system/pull/25#pullrequestreview-5943542094).
    - [PR #41](https://github.com/mert494/student-information-system/pull/41): `APPROVED` at `f4d49c1` (https://github.com/mert494/student-information-system/pull/41#pullrequestreview-5970428075).
    - [PR #44](https://github.com/mert494/student-information-system/pull/44): `COMMENTED` (https://github.com/mert494/student-information-system/pull/44#pullrequestreview-5992353101).
    - [PR #46](https://github.com/mert494/student-information-system/pull/46): `COMMENTED` at `0f0d2fb` on `2026-11-20` (`UTC+3`, recheck of QA matrix; https://github.com/mert494/student-information-system/pull/46#pullrequestreview-5998727032).
    - [PR #47](https://github.com/mert494/student-information-system/pull/47): `COMMENTED` (https://github.com/mert494/student-information-system/pull/47#pullrequestreview-5992352880).
- **Barış:**
  - **Integration & Release Evidence (`MERGED`):** Authored and revised Sprint 2 integration/release evidence in [PR #42](https://github.com/mert494/student-information-system/pull/42) (opened `2026-11-18 22:51:36 UTC+3`); merged into `develop` by Mert (`mert494`) on `2026-11-19 00:47:44` (`UTC+3` / `2026-11-18 21:47 UTC`, SHA `98f9b5a`).
- **Nurefşan:**
  - **SRS & Traceability (`Under Review`):** Authored and submitted revision commits for Sprint 2 requirements and traceability in [PR #43](https://github.com/mert494/student-information-system/pull/43).
- **Arda:**
  - **Architecture & UML/C4 Deliverables (`Draft / Open`):** Sprint 2 architecture PR ([PR #47](https://github.com/mert494/student-information-system/pull/47)) opened on `2026-11-19 23:46:54 UTC+3` (`Docs/arda sprint2 architecture`); `Under Review` / final acceptance `Pending` (historical Sprint 1 artifacts are excluded).

---

## 3. Figma Artifact & Independent Verification Status (#32, #33)

- **Design File URL:** [Figma Design File (SENG321 - OBS prototype)](https://www.figma.com/design/n5jM7D19uV3Yj2rQRkoV6F/SENG321---OBS-prototype?node-id=1-1681&t=TYQmKoo4qRKQGD8q-1) (Frozen snapshot: `v1.2-sprint2-recheck`; prior initial link: `https://www.figma.com/design/n5jM7D19uV3Yj2rQRkoV6F/Untitled?node-id=1-1681&t=obxBWqyIa9OpcM99-1`)
- **Interactive Prototype URL:** [Figma Interactive Prototype (SENG321 - OBS prototype)](https://www.figma.com/proto/n5jM7D19uV3Yj2rQRkoV6F/SENG321---OBS-prototype?node-id=1-1681&t=TYQmKoo4qRKQGD8q-1) (Prior initial link: `https://www.figma.com/proto/n5jM7D19uV3Yj2rQRkoV6F/Untitled?node-id=1-1681&t=obxBWqyIa9OpcM99-1`)
- **Issue Comment Evidence:** #32 initial comment (`https://github.com/mert494/student-information-system/issues/32#issuecomment-6992432115`) & recheck update (`https://github.com/mert494/student-information-system/issues/32#issuecomment-7050134256`); #33 initial comment (`https://github.com/mert494/student-information-system/issues/33#issuecomment-6996146017`), Ahmet's 2026-11-20 walkthrough (`https://github.com/mert494/student-information-system/issues/33#issuecomment-7039054965`), & recheck update (`https://github.com/mert494/student-information-system/issues/33#issuecomment-7050129787`).

| Verification Dimension | Current Status | Notes |
| :--- | :--- | :--- |
| GitHub Sharing & Acceptance Comments | `Recorded` | Responsibility acceptance and recheck updates posted via comments in [Issue #32](https://github.com/mert494/student-information-system/issues/32#issuecomment-6992432115) ([recheck](https://github.com/mert494/student-information-system/issues/32#issuecomment-7050134256)) and [Issue #33](https://github.com/mert494/student-information-system/issues/33#issuecomment-6996146017) ([recheck](https://github.com/mert494/student-information-system/issues/33#issuecomment-7050129787)) (Issue comments, not formal PR review states) |
| Independent Team Access & Reviewer Permissions | `Updated / Recheck Pending` | Access was `Pending` during initial walkthrough; `Anyone: can view` is now enabled on the Figma file, awaiting final reviewer confirmation (`NFR-ACCESS-01`) |
| Actual User-Flow Coverage (Student, Faculty, Student Affairs) | `Updated / Recheck Pending` | Ahmet's 2026-11-20 walkthrough noted partial flow coverage and missing student actions; `User Flow` page (Student, Faculty, Student Affairs) and `409 Conflict Error` / `Grades - Empty State` screens added in `v1.2-sprint2-recheck`, awaiting recheck acceptance (`NFR-USE-02`) |
| Click-Through Prototype Behavior & Usability Testing | `Static Walkthrough Recorded; Usability Test Pending` | Ahmet performed a **static walkthrough** on 2026-11-20 with documented findings (partial flow coverage, missing student actions, `NFR-USE-02` and `NFR-ACCESS-01` prototype-subset issues); **no user-based usability test (`NFR-USE-01`)** has been conducted, and any contrast observations were visual estimates rather than instrument-measured values |
| Frozen Version & Final UX Acceptance | `v1.2-sprint2-recheck` Saved; Final Acceptance `Pending` | Version `v1.2-sprint2-recheck` saved in Figma version history; final UX acceptance and any static/PDF/PNG exports remain `Pending` |

---

## 4. Peer Assessment Requirements Tracking (Issue #37)

| Item | Details | Status |
| :--- | :--- | :--- |
| Official Source | Course / Instructor guidelines (BM321 Software Engineering — Sprint 2 instructions) | `Pending` |
| Applicable Form / Method | Official Sprint 2 peer evaluation form / submission method | `Pending` |
| Assessment Results | Individual peer evaluation records | `Pending` |
