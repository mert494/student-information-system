# Sprint 1 submission checklist

Related tracking: [#9](https://github.com/mert494/student-information-system/issues/9), [#10](https://github.com/mert494/student-information-system/issues/10). Evidence snapshot: 4 November 2026. This checklist distinguishes documentation integration from deliverable acceptance and team decisions.

## Verified repository snapshot

- Verified integration baseline: [develop 6e5df4de1a0bc7ec2eda1dc6254868558716f773](https://github.com/mert494/student-information-system/commit/6e5df4de1a0bc7ec2eda1dc6254868558716f773). This is the baseline before this checklist update, not a promise that the branch HEAD will remain unchanged.
- Main: [7072b4176d274326bfa320d1f81977fa293a0838](https://github.com/mert494/student-information-system/commit/7072b4176d274326bfa320d1f81977fa293a0838). The develop-to-main submission integration is Pending.
- PRs #1, #16, #18, #7, #8, #6, #19, #17 and #2 are merged into develop with individual history preserved. PR #4 is closed without merging; its contribution was integrated through PR #1.
- No open PRs were returned at the snapshot, before this checklist PR is created.
- Issues #3, #5 and #9–#15 are open. Assignees are tracking assignments, not Product Owner, RACI, priority or delivery approval.
- Release list: empty. Tag status: **Unverified**; the available connector does not support the tags-list endpoint. Do not infer that no tag exists from that limitation.
- Projects board: Mert reports it was created and populated. Board URL, owner, fields, items, statuses and automation remain **Unverified** through the available connector.

## Six deliverable headings

The existing [deliverables guide](team-guides/sprint1/08_Sprint1_Final_Deliverables.md) maps five specification items into six submission headings. Course-source confirmation of the final format remains Pending.

| Heading / owner | Current files | Verified integration / QA | Remaining acceptance or decision |
| --- | --- | --- | --- |
| Project Proposal and Problem Definition / Nurefşan | [Proposal](Project_Proposal.md), [MIT LICENSE](../LICENSE) | PR #7 merged; preliminary OBS observations and limitations, and license rationale rechecked by Ahmet | Formal team license decision Pending (QA-02 / F-26); observations do not establish surveys or user dissatisfaction |
| System Vision and Boundary / Nurefşan and Arda | [Combined document](System_Vision_and_Boundary.md) | PR #7 and #19 merged; one shared document; F-20 and documentation QA correction F-21 closed | External-systems exclusion is proposed, awaiting team confirmation; role–permission matrix, scope and final Boundary approval Pending |
| OpenAPI Draft / Arda | [OpenAPI YAML](../api/openapi.yaml) | PR #8 merged; QA records Redocly CLI 2.72.1 spec 0 errors and recommended 0 errors, 1 warning; no live API tested | F-19 Partial; version/security/data policies remain proposed where marked |
| Team Roles and RACI / Azra | [Markdown](RACI_Matrix.md), [CSV](RACI_Matrix.csv), [process records](Sprint1_Process_Records.md) | PR #17 merged; 16/16 task rows match; exactly one A and at least one R per row; timezone and repository statements corrected | D-01/D-02 and MM-01 are team-reported; independent verification Pending (QA-28); recorder unknown |
| GitHub Repository and Git-Flow / Barış and Mert | [Setup](Repository_Setup.md), [workflow](Git_Workflow.md), [tracking guide](GitHub_Projects_Setup.md) | PR #6 and process PRs merged; actual main/develop rulesets active | Full Git-Flow policy approval and exact board evidence Pending / Unverified; personal repository is observed ownership, not proof of an Organization decision |
| Initial Product Backlog / Nurefşan | [Backlog](Initial_Backlog_Draft.md) | PR #7 merged; measurable response criteria and story benefits rechecked | QA-19 Pending: PO scope/priority approval, team estimates and implementation assignments; approved PB-to-Issue mapping Pending; F-23 Open |

All file links above resolve at the integration baseline. Existing files and successful PR reviews do not establish final acceptance. No application, deployment, unit, integration or E2E test completion is claimed.

## Merge and independent review evidence

Review links apply to the reviewed source commits, not automatically to unrelated decisions.

| PR | Merge commit | APPROVED review evidence |
| --- | --- | --- |
| [#1](https://github.com/mert494/student-information-system/pull/1) | [1f6c6ddca7bc1ced42db14ea527b8fa845397ac7](https://github.com/mert494/student-information-system/commit/1f6c6ddca7bc1ced42db14ea527b8fa845397ac7) | [ahmetserdar41](https://github.com/mert494/student-information-system/pull/1#pullrequestreview-5757090348), [baryyss-001](https://github.com/mert494/student-information-system/pull/1#pullrequestreview-5757194647), [ardaberkkara1](https://github.com/mert494/student-information-system/pull/1#pullrequestreview-5757465470) |
| [#16](https://github.com/mert494/student-information-system/pull/16) | [8f37ba56d2561e772c721104785bcc6c3de19ef4](https://github.com/mert494/student-information-system/commit/8f37ba56d2561e772c721104785bcc6c3de19ef4) | [ahmetserdar41](https://github.com/mert494/student-information-system/pull/16#pullrequestreview-5757812255), [azrayy](https://github.com/mert494/student-information-system/pull/16#pullrequestreview-5757849836) |
| [#18](https://github.com/mert494/student-information-system/pull/18) | [a2d4579221d092f5219ff3d5080da9ab8b8e7bb4](https://github.com/mert494/student-information-system/commit/a2d4579221d092f5219ff3d5080da9ab8b8e7bb4) | [azrayy](https://github.com/mert494/student-information-system/pull/18#pullrequestreview-5759853914), [ahmetserdar41](https://github.com/mert494/student-information-system/pull/18#pullrequestreview-5760012650) |
| [#7](https://github.com/mert494/student-information-system/pull/7) | [6ad16ce152a65f90a0f89d8841bef04cc38a3545](https://github.com/mert494/student-information-system/commit/6ad16ce152a65f90a0f89d8841bef04cc38a3545) | [ahmetserdar41](https://github.com/mert494/student-information-system/pull/7#pullrequestreview-5760061814), [mert494](https://github.com/mert494/student-information-system/pull/7#pullrequestreview-5760327611) |
| [#8](https://github.com/mert494/student-information-system/pull/8) | [36c7c8f771213959ff2f38002fee69d0adec419c](https://github.com/mert494/student-information-system/commit/36c7c8f771213959ff2f38002fee69d0adec419c) | [ahmetserdar41](https://github.com/mert494/student-information-system/pull/8#pullrequestreview-5760013037) |
| [#6](https://github.com/mert494/student-information-system/pull/6) | [1b6825bf4b4ed57a2617bb033b808bfe243c9f50](https://github.com/mert494/student-information-system/commit/1b6825bf4b4ed57a2617bb033b808bfe243c9f50) | [ardaberkkara1](https://github.com/mert494/student-information-system/pull/6#pullrequestreview-5769007552), [ahmetserdar41](https://github.com/mert494/student-information-system/pull/6#pullrequestreview-5769041263) |
| [#19](https://github.com/mert494/student-information-system/pull/19) | [5589968f26922385e802ecb326724c84f44b2ae5](https://github.com/mert494/student-information-system/commit/5589968f26922385e802ecb326724c84f44b2ae5) | [ahmetserdar41](https://github.com/mert494/student-information-system/pull/19#pullrequestreview-5770281506) |
| [#17](https://github.com/mert494/student-information-system/pull/17) | [eb9d72a8e6eff141d4e64cbcded737aada290fc3](https://github.com/mert494/student-information-system/commit/eb9d72a8e6eff141d4e64cbcded737aada290fc3) | [mert494](https://github.com/mert494/student-information-system/pull/17#pullrequestreview-5774346598) |
| [#2](https://github.com/mert494/student-information-system/pull/2) | [6e5df4de1a0bc7ec2eda1dc6254868558716f773](https://github.com/mert494/student-information-system/commit/6e5df4de1a0bc7ec2eda1dc6254868558716f773) | [mert494](https://github.com/mert494/student-information-system/pull/2#pullrequestreview-5774525036) |

The approvals of PR #17 and PR #2 cover documentation integration only. They do not independently verify D-01/D-02 or certify all Sprint 1 acceptance criteria.

## QA snapshot and unresolved findings

Authoritative source: [Sprint 1 quality report](Sprint1_Quality_Report.md), integrated through PR #2. Preserve its recorded results: **28 checks: 21 Passed, 3 Failed, 4 Pending**. This checklist does not reclassify the checks.

| Check | Recorded result | Unresolved evidence / owner |
| --- | --- | --- |
| QA-16 | Failed | PB-01–PB-07 have no actual Issues; F-04 Partial. Mert coordinates after PO approval and separate Issue-creation authorization |
| QA-17 | Failed | PB-05 owner field and backlog inconsistencies; F-23 Open. Nurefşan |
| QA-26 | Failed | Four earlier Nurefşan commits associated with nsankcc rather than nsnkcc in the QA snapshot; F-25 Open. Nurefşan verifies account association without rewriting history |
| QA-02 | Pending | Formal MIT team decision absent; F-26 Open. Nurefşan / team; Azra records real decision |
| QA-19 | Pending | PO backlog approval, team estimates and real implementation assignments. Nurefşan / team |
| QA-21 | Pending | Reviewed release/tag and target SHA. Barış / Mert |
| QA-28 | Pending | Independent D-01/D-02 evidence absent. Azra / team; PR review approval is not decision confirmation |

**Open:** F-23, F-25, F-26. **Partial:** F-04, F-19. F-19 concerns proposed Registration term/status fields and remains subject to PB-05 owner decisions. F-21's documentation QA closure does not approve the external-systems scope or permissions. See the [action list](Sprint1_Action_Items.md) for owner follow-up; archived prompts are [historical only](qa/archive/Sprint1_Codex_Prompts_2026-11-03.md).

## Individual contribution evidence

The table links actual reviewed source commits and merged PRs. Review submissions are in the evidence table above. GitHub account association and contribution completeness remain subject to F-25; no new work is attributed to another person's identity.

| Member | Observed account | Actual documented contribution | PR evidence | Reviewed source commit |
| --- | --- | --- | --- | --- |
| Arda | ardaberkkara1 | Boundary and OpenAPI | [#8](https://github.com/mert494/student-information-system/pull/8), [#19](https://github.com/mert494/student-information-system/pull/19) | [a34146be58049c46dc444ba33820286336d05a3f](https://github.com/mert494/student-information-system/commit/a34146be58049c46dc444ba33820286336d05a3f) |
| Barış | baryyss-001 | Repository setup and access evidence | [#6](https://github.com/mert494/student-information-system/pull/6) | [d948a11c36f421cf97f74f96a6a19634e7ce8ea3](https://github.com/mert494/student-information-system/commit/d948a11c36f421cf97f74f96a6a19634e7ce8ea3) |
| Ahmet | ahmetserdar41 | QA report, action list and archived prompts | [#2](https://github.com/mert494/student-information-system/pull/2) | [f3c1f0260c0012ccce2a5027e7aaf0c4930afdc5](https://github.com/mert494/student-information-system/commit/f3c1f0260c0012ccce2a5027e7aaf0c4930afdc5) |
| Mert | mert494 | Process documentation, tracking and evidence; initial work in PR #1 | [#18](https://github.com/mert494/student-information-system/pull/18), [#16](https://github.com/mert494/student-information-system/pull/16) | [1732cab50496c639c7b250100d45f1ae87381a37](https://github.com/mert494/student-information-system/commit/1732cab50496c639c7b250100d45f1ae87381a37) |
| Azra | azrayy | RACI MD/CSV and process records; initial contribution preserved through PR #1 | [#17](https://github.com/mert494/student-information-system/pull/17) | [85eec71e477b6f7522b09c914226b20f10978da2](https://github.com/mert494/student-information-system/commit/85eec71e477b6f7522b09c914226b20f10978da2) |
| Nurefşan | nsnkcc | Proposal, Vision and backlog | [#7](https://github.com/mert494/student-information-system/pull/7) | [e0226bb8da2cab5010a6e31879d9d9c9b1e58278](https://github.com/mert494/student-information-system/commit/e0226bb8da2cab5010a6e31879d9d9c9b1e58278) |

Mert's initial process work and Azra's initial contribution remain preserved in PR #1's merged source 79e3d407e304038f1eb159479059e1e79cf5e623 and its parent history. This table records selected evidence, not an exhaustive commit inventory or approval of role assignments.

## Issue and Projects tracking

| Issue | Actual GitHub assignee(s) | Acceptance status |
| --- | --- | --- |
| [#3](https://github.com/mert494/student-information-system/issues/3) | ahmetserdar41 | Open; QA documentation integrated, remaining acceptance and findings retained |
| [#5](https://github.com/mert494/student-information-system/issues/5) | baryyss-001 | Open; repository document integrated and reviewed; closure requires separate acceptance check |
| [#9](https://github.com/mert494/student-information-system/issues/9), [#10](https://github.com/mert494/student-information-system/issues/10) | mert494 | Open; workflow/tracking and final evidence follow-up |
| [#11](https://github.com/mert494/student-information-system/issues/11) | nsnkcc | Open; proposal integrated; formal license decision Pending |
| [#12](https://github.com/mert494/student-information-system/issues/12) | nsnkcc, ardaberkkara1 | Open; PR #7/#19 and QA evidence recorded; owner/team Boundary decisions Pending |
| [#13](https://github.com/mert494/student-information-system/issues/13) | ardaberkkara1 | Open; API draft integrated; owner policy decisions remain as marked |
| [#14](https://github.com/mert494/student-information-system/issues/14) | azrayy | Open; PR #17 integrated; independent decision evidence Pending |
| [#15](https://github.com/mert494/student-information-system/issues/15) | nsnkcc | Open; PO approval, estimates, owners and PB mapping Pending |

No Issue closure is implied. Do not duplicate Issues or create PB Issues before PO scope approval and separate authorization. Existing Issue prose may lag actual assignee fields; use verified tracking fields without treating them as RACI approval.

## Protection and release readiness

Active [main-protection](https://github.com/mert494/student-information-system/rules/26478471) requires 2 approving reviews; active [develop-protection](https://github.com/mert494/student-information-system/rules/26478727) requires 1. Both require PRs, dismiss stale approvals, require latest-push approval and conversation resolution, permit merge commits only, block deletion and force pushes, and have empty bypass lists. No required status checks or linear-history requirement are configured. These settings do not approve the proposed Git-Flow policy.

- [ ] Review and integrate this checklist update through develop with independent review.
- [ ] Obtain actual owner/team decisions or explicitly agree how unresolved items are disclosed in the submission; preserve the QA results until the responsible reviewer rechecks them.
- [ ] Recheck the full develop-to-main diff, current source SHA, conversations and protection conditions; obtain two valid independent approvals and separate merge authorization.
- [ ] Verify the resulting reviewed main SHA before a separately authorized tag/release. Proposed tag name in the QA task list: sprint-1; actual tag/name/URL remains Unverified.
- [ ] Record release/tag links and actual Issue/Project acceptance status after those actions occur.

## Course submission and decision evidence

| Field | Verified status / required evidence |
| --- | --- |
| Course deadline | **Unverified**. QA action list reports 5 November 2026, 23:59; official course source and timezone confirmation Pending |
| Week/grade statement | Existing guide says end of Week 2 and 15%; official assessment confirmation Unverified |
| Team number | [TODO] / Unverified |
| Submission channel and file format | [TODO] / Unverified; Teams is mentioned in guides, but exact course instructions must be checked |
| Projects board URL and live state | Unverified; do not invent board fields or completion |
| MIT decision | Pending; existing license and rationale do not establish team decision |
| PO backlog scope/priorities, estimates and implementers | Pending |
| RACI D-01/D-02 independent confirmation | Pending; records remain team-reported |
| Final Boundary, roles/permissions and scope approval | Pending |
| Git-Flow policy approval | Pending; active settings are separately verified |
| Sprint Goal, capacity, planning/review/retrospective evidence | Pending where existing records are [TODO]; record only events and decisions that actually occurred |
| Final document/package URLs | Files above exist on develop; final main/tag package Pending |
| Submission receipt | Pending; no final course submission is claimed |

- [ ] Mert verifies the official course instructions, team number, exact deadline/timezone and required attachments.
- [ ] Each member supplies actual contribution and acceptance evidence; Azra records genuine decisions, with unknowns left Pending.
- [ ] Mert checks the final repository/OpenAPI/board/tag links, submits through the designated channel only after authorization, and records the actual receipt.
