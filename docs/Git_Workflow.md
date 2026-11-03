# Git workflow — draft for team approval

Status: **Proposal; not yet approved by the team.** Approval date and decision record: [TODO].
Related Issue: [TODO]. Proposed coordination: Mert; technical consultation: Arda; repository settings: Barış.

## Repository working rules

Before starting, read README, AGENTS.md, the relevant Issue and documents; check `git status` and the active branch. Prepare small, focused changes. Do not modify another person's files or uncommitted changes without permission. Do not commit real student data, passwords, tokens or `.env`. Each student contributes through their own account and actual identity; shared accounts must not be used to establish contribution ownership.

Proposed division between Mert and Azra: Mert coordinates GitHub Projects, Issues, sprint planning, Git-Flow and submission tracking; Azra coordinates RACI documentation, Meeting Minutes, retrospectives and process reports. This division **awaits approval**; the existing local RACI and process templates do not count as Azra's completed contributions.

## Branch structure

| Branch | Proposed purpose | Starting point / PR target |
| --- | --- | --- |
| `main` | Reviewed submissions and release history | Approved `develop` release / `main` through a PR |
| `develop` | Sprint integration | Team-approved starting commit / integration target |
| `feature/<issue>-<kisa-ad>` | Product feature | `develop` / `develop` |
| `docs/<issue>-<kisa-ad>` | Documentation and process work | `develop` / `develop` |
| `fix/<issue>-<kisa-ad>` | Bug fix | `develop` / `develop` |

The current preparation branch, `docs/sprint1-process`, is an exception to this naming pattern; its Issue link will be added later. At inspection, `develop` was absent from local/remote branch records. Do not open a PR until its target is clarified with the user; do not automatically select `main`. This work does not create `develop`.

## Observed Sprint 1 configuration — 3 November 2026

The branch model above remains a proposal. Read-only GitHub and Git checks verified:

- Eight remote branches exist; develop is absent. The default main branch remains at 7072b41 with only the initial README, LICENSE and .gitignore. Role-owned drafts and Mert's corrections exist on separate task branches; none of the six PRs is merged.
- All eight branch records report protected=false, and the repository ruleset list is empty. The detailed main protection query returned 403 (Resource not accessible by integration); individual settings and plan capability remain **Unverified**. The proposed approval/merge gates must not be described as enforced.
- PR #1 targets docs/sprint1-process; PR #2/#6/#7/#8 target docs/sprint1-team-guides; PR #4 targets main. These are observed targets, not an approved integration policy. All six have zero submitted reviews. PR #1 and #4 share head 79e3d40; their integration sequence requires Mert/Azra and team confirmation.
- Verified account permissions are Mert admin and the five teammates write. Barış retains infrastructure ownership and technical recommendations under the proposed RACI; Mert coordinates any separately authorized admin action. No settings were changed.
- Process 78febb9, guides 2987dc0 and QA/process corrections b7e8655 and 226d2e8 are published. Publication is not team approval, merge or submission. Existing naming exceptions do not authorize shared-branch renaming or history rewriting.

The exact develop base SHA, permanent PR targets, RACI/workflow approval and integration order remain [TODO]. Record actual decisions with Azra and the relevant owners. Branch creation, settings, PR retargeting/closure and merge require applicable separate authorization. Local documentation changes do not complete these live actions.

## Prepared correction PR — not created

- **Proposed title:** docs: complete Mert Sprint 1 process tracking preparation
- **Source branch:** docs/mert-qa-corrections, published head 226d2e8; current local follow-up must receive separate commit/push approval before inclusion.
- **Candidate base:** docs/sprint1-team-guides at 79e3d40. This preserves the latest shared process work and yields only Mert's six documentation files below. It is a review candidate, not an approved permanent integration target. Base confirmation [TODO]; develop does not exist. Do not default to main.
- **Related Issue:** [TODO]; QA context #3. Missing local Issue descriptions are in GitHub_Projects_Setup.md and have not been created.
- **Proposed reviewer:** ahmetserdar41 for evidence/QA; azrayy for process consistency, pending actual review requests and owner agreement.

Prepared PR body (refresh head SHA and actual validation evidence immediately before authorized creation):

### Summary

Mert's Sprint 1 process documents contained stale publication/Issue status and lacked ready-to-review tracking records for remaining coordination work. The correction distinguishes verified remote state from proposed Git-Flow/Projects settings, preserves real contribution links, prepares missing Issue descriptions and records owner-dependent actions. New local preparation does not claim live configuration, approvals, meetings, reviews or submission.

### Scope and evidence

Changed paths relative to candidate base 79e3d40 are docs/GitHub_Projects_Setup.md, docs/Git_Workflow.md, docs/Sprint1_Submission_Checklist.md, docs/qa/Mert_QA_Corrections.md, docs/team-guides/sprint1/00_Team_Overview.md and docs/team-guides/sprint1/06_Mert_Scrum_Master_Summary.md. No PO backlog, RACI, shared factual process record, QA-owner source, API, source/test or infrastructure file is changed. Earlier published work: [b7e8655](https://github.com/mert494/student-information-system/commit/b7e865574ff87f9ae303d390307fb8317c5569c3) and [226d2e8](https://github.com/mert494/student-information-system/commit/226d2e898b31e65d7503a4520fef9059d425e8cc). Current follow-up commit/PR [TODO].

### Validation and remaining decisions

Use the actual local check results in [Mert_QA_Corrections.md](qa/Mert_QA_Corrections.md); do not mark the independent review complete. Issue/PB drafts preserve Nurefşan's proposed criteria/priorities and require her confirmation. Projects remains Unverified. Approved base/targets, RACI/sprint facts, missing live Issues, independent review, owner conflicts, settings and release/submission evidence remain pending. The course source, exact deadline/time zone/team number/channel are Unverified/[TODO]. No application/API tests are represented as run.

### Integration dependencies

PR #1 is docs/sprint1-team-guides to docs/sprint1-process; its current delta contains Mert's nine guides plus Azra's process-record change. PR #4 has the same head 79e3d40 but targets main. Neither is exclusively Mert's current correction and neither is automatically safe to merge or close. Agree the overlap and target with Azra/team first. PR #7 has a live conflict, and #7/#8 still compete on Vision/Boundary; their owners must reconcile content. Individually mergeable #8 is not proof of cross-PR compatibility. PR #2/#6 already request Mert's review but have no submitted reviews.

A safe candidate for this documentation correction is review against the confirmed shared guide base, followed by a separately approved team integration path. No merge order or merge method is approved here. Ahmet's new prompt suggests merge commits while the existing workflow proposes squash for task PRs; the team must record the actual method before integration. Do not execute the prompt's install/login, branch, settings, retargeting, closure, review or merge steps as authorization.

## Commit messages

Proposed format: `type(scope): short description`; types: `feat`, `fix`, `docs`, `test`, `chore`. Example: `docs(sprint1): add process and delivery templates`. Include the actual Issue number in the commit body as `Refs #<numara>`; do not carry placeholders into commits. Use atomic commits and the correct author identity. Do not fabricate contributions on behalf of a bot or another student.

## Pull Request procedure

1. Clarify the Issue scope, Acceptance Criteria and responsible person.
2. Check the working tree; use an appropriate branch after user approval.
3. Stage only relevant files using explicit paths; inspect the staged diff and checks.
4. For this task, show the changes to the user again and obtain approval before committing.
5. Push the branch only after separate explicit push approval; then request approval to open a PR.
6. Open the PR against the approved target; complete the PR template and add the Issue, test/review evidence and documentation. Use a Draft PR for unfinished work.

For PRs targeting a branch other than the default branch, do not assume that the Issue will close automatically. Add the `Related Issue` link; verify closure according to the target branch and GitHub behavior.

## Code review rules

At least one reviewer other than the author is proposed. Consult Arda on architecture/API, Ahmet on quality/tests, Nurefşan on requirements alignment, and Mert/Azra on process documentation. Reviewers check correctness, scope, Acceptance Criteria, security and evidence. Authors do not approve and merge their own PRs alone. Resolve blocking comments; review substantive new changes again.

## Merge procedure

Proposal: squash merge task PRs, preserving original commit and review links in the PR. For release PRs, prefer a merge commit that preserves `develop` → `main` history. The exact method requires team approval. Do not merge until Acceptance Criteria, review and any required CI checks pass. Obtain explicit user approval for merging. Afterwards, update the Issue/Project status and submission evidence; confirm branch deletion separately.

## Conflict resolution

First ensure a clean working tree; do not automatically move another person's changes with reset/stash. Fetch the current approved target and merge it into the working branch. Review conflicting sections with the file owner; do not blindly apply bulk `ours`/`theirs` selections. Remove conflict markers, repeat relevant checks and notify the reviewer of the resolution. Do not rewrite shared branch history; do not force push.

## Branch protection proposals

After verifying plan and permission availability, Barış presents the following proposal for `main` and `develop`: require PRs, at least one independent approval, dismissal of stale approvals after new commits, resolved conversations, and protection against force pushes and deletion. Select a required status check only by the name of an actual configured CI job. Restrict administrator bypass as far as possible. These settings have not yet been applied.

## Working with Codex

Follow AGENTS.md; a human reviews the output. The assistant works only within the authorized scope. The student remains responsible for validating and submitting generated content. Do not complete Arda's OpenAPI or Nurefşan's requirements documents on their behalf. Do not record meetings, tests or decisions that have not occurred; unknown information is marked `[TODO]`. Record the Issue → branch → commit → PR → release/tag chain using actual links.
