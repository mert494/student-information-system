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
- Process 78febb9, guides 2987dc0 and QA corrections b7e8655 are published. Publication is not team approval, merge or submission. Existing naming exceptions do not authorize shared-branch renaming or history rewriting.

The exact develop base SHA, permanent PR targets, RACI/workflow approval and integration order remain [TODO]. Record actual decisions with Azra and the relevant owners. Branch creation, settings, PR retargeting/closure and merge require applicable separate authorization. Local documentation changes do not complete these live actions.

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
