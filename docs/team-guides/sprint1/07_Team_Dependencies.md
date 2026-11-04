# Sprint 1 — team dependencies and working sequence

[Return to the main guide](00_Team_Overview.md). This plan is a proposal consistent with the [RACI](../../RACI_Matrix.md); do not fabricate dates or completed approvals. Exact sprint schedule [TODO]. “Ready” means a reviewable draft of an input; “approved” means a recorded decision.

## Input → output relationships

| Preceding work / input | Subsequent work / owner | Handoff and acceptance criterion | If the input is missing |
| --- | --- | --- | --- |
| Nurefşan's problem, scope, role/business rules and stories | Arda's Boundary/OpenAPI design | Stable story IDs, proposed roles/permissions, data and Acceptance Criteria; approved parts explicit | Arda can prepare the contract structure; uncertain endpoints/rules cannot be treated as approved |
| Arda's base, tools/versions and technical decisions | Barış's technical repository/setup organization | Approved base commit, tool prerequisites and decision record | Access/protection review continues; technology-dependent setup waits |
| Nurefşan's refined Product Backlog | Mert's Projects sprint planning | Epic/feature/story, priorities, team estimates, owners, Acceptance Criteria and dependencies | Board fields can be prepared; stories cannot be treated as commitments or confirmed assignments |
| Mert–Azra division and all six members' responsibility feedback | Azra/Mert's RACI approval | One A and at least one R per row; actual approvers/date/decision record | Existing matrix remains a draft; assignments do not count as contribution evidence |
| Reviewable versions of all team outputs | Ahmet's quality report | File/commit, check criterion, method and actual result | Missing files are Pending; check preparation continues |
| QA findings | Relevant author's fix → Ahmet's recheck | Finding ID, owner, fix PR/commit and new result | Unresolved impediments go to Mert; do not hide them in the report |
| Approved documents, GitHub evidence and QA results | Barış/Mert's Sprint 1 submission package | Actual URLs/SHAs, correct release/tag and contribution mapping for all six members | Do not mark tag/final submission complete |

## Work that can proceed in parallel

- While Nurefşan prepares proposal/vision, Arda can advise on technical feasibility and Boundary; define section owners in the shared file.
- While Barış inspects access and current branches/rules, Mert can prepare board fields/Issue drafts and Azra process records and RACI review.
- Ahmet can establish check criteria before files are complete and review sections as actual content becomes available.
- Arda can prepare the OpenAPI skeleton while Nurefşan refines stories; API behavior is clarified with the relevant requirement decision.
- After review, owners can make their fixes in parallel; use sequential PRs or section sharing for the same shared file.

## Gates requiring precedence

1. **Working base:** Preserve uncommitted work and make relevant process documents accessible; do not start an automatic branch/push flow until `develop` and the PR target are clarified.
2. **Scope agreement:** A reviewable draft of problem, target users and scope is input to OpenAPI behavior design. Draft work may proceed while open questions are recorded.
3. **Planning agreement:** Do not commit product stories to the sprint until PO priority, team estimates, owners and capacity are clear.
4. **Quality and fixes:** Ahmet reviews actual submission versions; repeat affected checks after fixes.
5. **Submission:** Review, approved merge actions, a release/tag pointing to the correct commit and accessible final links receive a final check.

## Shared file ownership and conflict prevention

| Shared area | Coordination |
| --- | --- |
| Vision/Boundary | Nurefşan owns Vision, Arda Boundary; both review shared scope changes |
| RACI Markdown/CSV | Azra coordinates editing, Mert supports tracking; synchronize CSV in the same change |
| Process records | Azra handles Meeting Minutes/decisions/retrospective, Mert supports planning/progress/impediments; proposed section division awaits approval |
| Git_Workflow | Mert owns the document, Barış provides technical-setting input; applied settings require separate evidence |
| Product Backlog | Nurefşan owns content/priorities, the team estimates/selects implementers, Mert maps Issues/board |
| Submission Checklist | Mert integrates; everyone provides their actual evidence |

In conflicts, do not discard another person's changes with reset or bulk “ours/theirs” selection. Agree on resolution with authors, then review the diff and relevant checks again. Do not rewrite history.

## Impediment and submission tracking

If an input is delayed, record impact, owner, expected decision/date and next step in the [Impediment Log](../../Sprint1_Process_Records.md). Mert updates board dependencies; Azra records actual decisions. `S1-*`/`PB-*` identifiers are not actual GitHub Issue numbers. Unknown URLs or dates remain `[TODO]`.

## Boundaries for later sprints

Sprint 2: detailed SRS, quality/non-functional measures, UI/UX prototypes and C4/UML. Sprint 3: working MVP and GitHub Actions CI with at least 50% unit-test coverage. Final: single-command Docker/docker-compose startup, integration/E2E report, static analysis and demo. Do not add these tasks to Sprint 1 completion gates.
