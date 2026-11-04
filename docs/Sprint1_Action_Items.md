# Sprint 1 open items and task list

Status: **Task list based on the QA checks; current as of 2026-11-04 (night: PRs #7, #8, #6, #19 and #17 merged; `develop` @ `eb9d72a`).** Prepared by: Ahmet (QA). Source: [Sprint1_Quality_Report.md](Sprint1_Quality_Report.md); the `F-xx` and `QA-xx` IDs are the findings and checks in that report. Related Issue: [#3](https://github.com/mert494/student-information-system/issues/3).

Submission: **5 November 2026, 23:59**. Proposed milestones: remaining fixes and reviews on **4 November**; merges, `develop` → `main` and the tag by **4 November evening**; 5 November is a buffer day.

The Codex prompts used for coordination on 3–4 November are kept for reference only in [qa/archive/Sprint1_Codex_Prompts_2026-11-03.md](qa/archive/Sprint1_Codex_Prompts_2026-11-03.md). They are historical and are not current instructions; this list is.

Members tick `[ ]` → `[x]` for their own items in their own PR as they finish them. If an item will not be done, do not delete it; add the reason next to it. QA rechecks ticked items and records them in the report.

## Status by Sprint 1 deliverable

| # | Deliverable (Teams) | Owner | Document / PR | Status | Open findings |
| --- | --- | --- | --- | --- | --- |
| 1 | Project Proposal | Nurefşan | `docs/Project_Proposal.md`, PR [#7](https://github.com/mert494/student-information-system/pull/7) | In `develop` (merge `6ad16ce`); no recorded team license decision | F-26 |
| 2 | System Vision and Boundary | Vision: Nurefşan, Boundary: Arda | `docs/System_Vision_and_Boundary.md`, PR #7 and PR [#19](https://github.com/mert494/student-information-system/pull/19) | One combined document in `develop`; the external-systems decision is "proposed" | — |
| 3 | OpenAPI Draft | Arda | `api/openapi.yaml`, PR [#8](https://github.com/mert494/student-information-system/pull/8) | In `develop` (merge `36c7c8f`); Redocly 0 errors | F-19 (minor) |
| 4 | Team Roles and RACI | Azra | `docs/RACI_Matrix.md` / `.csv`, `docs/Sprint1_Process_Records.md`, PR [#17](https://github.com/mert494/student-information-system/pull/17) | In `develop` (merge `eb9d72a`); F-24 fixed; approval evidence team-reported only | QA-28 |
| 5 | GitHub Repository and Git-Flow | Barış, Mert | `docs/Git_Workflow.md`, `docs/Repository_Setup.md` (both in `develop`) | `develop` and the rulesets are active; setup document merged (`1b6825b`); no `develop` → `main` merge and no tag yet | QA-21 |
| 6 | Initial Product Backlog | Nurefşan | `docs/Initial_Backlog_Draft.md`, PR #7 | In `develop`; minor inconsistencies; no PB Issues | F-23, F-04 |
| — | Submission (team details, links, tag) | Mert | `docs/Sprint1_Submission_Checklist.md` (in `develop`) | Current; final links and tag pending | — |

## Shared tasks for everyone

- [x] Target `develop` with your PR (all open PRs target `develop`).
- [ ] Get at least one approval from someone other than the author for your PR; review the PRs assigned to you.
- [ ] Make sure your commits are linked to your team GitHub account: `git config user.email` must be an email registered on that account.
- [ ] Send Mert the real Issue, PR and commit links for your deliverable (for the individual contribution table in the checklist).

## Nurefşan — Product Owner and Requirements Engineer

- [x] **F-10** A preliminary SIS review was added to the Proposal (`c7e9d79`).
- [x] **F-11** The four system roles and the stakeholder → role mapping match in all three documents (`e0226bb`).
- [x] **F-12** University Management → Administrators; dedicated functions are out of scope (`e0226bb`).
- [x] **F-13** MIT rationale added (`1184b26`).
- [x] **F-14** The backlog conflict in PR #7 was resolved (`6d92c07`).
- [x] **F-06** Concrete responses: 403 / 409 with an error code (`69832d5`, `e0226bb`).
- [x] **F-16** All seven stories contain "so that".
- [x] **F-20** Combined Vision/Boundary document (`243195e`).
- [ ] **F-23** (optional; needs a new PR from `develop` because PR #7 is merged) In PB-05, change "University Management is responsible for defining the enrollment dates" to "Administrators"; add a "Proposed Owner" field to PB-05; optionally rename "Administrators" → "Administrator".
- [x] **F-23** "Refs #11, #12, #15" added to the PR #7 description.
- [ ] **F-25** Remove your personal Gmail address from the `nsankcc` account and add it to `nsnkcc` (Settings → Emails), so that your first four commits show on the team account. History is not rewritten.
- [ ] **F-26** With Mert and Azra, get a real team decision on the MIT license and have it recorded as a decision (for example D-03). PR review approvals do not count as that decision.
- [ ] **QA-19** Record the PO approval of the backlog and the team estimates once they happen.
- [ ] Review PR #8 (Arda). Not needed: PR #8 was merged with Ahmet's approval.

## Arda — Lead Software Architect and Technical Lead

- [x] **F-18** `bearerAuth`, root `security`, `servers` and `license` added; `recommended` lint 0 errors (`a34146b`).
- [x] **F-19** Tags, examples and basic schema fields added (`c5425a4`, `a34146b`).
- [x] **F-20** `System_Vision_and_Boundary.md` removed from PR #8 (`c5425a4`).
- [x] **F-22** Commits are linked to the `ardaberkkara1` account.
- [ ] Update the PR #8 description (it still says "Boundary draft" and "validation has not been run"). Optional: the PR is merged.
- [x] **F-21** PR #19 (`0761004`, merge `5589968`): new branch from `develop` after PR #7 was merged; §4.4 states "No external systems are in scope for Sprint 1 (proposed)" and has an actor–SIS interaction table; PR "Related: #12".
- [ ] Optional **F-19**: add `term` / `status` to the `Registration` schema.
- [ ] Review PR #6 (Barış). Not needed: PR #6 was merged with Ahmet's approval.

## Mert — Scrum Master and Agile Process Coach

- [x] **F-03** `develop` created; the `develop-protection` and `main-protection` rulesets are active.
- [x] **F-07** Checklist updated (PRs #16, #18).
- [x] PR #4 closed; all open PRs retargeted to `develop`; Issues #9–#15 opened and assigned.
- [x] Merge the approved PRs: #7 (`6ad16ce`), #8 (`36c7c8f`), #6 (`1b6825b`), #19 (`5589968`).
- [x] Review PR #2 (QA report); review on 2026-11-04 addressed in this revision.
- [x] Approve PR #17 (`85eec71`) and merge it (`eb9d72a`).
- [ ] Re-review PR #2.
- [ ] Remaining merge: #2.
- [ ] Open the `develop` → `main` PR (2 approvals required by `main-protection`) and merge it.
- [ ] Have the team decide how the written review policy relates to the active rules: `Git_Workflow.md` proposes 1 reviewer, `main-protection` enforces 2 approvals (report §3.1).
- [ ] **F-26** Coordinate the team license decision with Nurefşan and Azra.
- [ ] **F-04** Optional: open Issues for PB-01…PB-07 from the drafts.
- [ ] Make the final submission on Teams: team number, project name, members, repository URL, OpenAPI YAML, Issue/PR/commit links and the Sprint 1 tag.

## Azra — Scrum Master and Agile Process Coach

- [x] **F-15** PR #4 closed.
- [x] **QA-09** RACI MD ↔ CSV in English and identical (`72b2f86`).
- [x] **QA-12** D-01 (RACI) and D-02 (Mert–Azra process division), meeting record MM-01 and 6/6 attendance (`3a18842`).
- [x] **F-24** (`85eec71`) `Sprint1_Process_Records.md`: MM-01 time "2026-11-03 20:00–21:00 Europe/Istanbul (17:00–18:00 UTC)"; the Decision Log paragraph about "no rulesets / protected=false / mixed PR targets" corrected to the current state.
- [ ] **QA-28** If evidence exists (screenshot, message link, minutes), add it to the MM-01 "Evidence" field; if you took the notes, fill in the MM-01 "Recorder" field. Do not add evidence that does not exist.
- [ ] **F-26** Record the license decision (for example D-03) once the team has actually decided.
- [x] Ask Mert to re-review PR #17 (approved and merged as `eb9d72a`).

## Barış — DevOps and CI/CD Infrastructure Engineer

- [x] **F-17** Merge `origin/develop` into the branch; link Issue #5 and PR #6 in `Repository_Setup.md`; fill in the access table from `gh api .../collaborators`.
- [x] **F-17** Update the "`develop` does not exist / temporary target `docs/sprint1-team-guides`" part; add the `develop-protection` and `main-protection` ruleset evidence; translate the document into English.
- [x] Add "Closes #5" to the PR #6 description; add Ahmet as reviewer (`d948a11`).
- [ ] **QA-21** After `develop` → `main` is merged, create the `sprint-1` tag and the release; add the link to the checklist.

## Ahmet — Quality Assurance and Test Automation Engineer

- [x] Check matrix for the six deliverable headings (28 checks).
- [x] Validate the OpenAPI with Redocly and map it to the backlog (QA-06…QA-08; `a34146b`).
- [x] PRs #1, #16, #18, #8, #7, #6 and #19 reviewed and approved.
- [x] 2026-11-04 rechecks recorded in the report's "Rechecks" table.
- [x] Mert's review of PR #2 addressed: English documents, QA-02 / QA-12 / QA-28, QA-14 / QA-23, the meaning of a 404 from the classic protection endpoint, archived Codex prompts, and active rules separated from the proposed review policy.
- [ ] Review PR #17. Not needed: the F-24 fix was checked and PR #17 was merged with Mert's approval (`eb9d72a`).
- [x] Final check on `develop` @ `eb9d72a`: one Vision/Boundary document, valid OpenAPI, RACI parity, PR #2 without conflicts.
- [ ] After the `develop` → `main` merge, verify that the `sprint-1` tag is on the right commit.
- [ ] Send Mert my own Issue/PR/commit links.

## Proposed merge order

Mert decides; this is a proposal.

1. Done: PR #7 (`6ad16ce`), PR #8 (`36c7c8f`), PR #6 (`1b6825b`), PR #19 (`5589968`).
2. Done: PR #17 (`eb9d72a`), after Mert's approval of `85eec71`.
3. Done: QA final check against `develop` @ `eb9d72a`. PR #2 is merged last.
4. The `develop` → `main` PR is opened and merged after 2 approvals, and the `sprint-1` tag is placed on the resulting `main` commit.
