# Sprint 2 integration and release evidence (S2-14)

Status: **Draft baseline, 18 November 2026. Preparation only; final acceptance Pending.** Prepared by Barış (`baryyss-001`). Issue: [#39](https://github.com/mert494/student-information-system/issues/39) (S2-14). Branch: `docs/39-baris-sprint2-release-evidence`. PR: [TODO]. Owner, priority and window remain Proposed as in the [task register](Sprint2_Task_Breakdown.md#s2-14); Mert coordinates. Final acceptance depends on S2-12 ([#37](https://github.com/mert494/student-information-system/issues/37)) and S2-13 ([#38](https://github.com/mert494/student-information-system/issues/38)), both open on 18 November 2026.

This document records the repository state as read, and the checks to repeat before integration and release. It does not perform or authorize any merge, tag, release, upload or Issue closure. Each of those needs separate user authorization ([AGENTS.md](../../AGENTS.md)).

## 1. Baseline read on 18 November 2026

All values were read with `git` and `gh` from Barış's account (`write` access, no Settings access). Commands are listed so that anyone can repeat them.

| Item | Value | Source command |
| --- | --- | --- |
| Repository | [mert494/student-information-system](https://github.com/mert494/student-information-system); public; default branch `main` | `gh repo view mert494/student-information-system --json defaultBranchRef,visibility` |
| `origin/main` | `c6af2af` — Merge PR [#23](https://github.com/mert494/student-information-system/pull/23) (2026-11-04 23:41 +0300) | `git rev-parse origin/main` |
| `origin/develop` | `2945b81` — Merge PR [#25](https://github.com/mert494/student-information-system/pull/25) | `git rev-parse origin/develop` |
| `main` vs `develop` | `main` has 2 commits not in `develop` (the merge commits of [#21](https://github.com/mert494/student-information-system/pull/21) and [#23](https://github.com/mert494/student-information-system/pull/23)); `develop` has 4 commits not in `main` (Sprint 2 planning [#24](https://github.com/mert494/student-information-system/pull/24) and traceability [#25](https://github.com/mert494/student-information-system/pull/25)) | `git rev-list --left-right --count origin/main...origin/develop` |
| Repository merge settings | Merge, squash and rebase are allowed at repository level; rulesets restrict `main` and `develop` to `merge` (section 2). Branches are not deleted automatically on merge. | `gh repo view ... --json mergeCommitAllowed,squashMergeAllowed,rebaseMergeAllowed,deleteBranchOnMerge` |
| Open PRs | [#41](https://github.com/mert494/student-information-system/pull/41) `feature/40-sprint2-submission-checker` → `develop`, review decision `APPROVED`, not merged | `gh pr list --state open` |
| CI | No GitHub Actions workflow exists; `.github/` holds only Issue and PR templates. There is no automated status check to require. | `git ls-tree -r --name-only origin/develop .github` |

## 2. Branch protection (rulesets)

Classic branch protection returns `404` for both `main` and `develop`; protection is provided by repository rulesets. Both rulesets are unchanged since the Sprint 1 check in [Repository_Setup.md](../Repository_Setup.md#7-pr-rule-and-release-evidence) (`updated_at` 2026-11-03).

| Ruleset | Target | Enforcement | PR required | Approvals | Stale approvals dismissed | Last-push approval | Threads resolved | Merge method | Deletion / force push blocked |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [main-protection](https://github.com/mert494/student-information-system/rules/26478471) | `refs/heads/main` | `active` | Yes | 2 | Yes | Yes | Yes | `merge` | Yes / Yes |
| [develop-protection](https://github.com/mert494/student-information-system/rules/26478727) | `refs/heads/develop` | `active` | Yes | 1 | Yes | Yes | Yes | `merge` | Yes / Yes |

Source: `gh api repos/mert494/student-information-system/rulesets` and `gh api repos/mert494/student-information-system/rulesets/<id>`. `bypass_actors` is `null` from a `write` account, so bypass settings remain unverified: [TODO — Mert, as admin, confirms the bypass list].

## 3. Sprint 1 tag and release (preserve, do not alter)

| Item | Value |
| --- | --- |
| Release | [Sprint 1](https://github.com/mert494/student-information-system/releases/tag/sprint-1), published 2026-11-04 20:14:53 UTC by `mert494`, not draft, not pre-release, no assets |
| Tag | `sprint-1`, lightweight tag (points directly to a commit) |
| Tag commit | `d64b7f33119d9ccccb20200aaed38ea6b54b1e16` — Merge PR [#21](https://github.com/mert494/student-information-system/pull/21) `develop` → `main`, approved by `azrayy` and `ahmetserdar41` |
| Reachable from | `origin/main` only |
| Later `main` commit | `c6af2af` (PR [#23](https://github.com/mert494/student-information-system/pull/23), Sprint 1 submission corrections) was merged after the tag, so `sprint-1` does not point to the current `main` head. This is recorded as history; the tag must not be moved. |

Commands: `git rev-parse sprint-1`, `git cat-file -t sprint-1`, `git branch -r --contains sprint-1`, `gh release view sprint-1 --json ...`.

## 4. Observations for the team

These are observations, not decisions. Each needs an owner's answer.

| ID | Observation | Proposed action | Decision owner |
| --- | --- | --- | --- |
| OBS-1 | No tag ruleset exists; both rulesets target branches only. Anyone with `write` access can technically delete or move a tag. | Consider a tag ruleset that blocks deletion and update of `sprint-*` tags. Proposed only. | Mert (admin) |
| OBS-2 | The collaborator list returns 7 accounts. `mhmttemin` (`write`) is not in the six-member account table in [Repository_Setup.md](../Repository_Setup.md#2-account-and-access-matrix). | Confirm who this account belongs to and whether the access is intended. Not assumed. | Mert (admin) |
| OBS-3 | Repository settings allow squash and rebase merges, but the rulesets allow only `merge` on `main` and `develop`. Individual commit history on protected branches is therefore preserved. | No change needed; recheck before each merge. | — |
| OBS-4 | `sprint-1` is a lightweight tag and the Sprint 1 release has no assets. | Agree whether the Sprint 2 tag is annotated and whether the release includes exported files (section 6). | Team / Mert |
| OBS-5 | There is no CI, so "checks passed" cannot be shown by GitHub status checks. Document checks are manual (section 5). | Keep manual check results in the PR description. | Barış / reviewers |

## 5. Pre-merge checklist (repeat for every integration PR)

Copy this into the PR description or a review comment and fill it against the actual PR. Values here are not pre-filled.

- [ ] PR is linked to its real Issue; source branch is owner-authored and target is `develop` (or `main` only for the final `develop` → `main` integration).
- [ ] Source head SHA recorded: `gh pr view <n> --json headRefOid,baseRefName,baseRefOid`.
- [ ] Target SHA recorded and compared with `git rev-parse origin/<target>` just before merging.
- [ ] Ruleset still `active` with the values in section 2 (`gh api .../rulesets/<id>`).
- [ ] Required approvals present from someone other than the author, given after the last push (`gh pr view <n> --json reviews,latestReviews`).
- [ ] All review threads resolved.
- [ ] Changed files match the Issue scope (`gh pr diff <n> --name-only`); no secrets, `.env` files or real student data.
- [ ] Document checks: `git diff --check`, relative links resolve, Markdown table columns consistent.
- [ ] Merge method is `merge`; no force push or history rewrite.
- [ ] Separate merge authorization obtained from the responsible person; merge commit SHA recorded afterwards.

## 6. Sprint 2 release preparation (Pending separate authorization)

Nothing in this section has been done. It is the plan for 23–24 November (Proposed window).

1. Wait until S2-12 (#37) and S2-13 (#38) record their results and the final `develop` → `main` PR passes section 5.
2. After separate authorization, create a new tag and release on the reviewed `main` merge commit. Proposed name: `sprint-2` [TODO — team confirms name and annotated vs lightweight].
3. Do not delete, move or reuse `sprint-1` or its release.
4. Verify after creation and record the output:

   ```bash
   git fetch --tags origin
   git rev-parse "sprint-2^{commit}"
   git rev-parse origin/main
   git rev-parse sprint-1
   gh release view sprint-2 --repo mert494/student-information-system --json tagName,targetCommitish,url
   ```

   Expected: the first two values are equal; `sprint-1` still returns `d64b7f33119d9ccccb20200aaed38ea6b54b1e16`.

5. Release notes contain the four Sprint 2 deliverable headings, known gaps and validation limits ([submission checklist](Sprint2_Submission_Checklist.md#authorized-integration-release-and-teams-delivery)).

| Release evidence | Value |
| --- | --- |
| Final integration PR (`develop` → `main`) | [TODO] |
| Reviewed `main` merge commit SHA | [TODO] |
| Sprint 2 tag name and SHA | [TODO] |
| Sprint 2 release URL | [TODO] |
| `sprint-1` SHA after release (unchanged) | [TODO] |
| Authorization for tag/release | [TODO] |

## 7. Tool and artifact access

No Sprint 2 artifact exists yet. Each row must be checked with a reviewer account (or the agreed sharing audience) once the artifact exists.

| Artifact | Location | Editable source preserved | Export available | Access checked by / date |
| --- | --- | --- | --- | --- |
| SRS and refined backlog | [TODO] | [TODO] | [TODO] | [TODO] |
| NFR and quality measures | [TODO] | [TODO] | [TODO] | [TODO] |
| Figma prototype and user flows | [TODO] | [TODO] | [TODO] | [TODO] |
| C4 and UML diagrams | [TODO] | [TODO] | [TODO] | [TODO] |
| OpenAPI contract ([api/openapi.yaml](../../api/openapi.yaml)) | In repository | Yes (Git) | Not needed | [TODO] |

## 8. Scope limits

- No production infrastructure, deployment, Docker or CI task is added by S2-14.
- No member's history is rewritten; account association questions (F-25) stay open as recorded elsewhere.
- Independent review of this document: [TODO].
