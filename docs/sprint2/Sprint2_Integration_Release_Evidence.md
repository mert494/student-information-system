# Sprint 2 integration and release evidence (S2-14)

Status: **Readiness update, 22 November 2026. Preparation only; final acceptance Pending.** Prepared by Barış (`baryyss-001`). Issue: [#39](https://github.com/mert494/student-information-system/issues/39) (S2-14), assigned to `baryyss-001` on 22 November 2026 (18:09 UTC, per the Issue event log). First version: PR [#42](https://github.com/mert494/student-information-system/pull/42), merged into `develop` as `98f9b5a`. This update: branch `docs/39-baris-sprint2-release-readiness`, PR [#49](https://github.com/mert494/student-information-system/pull/49) (target `develop`). Owner, priority and window remain Proposed as in the [task register](Sprint2_Task_Breakdown.md#s2-14); Mert coordinates. Final acceptance depends on S2-12 ([#37](https://github.com/mert494/student-information-system/issues/37)) and S2-13 ([#38](https://github.com/mert494/student-information-system/issues/38)), both open on 22 November 2026.

This document records the repository state as read, and the checks to repeat before integration and release. It does not perform or authorize any merge, approval, tag, release, upload, access change or Issue closure. Each of those needs separate user authorization ([AGENTS.md](../../AGENTS.md)). Mert's decisions of 22 November 2026, including the order in section 7.1, are recorded in section 9; rows still marked Open there need an action before the step they block.

## 1. Baseline read on 22 November 2026

All values were read with `git` and `gh` from Barış's account (`write` access, no Settings access); last recheck at about 19:00 UTC. Commands are listed so that anyone can repeat them. The 18 November baseline is in the version merged by PR #42.

| Item | Value | Source command |
| --- | --- | --- |
| Repository | [mert494/student-information-system](https://github.com/mert494/student-information-system); public; default branch `main` | `gh repo view mert494/student-information-system --json defaultBranchRef,visibility` |
| `origin/main` | `c6af2af9840d7166912370d645e002eb69649efb` — Merge PR [#23](https://github.com/mert494/student-information-system/pull/23) (2026-11-04); unchanged since 18 November | `git rev-parse origin/main` |
| `origin/develop` | `e265b6db9c801d9b5c0b1c01edfeb78646a1fb9a` — Merge PR [#43](https://github.com/mert494/student-information-system/pull/43) (2026-11-22 18:03 UTC), after PRs [#42](https://github.com/mert494/student-information-system/pull/42) (2026-11-18) and [#41](https://github.com/mert494/student-information-system/pull/41) (2026-11-19) | `git rev-parse origin/develop` |
| `main` vs `develop` | `main` has 2 commits not in `develop` (merge commits of [#21](https://github.com/mert494/student-information-system/pull/21) and [#23](https://github.com/mert494/student-information-system/pull/23)); `develop` has 17 commits not in `main` | `git rev-list --left-right --count origin/main...origin/develop` |
| `develop` → `main` conflicts | None at the SHAs above | `git merge-tree --write-tree origin/main origin/develop` |
| Repository merge settings | Merge, squash and rebase are allowed at repository level; rulesets restrict `main` and `develop` to `merge` (section 2). Branches are not deleted automatically on merge. | `gh repo view ... --json mergeCommitAllowed,squashMergeAllowed,rebaseMergeAllowed,deleteBranchOnMerge` |
| Sprint 2 source PRs | #43 merged; five open, [#44](https://github.com/mert494/student-information-system/pull/44)–[#48](https://github.com/mert494/student-information-system/pull/48); details in section 4. Read before this update's own PR was opened. | `gh pr list --state all` |
| Tags and releases | Only `sprint-1` and the "Sprint 1" release (section 3) | `git ls-remote --tags origin`, `gh release list` |
| CI | No GitHub Actions workflow; no required status check. The offline [submission checker](Submission_Checker_Usage.md) from PR #41 is run by hand (section 7). | `git ls-tree -r --name-only origin/develop .github` |

## 2. Branch protection (rulesets)

Classic branch protection returns `404` for both `main` and `develop`; protection is provided by repository rulesets. Both rulesets are unchanged since the Sprint 1 check in [Repository_Setup.md](../Repository_Setup.md#7-pr-rule-and-release-evidence) (`updated_at` 2026-11-03; rechecked 22 November 2026).

| Ruleset | Target | Enforcement | PR required | Approvals | Stale approvals dismissed | Last-push approval | Threads resolved | Merge method | Deletion / force push blocked |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [main-protection](https://github.com/mert494/student-information-system/rules/26478471) | `refs/heads/main` | `active` | Yes | 2 | Yes | Yes | Yes | `merge` | Yes / Yes |
| [develop-protection](https://github.com/mert494/student-information-system/rules/26478727) | `refs/heads/develop` | `active` | Yes | 1 | Yes | Yes | Yes | `merge` | Yes / Yes |

Source: `gh api repos/mert494/student-information-system/rulesets` and `gh api repos/mert494/student-information-system/rulesets/<id>`. `bypass_actors` is `null` from a `write` account, so bypass settings remain unverified (D-07 in section 9).

## 3. Sprint 1 tag and release (preserve, do not alter)

| Item | Value |
| --- | --- |
| Release | [Sprint 1](https://github.com/mert494/student-information-system/releases/tag/sprint-1), published 2026-11-04 20:14:53 UTC by `mert494`, not draft, not pre-release, no assets |
| Tag | `sprint-1`, lightweight tag (points directly to a commit) |
| Tag commit | `d64b7f33119d9ccccb20200aaed38ea6b54b1e16` — Merge PR [#21](https://github.com/mert494/student-information-system/pull/21) `develop` → `main`, approved by `azrayy` and `ahmetserdar41`; unchanged on 22 November 2026 |
| Reachable from | `origin/main` only |
| Later `main` commit | `c6af2af` (PR [#23](https://github.com/mert494/student-information-system/pull/23), Sprint 1 submission corrections) was merged after the tag, so `sprint-1` does not point to the current `main` head. This is recorded as history; the tag must not be moved. |

Commands: `git ls-remote --tags origin`, `git cat-file -t sprint-1`, `git branch -r --contains sprint-1`, `gh release view sprint-1 --json ...`.

## 4. Source PRs and proposed merge order

All six PRs target `develop`. Head SHAs and review states change with every push; recheck them with section 5 immediately before each merge.

| PR | Deliverable / task | Author | Head on 22 Nov | Review decision / merge state | Notes |
| --- | --- | --- | --- | --- | --- |
| [#43](https://github.com/mert494/student-information-system/pull/43) | SRS and refined backlog (S2-03, S2-04) | `nsnkcc` | `6bef5c9` | **Merged** 2026-11-22 18:03 UTC by `mert494` as `e265b6d`; approved by `ahmetserdar41` | Merged head `6bef5c9` |
| [#45](https://github.com/mert494/student-information-system/pull/45) | NFR and quality measures (S2-05, S2-06) | `ahmetserdar41` | `f5a545e` | `REVIEW_REQUIRED` / `BLOCKED` | Reviews so far are comments only |
| [#47](https://github.com/mert494/student-information-system/pull/47) | Architecture, C4 and UML (S2-09–S2-11) | `ardaberkkara1` | `5349b12` | `REVIEW_REQUIRED` / `BLOCKED` | Eight SVG diagrams and one Markdown document |
| [#44](https://github.com/mert494/student-information-system/pull/44) | Process and contribution log (S2-12) | `azrayy` | `67e08eb` | `REVIEW_REQUIRED` / `BLOCKED` | Records reviews and contributions of the other PRs |
| [#46](https://github.com/mert494/student-information-system/pull/46) | Cross-deliverable QA matrix (S2-13) | `mert494` | `b06ed7b` | `REVIEW_REQUIRED` / `BLOCKED`, draft | Checks the versions of the PRs above |
| [#48](https://github.com/mert494/student-information-system/pull/48) | Submission checklist and manifest (S2-15) | `mert494` | `23dd181` | `REVIEW_REQUIRED` / `BLOCKED`, draft | Manifest links point to the versions listed in section 8 |

**Merge order (decision D-01, decided by Mert on 22 November 2026):**

1. Deliverable PRs: #43 (merged), #45, #47. They change different files and can merge in any order once each is approved.
2. This document's PR [#49](https://github.com/mert494/student-information-system/pull/49) and #44.
3. #46, after the QA matrix is rechecked against the merged versions of 1 and 2.
4. #48 last, after the manifest evidence links are updated to the merged versions (section 8, note A). `expected_commit` and `release.*` stay empty in this PR (section 7.1).
5. `develop` → `main` integration (section 6).

Every PR needs its own independent approval and the pre-merge check in section 5. Reason for the order: each later PR refers to the exact versions of the earlier ones, so merging in this order avoids a second round of edits after merges.

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

## 6. `develop` → `main` integration (Pending)

Nothing in this section has been done.

1. Start only after the PRs in section 4 are merged or explicitly left out by a recorded decision.
2. Mert opens one PR from `develop` to `main` (D-02). Record its head SHA (the `develop` SHA being integrated) in the table in section 7.
3. Run the [submission checker](Submission_Checker_Usage.md) on that SHA with the committed manifest and attach the output (section 7.1, step 2). A blocking `ERROR` stops the integration; remaining `PENDING` items are listed in the PR.
4. Apply section 5. `main-protection` needs **2 approvals** from people other than the PR author, given after the last push. Planned reviewers: Ahmet and Nurefşan (D-02); their availability and reviewer permissions are checked before the PR is opened. Proposed window: 23–24 November.
5. After separate merge authorization, merge with `merge`. The resulting `main` merge commit is the candidate for the release (section 7.1, step 3).

### Running the submission checker on Windows

The checker prints text from the repository documents, including Turkish letters such as `ı`, `ş` and `ğ` that the Windows code page `cp1252` cannot represent. When Python's output encoding is such a code page, `--format text` stops with `UnicodeEncodeError` before printing the report (exit 1). This happens typically when the output is redirected or piped, for example `> report.txt` or `| grep` in Git Bash. `--format json` is not affected, because it writes ASCII only.

Force UTF-8 output for the run, using the line for your shell:

```bash
# Git Bash
PYTHONIOENCODING=utf-8 python -B tools/check_sprint2_submission.py --ref <SHA> --format text
```

```powershell
# PowerShell
$env:PYTHONIOENCODING = "utf-8"; python -B tools/check_sprint2_submission.py --ref <SHA> --format text
```

```bat
:: Command Prompt (cmd.exe)
set PYTHONIOENCODING=utf-8
python -B tools/check_sprint2_submission.py --ref <SHA> --format text
```

Alternative in any shell: `python -X utf8 -B tools/check_sprint2_submission.py --ref <SHA> --format text`. To keep a report file, redirect the output of one of these commands; the checker itself writes no file.

The exit code is the checker's own result (0 no blocking findings, 1 blocking `ERROR`, 2 blocking `PENDING`, 3 configuration error; see [Submission_Checker_Usage.md](Submission_Checker_Usage.md)). An exit code of 1 together with a `UnicodeEncodeError` traceback is the encoding problem, not a finding.

Tested on 22 November 2026 (Windows 11, Python 3.14.4) against `develop` `e265b6d`: in Git Bash, plain `--format text` with redirected output failed with `UnicodeEncodeError` (exit 1); with `PYTHONIOENCODING=utf-8` and with `-X utf8` the report printed (`Overall: PENDING`, exit 2); `--format json` printed without the variable (exit 2). The PowerShell and cmd lines ran without error (exit 2), but that PowerShell session already had UTF-8 output configured, so they do not prove the failure is absent there without the setting.

## 7. Sprint 2 release preparation (Pending separate authorization)

Nothing in this section has been done. It is the plan for 23–24 November (Proposed window).

1. Wait until S2-12 (#37) and S2-13 (#38) record their results and the `develop` → `main` PR (section 6) is merged.
2. Before tagging, record the full 40-character SHA of the reviewed `main` merge commit in the release evidence table below, and get the tag/release authorization for that exact SHA. This recorded SHA, not whatever `main` points to later, is the reference for verification. The same value is later written into `expected_commit` and `release.commit` in [submission_manifest.json](submission_manifest.json), in the order given in section 7.1 (D-05).
3. After separate authorization, create the annotated tag `sprint-2` on that recorded SHA, then the release from the existing tag (D-03; commands in section 7.1, step 5). Pass the SHA explicitly, not the branch name `main`. The release links to the verified artifacts instead of attaching files, unless the official Teams instructions require attachments (D-04).
4. Do not delete, move or reuse `sprint-1` or its release.
5. Verify after creation and record the full output. The check reads tags from the remote with `git ls-remote`, not from local tags, so a stale or locally created tag cannot pass it. It stops with `FAIL` and a non-zero exit code at the first fetch, SHA or ancestry error; only a final `PASS` line counts as evidence. Set `AUTHORIZED_SHA` to the SHA recorded in step 2 and run it in Bash (Git Bash on Windows):

   ```bash
   AUTHORIZED_SHA=<AUTHORIZED_SHA> NEW_TAG=sprint-2 bash -s <<'EOF'
   set -euo pipefail
   REPO="mert494/student-information-system"
   REMOTE_URL="https://github.com/${REPO}.git"
   SPRINT1_SHA="d64b7f33119d9ccccb20200aaed38ea6b54b1e16"
   fail() { echo "FAIL: $*" >&2; exit 1; }

   [[ "$AUTHORIZED_SHA" =~ ^[0-9a-f]{40}$ ]] || fail "AUTHORIZED_SHA is not a full 40-character SHA"

   # Remote tags only; annotated tags are peeled (^{}) to their commit.
   remote_tags="$(git ls-remote --tags "$REMOTE_URL")" || fail "git ls-remote failed"
   remote_tag_commit() {
     printf '%s\n' "$remote_tags" | awk -v t="refs/tags/$1" '
       $2 == t "^{}" { peeled = $1 }
       $2 == t       { direct = $1 }
       END { if (peeled) print peeled; else if (direct) print direct }'
   }

   new_sha="$(remote_tag_commit "$NEW_TAG")"
   [[ -n "$new_sha" ]] || fail "remote tag $NEW_TAG not found"
   [[ "$new_sha" == "$AUTHORIZED_SHA" ]] || fail "remote $NEW_TAG -> $new_sha, expected $AUTHORIZED_SHA"

   s1_sha="$(remote_tag_commit sprint-1)"
   [[ -n "$s1_sha" ]] || fail "remote tag sprint-1 not found"
   [[ "$s1_sha" == "$SPRINT1_SHA" ]] || fail "remote sprint-1 -> $s1_sha, expected $SPRINT1_SHA (sprint-1 was changed)"

   git fetch --no-tags origin main || fail "git fetch origin main failed"
   git cat-file -e "${AUTHORIZED_SHA}^{commit}" 2>/dev/null || fail "authorized commit not found after fetch"
   if git merge-base --is-ancestor "$AUTHORIZED_SHA" origin/main; then :; else
     rc=$?; [[ $rc -eq 1 ]] && fail "authorized commit is not on origin/main" || fail "ancestry check error (exit $rc)"
   fi

   release_tag="$(gh release view "$NEW_TAG" --repo "$REPO" --json tagName --jq .tagName)" || fail "gh release view $NEW_TAG failed"
   [[ "$release_tag" == "$NEW_TAG" ]] || fail "release tag is $release_tag, expected $NEW_TAG"

   # Informational output is collected first; a failure here also stops the run before PASS.
   main_sha="$(git rev-parse origin/main)" || fail "git rev-parse origin/main failed"
   later="$(git log --oneline "${AUTHORIZED_SHA}..origin/main")" || fail "git log ${AUTHORIZED_SHA}..origin/main failed"
   echo "INFO: origin/main is $main_sha; commits after the authorized SHA (not in the release):"
   if [[ -n "$later" ]]; then printf '%s\n' "$later"; else echo "(none)"; fi

   # PASS is printed last, only after every check and informational step succeeded.
   echo "PASS: remote $NEW_TAG -> $new_sha (authorized), on origin/main; sprint-1 unchanged -> $s1_sha"
   EOF
   ```

   What it checks, in order (any failure stops the run):
   - `AUTHORIZED_SHA` is a full 40-character SHA, so an unfilled placeholder or short SHA fails.
   - The remote `sprint-2` tag exists and resolves to exactly `AUTHORIZED_SHA`. This is the pass/fail check.
   - The remote `sprint-1` tag still resolves to `d64b7f33119d9ccccb20200aaed38ea6b54b1e16`.
   - `origin/main` is fetched and the authorized commit is on it (an ancestry error is reported separately from "not on main").
   - A GitHub release exists for the new tag.
   - `origin/main` and any commits after the authorized SHA are printed for information only; they are not part of the release and the tag is not moved. If reading them fails, the run stops with `FAIL`.
   - `PASS` is printed as the very last line, only after all of the above succeeded.

   Tested on 19 November 2026 with `NEW_TAG=sprint-1` and `AUTHORIZED_SHA=d64b7f3…` as a stand-in (`PASS`, exit 0), and with a wrong SHA, a missing tag (`sprint-2`), a placeholder and a short SHA, an unreachable remote and a commit not on `main` (each `FAIL`, exit 1). After moving `PASS` to the last line, the block was run again as written: the normal run ends with `PASS` (exit 0), and a simulated failure of `git log` or `git rev-parse` in the informational step stops with `FAIL` and no `PASS` line (exit 1). The annotated-tag (peeled `^{}`) branch was first checked with sample `ls-remote` output; on 22 November 2026 it was also checked with real `git ls-remote --tags` output from a local throwaway bare clone holding an annotated `sprint-2` tag on `e265b6d` (resolved to `e265b6d`; `sprint-1` resolved to `d64b7f3…`). No tag was created on GitHub.

6. Run the submission checker against the same commit with the manifest filled after tagging (section 7.1, steps 6–7).
7. Release notes follow the draft below, filled with actual values ([submission checklist](Sprint2_Submission_Checklist.md#authorized-integration-release-and-teams-delivery)).

| Release evidence | Value |
| --- | --- |
| Final integration PR (`develop` → `main`) | [TODO] |
| Integrated `develop` SHA (PR head) | [TODO] |
| Submission checker output on the integrated SHA (committed manifest) | [TODO] |
| Reviewed `main` merge commit SHA (authorized, recorded before tagging) | [TODO] |
| Sprint 2 tag name and resolved commit SHA (must equal the authorized SHA) | [TODO] |
| Sprint 2 release URL | [TODO] |
| `sprint-1` SHA after release (unchanged) | [TODO] |
| Verification output (`PASS` line and date) | [TODO] |
| Submission checker output on the authorized SHA (filled manifest, `manifest_sha256`) | [TODO] |
| Post-release manifest PR and commit | [TODO] |
| Authorization for tag/release | [TODO] |

### 7.1 Final integration, manifest and tag order (D-05)

**Problem.** A commit cannot contain its own SHA. The final `main` merge commit (called `M` below) does not exist until the `develop` → `main` PR is merged, so the manifest inside `M` cannot name `M`. Writing a placeholder or a guessed SHA is not allowed.

**How the checker resolves this** (read from `tools/check_sprint2_submission.py` on `develop` `e265b6d`):

- The manifest is always read from the working tree, even with `--ref` (`main()`, `--manifest` help text). In `--ref` mode the files under audit come from the commit, and an uncommitted manifest does not raise `git.dirty`.
- An empty `expected_commit` means "no comparison requested" (`git.expected` is a non-blocking `PENDING`). An empty `release.tag` gives a blocking `PENDING` ("Sprint 2 tag unspecified"), not an `ERROR`.
- When filled: `git.expected` is `PASS` only if `expected_commit` equals the `--ref` commit; `release.tag` is `PASS` only if the local tag resolves to `release.commit`; `release.source` is an `ERROR` if the tag does not resolve to the `--ref` commit. So all four values must be the same SHA: `--ref` = `expected_commit` = `release.commit` = commit of `sprint-2`.
- `release.remote`, `submission.manual`, review and access gates are always manual `PENDING`, so the overall result stays `PENDING` (exit 2) even when everything automatic passes. Release acceptance therefore means: **no blocking `ERROR`, and `git.expected` and `release.tag` are `PASS`.**

**Order.** The manifest committed in `M` keeps the final fields empty, which is true at that time. The final values are written only after `M` and the tag exist, and are committed after the release, outside it.

1. **#48 merged into `develop`** (last source PR, section 4) with evidence links pointing to merged versions and `expected_commit`, `release.tag`, `release.commit`, `release.url` left as empty strings. Empty is the checker's "not requested" value, not a placeholder.
2. **Integration check on `develop` head `D`.** Mert opens the `develop` → `main` PR. Run, with the committed manifest:

   ```bash
   git fetch origin
   python -B tools/check_sprint2_submission.py --ref <D> --format json
   ```

   Expected: no blocking `ERROR`; `git.expected` non-blocking `PENDING`; `release.tag` `PENDING`. Attach the output to the PR.
3. **Merge to `main`** after 2 approvals and separate authorization (section 6). Read the full merge commit SHA from GitHub, not from a local branch:

   ```bash
   gh pr view <PR> --repo mert494/student-information-system --json mergeCommit --jq .mergeCommit.oid
   ```

   Record it as `M` in the release evidence table and get the tag/release authorization for exactly this SHA.
4. **Tag ruleset** (D-06), if Mert decides to add it, is applied before step 5 (section 9).
5. **Annotated tag, then release from the existing tag.** By the person named in the authorization:

   ```bash
   git fetch origin
   git tag -a sprint-2 <M> -m "Sprint 2 — Requirements and Architecture"
   git push origin refs/tags/sprint-2
   gh release create sprint-2 --repo mert494/student-information-system --verify-tag --title "Sprint 2" --notes-file <release-notes.md>
   ```

   `--verify-tag` makes `gh` stop if the tag is not on GitHub, so `gh` cannot create a lightweight tag of its own. Then run the remote verification in step 5 of section 7 with `AUTHORIZED_SHA=<M>`; only a final `PASS` line counts.
6. **Fill the manifest locally after the tag exists.** On a new branch from current `develop`, set `expected_commit` = `M`, `release.tag` = `sprint-2`, `release.commit` = `M`, `release.url` = the release URL from step 5. Do not commit yet.
7. **Final checker run on `M` with the filled manifest:**

   ```bash
   git fetch origin --tags
   python -B tools/check_sprint2_submission.py --ref <M> --format json
   ```

   Expected: no blocking `ERROR`; `git.expected` `PASS`; `release.tag` `PASS`; no `release.source` finding; overall `PENDING` only from the manual gates. Record the output and its `manifest_sha256`. If `release.tag` is `PENDING` with "Local tag commit: None", the tag was not fetched; repeat `git fetch origin --tags`.
8. **Post-release evidence PR.** Commit the filled manifest from step 6 unchanged (same `manifest_sha256`) and open a PR to `develop` (Mert, as manifest owner). This commit comes after `M`, is not part of the release, and the tag is not moved. Whether it also goes to `main` is not required for the release; it would need another `main` PR with 2 approvals.
9. **Teams submission** (S2-15, #40) cites the tag `sprint-2`, the SHA `M`, the release URL and the step 7 output.

**Three separate pieces of evidence.** They are kept apart and none replaces another:

- **Tagged release:** the content of `M` only. The post-release manifest commit of step 8 is not part of it, and the release is never re-pointed to include it.
- **Remote tag verification:** the Bash check in section 7, step 5, run against GitHub. Its `PASS` line is required in addition to the checker result, because the checker reads local tags only.
- **Manual submission evidence:** official format and timezone, package, six-member evidence, release publication and Teams receipt (#40). The checker always leaves these as manual `PENDING`; they are confirmed and recorded by people.

If anything changes on `develop` after step 2, repeat steps 2–3 for the new head; stale approvals are dismissed by the rulesets. If the tag points to the wrong commit, stop and report; do not move or recreate it without a new decision.

**Tested on 22 November 2026** in a local throwaway clone with its remote removed (nothing pushed, no GitHub tag): with the committed manifest and `--ref e265b6d`, overall `PENDING`, `release.tag` `PENDING`, `git.expected` non-blocking `PENDING`, exit 2. With a local annotated `sprint-2` tag on `e265b6d` and the manifest filled in the working tree only, `--ref e265b6d` gave `git.expected` `PASS`, `release.tag` `PASS`, `release.url` `PASS`, no blocking `ERROR`, overall `PENDING` from manual gates, exit 2. Negative cases, each exit 1: filled manifest checked against a different `--ref` (`git.expected` and `release.source` `ERROR`); tag on another commit (`release.tag` `ERROR`); `expected_commit` different from `--ref` (`git.expected` `ERROR`). A tag missing locally gave `release.tag` `PENDING`, not `PASS`.

### Release notes draft

Values in angle brackets are filled at release time; nothing below describes a finished release.

```markdown
# Sprint 2 — Requirements and Architecture

Commit: <AUTHORIZED_SHA> (main). Integration PR: <link>. Previous release: sprint-1 (unchanged).

## Detailed SRS and refined Product Backlog
<links to the merged SRS and backlog versions>

## Non-functional requirements and quality-measure specifications
<link to the merged NFR document>

## Figma UI/UX prototypes and user-flow diagrams
<Figma file, prototype and user-flow links with version/date; access audience>

## Architecture documentation (C4 and UML)
<links to the architecture document and diagrams>

## Known gaps and open decisions
<open findings from the QA matrix and unresolved decisions, copied as they stand>

## Validation limits
Documentation and design artifacts only; no implementation, deployment, runtime or performance test is part of this release.
<submission checker result and manual checks that remain Pending>
```

## 8. Tool and artifact access

Links below are the evidence entries in `submission_manifest.json` at PR #48 head `23dd181`, read on 22 November 2026. Of these deliverables, only the SRS and refined backlog are merged into `develop` (PR #43, `e265b6d`). No access test was performed by Barış; Figma links were not opened.

| Artifact | Location (version in manifest) | Editable source preserved | Export available | Access checked by / date |
| --- | --- | --- | --- | --- |
| SRS and refined backlog | [SRS_Draft.md](https://github.com/mert494/student-information-system/blob/a9b6b4819ca18146e4e2b72346405283dbdd0c60/docs/sprint2/SRS_Draft.md), [Refined_Backlog_Draft.md](https://github.com/mert494/student-information-system/blob/a9b6b4819ca18146e4e2b72346405283dbdd0c60/docs/sprint2/Refined_Backlog_Draft.md) (`a9b6b48`; merged head `6bef5c9` is in `develop` at [`e265b6d`](https://github.com/mert494/student-information-system/tree/e265b6db9c801d9b5c0b1c01edfeb78646a1fb9a/docs/sprint2), note A) | Yes (Markdown in Git) | Not needed | [TODO] |
| NFR and quality measures | [NFR_Quality_Measures.md](https://github.com/mert494/student-information-system/blob/4502c7e9ffdd8c38599e6e5addbfdd7bf7a641c8/docs/sprint2/NFR_Quality_Measures.md) (`4502c7e`; PR #45 head is `f5a545e`, note A) | Yes (Markdown in Git) | Not needed | [TODO] |
| Figma prototype | [design](https://www.figma.com/design/n5jM7D19uV3Yj2rQRkoV6F/Untitled?node-id=1-1681&t=obxBWqyIa9OpcM99-1), [prototype](https://www.figma.com/proto/n5jM7D19uV3Yj2rQRkoV6F/Untitled?node-id=1-1681&t=obxBWqyIa9OpcM99-1) (no version recorded, note B) | In Figma; version/freeze [TODO] | [TODO] | [TODO] |
| User-flow diagrams | [Figma node 64-3](https://www.figma.com/design/n5jM7D19uV3Yj2rQRkoV6F/SENG321---OBS-prototype?node-id=64-3) (no version recorded, note B) | In Figma; version/freeze [TODO] | [TODO] | [TODO] |
| Architecture document | [Architecture_Decisions_and_Contract_Mapping.md](https://github.com/mert494/student-information-system/blob/df477c07c8adfcb37382fc129c26c98c80502bd5/docs/sprint2/Architecture_Decisions_and_Contract_Mapping.md) (`df477c0`; PR #47 head is `5349b12`, note A) | Yes (Markdown in Git) | Not needed | [TODO] |
| C4 diagrams | System Context, Container, Component SVGs in `docs/diagrams/` (`df477c0`) | SVG in Git; whether another editable source exists: [TODO — Arda] (note C) | SVG renders on GitHub | [TODO] |
| UML diagrams | Domain/Class and four sequence SVGs in `docs/diagrams/` (`df477c0`, Session Lifecycle at `5349b12`) | SVG in Git; [TODO — Arda] (note C) | SVG renders on GitHub | [TODO] |
| OpenAPI contract ([api/openapi.yaml](../../api/openapi.yaml)) | In repository | Yes (Git) | Not needed | [TODO] |

- **Note A:** The manifest links point to older commits on the PR branches than the current PR heads. After each PR is merged, its evidence entries should point to the merged version on `develop`, otherwise the release would cite versions that differ from the reviewed ones.
- **Note B:** The Figma design/prototype links and the user-flow link name different files (`Untitled` and `SENG321---OBS-prototype`) with the same file key. Which one is authoritative, the frozen version and the reviewer access audience are not recorded.
- **Note C:** The SVG files are text and can be edited in Git. Whether they were exported from another tool whose source should also be kept is not stated.

## 9. Open decisions and observations

Answers below are Mert's decisions as written in his message to Barış on 22 November 2026 (relayed to Barış; a link to a written record is [TODO]). Rows still marked Open need an action before the step they block.

| ID | Question / observation | Blocks | Owner | Decision / status |
| --- | --- | --- | --- | --- |
| D-01 | Merge order of the source PRs | Section 4 | Mert | Decided: #45/#47 → #49 and #44 → #46 → #48 → `main`; independent approval and pre-merge check for every PR |
| D-02 | Who opens the `develop` → `main` PR and gives the 2 `main` approvals | Section 6 | Mert | Decided: Mert opens it; planned approvers Ahmet and Nurefşan. Open: their availability and reviewer permissions |
| D-03 | Sprint 2 tag name and type | Section 7, step 3 | Mert | Decided: `sprint-2`, annotated |
| D-04 | Release assets | Section 7, step 3 | Mert | Decided: verified artifact links in the release, unless the official Teams instructions require attached files. Open: those instructions are not confirmed here |
| D-05 | Who fills `expected_commit` and `release.*`, and in which order | Section 7.1 | Mert | Decided: Mert owns the manifest and final submission coordination. The order in section 7.1 (final fields empty in the release commit, real SHA recorded afterwards in a separate post-release PR) was accepted by Mert on 22 November 2026 after reviewing `42e2178` |
| D-06 | Tag ruleset protecting `sprint-*` tags (OBS-1) | Before tagging | Mert (admin) | Open: to be evaluated without changing the branch rulesets. Proposal: a ruleset with target `tag`, include `refs/tags/sprint-*`, rules "Restrict deletions" and "Restrict updates" only, no bypass. "Restrict creations" is left out, because with no bypass it would also block creating `sprint-2`. The rule names and behaviour are to be confirmed in the GitHub settings by Mert before applying; Barış cannot read or change rulesets |
| D-07 | Ruleset bypass | Section 2 | Mert (admin) | Decided: no bypass will be used. Open: Mert verifies the current configuration with admin access |
| D-08 | `mhmttemin` (`write`) is not in the six-member table in [Repository_Setup.md](../Repository_Setup.md#2-account-and-access-matrix) (OBS-2) | Section 2 | Mert (admin) | Open: no permission change until the account's owner and reason for access are clarified |
| D-09 | Assignee of Issue #39 | Contribution evidence | Mert | Resolved: assigned to `baryyss-001` on 22 November 2026 (Issue event log) |

| ID | Observation | Proposed action | Owner |
| --- | --- | --- | --- |
| OBS-1 | No tag ruleset exists; both rulesets target branches only. Anyone with `write` access can technically delete or move a tag. | D-06 | Mert (admin) |
| OBS-2 | The collaborator list returns 7 accounts, including `mhmttemin`. | D-08 | Mert (admin) |
| OBS-3 | Repository settings allow squash and rebase merges, but the rulesets allow only `merge` on `main` and `develop`, so individual commit history on protected branches is preserved. | No change; recheck before each merge. | — |
| OBS-4 | `sprint-1` is a lightweight tag and the Sprint 1 release has no assets. `sprint-2` will be annotated (D-03). | `sprint-1` stays as it is. | — |
| OBS-5 | There is no CI, so "checks passed" cannot be shown by GitHub status checks. | Keep manual and checker results in each PR description. | Barış / reviewers |
| OBS-6 | `tools/check_sprint2_submission.py --format text` fails on Windows with `UnicodeEncodeError` when the output encoding is a code page such as `cp1252`. Its 24 unit tests pass (`python -B -m unittest discover -s tests`, Python 3.14.4). On `develop` `e265b6d` the checker returns `Overall: PENDING` (exit 2), as expected before all deliverables are merged. | Decided by Mert: use the documented UTF-8 workaround (section 6); a code change is not required for submission. The checker's own comment says stdout is deliberately not reconfigured, so any change would be a separate, small, tested PR if needed. | Mert |

## 10. Scope limits

- No production infrastructure, deployment, Docker or CI task is added by S2-14.
- No member's history is rewritten; account association questions (F-25) stay open as recorded elsewhere.
- The content of the source PRs was not reviewed here; only their state, versions and file lists were read.
- Independent review of this update: [TODO].
