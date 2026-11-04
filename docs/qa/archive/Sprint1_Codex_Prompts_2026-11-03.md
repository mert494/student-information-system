# Sprint 1 Codex prompts (archive, 2026-11-03)

Status: **Archived; historical record only. Do not use these as current instructions.** This file keeps the Codex prompts that the QA role prepared on 2026-11-03 for Sprint 1 coordination, translated into English. They describe the repository as it was on that date; most steps have since been completed or replaced. The current task list is [Sprint1_Action_Items.md](../../Sprint1_Action_Items.md) and the current QA results are in [Sprint1_Quality_Report.md](../../Sprint1_Quality_Report.md). Prepared by: Ahmet (QA). Related Issue: [#3](https://github.com/mert494/student-information-system/issues/3).

Moved here from `docs/Sprint1_Codex_Prompts.md` on 2026-11-04 after Mert's review of PR #2.

## Known errors and outdated points in this archive

These points were wrong or became outdated; the prompts below are kept unchanged apart from translation.

| Where | Original instruction | Correction |
| --- | --- | --- |
| Step 2, Barış, task 3 | Read `branches/{branch}/protection` and write "no protection" if it returns 404 | Wrong. This repository is protected by rulesets, and the classic protection endpoint returns 404 for them. Use `rulesets`, `rulesets/{id}`, `rules/branches/{branch}` and the `protected` field of `branches/{branch}` (see report §2 and §3.1) |
| Step 1, Mert, task 3 | Apply branch protection through `gh api` with at least 1 approval for `main` and `develop` | Protection was applied as the `main-protection` (2 approvals) and `develop-protection` (1 approval) rulesets |
| Step 2, Nurefşan, task 3, and Arda, task 3 | Role names "Administrator" (singular) | The agreed documents use "Administrators" |
| Step 4, Mert | Merge order #6 → #8 → #7 → … | Actual order: #7, #8, #6, #19; #17 and #2 still open on 2026-11-04 |
| All steps | PR #1, #2, #6, #7, #8 targets and branch names as of 2026-11-03 | See the report's §1 for the current state |

## Order (as planned on 2026-11-03)

| Step | Who | When |
| --- | --- | --- |
| 1 | Mert | Immediately; everyone else waits for this |
| 2 | Nurefşan, Arda, Barış, Azra | In parallel, once Mert posts "develop is open" |
| 3 | Ahmet (QA) | After the step 2 pushes: recheck, report and review |
| 4 | Mert | Once reviews are approved: merge |
| 5 | Barış | After `develop` → `main` is merged: tag and release |

Submission: **5 November 2026, 23:59**.

## Step 1: Mert

```text
I am Mert, Scrum Master of the BM321 SIS project. Repo: mert494/student-information-system (I own it).
First read AGENTS.md, docs/Git_Workflow.md and docs/Sprint1_Action_Items.md on the
origin/docs/ahmet-sprint1-quality branch. Check the current state with git fetch --all, git branch -a,
gh pr list and gh issue list. If gh CLI is missing, install it and log in with gh auth login.

Tasks (show what you will do before each step and get my approval):
1. Merge PR #1 (docs/sprint1-team-guides -> docs/sprint1-process).
2. Create the develop branch from the current docs/sprint1-process and push it.
3. Apply branch protection to main and develop with gh api: PR required, at least 1 approval,
   stale approvals dismissed on new commits, force push and deletion disabled. Read the applied
   settings back with gh api and show the output.
4. Retarget PRs #2, #6, #7 and #8 to develop (gh pr edit <n> --base develop).
5. Close PR #4 with an explanatory comment, because its content reached develop through PR #1.
6. Open a PR to develop for my docs/mert-qa-corrections branch. List the changed files in the
   description (Sprint1_Submission_Checklist.md, docs/qa/Mert_QA_Corrections.md, Git_Workflow.md,
   GitHub_Projects_Setup.md, team-guides); reviewer ahmetserdar41.
   Show any conflicts with develop; do not change anything outside my own files.
7. Open Issues with the .github/ISSUE_TEMPLATE/documentation.md template and assign the owners:
   Project Proposal (nsnkcc), System Vision and Boundary (nsnkcc, ardaberkkara1),
   OpenAPI Draft (ardaberkkara1), Team Roles and RACI (azrayy), Initial Product Backlog (nsnkcc).
   Add the new Issue numbers to the related PR descriptions as "Related: #n".
   Verify the usernames with gh api repos/.../collaborators before opening them.
8. Assign reviewers: #6 -> ardaberkkara1, #7 -> ahmetserdar41, #8 -> ahmetserdar41 and nsnkcc,
   #2 -> mert494.
9. When done, write a short message for the team: develop is open, PRs retargeted to develop,
   the new Issue numbers.
Rules: no direct commits to main, no force push, ask for my approval separately for every merge.
In this step merge only PR #1; do not merge the other PRs.
```

## Step 2: Nurefşan

```text
I am Nurefşan, Product Owner of the BM321 SIS project. My branch: docs/nurefsan-sprint1-requirements, PR #7.
First read AGENTS.md, the "Nurefşan" section of docs/Sprint1_Action_Items.md on the
origin/docs/ahmet-sprint1-quality branch, and findings F-06, F-11, F-12, F-14 and F-16 in
docs/Sprint1_Quality_Report.md. I already did F-10 and F-13 (c7e9d79, 1184b26); do not touch them.
The documents must stay in English.

Tasks (show the diff and get my approval before every commit/push):
1. Run git fetch origin. PR #7 must target develop (gh pr view 7). Merge origin/develop into
   my branch. In the docs/Initial_Backlog_Draft.md conflict keep my English version, remove the
   conflict markers and make a merge commit. No rebase and no force push.
2. F-06: replace "appropriate response" in PB-02 AC4 and PB-05 AC5 with a concrete outcome
   (unauthorized action: 403 Forbidden; prerequisite/quota problem: 409 Conflict + error message).
   Keep it consistent with the responses in api/openapi.yaml (origin/docs/arda-sprint1-architecture).
3. F-11: map the four roles in Vision §2.1 (Student, Instructor, Administrator, Student Affairs Staff)
   to the stakeholder table in the Proposal and to the backlog. Stakeholder names may stay in the
   Proposal, but write in a table or sentence which system role each stakeholder maps to. Replace
   "user", "system administrator" and "authorized administrator" in the backlog with these roles.
4. F-12: either add a PB item for "University Management", or state in the Proposal and Vision
   that it is out of Sprint 1 scope. Ask me which one to choose.
5. F-16: add the "so that ..." part to the PB-05, PB-06 and PB-07 user stories.
6. Keep the combined docs/System_Vision_and_Boundary.md; do not delete Arda's Boundary text.
7. Add the Issue numbers Mert opened to the PR #7 description as "Related: #n" and list my
   changes. If an Issue number is unknown, write [TODO].
```

## Step 2: Arda

```text
I am Arda, Lead Architect of the BM321 SIS project. My branch: docs/arda-sprint1-architecture, PR #8.
First read AGENTS.md, the "Arda" section of docs/Sprint1_Action_Items.md on the
origin/docs/ahmet-sprint1-quality branch, and findings F-18…F-21 in docs/Sprint1_Quality_Report.md.
Check that git config user.email is the school email on the ardaberkkara1 account (the account issue is fixed).

Tasks (show the diff and get my approval before every commit/push):
1. F-20: the combined docs/System_Vision_and_Boundary.md is in Nurefşan's PR #7. Remove this file
   from my branch with git rm; only api/openapi.yaml should remain in PR #8.
2. F-18: add to api/openapi.yaml:
   - components.securitySchemes.bearerAuth (type: http, scheme: bearer, bearerFormat: JWT)
   - root-level security: [{bearerAuth: []}]; security: [] for POST /sessions (login is public)
   - servers: [{url: http://localhost:8080, description: Local development (placeholder)}]
   - info.license: {name: MIT, identifier: MIT}
   Update the x-security-status and x-servers-status descriptions (still "proposed").
3. F-19: add tags to every operation (Sessions, Students, Courses, Registrations, Grades) and define
   the tags list at the root. Add one example with fake values to each main success response; do not
   use real student data. Add basic fields to the Student, Course, Registration and Grade schemas
   (for example studentNumber, fullName, courseCode, title, credits, term, status, value).
   Role names: Student, Instructor, Administrator, Student Affairs Staff.
4. Run npx @redocly/cli lint api/openapi.yaml; fix it until no errors remain and add the output to the
   PR #8 description. State that this is contract validation, not a live API test.
5. PR #8 must target develop (gh pr view 8). Add the OpenAPI Issue Mert opened to the description as
   "Related: #n"; if unknown, [TODO].
6. F-21 (after PR #7 is merged, with a new branch docs/arda-sprint1-boundary from the current develop):
   add the "No external systems are in scope for Sprint 1" decision and a simple actor–SIS
   interaction table to §4.4 of the combined document; open a PR to develop.
Do not write invented decisions; mark everything unapproved as "proposed". No force push.
```

## Step 2: Barış

```text
I am Barış, DevOps owner of the BM321 SIS project. My branch: docs/baris-sprint1-repository, PR #6.
First read AGENTS.md, docs/Repository_Setup.md and the "Barış" section of
docs/Sprint1_Action_Items.md on the origin/docs/ahmet-sprint1-quality branch.

Tasks (show the diff and get my approval before every commit/push):
1. F-17: in Repository_Setup.md replace "Related Issue: [TODO]" with #5, and "This work's PR" in the
   evidence table with #6; update the PR/Issue list with gh pr list and gh issue list.
2. Verify the access table with gh api repos/mert494/student-information-system/collaborators
   and fill it in from the real output. If my permissions are not enough, write the command and the
   error; do not invent values.
3. develop now exists: update the temporary PR target in §4 to develop.
   Read the rules with gh api repos/mert494/student-information-system/branches/main/protection and
   .../branches/develop/protection and add a summary to the evidence table
   (PR required, number of approvals, force push disabled). If it returns 404, write "no protection".
   [Archive note: this last sentence was wrong; see "Known errors" above.]
4. Check that PR #6 targets develop; make Issue #5 "Closes #5" in the description.
Do not do the tag now; it is a separate prompt once all merges are done.
```

## Step 2: Azra

```text
I am Azra, Agile Process owner of the BM321 SIS project.
First read AGENTS.md, docs/RACI_Matrix.md, docs/RACI_Matrix.csv, docs/Sprint1_Process_Records.md and
the "Azra" section of docs/Sprint1_Action_Items.md on the origin/docs/ahmet-sprint1-quality branch.
Fetch develop with git fetch origin.

Tasks (show the diff and get my approval before every commit/push):
1. Check PR #4 with gh pr view 4. If Mert closed it, skip. If not, verify that its content reached
   develop through PR #1 and prepare a closing comment; get my approval before closing.
2. Create a new branch docs/azra-sprint1-process from origin/develop.
3. In Sprint1_Process_Records.md fill in the "Role Assignment" table and the meeting/decision records
   only with meetings and decisions that actually happened and that I tell you about. First ask me
   which information is needed (date, participants, decisions). Do not record meetings that did not
   happen; unknowns stay [TODO].
4. QA-12 / F-09: if the team approved the RACI, add the approval date / Decision ID and the
   Mert–Azra division to RACI_Matrix.md; if Mert's load (5 A, 11 R) was discussed, record the decision.
   Keep .md and .csv identical (exactly one A and at least one R per row); compare the two files after
   the change and show the result.
5. Open a PR to develop; list the files that actually changed in the description and add the RACI
   Issue Mert opened as "Related: #n" (if unknown, [TODO]). Reviewer: mert494.
```

## Step 3: Ahmet (QA)

No separate prompt. After the step 2 pushes, QA:

- rechecks the changes (Redocly lint, RACI MD/CSV parity, conflicts with `git merge-tree`),
- updates [Sprint1_Quality_Report.md](../../Sprint1_Quality_Report.md) and [Sprint1_Action_Items.md](../../Sprint1_Action_Items.md),
- reviews PR #7, PR #8 and Mert's PR.

## Step 4: Mert (merge)

```text
I am Mert. Check with gh pr list and gh pr view that all PRs target develop and have at least one
approval. If any PR is unapproved or has conflicts, do not merge; list them for me.
Merge in this order, getting my approval separately for each (merge commit, no squash):
PR #6 (Barış) -> PR #8 (Arda) -> PR #7 (Nurefşan) -> Azra's PR -> my mert-qa-corrections PR
-> Arda's boundary PR if it exists -> last, PR #2 (Ahmet QA).
After every merge check that develop has exactly one docs/System_Vision_and_Boundary.md and that
api/openapi.yaml exists.
Then open a develop -> main PR ("Sprint 1 submission") and list the merged PRs in the description.
Merge once approved. No force push.
```

## Step 5: Barış (tag)

```text
I am Barış. Run git fetch origin; show the latest commit of origin/main and verify that the
develop -> main PR has been merged. Prepare these commands and run them with my approval:
git tag -a sprint-1 <main commit> -m "Sprint 1 submission"
git push origin sprint-1
gh release create sprint-1 --title "Sprint 1" --notes "<list of merged PRs>"
To add the release link to docs/Repository_Setup.md and docs/Sprint1_Submission_Checklist.md,
create a new branch from develop and prepare a PR.
```
