# Repository access and setup instructions

Status: **Proposal for team approval.** Prepared by: Barış. Related Issue: [#5](https://github.com/mert494/student-information-system/issues/5). PR: [#6](https://github.com/mert494/student-information-system/pull/6). RACI: S1-07 (A/R), S1-08 (R), S1-14 (R), S1-15 (A/R), S1-16 (R). Branch, PR, review, merge and protection rules are in [Git_Workflow.md](Git_Workflow.md).

## 1. Repository and Organization

Repository: [mert494/student-information-system](https://github.com/mert494/student-information-system); public, default branch `main`. Checked on 2026-11-04 with `git` and `gh`. Barış has no Settings access, so the collaborator list and branch rules were read with `gh api` instead of Settings.

The repository belongs to the personal account `mert494`, not an Organization. In this setup, only the repository owner can change Settings, collaborators and branch rules. Organization decision: Personal repository (mert494); no Organization in Sprint 1.

## 2. Account and access matrix

The name–account mapping was inferred from repository records (PR authors); each member must confirm their own account. Access levels were verified on 2026-11-04 with `gh api repos/mert494/student-information-system/collaborators --jq '.[]|"\(.login) \(.role_name)"'`.

| Member | GitHub account | Repository access |
| --- | --- | --- |
| Arda | `ardaberkkara1` | `write` |
| Barış | `baryyss-001` | `write`; no Settings access |
| Ahmet | `ahmetserdar41` | `write` |
| Mert | `mert494` | `admin`; repository owner |
| Azra | `azrayy` | `write` |
| Nurefşan | `nsnkcc` | `write` |

## 3. Prerequisites

- Your own GitHub account and repository access.
- Git; your commit identity must be your own name and an email that matches your GitHub account.
- A text editor that can edit Markdown.
- Optional: GitHub CLI (`gh`). Each member logs in themselves; tokens are not placed in documents or logs.

Technology and version requirements are not decided yet: [TODO — Arda].

## 4. Clone and branch

```bash
git clone https://github.com/mert494/student-information-system.git
cd student-information-system
git config user.name "<Full Name>"
git config user.email "<email matching your GitHub account>"
git fetch origin
```

`develop` exists; its current commit is `a2d4579` (`git rev-parse --short origin/develop`, 2026-11-04). All Sprint 1 PRs target `develop`. Start a new branch from it:

```bash
git switch -c docs/<name>-sprint1-<topic> origin/develop
```

Each branch, commit, push, PR and merge step needs separate approval ([AGENTS.md](../AGENTS.md)). Do not push directly to `main` and do not force push.

## 5. Current validation steps

The repository has no application code, manifest, CI or Docker file, so there are no run or test commands. GitHub Actions and the 50% unit-test coverage target belong to Sprint 3; single-command Docker startup and deployment belong to the final submission. For document changes:

1. Use `git status --short` to check that only task files changed.
2. Use `git diff --check` to check for whitespace errors and conflict markers.
3. Check that relative links point to existing files and that table columns are consistent.
4. Check that there are no secrets, tokens, passwords, `.env` files or real student data.

## 6. Open items

- [TODO] Each member confirms their own account mapping.
- Access levels: verified on 2026-11-04 (see section 2).
- Organization decision: Personal repository (mert494); no Organization in Sprint 1.
- `develop` start: develop created; PR #1 merged as `1f6c6dd`.
- Protection/rulesets: verified on 2026-11-04 (see section 7).
- Sprint 1 release/tag: Planned: `sprint-1` tag on `main` after `develop` → `main` merge. No tag or release exists yet (2026-11-04). The tag is created only after a reviewed, merged submission commit exists and separate approval is given ([02_Baris_DevOps.md](team-guides/sprint1/02_Baris_DevOps.md)).

## 7. PR, rule and release evidence

This document's PR serves as workflow evidence; no separate test PR is opened and no push to `main` is attempted.

| Evidence | Link / value (2026-11-04) |
| --- | --- |
| Merged PRs | [#1](https://github.com/mert494/student-information-system/pull/1), [#16](https://github.com/mert494/student-information-system/pull/16), [#18](https://github.com/mert494/student-information-system/pull/18) |
| Closed PRs (not merged) | [#4](https://github.com/mert494/student-information-system/pull/4) |
| Open PRs | [#2](https://github.com/mert494/student-information-system/pull/2), [#6](https://github.com/mert494/student-information-system/pull/6), [#7](https://github.com/mert494/student-information-system/pull/7), [#8](https://github.com/mert494/student-information-system/pull/8), [#17](https://github.com/mert494/student-information-system/pull/17) |
| Issues (all open) | [#3](https://github.com/mert494/student-information-system/issues/3), [#5](https://github.com/mert494/student-information-system/issues/5), [#9](https://github.com/mert494/student-information-system/issues/9), [#10](https://github.com/mert494/student-information-system/issues/10), [#11](https://github.com/mert494/student-information-system/issues/11), [#12](https://github.com/mert494/student-information-system/issues/12), [#13](https://github.com/mert494/student-information-system/issues/13), [#14](https://github.com/mert494/student-information-system/issues/14), [#15](https://github.com/mert494/student-information-system/issues/15) |
| This work's Issue and PR | Issue [#5](https://github.com/mert494/student-information-system/issues/5), PR [#6](https://github.com/mert494/student-information-system/pull/6) (target `develop`) |
| Independent review of this work | [TODO] |
| Active rulesets | `develop-protection` (1 approval) and `main-protection` (2 approvals) are active; see the table below |
| Sprint 1 release/tag | Pending; `main` is still at `7072b41` |

| Ruleset | Target branch | PR required | Approvals | Stale approvals dismissed | Allowed merge method | Deletion / force push blocked | Enforcement |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [develop-protection](https://github.com/mert494/student-information-system/rules/26478727) | `develop` | Yes | 1 | Yes | `merge` | Yes / Yes | `active` |
| [main-protection](https://github.com/mert494/student-information-system/rules/26478471) | `main` | Yes | 2 | Yes | `merge` | Yes / Yes | `active` |

Source: `gh api repos/mert494/student-information-system/rulesets` and `gh api repos/mert494/student-information-system/rulesets/<id>`. Both rulesets also require conversation resolution and approval of the last push. `bypass_actors` returned `null` for Barış's account, so bypass settings remain unverified.
