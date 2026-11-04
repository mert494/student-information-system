# Sprint 1 quality report

Status: **Revised after Mert's review on 2026-11-04; final check done on `develop` @ `eb9d72a` after the PR #17 merge.** The `develop` → `main` merge and the `sprint-1` tag are still pending. Prepared by: Ahmet (Quality Assurance and Test Automation Engineer). Related Issue: [#3](https://github.com/mert494/student-information-system/issues/3). RACI: S1-13 (A/R), S1-05 / S1-09 (C), S1-14 (R).

This report checks documents, the API contract and repository evidence only. There is no running product, so no unit, integration or E2E tests were run; the 50% unit-test coverage target belongs to Sprint 3 and is not assessed here. Deliverables that do not exist yet are marked `Pending`; no check passes without its file. Documents in unmerged PRs were assessed at the PR's head commit.

## 1. Scope and source versions

| Source | Branch / commit | Note |
| --- | --- | --- |
| Repository | `mert494/student-information-system` | First check: 2026-11-01; rechecks: 2026-11-02 (two rounds), 2026-11-03 (two rounds), 2026-11-04 (five rounds) |
| Integration branch | `develop` @ `eb9d72a` | Merged PRs: [#1](https://github.com/mert494/student-information-system/pull/1) (`1f6c6dd`), [#16](https://github.com/mert494/student-information-system/pull/16) (`8f37ba5`), [#18](https://github.com/mert494/student-information-system/pull/18) (`a2d4579`), [#7](https://github.com/mert494/student-information-system/pull/7) (`6ad16ce`), [#8](https://github.com/mert494/student-information-system/pull/8) (`36c7c8f`), [#6](https://github.com/mert494/student-information-system/pull/6) (`1b6825b`), [#19](https://github.com/mert494/student-information-system/pull/19) (`5589968`), [#17](https://github.com/mert494/student-information-system/pull/17) (`eb9d72a`) |
| Requirements documents | `develop` @ `eb9d72a` | Proposal, combined Vision/Boundary, backlog; merged through PR [#7](https://github.com/mert494/student-information-system/pull/7) (`e0226bb`) and the Boundary context through PR [#19](https://github.com/mert494/student-information-system/pull/19) (`0761004`, Arda) |
| OpenAPI draft | `develop` @ `eb9d72a` | `api/openapi.yaml` only; merged through PR [#8](https://github.com/mert494/student-information-system/pull/8) (`a34146b`); unchanged since |
| RACI and process records | `develop` @ `eb9d72a` | Merged through PR [#17](https://github.com/mert494/student-information-system/pull/17) (head `85eec71`, merge `eb9d72a`, 2026-11-04) after Mert's approval of `85eec71`; the RACI and process files in `develop` are identical to `85eec71` |
| Repository setup document | `develop` @ `eb9d72a` | `docs/Repository_Setup.md`; Issue [#5](https://github.com/mert494/student-information-system/issues/5), merged through PR [#6](https://github.com/mert494/student-information-system/pull/6) (`d948a11`) |
| `main` | `7072b41` | README, LICENSE and .gitignore only |

Result values: `Passed`, `Failed`, `Pending`, `Not applicable (with reason)`.

## 2. Method and tools

| Check type | Method / tool | Status |
| --- | --- | --- |
| Document content | Manual reading against the deliverable headings | Applied (existing files) |
| Scope consistency | Cross-comparison of roles, features and out-of-scope lists in the Proposal, Vision/Boundary and backlog | Applied (`e0226bb`) |
| RACI consistency | Python `csv` comparison of the Markdown table and the CSV (ID, task name, assignments); A and R count per row | Applied (`85eec71`; rechecked on `develop` @ `eb9d72a`: identical) |
| Unmeasurable wording scan | `grep` for "easy, fast, appropriate, proper, user-friendly" and the Turkish equivalents, plus manual reading | Applied (`e0226bb`) |
| GitHub evidence | `gh api` queries for branches, rulesets, tags, releases, Issues, PRs, reviews, collaborators and commit author accounts. Branch protection is read from `repos/{owner}/{repo}/rulesets`, `rulesets/{id}` and `rules/branches/{branch}`, plus the `protected` field of `branches/{branch}`. The classic `branches/{branch}/protection` endpoint returns 404 for rulesets-based protection, so a 404 there is **not** evidence that a branch is unprotected | Applied (2026-11-04) |
| Integration | `git merge-tree` simulation of each open PR against `develop` and against each other | Applied |
| Document links | Relative links checked against files in the branch with `git ls-tree` / `git cat-file`; whitespace and conflict markers with `git diff --check` | Applied |
| OpenAPI validation | Redocly CLI 2.72.1 with two rule sets: `npx redocly lint api/openapi.yaml --extends=spec` (OpenAPI 3.1 specification only) and the default `recommended`; plus a PyYAML inventory of operations, `operationId`s, security, examples, schemas and responses. Node v24.13.1 | Applied (`a34146b`; rechecked on `develop` @ `5589968` and `eb9d72a`). This is contract validation only; there is no live API and none was tested |

## 3. Check matrix

| ID | Deliverable | File @ commit | Expected criterion | Method | Result | Evidence / note | Finding owner |
| --- | --- | --- | --- | --- | --- | --- | --- |
| QA-01 | Project Proposal — sections | `docs/Project_Proposal.md` @ `e0226bb` (in `develop`) | Problem, stakeholder analysis, solution and expected outcomes, feasibility/scope, assumptions/risks, license | Manual | Passed | All required sections are present; a stakeholder → system role mapping table was added | Nurefşan |
| QA-22 | Project Proposal — evidence | same | The problem statement is supported by evidence | Manual | Passed | A preliminary review of the current university SIS interface was added (`c7e9d79`); the document states that no survey or interviews were run and notes the limits of the observation | Nurefşan |
| QA-02 | License choice | `LICENSE` @ `7072b41`, Proposal §10 @ `e0226bb` | License file + project-specific rationale + recorded team decision | Manual | Pending | The MIT file and a project-specific rationale exist (`1184b26`); OpenAPI also declares `license: MIT` (`a34146b`). No team license decision is recorded. The PR #7 approvals (Ahmet, Mert) are document reviews and are **not** counted as a formal team license decision. Finding F-26 | Nurefşan, Mert |
| QA-03 | System Vision | `docs/System_Vision_and_Boundary.md` @ `eb9d72a` | Purpose, target users, system responsibilities and main functions | Manual | Passed | §1–3 present; the four system roles chosen by the PO (§2.1) and the main functions are defined | Nurefşan |
| QA-04 | System Boundary | `docs/System_Vision_and_Boundary.md` @ `eb9d72a` | System context and external interactions, in/out of scope, constraints and assumptions | Manual | Passed | §4.4 states "No external systems are in scope for Sprint 1" (proposed, pending team confirmation) and has an actor–SIS interaction table for the four roles; consistent with the out-of-scope list in §5.2 (PR #19, `0761004`). The role–permission matrix and the approved scope list are explicitly marked "pending" / `[TODO]` (5 `[TODO]`) | Arda |
| QA-05 | Scope consistency | Proposal ↔ Vision/Boundary ↔ backlog @ `eb9d72a` | Roles and features match across documents; backlog work stays inside the boundary | Cross-reading | Passed | All three documents use the same four roles (Student, Instructor, Administrators, Student Affairs Staff); the University Management → Administrators mapping and the out-of-scope status of dedicated management functions are written down. The one remaining sentence is finding F-23 (P3) | Nurefşan |
| QA-06 | OpenAPI — syntax | `api/openapi.yaml` @ `a34146b` (in `develop`) | YAML parses; valid for the chosen OpenAPI version | Redocly `--extends=spec` | Passed | OpenAPI 3.1.0; 0 errors against the specification rules. The file marks the version as "candidate, not team-approved" | Arda |
| QA-07 | OpenAPI — content | same | Paths/HTTP operations, `$ref`s resolve, request/response schemas, unique operationIds, defined path parameters, success + error (400/401/403/404) responses, security definition | Redocly `recommended` + PyYAML inventory | Passed | `recommended`: 0 errors, 1 warning (`no-server-example.com`; `localhost` is a deliberate placeholder). `bearerAuth` + root `security`, `security: []` for `createSession`, `servers` and `license` present. All 12 operations have tags; 11 have fake examples (`deleteCurrentSession` returns 204 without a body). The `Registration` schema has no `term`/`status`. Finding F-19 | Arda |
| QA-08 | OpenAPI ↔ backlog | YAML @ `a34146b` ↔ backlog @ `e0226bb` | Authorization and error scenarios of PB-01…PB-07 appear in the contract | Cross-reading | Passed | Every operation has `x-backlog-reference`. The concrete backlog responses match the contract: unauthorized → 403; duplicate registration / quota / prerequisite / inactive student → 409; invalid grade → 400 | Arda, Nurefşan |
| QA-09 | RACI — MD ↔ CSV | `docs/RACI_Matrix.md`, `.csv` @ `eb9d72a` (`develop`; identical to `85eec71`) | IDs, task names and cells of all 16 rows match | Python comparison | Passed | 16/16 rows identical; the CSV was translated to English (`72b2f86`) and keeps its UTF-8 BOM | Azra |
| QA-10 | RACI — A/R rule | same | Exactly one A and at least one R per row; only R/A/C/I and A/R values | Python count | Passed | All 16 rows follow the rule | Azra |
| QA-11 | RACI — team coverage | same | All six members and their official roles are listed | Manual | Passed | Six members and roles are in the table | Azra |
| QA-12 | RACI — decision record | same + `docs/Sprint1_Process_Records.md` @ `eb9d72a` (`develop`; identical to `85eec71`) | A dated team decision record for the RACI exists | Manual | Passed | Decision records D-01 (RACI) and D-02 (Mert–Azra process division), dated 2026-11-03, linked to meeting MM-01 (WhatsApp, 6/6 attendance). This check covers only that a record exists. The records are marked "team-reported"; their independent verification is QA-28. Merged into `develop` through PR #17 (`eb9d72a`) | Azra, Mert |
| QA-28 | RACI — independent approval evidence | `docs/Sprint1_Process_Records.md` @ `eb9d72a` + GitHub | The team approval in D-01 / D-02 can be verified independently of the team-reported record (meeting evidence link, minutes, or each member's confirmation) | Manual + `gh api` | Pending | No evidence link (screenshot, message link or minutes) is attached to MM-01, D-01 or D-02; the MM-01 "Recorder" field is `[TODO]`. Mert's approval of PR #17 (`85eec71`, 2026-11-04) approves the documentation changes only; it is not an independent verification of the D-01 / D-02 decisions or of the meeting | Azra, Mert |
| QA-27 | Process record accuracy | `docs/Sprint1_Process_Records.md` @ `eb9d72a` (`develop`; identical to `85eec71`) | Records do not contradict the actual, current state | `gh api` + manual | Passed | MM-01 time is "20:00–21:00 Europe/Istanbul (17:00–18:00 UTC)"; the Decision Log paragraph correctly lists the two active rulesets, the `develop` target and the merged PRs (#1, #6, #7, #8, #16, #18, #19); verified with `gh api` | Azra |
| QA-13 | Git-Flow rules (written) | `docs/Git_Workflow.md` @ `eb9d72a` (unchanged since `a2d4579`) | `main` / `develop` / `feature` branch model, commit format, PR, review, merge and protection rules | Manual | Passed | All sections present; the document is marked "Proposal; not yet approved by the team" and keeps observed settings apart from the proposed policy (see §3.1) | Mert |
| QA-14 | Git-Flow — in practice | GitHub (live) | `develop` exists; `main` and `develop` are protected; PRs target `develop` | `gh api` | Passed | `develop` exists at `eb9d72a`. `branches/{main,develop}` report `protected: true`; `rules/branches/{branch}` returns the `deletion`, `non_fast_forward` and `pull_request` rules of `main-protection` (26478471) and `develop-protection` (26478727), both `active` (details in §3.1). The classic `branches/{branch}/protection` endpoint returns 404 because protection comes from rulesets. The only open PR, #2, targets `develop`; PRs #1, #6, #7, #8, #16, #17, #18 and #19 are merged into `develop`; PR #4 (→ `main`) was closed without merging | Mert, Barış |
| QA-15 | GitHub access | GitHub (live) | All six members can write | `gh api` | Passed | `nsnkcc`, `ardaberkkara1`, `ahmetserdar41`, `baryyss-001`, `azrayy`: write; `mert494`: admin (2026-11-04) | Barış |
| QA-16 | Issues / Projects | GitHub (live) | Real Issues for deliverables and backlog items | `gh issue list` | Failed | Delivery Issues #9–#15 are open and assigned; #3 and #5 exist. PB-01…PB-07 have no Issues (drafts only in `GitHub_Projects_Setup.md`). Finding F-04 | Mert |
| QA-17 | Backlog — field completeness | `docs/Initial_Backlog_Draft.md` @ `eb9d72a` | Each item has epic, story, acceptance criteria, priority, points, dependencies and owner | Manual | Failed | All seven items have epic, story, priority, points, dependencies and status; PB-05 has no "Proposed Owner" field. Finding F-23 | Nurefşan |
| QA-18 | Backlog — testability | same | Acceptance criteria are measurable and include positive and negative conditions | grep + manual | Passed | The "appropriate response" wording is gone; 403 / 409 with an error code and message are defined. All seven stories contain "so that" | Nurefşan |
| QA-19 | Backlog — approval | same | PO approval, team estimates, real assignments | Manual | Pending | PO approval, team estimates and assignments are "Pending"; the API and Issue mapping is filled in | Nurefşan |
| QA-20 | Submission checklist | `docs/Sprint1_Submission_Checklist.md` @ `eb9d72a` (unchanged since `a2d4579`) | Current status, aligned with the six deliverable headings | Manual | Passed | The six deliverable headings are mapped; real PR/review/commit links are present; outstanding evidence is marked "pending" | Mert |
| QA-21 | Release / tag | GitHub (live) | A Sprint 1 tag on a reviewed commit | `gh api` | Pending | No tag or release; expected after the `develop` → `main` merge | Barış |
| QA-23 | Integration of the requirements documents | `develop` @ `eb9d72a` | Documents reach the approved target through a PR linked to Issues; no second copy of a file appears | `git merge-tree` + `gh` | Passed | PR #7 was merged into `develop` as `6ad16ce` with approvals from Ahmet and Mert; the backlog conflict had been resolved in `6d92c07`. The PR description references #11, #12 and #15. The Boundary follow-up arrived through PR #19 (`5589968`, Related #12) | Nurefşan, Mert |
| QA-25 | Single Vision/Boundary document | `develop` @ `eb9d72a` | One combined version of the deliverable exists | `git ls-tree` | Passed | `develop` contains exactly one `docs/System_Vision_and_Boundary.md`; PR #8 contained only `api/openapi.yaml` (`c5425a4`) | Arda, Nurefşan |
| QA-26 | Commit identity | All Sprint 1 PR commits | Commits are linked to the author's team GitHub account | `gh api` | Failed | Arda's commits are linked to `ardaberkkara1`. Nurefşan's commits `26fc3f4`, `243195e`, `c7e9d79` and `1184b26` are linked to `nsankcc`; the team account is `nsnkcc` (the later `69832d5`, `6d92c07` and `e0226bb` are correct). Finding F-25 | Nurefşan |
| QA-24 | Repository setup document | `docs/Repository_Setup.md` @ `d948a11` (in `develop`) | Access matrix, clone/branch steps, validation steps, open items and evidence table; valid and current | Manual + `gh api` + `git merge-tree` + `git diff --check` | Passed | The document is in English; the access table matches the `collaborators` output and the ruleset table matches `rulesets/26478727` and `26478471`; the `develop` target is correct; the tag is written as "planned"; links resolve and there are no conflicts. F-17 closed | Barış |

Summary: 28 checks: 21 `Passed`, 3 `Failed`, 4 `Pending`.

### 3.1 Active protection rules and the proposed review policy

These are two different things and must not be mixed. The active rules are enforced by GitHub today. The review policy in `Git_Workflow.md` is still a proposal awaiting team approval.

**Active protection rules** (GitHub rulesets, read with `gh api` on 2026-11-04):

| Ruleset | Branch | PR required | Required approvals | Other enforced rules | Enforcement |
| --- | --- | --- | --- | --- | --- |
| [develop-protection](https://github.com/mert494/student-information-system/rules/26478727) (26478727) | `develop` | Yes | 1 | Stale approvals dismissed on push; approval of the last push required; review threads must be resolved; merge commits only; deletion and non-fast-forward (force push) blocked | `active` |
| [main-protection](https://github.com/mert494/student-information-system/rules/26478471) (26478471) | `main` | Yes | 2 | Same as `develop-protection` | `active` |

**Proposed review policy** (`docs/Git_Workflow.md` @ `eb9d72a`, status "Proposal; not yet approved by the team"):

| Topic | Proposal |
| --- | --- |
| Reviewers | At least one reviewer other than the author; Arda for architecture/API, Ahmet for quality/tests, Nurefşan for requirements, Mert/Azra for process documents |
| Author rule | Authors do not approve and merge their own PRs alone |
| Merge | Use the merge strategy chosen by the team; only merge commits are currently possible under the rulesets |
| Approval | Explicit user approval before merging |

Gap: the proposal names one reviewer for every PR, but `main-protection` enforces two approvals. The team should align the two (see §6).

## 4. Findings

| ID | Priority | Finding | Proposed fix | Owner | Status |
| --- | --- | --- | --- | --- | --- |
| F-01 | P1 | The System Boundary and `api/openapi.yaml` did not exist. | — | Arda | Closed (`e522c95`, PR #8) |
| F-02 | — | The first report stated that members had no write access. This was a **wrong finding** caused by checking with the wrong GitHub account; all six members have access. | — | Ahmet | Closed (withdrawn) |
| F-03 | P1 | There was no `develop` branch and no branch protection; the written Git-Flow rules were not applied. | — | Mert, Barış | Closed (`develop` created, PR #1 `1f6c6dd`; `develop-protection` and `main-protection` rulesets active) |
| F-04 | P2 | There were no Issues for the deliverables and PB-01…PB-07. | Open Issues for PB-01…PB-07 from the drafts in `GitHub_Projects_Setup.md` | Mert | Partial (delivery Issues #9–#15 open and assigned; no PB Issues) |
| F-05 | P2 | PB-07: "understandable empty state" was not measurable. | — | Nurefşan | Closed (`26fc3f4`) |
| F-06 | P2 | PB-02 and PB-05: "appropriate response" was not measurable. | — | Nurefşan, Arda | Closed (`69832d5`, `e0226bb`: 403 / 409 with error code and message; consistent with OpenAPI) |
| F-07 | P3 | The checklist said "five official deliverables"; the "not committed" row was out of date. | — | Mert | Closed (PR #16 `8f37ba5`, PR #18 `a2d4579`) |
| F-08 | P3 | All proposed backlog owners were Arda. | — | Nurefşan, Mert | Closed (`26fc3f4`) |
| F-09 | P3 | In the RACI, Mert is A in 5 rows and R in 11; other members have 1–4 A. Not an error; workload information. | — | Azra | Closed (information; the RACI was recorded as approved as-is in D-01, team-reported) |
| F-10 | P2 | The Proposal had no evidence for the problem statement. | — | Nurefşan | Closed (`c7e9d79`: preliminary SIS review; the absence of a survey and the limits are stated) |
| F-11 | P2 | Role names differed between documents. | — | Nurefşan, Arda | Closed (`e0226bb`: the four system roles and the stakeholder → role mapping match in all three documents) |
| F-12 | P3 | The University Management need had no backlog counterpart. | — | Nurefşan | Closed (`e0226bb`: mapped to the Administrators role; dedicated management functions are out of Sprint 1 scope) |
| F-13 | P3 | The license rationale was generic. | — | Nurefşan, Arda | Closed (`1184b26`) |
| F-14 | P2 | The requirements PR had no Issue and conflicted with the target in the backlog file. | — | Nurefşan, Mert | Closed (`6d92c07` conflict resolution; the backlog references #11, #12, #15) |
| F-15 | P2 | PR #4 targeted `main`, bypassing `develop`. | — | Azra, Mert | Closed (PR #4 closed; its content reached `develop` through PR #1) |
| F-16 | P3 | PB-05, PB-06 and PB-07 had no "so that". | — | Nurefşan | Closed (`69832d5`) |
| F-17 | P3 | `Repository_Setup.md` was out of date: Issue/PR, access and ruleset fields were `[TODO]`, and it said "`develop` does not exist" and "temporary target `docs/sprint1-team-guides`". | — | Barış | Closed (`d948a11`, PR #6) |
| F-18 | P2 | OpenAPI had no security scheme, `security`, `servers` or `license`. | — | Arda | Closed (`a34146b`; `recommended` lint 0 errors) |
| F-19 | P3 | OpenAPI lacked examples, tags and schema fields. | `term`/`status` could be added to the `Registration` schema (subject to the PB-05 decision) | Arda, Nurefşan | Partial (`c5425a4`, `a34146b`: all tags, 11 examples, basic fields) |
| F-20 | P1 | `docs/System_Vision_and_Boundary.md` existed in different versions in two PRs. | — | Arda, Nurefşan | Closed (`c5425a4`: removed from PR #8) |
| F-21 | P2 | External systems/interfaces and role permissions in the Boundary were undefined (`[TODO]`). | — | Arda | Closed (`0761004`, PR #19, merge `5589968`) |
| F-22 | P2 | Commit `e522c95` was linked to the non-team account `ardaberk00`. | — | Arda | Closed (email moved to `ardaberkkara1`; history not rewritten) |
| F-23 | P3 | Minor backlog inconsistencies: PB-05 says "University Management is responsible for defining the enrollment dates" (University Management now maps to Administrators and its dedicated functions are out of scope); PB-05 has no "Proposed Owner" field; the role name "Administrators" is plural while the others are singular. | Replace the sentence with "Administrators"; add an owner field to PB-05; optionally make the role name singular. The file is in `develop`, so this needs a new PR | Nurefşan | Open (the PR #7 description part is fixed: it references #11, #12, #15) |
| F-24 | P2 | `Sprint1_Process_Records.md` @ `98e323b` gave the MM-01 time in UTC (20:00–21:00 Europe/Istanbul according to the team), and the Decision Log said there were no rulesets, branches were unprotected and PR targets were mixed. | — | Azra | Closed (`85eec71`, PR #17, merge `eb9d72a`) |
| F-25 | P2 | Nurefşan's commits `26fc3f4`, `243195e`, `c7e9d79` and `1184b26` were made with a personal Gmail address and are linked to the non-team account `nsankcc`; the team account is `nsnkcc`. These contributions do not show on the team account. | Without rewriting history: remove the Gmail address from `nsankcc` and add it to `nsnkcc` (Settings → Emails). Later commits are already correct | Nurefşan | Open |
| F-26 | P3 | No team decision for the MIT license is recorded. The PR #7 approvals review the documents; they are not a team license decision. | When the team confirms the license, record it as a decision (for example D-03 in `Sprint1_Process_Records.md`) with date and participants; do not record it before the team has decided | Nurefşan, Mert, Azra | Open |

No separate Issues were opened for the findings; opening them is coordinated with Mert and requires approval. The draft Issue template is `.github/ISSUE_TEMPLATE/documentation.md`.

## 5. Rechecks

| Finding | Fix PR / commit | Recheck date | Result |
| --- | --- | --- | --- |
| F-01 | `26fc3f4` (Proposal, Vision) | 2026-11-02 | Partial: Boundary and OpenAPI awaited |
| F-02 | — (wrong finding) | 2026-11-02 | Withdrawn; QA-15 `Passed` |
| F-05 | `26fc3f4` | 2026-11-02 | Closed |
| F-06 | `26fc3f4` | 2026-11-02 | Partial; "appropriate response" wording remained |
| F-08 | `26fc3f4` | 2026-11-02 | Closed |
| F-04, F-07, F-09 | — | 2026-11-02 | No change (F-04: Issue #5 added, still no delivery Issues) |
| F-14 | PR #7 | 2026-11-02 | Partial; PR opened, but it targeted `main` and had no Issue link |
| F-03 | `81a66a9` (proposal document) | 2026-11-02 | Open; settings not applied, the permission lies with Mert |
| F-01 | `e522c95` (PR #8) | 2026-11-03 | Closed; new findings F-18…F-22 |
| F-03, F-04, F-07 | — | 2026-11-03 | No change |
| F-11, F-20, F-21 | `243195e` | 2026-11-03 | Partial; combined Vision/Boundary, proposed role list, aligned out-of-scope list. PR #8 still contained the old file |
| F-14, F-15 | PR #7 retargeted | 2026-11-03 | Partial; PR #7 retargeted to `docs/sprint1-team-guides` but conflicted in the backlog file. PR #4 still targeted `main` |
| F-18, F-19, F-22 | — | 2026-11-03 | No change (`e522c95` still on `ardaberk00`) |
| F-03 | PR #1 (`1f6c6dd`), rulesets | 2026-11-04 | Closed; `develop` protected (1 approval), `main` protected (2 approvals) |
| F-04 | Issues #9–#15 | 2026-11-04 | Partial; delivery Issues exist, PB Issues do not |
| F-07 | PR #16 (`8f37ba5`), PR #18 (`a2d4579`) | 2026-11-04 | Closed |
| F-06, F-11, F-12, F-14, F-16 | `69832d5`, `6d92c07`, `e0226bb` (PR #7) | 2026-11-04 | Closed; new minor finding F-23 |
| F-10, F-13 | `c7e9d79`, `1184b26` (PR #7) | 2026-11-04 | Closed |
| F-15 | PR #4 closed | 2026-11-04 | Closed |
| F-18, F-20 | `c5425a4`, `a34146b` (PR #8) | 2026-11-04 | Closed; Redocly `recommended` 0 errors, 1 warning |
| F-19 | `c5425a4`, `a34146b` (PR #8) | 2026-11-04 | Partial |
| F-22 | Account email setting | 2026-11-04 | Closed; `e522c95`, `c5425a4`, `a34146b` → `ardaberkkara1` |
| F-09, QA-12 | `3a18842`, `98e323b` (PR #17) | 2026-11-04 | D-01 / D-02 recorded; new finding F-24 |
| F-21 | — | 2026-11-04 | No change; waiting for the PR #7 merge |
| F-17 | `99d197a`, `d948a11` (PR #6) | 2026-11-04 (night) | Closed; QA-24 `Passed` |
| F-21 | `0761004` (PR #19) | 2026-11-04 (evening) | Closed; QA-04 `Passed`. PRs #7, #8, #6 and #19 are in `develop`; there is one `System_Vision_and_Boundary.md`; `api/openapi.yaml` revalidated with Redocly (0 errors, 1 warning) |
| F-24 | `85eec71` (PR #17) | 2026-11-04 (evening) | Closed; QA-27 `Passed` |
| F-04, F-23, F-25 | — | 2026-11-04 (evening) | No change (F-25: the four commits are still on `nsankcc`) |
| QA-02, QA-12, QA-14, QA-23 | Mert's review of PR #2 | 2026-11-04 (evening) | QA-02 reassessed as `Pending` (PR reviews are not a team license decision; new finding F-26). QA-12 split: the decision record stays `Passed`, independent approval evidence moved to new check QA-28 (`Pending`). QA-14 and QA-23 updated to `develop` @ `5589968`; the meaning of a 404 from the classic protection endpoint is corrected in §2 and QA-14 |
| F-24, QA-09…QA-12, QA-27, QA-28 | PR #17 merged (`eb9d72a`) | 2026-11-04 (night) | Final check on `develop` @ `eb9d72a`: RACI MD ↔ CSV 16/16 identical, one A and at least one R per row; process records identical to `85eec71`; one `System_Vision_and_Boundary.md`; Redocly `--extends=spec` 0 errors and `recommended` 0 errors, 1 warning; PR #2 has no conflicts with `develop`. QA-28 stays `Pending`: the PR #17 approval covers the documentation changes only |

## 6. Open risks and pending decisions

- **Release:** PR #17 is merged (`eb9d72a`); PR #2 is the last open PR. After it is merged, the `develop` → `main` PR needs 2 approvals under `main-protection`.
- **Barış (QA-21):** the `sprint-1` tag is expected after the `develop` → `main` merge.
- **Remaining minor findings (F-23, F-25, F-26):** they do not block submission. F-23 needs a new PR because the file is in `develop`; F-25 is only an account email setting; F-26 needs a real team decision first.
- **Review policy vs. active rules:** `main-protection` enforces 2 approvals while the proposed policy in `Git_Workflow.md` names 1 reviewer. The team should decide which one the written policy follows (§3.1).
- **PB Issues (F-04):** opening Issues for PB-01…PB-07 would strengthen backlog traceability in the submission.
- **Approval records (QA-28):** D-01 / D-02 and MM-01 are "team-reported" with no evidence link (screenshot, message link or minutes).
- OpenAPI 3.1.0 is marked "candidate, not team-approved" in the file and the security policy is "proposed". If the team decides differently, QA-06…QA-08 are repeated.
- The submission date, team number and the Teams "Sprint 1 Examples" format are not reflected in this report [TODO].
- This report was prepared by one person; Mert reviewed the previous version on 2026-11-04 and will review this revision.
