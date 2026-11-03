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

The historical preparation branch `docs/sprint1-process` is a naming exception. The current evidence-refresh branch is `docs/mert-sprint1-evidence-update`, created locally from the verified `develop` HEAD below. This observed branch does not approve a general workflow policy.

## Observed Sprint 1 configuration — 4 November 2026

The branch model above remains a proposal; the following records are observed GitHub state. `main` is at [7072b417](https://github.com/mert494/student-information-system/commit/7072b4176d274326bfa320d1f81977fa293a0838), and `develop` is at [8f37ba56](https://github.com/mert494/student-information-system/commit/8f37ba56d2561e772c721104785bcc6c3de19ef4). PR #16's merge commit is the current `develop` HEAD.

[PR #1](https://github.com/mert494/student-information-system/pull/1) merged to `develop` with merge commit [1f6c6dd](https://github.com/mert494/student-information-system/commit/1f6c6ddca7bc1ced42db14ea527b8fa845397ac7). Ahmet, Barış and Arda approved source `79e3d407e304038f1eb159479059e1e79cf5e623`: [Ahmet](https://github.com/mert494/student-information-system/pull/1#pullrequestreview-5757090348), [Barış](https://github.com/mert494/student-information-system/pull/1#pullrequestreview-5757194647), [Arda](https://github.com/mert494/student-information-system/pull/1#pullrequestreview-5757465470). [PR #16](https://github.com/mert494/student-information-system/pull/16) merged with commit [8f37ba5](https://github.com/mert494/student-information-system/commit/8f37ba56d2561e772c721104785bcc6c3de19ef4); Ahmet and Azra approved source `eece32a2fa412c993900d081f723076994a2f4d4`: [Ahmet](https://github.com/mert494/student-information-system/pull/16#pullrequestreview-5757812255), [Azra](https://github.com/mert494/student-information-system/pull/16#pullrequestreview-5757849836). Those reviews do not approve RACI decisions or this current change.

| PR | Current GitHub state | Head → base | Current evidence |
| --- | --- | --- | --- |
| [#2](https://github.com/mert494/student-information-system/pull/2) | Open, draft, mergeable | `8fac0cfa` → `develop` (`8f37ba56`) | QA report; review/QA follow-up pending |
| [#4](https://github.com/mert494/student-information-system/pull/4) | Closed, not merged | `79e3d407` → `main` | Its contribution is present in PR #1's merged history; closure is not RACI approval |
| [#6](https://github.com/mert494/student-information-system/pull/6) | Open, mergeable | `81a66a93` → `develop` (`8f37ba56`) | Repository setup; owner/review work remains |
| [#7](https://github.com/mert494/student-information-system/pull/7) | Open, mergeable | `6d92c07b` → `develop` (`8f37ba56`) | Proposal, backlog and combined Vision/Boundary; owner decisions/review remain |
| [#8](https://github.com/mert494/student-information-system/pull/8) | Open, mergeable | `c5425a4c` → `develop` (`8f37ba56`) | `api/openapi.yaml`; API validation and review remain |
| [#17](https://github.com/mert494/student-information-system/pull/17) | Open; Mert's review is `CHANGES_REQUESTED` on the previous head | `271e102ddbfe311d2cc5a546e8e189b41465cf1c` → `develop` (`8f37ba56`) | Two changed files: `docs/RACI_Matrix.md` and `docs/Sprint1_Process_Records.md`; the review is on `ce9ac8b0` and the new changes need review. RACI/team approvals remain pending |

Delivery Issues #9–#15 are open with actual GitHub assignees: #9/#10 `mert494`; #11 `nsnkcc`; #12 `nsnkcc` and `ardaberkkara1`; #13 `ardaberkkara1`; #14 `azrayy`; #15 `nsnkcc`. These assignee fields are tracking assignments, not PO approval, RACI approval, priority decisions or acceptance. PB-01–PB-07 remain local drafts pending Product Owner/team approval.

GitHub shows active rulesets [main-protection](https://github.com/mert494/student-information-system/rules/26478471) and [develop-protection](https://github.com/mert494/student-information-system/rules/26478727). Both branches report `protected: true`. Main requires 2 approvals; develop requires 1. Both require PRs, dismiss stale approvals, require approval of the latest push and resolution of review conversations, block deletion and force-push/non-fast-forward updates, allow only merge commits, have empty bypass lists, and have no required status checks. Linear history is not enabled. These are active repository settings, distinct from the proposed process guidance above.

Mert reports that a Projects board was created and populated, but the available GitHub connector cannot read Projects. Board URL, owner, fields, items and live statuses therefore remain **Unverified** here. The proposed Mert–Azra division and RACI approval remain pending. No remote state was changed by this documentation update.

## Current Mert evidence update

This local feature branch is `docs/mert-sprint1-evidence-update`, based on the verified `develop` SHA above. Its scope is the three Mert Scrum Master process documents. The branch is not pushed and no PR has been opened. Issue #9/#10 description corrections are prepared in [GitHub_Projects_Setup.md](GitHub_Projects_Setup.md) but have not been posted. This is task status, not a general team decision.

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

General proposal only: use the merge strategy selected by the team for the relevant PR. The previous squash suggestion is not an approved rule and is currently unavailable under the active rulesets, which allow merge commits only. PR #1 and #16 used merge commits and preserved individual history. Do not merge until Acceptance Criteria, review and any required CI checks pass. Obtain explicit user approval for merging. Afterwards, update the Issue/Project status and submission evidence; confirm branch deletion separately.

## Conflict resolution

First ensure a clean working tree; do not automatically move another person's changes with reset/stash. Fetch the current approved target and merge it into the working branch. Review conflicting sections with the file owner; do not blindly apply bulk `ours`/`theirs` selections. Remove conflict markers, repeat relevant checks and notify the reviewer of the resolution. Do not rewrite shared branch history; do not force push.

## Active branch protection configuration

Read-only GitHub verification on 4 November 2026 found the active [main-protection ruleset](https://github.com/mert494/student-information-system/rules/26478471) targeting `main` and [develop-protection ruleset](https://github.com/mert494/student-information-system/rules/26478727) targeting `develop`. Both branches report protected. Main requires 2 approving reviews; develop requires 1. Both rulesets require PRs, dismiss stale approvals after new commits, require approval of the latest push and resolved review conversations, block force pushes/non-fast-forward updates and branch deletion, permit only merge commits, and have empty bypass lists. Linear history and required status checks are not enabled. No CI status check is represented as configured.

These verified settings are separate from the proposed branch and review workflow in this document; their existence does not mean the team approved the full Git-Flow proposal or the RACI assignments.

## Working with Codex

Follow AGENTS.md; a human reviews the output. The assistant works only within the authorized scope. The student remains responsible for validating and submitting generated content. Do not complete Arda's OpenAPI or Nurefşan's requirements documents on their behalf. Do not record meetings, tests or decisions that have not occurred; unknown information is marked `[TODO]`. Record the Issue → branch → commit → PR → release/tag chain using actual links.
