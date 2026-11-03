# Git workflow — draft for team approval

Status: **Proposal; not yet approved by the team.** Approval date and decision record: [TODO].
Related Issues: [#9](https://github.com/mert494/student-information-system/issues/9) and [#10](https://github.com/mert494/student-information-system/issues/10). Proposed coordination: Mert; technical consultation: Arda; repository settings: Barış.

## Repository working rules

Before starting, read README, AGENTS.md, the relevant Issue and documents; check `git status` and the active branch. Prepare small, focused changes. Do not modify another person's files or uncommitted changes without permission. Do not commit real student data, passwords, tokens or `.env`. Each student contributes through their own account and actual identity; shared accounts must not be used to establish contribution ownership.

Proposed division between Mert and Azra: Mert coordinates GitHub Projects, Issues, sprint planning, Git-Flow and submission tracking; Azra coordinates RACI documentation, Meeting Minutes, retrospectives and process reports. This division **awaits approval**; the existing local RACI and process templates do not count as Azra's completed contributions.

## Branch structure

| Branch | Proposed purpose | Starting point / PR target |
| --- | --- | --- |
| `main` | Reviewed submissions and release history | Approved `develop` release / `main` through a PR |
| `develop` | Sprint integration | Team-approved starting commit / integration target |
| `feature/<issue>-<short-name>` | Product feature | `develop` / `develop` |
| `docs/<issue>-<short-name>` | Documentation and process work | `develop` / `develop` |
| `fix/<issue>-<short-name>` | Bug fix | `develop` / `develop` |

The historical preparation branch docs/sprint1-process is a naming exception. The current correction branch is docs/mert-qa-corrections at c2d6d39; develop exists at 1f6c6ddca7bc1ced42db14ea527b8fa845397ac7. The planned correction PR targets develop, not main. This does not approve a general workflow policy.

## Observed Sprint 1 configuration — 3 November 2026

The branch model above remains a proposal. Read-only GitHub queries verified nine branches. Main remains at 7072b41; develop is at 1f6c6ddca7bc1ced42db14ea527b8fa845397ac7. The published correction head is c2d6d39fde35b967182284ea3a3e668b3ddcd3bf.

[PR #1](https://github.com/mert494/student-information-system/pull/1) was merged into develop with merge commit [1f6c6dd](https://github.com/mert494/student-information-system/commit/1f6c6ddca7bc1ced42db14ea527b8fa845397ac7) on 3 November 2026 at 21:29:25 Europe/Istanbul. Ahmet (ahmetserdar41), Barış (baryyss-001) and Arda (ardaberkkara1) each submitted APPROVED reviews of source 79e3d407e304038f1eb159479059e1e79cf5e623: [Ahmet](https://github.com/mert494/student-information-system/pull/1#pullrequestreview-5757090348), [Barış](https://github.com/mert494/student-information-system/pull/1#pullrequestreview-5757194647), [Arda](https://github.com/mert494/student-information-system/pull/1#pullrequestreview-5757465470). No review threads were returned. These approvals cover PR #1, not the separate correction branch or RACI/team decisions.

PR #2/#6/#7/#8 still target docs/sprint1-team-guides; PR #4 remains open against main. Its source is an ancestor of develop and has no file-content difference from it. Do not close #4 without Azra's approval. Nine actual Issues are open: #3 (assigned to ahmetserdar41), #5 (assigned to baryyss-001), and #9–#15 (all unassigned). Delivery Issue creation is complete, not deliverable acceptance. PB-01–PB-07 remain local drafts pending Nurefşan's approval; no PB Issues were created.

All nine branch records report protected=false; rulesets=[]. The earlier detailed protection read returned 403; individual protection settings and plan capability remain Unverified. These proposals are not enforced GitHub rules. Projects and RACI/team approvals remain pending. Barış owns configuration work; this update changes no settings.

## Prepared correction PR — not created

- **Proposed title:** docs: complete Mert Sprint 1 process tracking preparation
- **Source branch:** docs/mert-qa-corrections, published head c2d6d39fde35b967182284ea3a3e668b3ddcd3bf. This local evidence refresh is uncommitted.
- **Planned base:** develop at 1f6c6ddca7bc1ced42db14ea527b8fa845397ac7. Common ancestor is 79e3d407e304038f1eb159479059e1e79cf5e623; the correction branch is three commits ahead and one behind. Develop has the same file tree as the common ancestor, so no content conflict is expected at these SHAs. Local synchronization with a merge commit is deferred because the current instruction also prohibits commits/merges. No rebase, reset or force push is proposed.
- **Related Issues:** [#9](https://github.com/mert494/student-information-system/issues/9) and [#10](https://github.com/mert494/student-information-system/issues/10); QA context [#3](https://github.com/mert494/student-information-system/issues/3), RACI coordination [#14](https://github.com/mert494/student-information-system/issues/14). Use reference links, not automatic Issue-closing language.
- **Proposed reviewer:** ahmetserdar41 for evidence/QA; azrayy for process consistency, pending actual review requests and owner agreement.

Prepared PR body (refresh head SHA and actual validation evidence immediately before authorized creation):

### Summary

Mert's Sprint 1 process documents contained stale publication/Issue status and lacked ready-to-review tracking records for remaining coordination work. The correction distinguishes verified remote state from proposed Git-Flow/Projects settings, preserves real contribution links, prepares missing Issue descriptions and records owner-dependent actions. The refresh records actual earlier GitHub actions without claiming completion of pending configuration, team approvals, meetings, correction reviews or submission.

### Scope and evidence

Changed paths relative to develop at 1f6c6dd are docs/GitHub_Projects_Setup.md, docs/Git_Workflow.md, docs/Sprint1_Submission_Checklist.md, docs/qa/Mert_QA_Corrections.md, docs/team-guides/sprint1/00_Team_Overview.md and docs/team-guides/sprint1/06_Mert_Scrum_Master_Summary.md. No PO backlog, RACI, shared factual process record, QA-owner source, API, source/test or infrastructure file is changed. Earlier published work: [b7e8655](https://github.com/mert494/student-information-system/commit/b7e865574ff87f9ae303d390307fb8317c5569c3) and [226d2e8](https://github.com/mert494/student-information-system/commit/226d2e898b31e65d7503a4520fef9059d425e8cc). Published preparation: [c2d6d39](https://github.com/mert494/student-information-system/commit/c2d6d39fde35b967182284ea3a3e668b3ddcd3bf). Current local refresh commit/PR [TODO].

### Validation and remaining decisions

Use the actual local check results in [Mert_QA_Corrections.md](qa/Mert_QA_Corrections.md); do not mark the independent review complete. Issue/PB drafts preserve Nurefşan's proposed criteria/priorities and require her confirmation. Projects remains Unverified. RACI/sprint facts, PB approval/mapping, independent review of this correction, owner conflicts, settings and release/submission evidence remain pending. Delivery Issues #9–#15 are open, not completed. The course source, exact deadline/time zone/team number/channel are Unverified/[TODO]. No application/API tests are represented as run.

### Integration dependencies

[PR #1](https://github.com/mert494/student-information-system/pull/1) was merged into develop with merge commit [1f6c6dd](https://github.com/mert494/student-information-system/commit/1f6c6ddca7bc1ced42db14ea527b8fa845397ac7) on 3 November 2026 at 21:29:25 Europe/Istanbul. Ahmet (ahmetserdar41), Barış (baryyss-001) and Arda (ardaberkkara1) each submitted APPROVED reviews of source 79e3d407e304038f1eb159479059e1e79cf5e623: [Ahmet](https://github.com/mert494/student-information-system/pull/1#pullrequestreview-5757090348), [Barış](https://github.com/mert494/student-information-system/pull/1#pullrequestreview-5757194647), [Arda](https://github.com/mert494/student-information-system/pull/1#pullrequestreview-5757465470). No review threads were returned. These approvals cover PR #1, not the separate correction branch or RACI/team decisions.

PR #4 remains open against main, with all source contributions preserved in develop. Await Azra's approval before closure. PR #7 remains conflicted, and #7/#8 share competing Vision/Boundary content; their owners must reconcile it. This correction changes neither PR's target or files. PR #1 approvals do not approve this six-file correction.

Use the existing correction worktree, preserve all original commits, and show the refreshed six-file diff before a separately authorized commit/push/PR. No local merge commit, new commit, push or PR has been made in this refresh.

## Commit messages

Proposed format: `type(scope): short description`; types: `feat`, `fix`, `docs`, `test`, `chore`. Example: `docs(sprint1): add process and delivery templates`. Include the actual Issue number in the commit body as `Refs #<issue-number>`; do not carry placeholders into commits. Use atomic commits and the correct author identity. Do not fabricate contributions on behalf of a bot or another student.

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

General proposal only: squash merge task PRs, preserving original commit and review links in the PR. This is not enforced or authorization to rewrite this branch. PR #1 used a merge commit to preserve individual history. For release PRs, prefer a merge commit that preserves `develop` → `main` history. The exact method requires team approval. Do not merge until Acceptance Criteria, review and any required CI checks pass. Obtain explicit user approval for merging. Afterwards, update the Issue/Project status and submission evidence; confirm branch deletion separately.

## Conflict resolution

First ensure a clean working tree; do not automatically move another person's changes with reset/stash. Fetch the current approved target and merge it into the working branch. Review conflicting sections with the file owner; do not blindly apply bulk `ours`/`theirs` selections. Remove conflict markers, repeat relevant checks and notify the reviewer of the resolution. Do not rewrite shared branch history; do not force push.

## Branch protection proposals

After verifying plan and permission availability, Barış presents the following proposal for `main` and `develop`: require PRs, at least one independent approval, dismissal of stale approvals after new commits, resolved conversations, and protection against force pushes and deletion. Select a required status check only by the name of an actual configured CI job. Restrict administrator bypass as far as possible. These settings have not yet been applied.

## Working with Codex

Follow AGENTS.md; a human reviews the output. The assistant works only within the authorized scope. The student remains responsible for validating and submitting generated content. Do not complete Arda's OpenAPI or Nurefşan's requirements documents on their behalf. Do not record meetings, tests or decisions that have not occurred; unknown information is marked `[TODO]`. Record the Issue → branch → commit → PR → release/tag chain using actual links.
