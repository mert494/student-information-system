# GitHub Projects setup and Sprint 1 tracking

**Board configuration below is a proposal for team approval.** Evidence refreshed on 4 November 2026 through read-only GitHub queries. Issues #3, #5 and #9–#15 are open; current assignee fields are recorded below. Assignment is not approval, priority selection or deliverable acceptance. PB-01–PB-07 remain local drafts pending Nurefşan's approval; no PB Issues were created. The repository belongs to personal account `mert494`; no Organization decision is inferred. Mert reports that a Projects board was created and populated with Issues #3, #5 and #9–#15 and that task statuses/assignees were set. The available connector cannot independently inspect Projects, so board owner, URL, exact fields, views, items, live statuses and automations remain **Unverified**. The status and field tables below are proposals, not verified live configuration. This local update performs no remote operations.

## Board statuses

| Status | Entry / exit criteria |
| --- | --- |
| Backlog | Proposal recorded; PO/team scope decision and refinement pending |
| To Do | Scope, owner, Acceptance Criteria and dependencies clear; selected for the sprint |
| In Progress | Owner has started work; Issue/branch link added |
| In Review | Reviewable PR or document and check evidence ready |
| Done | Acceptance Criteria, independent review and relevant checks complete; PR merged if applicable and evidence linked |

For impediments, a separate `Blocked` field and impediment link alongside Status are proposed. A ready template file does not make the entire Sprint 1 submission Done.

## Proposed fields and views

Status, Assignees (actual GitHub accounts [TODO]), Priority (P1/P2/P3), Story Points (Number), Sprint (Sprint 1), Epic, Requirement, Dependencies, Evidence and Blocked. Preserve task IDs S1-01…S1-16; they do not replace actual Issue numbers. Organize Board view by Status; configure table view with owner, priority, sprint and evidence fields. The proposed default status is Backlog.

## Sprint 1 task list

The task roles below remain proposed and do not amend the [RACI](RACI_Matrix.md); team approval is [TODO]. Actual Issue assignee fields are separate from proposed task roles: #3 `ahmetserdar41`, #5 `baryyss-001`, #9/#10 `mert494`, #11 `nsnkcc`, #12 `nsnkcc` and `ardaberkkara1`, #13 `ardaberkkara1`, #14 `azrayy`, #15 `nsnkcc`. These Issues are open and tracked, not accepted deliverables. PB-01–PB-07 remain local drafts pending Nurefşan's approval; no PB Issues were created. Approved priorities, estimates and sprint selection remain [TODO]; assignment/creation does not establish an approved Sprint Backlog.

| ID | Task | Proposed responsible person (R) | Acceptance Criteria |
| --- | --- | --- | --- |
| S1-01 | Proposal and problem definition | Nurefşan | Problem, purpose, stakeholders and scope documented; team/PO review recorded |
| S1-02 | License decision | Nurefşan, Arda | Existing MIT file reviewed; selection rationale added to proposal; decision recorded |
| S1-03 | System Vision | Nurefşan, Arda | System goals and stakeholder needs explained; consistent with proposal |
| S1-04 | System Boundary | Arda, Nurefşan | Actors, external systems and in/out-of-scope areas clear; consistent with vision |
| S1-05 | Draft OpenAPI YAML | Arda | YAML parses; validated against selected OpenAPI version; requirements mapping and draft limitations documented |
| S1-06 | Roles and RACI | Azra, Mert | All six members included; one A per row; CSV/Markdown match; team approval recorded |
| S1-07 | Organization/repository access | Barış, Mert | Organization decision made; six members' accounts/access and repository URL verified |
| S1-08 | Git-Flow and review policy | Mert, Barış | Branch, commit, PR, review, merge, conflict and protection rules reviewed; develop decision recorded |
| S1-09 | Initial Product Backlog | Nurefşan, Mert | Stories, Acceptance Criteria, priorities, estimates and dependencies reviewed by PO/team; draft/approved distinction clear |
| S1-10 | Projects, Issues and sprint plan | Mert, Azra | Board and actual Issue links available after permission; owners, sprint goal and statuses verified |
| S1-11 | Issue/PR templates and AGENTS | Mert | All fields in three Issue templates and one PR template complete; security and approval boundaries clear; review performed |
| S1-12 | Process records | Azra, Mert | Actual meeting/attendance/decision/action records supported by evidence; events that have not occurred explicitly blank/planned |
| S1-13 | Quality and submission compliance | Ahmet, Arda, Mert | All six Sprint 1 deliverable headings and links checked; gaps and results recorded |
| S1-14 | Individual contribution evidence | All six members | Each member's actual account, Issue, PR/review and commit evidence mapped |
| S1-15 | Release/tag | Barış, Mert | Reviewed commit versioned after user approval; URL and SHA recorded |
| S1-16 | Final submission tracking | Mert, Azra, Barış | Checklist completed; submission links and course-channel submission evidence recorded |

## Verified Issue and PR mapping — 4 November 2026

| Sprint 1 work | Existing Issue | Existing PR / evidence | Remaining coordination |
| --- | --- | --- | --- |
| Quality checks | [#3](https://github.com/mert494/student-information-system/issues/3), assigned `ahmetserdar41` | [PR #2](https://github.com/mert494/student-information-system/pull/2) open, draft, head `8fac0cfa` → `develop` | Independent review and affected rechecks pending |
| Repository setup | [#5](https://github.com/mert494/student-information-system/issues/5), assigned `baryyss-001` | [PR #6](https://github.com/mert494/student-information-system/pull/6) open, head `81a66a93` → `develop` | Owner updates and reviews pending |
| Proposal, combined Vision/Boundary and Initial Backlog | [#11](https://github.com/mert494/student-information-system/issues/11), assigned `nsnkcc`; [#12](https://github.com/mert494/student-information-system/issues/12), assigned `nsnkcc` and `ardaberkkara1`; [#15](https://github.com/mert494/student-information-system/issues/15), assigned `nsnkcc` | [PR #7](https://github.com/mert494/student-information-system/pull/7) open, head `6d92c07b` → `develop`; three changed docs | Owner decisions and review pending; GitHub reports mergeable, which is not approval |
| OpenAPI draft | [#13](https://github.com/mert494/student-information-system/issues/13), assigned `ardaberkkara1` | [PR #8](https://github.com/mert494/student-information-system/pull/8) open, head `c5425a4c` → `develop`; `api/openapi.yaml` only | Arda's validation, requirements alignment and review remain pending |
| Roles/process records | [#14](https://github.com/mert494/student-information-system/issues/14), assigned `azrayy` | [PR #4](https://github.com/mert494/student-information-system/pull/4) closed, not merged; its source is represented in PR #1's merged history. [PR #17](https://github.com/mert494/student-information-system/pull/17) is open at head `271e102ddbfe311d2cc5a546e8e189b41465cf1c` with two changed files: `docs/RACI_Matrix.md` and `docs/Sprint1_Process_Records.md`. Mert's `CHANGES_REQUESTED` review is anchored to older head `ce9ac8b0`; the current diff needs review | RACI and Mert–Azra team approval remain pending; PR #17 is not approved or complete |
| Mert's process templates, guides and QA checklist corrections | [#9](https://github.com/mert494/student-information-system/issues/9) and [#10](https://github.com/mert494/student-information-system/issues/10), both assigned `mert494` | [PR #1](https://github.com/mert494/student-information-system/pull/1) merged as `1f6c6dd`; [PR #16](https://github.com/mert494/student-information-system/pull/16) merged as `8f37ba56` | Both PRs are merged; Issues remain open pending acceptance and other evidence |
| Sprint planning, Projects and submission tracking; PB-01–PB-07 mapping | [#10](https://github.com/mert494/student-information-system/issues/10), assigned `mert494`; [#15](https://github.com/mert494/student-information-system/issues/15), assigned `nsnkcc` | [Submission checklist](Sprint1_Submission_Checklist.md); board URL/details **Unverified** | Real sprint facts, independent board verification and PO-approved PB mapping remain pending |

[PR #1](https://github.com/mert494/student-information-system/pull/1) merged into `develop` as [1f6c6dd](https://github.com/mert494/student-information-system/commit/1f6c6ddca7bc1ced42db14ea527b8fa845397ac7); Ahmet, Barış and Arda approved its source `79e3d407e304038f1eb159479059e1e79cf5e623`: [Ahmet](https://github.com/mert494/student-information-system/pull/1#pullrequestreview-5757090348), [Barış](https://github.com/mert494/student-information-system/pull/1#pullrequestreview-5757194647), [Arda](https://github.com/mert494/student-information-system/pull/1#pullrequestreview-5757465470). [PR #16](https://github.com/mert494/student-information-system/pull/16) merged into `develop` as [8f37ba56](https://github.com/mert494/student-information-system/commit/8f37ba56d2561e772c721104785bcc6c3de19ef4), its current HEAD; Ahmet and Azra approved source `eece32a2fa412c993900d081f723076994a2f4d4`: [Ahmet](https://github.com/mert494/student-information-system/pull/16#pullrequestreview-5757812255), [Azra](https://github.com/mert494/student-information-system/pull/16#pullrequestreview-5757849836). PR #4 is closed but unmerged. PR #17 is open at head `271e102ddbfe311d2cc5a546e8e189b41465cf1c` with two files changed: `docs/RACI_Matrix.md` and `docs/Sprint1_Process_Records.md`. Mert's `CHANGES_REQUESTED` review is for the previous head `ce9ac8b0`; the current diff needs review. These reviews and PR states do not approve the RACI or the Mert–Azra division. Mert reports the board has been created and populated, but its details are not independently verifiable through the available connector. No remote Project or Issue changes were made by this documentation update.

## Delivery Issue source descriptions — created as #9–#15

The seven descriptions below are retained as the original source drafts for actual Issues #9–#15; do not create duplicates. All seven are open and have actual GitHub assignees: #9/#10 `mert494`, #11 `nsnkcc`, #12 `nsnkcc` plus `ardaberkkara1`, #13 `ardaberkkara1`, #14 `azrayy`, and #15 `nsnkcc`. The assignment field records tracking responsibility only; it does not approve RACI, Product Owner decisions, priorities, estimates or acceptance. Nurefşan's verified account is `nsnkcc`. PB drafts below remain separate and uncreated. Live Issue creation does not certify acceptance.

### Workflow coordination

Actual Issue: [#9](https://github.com/mert494/student-information-system/issues/9) — Open; GitHub assignee `mert494`. The following source description is not a completion record.

- **Title:** [Docs] Coordinate Sprint 1 Git-Flow and integration decisions
- **Description:** Track Mert's workflow decisions, the shared process base, overlapping PR #1/#4 and the review route for the correction branch. Reuse #5 for Barış's infrastructure/configuration scope; #9 records the distinct coordination gap.
- **Sprint 1 requirement:** GitHub Repository and Git-Flow; S1-08, F-03/F-15 support.
- **Acceptance criteria:** Exact base SHA and permanent PR targets have a real team decision; PR #1/#4 scope is reconciled with Azra; proposed rules are distinguished from verified settings; owner actions and independent review links are recorded without premature closure.
- **GitHub assignee:** `mert494` (verified). This records issue tracking responsibility; team, RACI, priority and acceptance decisions remain pending. Barış owns configuration; Arda advises base/technical dependencies; Azra records actual decisions.
- **Priority:** [TODO] — pending team agreement; source finding priorities remain F-03 P1 and F-15 P2.
- **Dependencies:** Existing #5; team base/policy decision; separate authorization for branches, settings, retargeting, closure and merges. Estimate [TODO].
- **Evidence required:** Actual decision/date/approvers, approved target SHA, settings evidence supplied by Barış, and review/integration links.
- **Related PRs:** [#1](https://github.com/mert494/student-information-system/pull/1) merged; [#4](https://github.com/mert494/student-information-system/pull/4) closed unmerged; [#6](https://github.com/mert494/student-information-system/pull/6) open; [#16](https://github.com/mert494/student-information-system/pull/16) merged. Current branch activity also includes this local evidence update; its PR does not yet exist.
- **Verified commit evidence:** [PR #1 merge `1f6c6dd`](https://github.com/mert494/student-information-system/commit/1f6c6ddca7bc1ced42db14ea527b8fa845397ac7) and [PR #16 merge/current develop `8f37ba56`](https://github.com/mert494/student-information-system/commit/8f37ba56d2561e772c721104785bcc6c3de19ef4).

### Sprint tracking and submission coordination

Actual Issue: [#10](https://github.com/mert494/student-information-system/issues/10) — Open; GitHub assignee `mert494`. The following source description is not a completion record.

- **Title:** [Docs] Complete Sprint 1 task tracking and submission evidence
- **Description:** Track actual Sprint 1 goal/capacity, selected task Issues, Projects verification, dependency/owner progress, independent reviews and the six-member contribution/submission chain. Reuse QA #3 and DevOps #5 rather than duplicating them.
- **Sprint 1 requirement:** Six-deliverable tracking and identifiable team/contribution evidence; S1-10/S1-14/S1-16, F-04/F-07.
- **Acceptance criteria:** Actual sprint facts are recorded with sources; selected Issues have confirmed owners/criteria/dependencies; existing board is verified or explicitly Unverified; checklist links real commits/PRs/reviews and pending approvals; no meeting, tag or receipt is fabricated.
- **GitHub assignee:** `mert494` (verified). This records issue tracking responsibility; sprint scope, team decisions and delivery acceptance remain pending. Azra supports actual records; all members provide their own evidence.
- **Priority:** [TODO] — pending team agreement; F-04 P2 and F-07 P3 are source finding priorities, not new Issue approval.
- **Dependencies:** Course deadline/time-zone/team-number/channel confirmation, Azra/team actual facts, PO scope, real owner/review evidence; board/live Issue operations and release/submission require authorization. Estimate [TODO].
- **Evidence required:** Existing process record/checklist links, actual selected Issue URLs, verified board URL/items or explicit limitation, all six contribution chains and eventually authorized final SHA/tag/receipt.
- **Related PRs:** [#1](https://github.com/mert494/student-information-system/pull/1) and [#16](https://github.com/mert494/student-information-system/pull/16) merged; [#2](https://github.com/mert494/student-information-system/pull/2) open/draft; [#4](https://github.com/mert494/student-information-system/pull/4) closed/unmerged; [#6](https://github.com/mert494/student-information-system/pull/6), [#7](https://github.com/mert494/student-information-system/pull/7), [#8](https://github.com/mert494/student-information-system/pull/8) and [#17](https://github.com/mert494/student-information-system/pull/17) open. PR #17 has `CHANGES_REQUESTED`; do not treat it as accepted evidence.
- **Verified commit evidence:** [PR #1 merge `1f6c6dd`](https://github.com/mert494/student-information-system/commit/1f6c6ddca7bc1ced42db14ea527b8fa845397ac7), [PR #16 merge/current develop `8f37ba56`](https://github.com/mert494/student-information-system/commit/8f37ba56d2561e772c721104785bcc6c3de19ef4). Final submission receipt, release/tag and all-member contribution chain remain pending.

### Proposal and license

Actual Issue: [#11](https://github.com/mert494/student-information-system/issues/11) — Open; GitHub assignee `nsnkcc`. The following source description is not a completion record.

- **Title:** [Docs] Review Sprint 1 Project Proposal and license decision
- **Description:** Track Nurefşan's existing proposal, preliminary OBS observations and license rationale without rewriting her content or inventing research.
- **Sprint 1 requirement:** Project Proposal and Problem Definition, including license rationale; S1-01/S1-02.
- **Acceptance criteria:** Required proposal sections are reviewed; assumptions and actual evidence are distinguished; new c7e9d79/1184b26 changes receive QA recheck; a real license decision is recorded or explicitly pending.
- **Proposed assignee:** nsnkcc (Nurefşan), pending her approval; Arda supports license/technical feasibility.
- **Priority:** [TODO] — PO/team decision pending.
- **Dependencies:** Nurefşan scope approval, Arda consultation, Ahmet recheck F-10/F-13. Estimate [TODO].
- **Evidence required:** Proposal source commit, decision record and actual independent review.
- **Related PRs:** #7.

### Vision and Boundary

Actual Issue: [#12](https://github.com/mert494/student-information-system/issues/12) — Open; GitHub assignees `nsnkcc` and `ardaberkkara1`. The following source description is not a completion record.

- **Title:** [Docs] Reconcile the Sprint 1 System Vision and Boundary
- **Description:** Track one combined owner-reviewed document across PR #7/#8. Preserve Vision and technical Boundary contributions and leave unapproved scope/role decisions explicit.
- **Sprint 1 requirement:** System Vision and System Boundary; S1-03/S1-04, F-11/F-14/F-20/F-21.
- **Acceptance criteria:** Nurefşan/Arda agree the authoritative shared version; duplicate PR scope is reconciled; role/context/open decisions are clear; independent review and actual Issue/PR links are supplied.
- **Proposed assignee:** nsnkcc, pending approval; ardaberkkara1 owns technical Boundary contributions; Mert coordinates links only.
- **Priority:** [TODO] — owner/team agreement pending.
- **Dependencies:** Product/technical scope decisions, owner conflict resolution, approved PR targets; no automatic merge. Estimate [TODO].
- **Evidence required:** Combined file commit, actual owner decision and QA recheck; no assumed external-system decision.
- **Related PRs:** #7 and #8.

### OpenAPI draft

Actual Issue: [#13](https://github.com/mert494/student-information-system/issues/13) — Open; GitHub assignee `ardaberkkara1`. The following source description is not a completion record.

- **Title:** [Docs] Review and validate the Sprint 1 OpenAPI draft
- **Description:** Track Arda's existing contract draft and its unresolved policy/data/examples; Mert does not select or implement API behavior.
- **Sprint 1 requirement:** Draft OpenAPI YAML Contract; S1-05, F-18/F-19.
- **Acceptance criteria:** Arda records version/tool choice and scope mapping; owner-approved policy/data corrections are validated; actual command/tool/version/results and limitations distinguish contract validation from live API testing.
- **Proposed assignee:** ardaberkkara1, pending approval; Nurefşan supplies requirements and Ahmet verifies.
- **Priority:** [TODO] — owner/team agreement pending.
- **Dependencies:** Scope/roles/data/security decisions, selected available validator, QA #3; no dependency installation authorized by this draft. Estimate [TODO].
- **Evidence required:** api/openapi.yaml commit, owner decisions and affected validation/review links.
- **Related PRs:** #8.

### Roles and RACI

Actual Issue: [#14](https://github.com/mert494/student-information-system/issues/14) — Open; GitHub assignee `azrayy`. The following source description is not a completion record.

- **Title:** [Docs] Confirm Sprint 1 roles, RACI and Agile process division
- **Description:** Track Azra's existing RACI proposal and actual team approval, including the Mert–Azra division and workload discussion. Do not treat PR #4's RACI checks as a matrix edit.
- **Sprint 1 requirement:** Team Roles and RACI Matrix; S1-06, QA-12/F-09.
- **Acceptance criteria:** Six members and official roles retained; one A and at least one R per task; MD/CSV parity verified; real approvers/date/Decision ID recorded, or approval remains explicitly pending.
- **Proposed assignee:** azrayy, pending approval; Mert coordinates and all members confirm assignments.
- **Priority:** [TODO] — team agreement pending.
- **Dependencies:** Team availability, actual workload/assignment decisions and Azra's record ownership. Estimate [TODO].
- **Evidence required:** RACI MD/CSV checks and real decision link, not fabricated minutes or attendance.
- **Related PRs:** #4, overlapping #1.

### Initial Product Backlog

Actual Issue: [#15](https://github.com/mert494/student-information-system/issues/15) — Open; GitHub assignee `nsnkcc`. The following source description is not a completion record.

- **Title:** [Docs] Review and map the Sprint 1 Initial Product Backlog
- **Description:** Track Nurefşan's draft and its Issue mapping after her approval. Resolve the PR #7 content conflict with its owner; Mert does not replace the PO version or silently repair acceptance criteria.
- **Sprint 1 requirement:** Initial Product Backlog; S1-09, F-04/F-06/F-14/F-16.
- **Acceptance criteria:** PO scope/priority approval is explicit; team estimates and implementers are distinguished from proposals; measurable criteria and missing benefits are addressed by the PO; approved PB items map to actual Issues without an inferred Sprint 1 implementation commitment.
- **Proposed assignee:** nsnkcc, pending approval; Mert maps Issues, Arda advises API and Ahmet checks testability.
- **Priority:** [TODO] — PO/team decision pending.
- **Dependencies:** Role/business-rule decisions, owner conflict resolution and approved Issue creation; source PB-01–PB-07 draft below. Estimate [TODO].
- **Evidence required:** Authoritative backlog commit, actual PO/team approval and Issue/PR/QA links.
- **Related PRs:** #7.

## Prepared Issue #9 and #10 description corrections — not posted

These proposed replacements are compared with the current live Issue bodies. Both Issues remain open and are assigned to `mert494`; neither Issue is being closed or updated by this branch.

### Issue #9 — Git-Flow and integration coordination

**Current text to replace:** “No GitHub assignee is set; proposed ownership below is not a confirmed assignment.” The body also labels `mert494` only as a proposed assignee. Both statements conflict with the verified GitHub assignee field.

**Proposed replacement:**

> **Status:** Sprint 1 tracking task; open. The GitHub assignee field is `mert494`. This records tracking responsibility only; it does not confirm team approval of the workflow, RACI, priority, target-base policy or deliverable acceptance. This Issue does not certify a deliverable as accepted.
>
> **Description:** Track Mert's Git-Flow and PR coordination. `develop` exists at [`8f37ba56`](https://github.com/mert494/student-information-system/commit/8f37ba56d2561e772c721104785bcc6c3de19ef4). PR #1 and PR #16 were merged into `develop` with merge commits [`1f6c6dd`](https://github.com/mert494/student-information-system/commit/1f6c6ddca7bc1ced42db14ea527b8fa845397ac7) and [`8f37ba56`](https://github.com/mert494/student-information-system/commit/8f37ba56d2561e772c721104785bcc6c3de19ef4). PR #4 is closed unmerged. PR #2 is an open draft; PR #6, #7 and #8 are open and currently target `develop`. Current branch targets are observed state and do not by themselves document team approval of a permanent workflow policy.
>
> **Acceptance criteria:** Record the team's actual workflow/base-target decision when made; keep active GitHub protection settings separate from proposed policy; track PR coordination and reviews using real links; keep approvals and outstanding owner decisions pending until evidenced.
>
> **Related evidence:** [PR #1](https://github.com/mert494/student-information-system/pull/1), [#2](https://github.com/mert494/student-information-system/pull/2), [#4](https://github.com/mert494/student-information-system/pull/4), [#6](https://github.com/mert494/student-information-system/pull/6), [#7](https://github.com/mert494/student-information-system/pull/7), [#8](https://github.com/mert494/student-information-system/pull/8), [#16](https://github.com/mert494/student-information-system/pull/16); active rulesets [main-protection](https://github.com/mert494/student-information-system/rules/26478471) and [develop-protection](https://github.com/mert494/student-information-system/rules/26478727). Priority and estimate remain `[TODO]` pending team agreement.

### Issue #10 — task tracking and submission evidence

**Current text to replace:** “No GitHub assignee is set” and the related statement that assignment is unconfirmed. These statements conflict with the verified GitHub assignee field.

**Proposed replacement:**

> **Status:** Sprint 1 tracking task; open. The GitHub assignee field is `mert494`. Assignment identifies tracking responsibility; it is not PO/RACI approval, a sprint commitment or deliverable acceptance.
>
> **Description:** Track Sprint 1 deliverable evidence, verified Issues and PRs, contribution links, Projects verification and final submission prerequisites. Do not record meetings, decisions, reviews, release/tag or submission receipt that have not occurred.
>
> **Verified integration evidence:** PR #1 merged with [`1f6c6dd`](https://github.com/mert494/student-information-system/commit/1f6c6ddca7bc1ced42db14ea527b8fa845397ac7), after APPROVED reviews by Ahmet, Barış and Arda. PR #16 merged with [`8f37ba56`](https://github.com/mert494/student-information-system/commit/8f37ba56d2561e772c721104785bcc6c3de19ef4), after APPROVED reviews by Ahmet and Azra; this is the current `develop` HEAD. PR #4 is closed unmerged. PR #2 is open/draft; #6, #7 and #8 are open. PR #17 is open at `271e102ddbfe311d2cc5a546e8e189b41465cf1c` and changes two files; Mert's `CHANGES_REQUESTED` review is for the previous head `ce9ac8b0`, so the current diff still needs review.
>
> **Remaining evidence:** Verify the Projects board identity, URL, fields, items and statuses; confirm team/RACI decisions and sprint facts; obtain owner reviews and QA rechecks; record all six members' actual contribution chains; confirm release/tag and final submission channel/receipt only when they exist. Course deadline source, time zone, team number and channel remain `[TODO]`/Unverified. Preserve pending decisions.
>
> **Related Issues:** [#3](https://github.com/mert494/student-information-system/issues/3), [#5](https://github.com/mert494/student-information-system/issues/5), [#9](https://github.com/mert494/student-information-system/issues/9)–[#15](https://github.com/mert494/student-information-system/issues/15). The verified assignee fields for #9–#15 are listed in this guide; assignments are not acceptance evidence.

These replacement bodies are prepared for review only and have not been posted. Both Issues remain open.

## Local PB Issue drafts — PO confirmation required

Each separate draft below reproduces the corresponding story, acceptance criteria, proposed priority/points, dependencies and open decisions from Nurefşan's immutable source at 1184b261f4eebca2a741cb55550d3a9b3cd67294. No Product Backlog file is edited. The copied content remains unapproved: in particular F-06/F-16 wording is not silently fixed. Before live creation Nurefşan confirms scope and criteria, the team confirms implementers/estimates, and Mert obtains explicit creation approval. These are tracking drafts for Sprint 1's Initial Product Backlog deliverable, not a commitment to implement features in Sprint 1.

### PB-01 — local Issue draft

- **Title:** [Backlog] PB-01 — User Login
- **Description:** Track and refine the source story below under PO ownership; approval is pending, not inferred.
- **Sprint 1 requirement:** Initial Product Backlog tracking; S1-09/S1-10, F-04.
- **Proposed assignee:** ardaberkkara1 (source proposed owner Arda); assignment approval [TODO].
- **Related PRs:** #7 for requirements and #8 for API consultation; actual Issue URL [TODO].
- **Evidence required:** Nurefşan's source/approval, confirmed criteria, team owner/estimate decisions and actual mapping links; eventual implementation evidence only when separately in scope.
- **Source:** [PO backlog at 1184b26](https://github.com/mert494/student-information-system/blob/1184b261f4eebca2a741cb55550d3a9b3cd67294/docs/Initial_Backlog_Draft.md), section PB-01.

- **Epic:** Identity and Access
- **User Story:** As a user, I want to log in with my account so that I can access the operations I am authorized to perform.

**Acceptance Criteria:**

1. A user must be able to log in with valid credentials.
2. Access must be denied when invalid credentials are provided.
3. An invalid-login message must not reveal whether the account exists in the system.
4. After logging out, a user must be required to authenticate again before performing a protected operation.

- **Priority:** P1 – High (proposed)
- **Story Points:** 5 (proposed)
- **Dependencies:** Approval of authentication requirements and test-account policy.
- **Proposed Owner:** Arda
- **Quality Reviewer:** Ahmet
- **Status:** Pending Product Owner and team approval.

### PB-02 — local Issue draft

- **Title:** [Backlog] PB-02 — Role-Based Authorization
- **Description:** Track and refine the source story below under PO ownership; approval is pending, not inferred.
- **Sprint 1 requirement:** Initial Product Backlog tracking; S1-09/S1-10, F-04.
- **Proposed assignee:** ardaberkkara1 (source proposed owner Arda); assignment approval [TODO].
- **Related PRs:** #7 for requirements and #8 for API consultation; actual Issue URL [TODO].
- **Evidence required:** Nurefşan's source/approval, confirmed criteria, team owner/estimate decisions and actual mapping links; eventual implementation evidence only when separately in scope.
- **Source:** [PO backlog at 1184b26](https://github.com/mert494/student-information-system/blob/1184b261f4eebca2a741cb55550d3a9b3cd67294/docs/Initial_Backlog_Draft.md), section PB-02.

- **Epic:** Identity and Access
- **User Story:** As a system administrator, I want to restrict students', instructors', and administrators' operations according to their roles so that users can access only the functions they are authorized to use.

**Acceptance Criteria:**

1. User permissions must follow the role-and-permission matrix approved by the Product Owner.
2. An unauthorized user must be denied when attempting an operation through a direct API request.
3. A student must not be able to access another student's protected academic information.
4. The system must return an appropriate response indicating that permission is insufficient for an unauthorized operation.

- **Priority:** P1 – High (proposed)
- **Story Points:** 5 (proposed)
- **Dependencies:** PB-01 and approval of the role-and-permission matrix.
- **Proposed Owner:** Arda
- **Quality Reviewer:** Ahmet
- **Status:** Pending approval of the role-and-permission matrix.

### PB-03 — local Issue draft

- **Title:** [Backlog] PB-03 — Student Management
- **Description:** Track and refine the source story below under PO ownership; approval is pending, not inferred.
- **Sprint 1 requirement:** Initial Product Backlog tracking; S1-09/S1-10, F-04.
- **Proposed assignee:** [TODO] — implementation team to determine; no assignment approval.
- **Related PRs:** #7 for requirements and #8 for API consultation; actual Issue URL [TODO].
- **Evidence required:** Nurefşan's source/approval, confirmed criteria, team owner/estimate decisions and actual mapping links; eventual implementation evidence only when separately in scope.
- **Source:** [PO backlog at 1184b26](https://github.com/mert494/student-information-system/blob/1184b261f4eebca2a741cb55550d3a9b3cd67294/docs/Initial_Backlog_Draft.md), section PB-03.

- **Epic:** Student Affairs
- **User Story:** As an authorized administrator, I want to create, list, and update student records so that student information can be managed.

**Acceptance Criteria:**

1. Required fields must be validated when a student record is created.
2. Creating a second record with the same student number must be prevented.
3. Unauthorized users must not be able to modify student records.
4. After a successful update, the updated information must be visible in the student list.
5. A student record request containing missing or invalid information must be rejected.

- **Priority:** P1 – High (proposed)
- **Story Points:** 5 (proposed)
- **Dependencies:** PB-02 and approval of student data fields.
- **Proposed Owner:** To be determined by the implementation team.
- **Acceptance Criteria Advisor:** Nurefşan
- **Status:** Pending approval of data fields and owner assignment.

### PB-04 — local Issue draft

- **Title:** [Backlog] PB-04 — Course Management
- **Description:** Track and refine the source story below under PO ownership; approval is pending, not inferred.
- **Sprint 1 requirement:** Initial Product Backlog tracking; S1-09/S1-10, F-04.
- **Proposed assignee:** [TODO] — implementation team to determine; no assignment approval.
- **Related PRs:** #7 for requirements and #8 for API consultation; actual Issue URL [TODO].
- **Evidence required:** Nurefşan's source/approval, confirmed criteria, team owner/estimate decisions and actual mapping links; eventual implementation evidence only when separately in scope.
- **Source:** [PO backlog at 1184b26](https://github.com/mert494/student-information-system/blob/1184b261f4eebca2a741cb55550d3a9b3cd67294/docs/Initial_Backlog_Draft.md), section PB-04.

- **Epic:** Course Catalog
- **User Story:** As an authorized administrator, I want to create courses and update existing course information so that course records can be maintained.

**Acceptance Criteria:**

1. Required fields must be validated when a course is created.
2. Creating a second course with the same course code within the approved uniqueness scope must be prevented.
3. Unauthorized users must not be able to modify course information.
4. A newly created course must be visible in the course list.
5. A course creation request containing missing or invalid information must be rejected.

- **Priority:** P1 – High (proposed)
- **Story Points:** 5 (proposed)
- **Dependencies:** PB-02 and approval of the course/term data model.
- **Proposed Owner:** To be determined by the implementation team.
- **Quality Reviewer:** Ahmet
- **Status:** Pending clarification of course-code uniqueness scope and owner assignment.

### PB-05 — local Issue draft

- **Title:** [Backlog] PB-05 — Course Enrollment
- **Description:** Track and refine the source story below under PO ownership; approval is pending, not inferred.
- **Sprint 1 requirement:** Initial Product Backlog tracking; S1-09/S1-10, F-04.
- **Proposed assignee:** [TODO] — implementation team to determine; no assignment approval.
- **Related PRs:** #7 for requirements and #8 for API consultation; actual Issue URL [TODO].
- **Evidence required:** Nurefşan's source/approval, confirmed criteria, team owner/estimate decisions and actual mapping links; eventual implementation evidence only when separately in scope.
- **Source:** [PO backlog at 1184b26](https://github.com/mert494/student-information-system/blob/1184b261f4eebca2a741cb55550d3a9b3cd67294/docs/Initial_Backlog_Draft.md), section PB-05.

- **Epic:** Course Enrollment
- **User Story:** As a student, I want to enroll in a course when I meet the enrollment conditions and view my current course enrollments.

**Acceptance Criteria:**

1. A student must be able to enroll in a course when the approved enrollment conditions are met and the enrollment period is open.
2. A second enrollment record for the same student, course, and term must be prevented.
3. A new enrollment request must be rejected when the enrollment period is closed.
4. A student must be able to view only their own course enrollments.
5. When enrollment conditions are not met, the system must reject the enrollment request and return an appropriate error response.

**Open Decisions:**

- Is active student status required for enrollment?
- Must course capacity be checked?
- Do course prerequisites apply?
- Who defines the enrollment dates for each term?

These rules must be finalized by the Product Owner and the team. Unapproved conditions must not be treated as established system requirements.

- **Priority:** P1 – High (proposed)
- **Story Points:** 8 (proposed)
- **Dependencies:** PB-03, PB-04, and approval of enrollment conditions.
- **Business Rules Advisor:** Nurefşan
- **Validation Advisor:** Ahmet
- **Status:** Pending clarification of enrollment conditions and team estimation.

### PB-06 — local Issue draft

- **Title:** [Backlog] PB-06 — Instructor Grade Entry
- **Description:** Track and refine the source story below under PO ownership; approval is pending, not inferred.
- **Sprint 1 requirement:** Initial Product Backlog tracking; S1-09/S1-10, F-04.
- **Proposed assignee:** [TODO] — implementation team to determine; no assignment approval.
- **Related PRs:** #7 for requirements and #8 for API consultation; actual Issue URL [TODO].
- **Evidence required:** Nurefşan's source/approval, confirmed criteria, team owner/estimate decisions and actual mapping links; eventual implementation evidence only when separately in scope.
- **Source:** [PO backlog at 1184b26](https://github.com/mert494/student-information-system/blob/1184b261f4eebca2a741cb55550d3a9b3cd67294/docs/Initial_Backlog_Draft.md), section PB-06.

- **Epic:** Grade Management
- **User Story:** As an instructor, I want to enter grades for students enrolled in a course assigned to me.

**Acceptance Criteria:**

1. Only an instructor assigned to the relevant course must be able to enter grades for that course.
2. Values outside the approved grading range must be rejected.
3. Entering a grade for a student who is not enrolled in the relevant course must be prevented.
4. A successfully saved grade must be retrievable later.
5. An unauthorized user must not be able to perform grade-entry operations.

- **Priority:** P2 – Medium (proposed)
- **Story Points:** 8 (proposed)
- **Dependencies:** PB-02, PB-05, instructor/course assignment, and approval of the grading scale.
- **Proposed Owner:** To be determined by the implementation team.
- **Acceptance Criteria Advisors:** Nurefşan and Ahmet
- **Status:** Pending approval of grading scale and publication rules.

### PB-07 — local Issue draft

- **Title:** [Backlog] PB-07 — Student Grade Viewing
- **Description:** Track and refine the source story below under PO ownership; approval is pending, not inferred.
- **Sprint 1 requirement:** Initial Product Backlog tracking; S1-09/S1-10, F-04.
- **Proposed assignee:** [TODO] — implementation team to determine; no assignment approval.
- **Related PRs:** #7 for requirements and #8 for API consultation; actual Issue URL [TODO].
- **Evidence required:** Nurefşan's source/approval, confirmed criteria, team owner/estimate decisions and actual mapping links; eventual implementation evidence only when separately in scope.
- **Source:** [PO backlog at 1184b26](https://github.com/mert494/student-information-system/blob/1184b261f4eebca2a741cb55550d3a9b3cd67294/docs/Initial_Backlog_Draft.md), section PB-07.

- **Epic:** Grade Management
- **User Story:** As a student, I want to view the grades published for my courses.

**Acceptance Criteria:**

1. A student must be able to view only their own published grades.
2. Grades that have not yet been published must not be displayed to the student.
3. If the student has no published grades, the system must display the message: "No published grades are available."
4. If a student attempts to access another student's grade information through a direct request, access must be denied.
5. When a grade-viewing request is successful, only information the student is authorized to access must be displayed.

- **Priority:** P2 – Medium (proposed)
- **Story Points:** 3 (proposed)
- **Dependencies:** PB-06 and approval of the grade publication rule.
- **Proposed Owner:** To be determined by the implementation team.
- **Validation Advisor:** Ahmet
- **Status:** Pending approval of the empty-state message proposal and publication rule.

## Projects verification before any live operation

- [ ] Obtain the actual board owner/URL and authorized read access; determine whether a board already exists. Feature availability alone is insufficient.
- [ ] Inspect current items, fields, views and automation; retain existing accepted configuration rather than creating duplicates.
- [ ] Map the selected Sprint 1 Issues, assignees, priorities, dependencies and evidence to actual items; confirm scope with the team.
- [ ] Compare live Status/Done against verified criteria/review/merge evidence. An Issue close or a template file is not acceptance.
- [ ] Record the verified result in the existing submission checklist. Until then board URL/items/automation remain Unverified/[TODO].
- [ ] Obtain explicit approval for any creation, assignment, field/item/status or automation change. No such operation has been executed here.

## GitHub interface steps — only after approval

1. Check existing Organization/Projects and repository access; do not unnecessarily duplicate the board. Organization creation or repository transfer requires a separate team/authorization decision.
2. Under the appropriate owner, open a new board through Projects or select an existing board. Link it to the repository.
3. Configure Status with the five options above. Add required fields; group the Board by Status.
4. Barış verifies member access. Reuse existing #3/#5 and #9–#15; obtain separate approval for any new Issue or assignment. Confirm actual assignees, Acceptance Criteria and dependency links.
5. Add Issues to the board. Select S1 tasks as Sprint 1 scope; do not automatically turn PB product examples into implementation commitments.
6. Review Projects Workflows settings. Check default automations that set Done when an Issue closes/a PR merges; do not mistakenly mark unaccepted or canceled work complete. Initially verify transitions manually.
7. Mert updates progress/impediment tracking; Azra updates actual meeting and decision records. At submission, check actual Issue → PR → commit → release/tag links.

## Read-only CLI check examples when available

No installation or login was performed in this task. The following PowerShell commands check current status after the CLI is installed and the account authorized. If the Project owner is an Organization, replace the example personal owner with the verified Organization name.

```powershell
gh --version
gh auth status
gh repo view mert494/student-information-system
gh issue list --repo mert494/student-information-system --state all --limit 100
gh pr list --repo mert494/student-information-system --state all --limit 100
gh project list --owner mert494
```

Once the Project number is known, use `gh project view <NUMBER> --owner <OWNER>` and `gh project item-list <NUMBER> --owner <OWNER>`; do not run them until `<...>` placeholders have been replaced with actual values. Pagination/limits mean the first results must not be assumed to include all records. Do not interpret an access error as “no board exists”. Verify account permissions needed for Project reading against CLI help; expanding permissions and remote changes are outside this preparation's scope.

Do not execute commands here that change Issues, Projects, releases, branch protection or other remote resources. Explicit push approval is required, followed by separate approval to open a PR. The planned correction PR targets develop; its creation still requires separate approval.

## Sources

- [GitHub Projects single-select fields](https://docs.github.com/en/issues/planning-and-tracking-with-projects/understanding-fields/about-single-select-fields)
- [GitHub Projects built-in automations](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/using-the-built-in-automations)
- [GitHub CLI project commands](https://cli.github.com/manual/gh_project)
