# BM321 Sprint 1 — team execution guide

Shareable summary: Team, please use your individual guide below and its Codex prompt for Sprint 1. Nurefşan will coordinate proposal/vision/Product Backlog, Arda System Boundary/OpenAPI, Barış GitHub infrastructure, Ahmet quality checks, Azra process records/RACI, and Mert board/Issue/submission tracking. This division is a proposal awaiting team approval. Start with local work and review; obtain separate approval for commit, push and PR. Do not record meetings or approvals that have not occurred.

## Purpose and source limitations

Sprint 1 goal: Submit an initial package by the end of Week 2 with clear scope, a validated API draft, identified owners and traceable individual contributions. Weight: 15%; exact date/time and team number [TODO].

These guides are execution packages for the people preparing the deliverables, not the deliverables themselves. The inspected repository contains neither the course specification nor a Teams instruction file. Sources are the existing process documents, the BM321 specification shared in this conversation and the Teams screenshot/text. The full detailed instructions and examples in Teams Files have not been verified; the team must check the final format/submission method. No PDF or Word requirement has been assumed.

The last of the specification's five main items includes GitHub and the Product Backlog together; Teams separates them into the six headings below. This is not a difference in scope.

## Roles and individual guides

| Person | Official role | Guide / proposed focus |
| --- | --- | --- |
| Arda | Lead Software Architect and Technical Lead | [Arda](01_Arda_Architecture_Lead.md): System Boundary, OpenAPI, technical review |
| Barış | DevOps and CI/CD Infrastructure Engineer | [Barış](02_Baris_DevOps.md): access, branches/protection and setup |
| Ahmet | Quality Assurance and Test Automation Engineer | [Ahmet](03_Ahmet_QA.md): deliverable and contract validation |
| Azra | Scrum Master and Agile Process Coach | [Azra](04_Azra_Agile_Process.md): RACI, Meeting Minutes, decision/impediment records |
| Nurefşan | Product Owner and Requirements Engineer | [Nurefşan](05_Nurefsan_Requirements.md): proposal, vision, scope and Product Backlog |
| Mert | Scrum Master and Agile Process Coach | [Mert](06_Mert_Scrum_Master_Summary.md): Projects, Issues, planning and submission tracking |

The Mert–Azra division and all assignments are proposals consistent with the [existing RACI](../../RACI_Matrix.md); they are not yet team decisions. In this six-person team, implementation tasks will later be assigned per story; no separate Implementation Engineer role reserved for a seventh member is added.

## Six required deliverable headings and owners

Paths are proposed shared destinations when no existing file is available; if an equivalent deliverable is found elsewhere, use it rather than creating a second version.

| Deliverable | Primary owner / Accountable (A) | Working location |
| --- | --- | --- |
| Project Proposal and Problem Definition, license rationale | Nurefşan; Arda as license consultant/contributor | New proposal: `docs/Project_Proposal.md`; preserve existing `LICENSE` |
| System Vision and Boundary | Vision: Nurefşan; Boundary: Arda | New shared proposal: `docs/System_Vision_and_Boundary.md`; separate section owners |
| OpenAPI Draft | Arda; Nurefşan as scope consultant | New proposal: `api/openapi.yaml` |
| Team Roles and RACI | Azra; Mert as contributor | Existing `docs/RACI_Matrix.md` and `.csv` |
| GitHub Repository and Git-Flow | Access/infrastructure: Barış; rules/tracking: Mert | Existing `docs/Git_Workflow.md`, `docs/GitHub_Projects_Setup.md` and actual GitHub evidence |
| Initial Product Backlog | Nurefşan; Mert as tracking support | Existing `docs/Initial_Backlog_Draft.md`; update approval status in its content |

## Current status and reuse

Mert's 12-file process preparation was pushed to `docs/sprint1-process` in commit `78febb9`. This does not mean team approval, PR merge or Sprint 1 submission. The working tree was clean when this guide was prepared; no proposal, vision or OpenAPI file was found. Records exist for `main` and `docs/sprint1-process`; `develop` is not visible. Remote Issues/Projects and protection settings were not verified in this task.

The [submission checklist](../../Sprint1_Submission_Checklist.md) contains the previous preparation's status; for example, “This preparation has not been committed” is now outdated. Mert should update it with the actual commit link. Do not automatically treat all previous records as current. The [process records](../../Sprint1_Process_Records.md) are a fillable template, not evidence of meetings held.

## Proposed working sequence

1. Everyone verifies their account/access; the team clarifies the Mert–Azra division, RACI and sprint goal. Mert prepares actual Issue links; unknown information remains `[TODO]`.
2. Nurefşan prepares the problem, stakeholders and scope; Arda jointly reviews technical feasibility and boundaries.
3. Barış reviews access/workflow while Azra prepares process records in parallel. Ahmet prepares check criteria in advance.
4. Nurefşan refines the Product Backlog; Arda develops an OpenAPI draft from clarified stories. Uncertain parts remain explicitly proposed.
5. Mert transfers the approved Product Backlog to the board; Ahmet validates actual files. Findings return to their owners, and fixes are checked again.
6. Complete the submission package with approved PRs, contribution evidence and a release/tag pointing to the correct commit.

[Dependencies and parallel work](07_Team_Dependencies.md) provide details of this sequence.

## Shared GitHub workflow

Follow [AGENTS.md](../../../AGENTS.md), [Git rules](../../Git_Workflow.md), [Issue templates](../../../.github/ISSUE_TEMPLATE/documentation.md) and the [PR template](../../../.github/pull_request_template.md). This task creates local guides only; previous push permission does not authorize committing/pushing/opening a PR for these guides.

1. Check `git status --short`, `git branch -a`, `git remote -v` and relevant documents. Stop if someone else's uncommitted work exists; do not reset or automatically stash it.
2. With user approval, run `git fetch origin` and update the approved base. If `develop` does not exist, obtain a base/target decision from Mert/Barış and the user; do not automatically select `main`. If Mert's process documents are not yet integrated into the base, resolve that dependency first.
3. With user approval, create your task branch. Names in the guides are examples; add the actual Issue ID when available.
4. Work locally and run checks. Show the diff and obtain **separate commit approval**; stage only task files using explicit paths. Each student uses their own identity.
5. Obtain **separate push approval**, then **separate PR approval** after pushing. Include the Issue, scope, check results, gaps and reviewer in the PR. Do not describe failed/unrun checks as passed.
6. After independent review and resolution of blocking comments, **merging requires separate explicit approval**. Do not commit directly to `main`/`develop`, force push or close existing PRs.

## Final submission check

- [ ] Compare content under all six headings against the [final deliverables guide](08_Sprint1_Final_Deliverables.md).
- [ ] License rationale, scope, RACI and Product Backlog approvals recorded.
- [ ] Actual OpenAPI YAML file present; validation results and limitations documented.
- [ ] Accounts, actual Issue/PR/review/commit evidence and team information available for all six members.
- [ ] Sprint 1 release/tag points to the correct reviewed commit; final links accessible.
- [ ] Teams Files details, exact deadline and submission channel verified.

## Pending team decisions

Team number and schedule; Mert–Azra division; RACI; `develop` base and PR targets; Git-Flow/merge/protection policy; Organization/access; product scope and role permissions; OpenAPI version and validator; technology stack; story estimates and implementers; release/tag name and submission format [TODO].
