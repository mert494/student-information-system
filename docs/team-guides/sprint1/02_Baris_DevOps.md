# Barış — DevOps execution package

Status: Guide for team approval. Read the [main guide](00_Team_Overview.md), [Git rules](../../Git_Workflow.md), [Projects preparation](../../GitHub_Projects_Setup.md) and [RACI](../../RACI_Matrix.md) together. Related work: S1-07, S1-08, S1-14, S1-15, S1-16.

## A. Purpose of the role

Provide repository infrastructure that the team can access, where changes proceed through review and contribution history is preserved. Sprint 1 focuses on access, Git organization and reproducible initial setup instructions.

## B. Sprint 1 responsibilities

1. Verify repository/Organization ownership and access through each of the six members' own accounts.
2. Clarify `main`/`develop`, task branches, PR/review and protection proposals with Mert.
3. Apply agreed settings after authorization and separate user approvals; record actual results.
4. Inspect existing repository tools and prepare setup instructions reflecting the current state.
5. Verify that the review/PR workflow actually works; coordinate release/tag preparation with Mert.

GitHub Actions CI and at least 50% unit-test coverage are Sprint 3 requirements. Single-command product startup with Docker/docker-compose and deployment are for the final submission. Do not present them as Sprint 1 requirements or currently working capabilities.

## C. Step-by-step implementation

1. Use Git CLI, the GitHub web interface and a text editor. Record the initial state with `git status --short`, `git branch -a`, `git remote -v`; follow the [shared update/approval sequence](00_Team_Overview.md).
2. Request all six members' GitHub usernames; verify repository access for each account. The repository currently shows a personal remote; do not assume an Organization exists. Organization creation/transfer, membership and permission changes require explicit approval.
3. Compare `main` and `develop` records. If `develop` is missing, prepare a proposal with Mert/Arda for its starting commit and integration of the current process branch. Do not create branches, transfer the repository or change the default branch without approval.
4. Read active rules in GitHub Settings → Rules/Branches. Compare proposed PR requirements, at least one independent review, conversation resolution and force-push/deletion protection for `main` and `develop` with plan/permission availability. Record current settings and proposals separately.
5. After user approval, apply accepted settings; record before/after status and the actual rule link. If no CI exists yet, do not select an imaginary check name; do not mark unavailable settings as applied.
6. Look for existing manifests/tools. If only documents currently exist, document clone, branch selection and document/API validation preparation; do not invent `npm start`, Docker or backend startup commands. Wait for Arda's tool/version decision.
7. Use your actual documentation PR to exercise the workflow; do not open unnecessary test PRs. After approved push/PR, observe independent reviewer assignment, comments and check visibility. Do not test protection by pushing to `main`.
8. Provide results to Mert's submission checklist and evidence record. Prepare a release/tag only after a reviewed submission commit and separate explicit approval; do not create tags in advance.

If the CLI exists, use read commands such as `gh auth status`, `gh repo view mert494/student-information-system`; otherwise the web interface is sufficient. Do not place credentials/token output in documents or logs. If commands cannot resolve permission problems, notify the repository owner; do not treat access errors as “resource does not exist”.

## D. Files to produce or update

| File / format / location | Required content | Requirement status | Completion criterion |
| --- | --- | --- | --- |
| `docs/Git_Workflow.md` — existing Markdown | Branch base/target, review/merge, protection decision and implementation evidence | Git-Flow content required; shared editing under Mert's ownership | Diff approved with Mert; proposals distinguished from active settings |
| `docs/Repository_Setup.md` — new Markdown proposal | Repository/Organization, account/access matrix, prerequisites, clone/branch, current validation steps, gaps, actual PR/rules/release links | Separate file proposed; repository/workflow evidence required | Matches the actual environment; no startup commands for a nonexistent application |
| `docs/Sprint1_Submission_Checklist.md` — existing Markdown | Proposed updates for Mert on GitHub access, rules and release/tag evidence | Submission evidence required; coordinate this document with Mert | Correct URL/SHA; work not performed is not marked complete |

## E. Prompt to paste into Codex

```text
I am Barış, the BM321 SIS DevOps and CI/CD Infrastructure Engineer.
Inspect README, all applicable AGENTS.md files, git status/branch/remote,
docs/Git_Workflow.md, docs/RACI_Matrix.md, docs/GitHub_Projects_Setup.md, the submission
checklist and docs/team-guides/sprint1/02_Baris_DevOps.md.
First summarize current access/branch/tool status; do not touch others' work.
If no existing equivalent file exists, prepare access and setup instructions in
docs/Repository_Setup.md. If GitHub is connected, perform only permitted read-only
status checks; do not claim inaccessible settings were verified. Mark all six members'
unknown account information and other gaps [TODO]. First propose necessary corrections
to Mert's Git_Workflow document; do not create a separate workflow. If develop is missing,
ask the user for the base/target. Do not apply Organization creation/transfer, membership,
protection or default-branch changes without approval. Explain how the actual PR workflow
will be verified; do not push to main or close PRs for testing.
Do not invent nonexistent applications, manifests, CI or Docker commands. Separate GitHub
Actions and the 50% unit-test coverage target into Sprint 3, and single-command
Docker/deployment into the final submission. Do not add secrets or .env files. Do not
delete existing files or make unrelated changes. Present local diff and validation results.
Wait for branch/commit approval; obtain separate explicit approval for push, PR and merge.
Do not force push.
```

## F. GitHub workflow

Example branch: `docs/baris-sprint1-repository`; example commit: `docs(devops): document repository setup and access checks`. Link an actual Issue. Proposed reviewers: Arda (technical base) and Mert (workflow); do not finalize settings based solely on your own approval. Stage only relevant files; follow separate commit/push/PR/merge permissions in the [shared workflow](00_Team_Overview.md). Ask the user if the PR target is missing.

## G. Collaboration

Mert: workflow and board access; Arda: base commit and tool/version needs; Ahmet: actual checks/PR evidence; Azra: decision records; Nurefşan: license decision and submission scope. Full API details do not block access/protection inspection; application setup instructions require technical decisions.

## H. Submission checklist

- [ ] Six accounts' access and Organization status verified or explicitly listed as gaps.
- [ ] `develop` base/target and Git-Flow proposal clarified by the team.
- [ ] Protection proposals and actual active settings recorded separately.
- [ ] Independent review workflow observed in an actual documentation PR.
- [ ] Setup instructions match current tools and contain no secrets.
- [ ] Release/tag and submission evidence coordinated with Mert; later-sprint infrastructure not presented as required now.
