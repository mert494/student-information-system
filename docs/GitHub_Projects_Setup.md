# GitHub Projects setup and Sprint 1 tracking

**Proposal for team approval.** This document does not create remote resources or apply settings. Proposed responsibilities: Mert for tracking, Barış for infrastructure/access, Nurefşan for product scope. Evidence snapshot: 3 November 2026, from read-only GitHub connector queries and git ls-remote. Two assigned Issues and six open PRs were verified. The repository is owned by the personal account mert494; an Organization has not been established for this repository. Projects board existence, URL, fields, items and automation are **Unverified**: gh is unavailable, the connector has no Projects read capability, and the web read failed. Repository metadata has_projects=true indicates feature availability, not a verified board. No live Issue or Project was created or updated.

## Board statuses

| Status | Entry / exit criteria |
| --- | --- |
| Backlog | Proposal recorded; PO/team scope decision and refinement pending |
| To Do | Scope, owner, Acceptance Criteria and dependencies clear; selected for the sprint |
| In Progress | Owner has started work; Issue/branch link added |
| In Review | Reviewable PR or document and check evidence ready |
| Done | Acceptance Criteria, independent review and relevant checks complete; PR merged if applicable and evidence linked |

For impediments, a separate `Blocked` field and impediment link alongside Status are proposed. A ready template file does not make the entire Sprint 1 submission Done.

## Proposed fields and views

Status, Assignees (actual GitHub accounts [TODO]), Priority (P1/P2/P3), Story Points (Number), Sprint (Sprint 1), Epic, Requirement, Dependencies, Evidence and Blocked. Preserve task IDs S1-01…S1-16; they do not replace actual Issue numbers. Organize Board view by Status; configure table view with owner, priority, sprint and evidence fields. The proposed default status is Backlog.

## Sprint 1 task list

The assignments below remain proposals matching the [RACI](RACI_Matrix.md); team approval is [TODO]. The complete Issue inventory contains two open Issues: QA #3 assigned to ahmetserdar41 and DevOps #5 assigned to baryyss-001. Both bodies contain acceptance criteria, textual P1 priorities and dependencies. Labels and milestones are empty; approved estimates are [TODO]. These actual assignments do not establish an approved Sprint Backlog. Check the latest inventory and reuse existing Issues before any separately authorized creation.

| ID | Task | Proposed responsible person (R) | Acceptance Criteria |
| --- | --- | --- | --- |
| S1-01 | Proposal and problem definition | Nurefşan | Problem, purpose, stakeholders and scope documented; team/PO review recorded |
| S1-02 | License decision | Nurefşan, Arda | Existing MIT file reviewed; selection rationale added to proposal; decision recorded |
| S1-03 | System Vision | Nurefşan, Arda | System goals and stakeholder needs explained; consistent with proposal |
| S1-04 | System Boundary | Arda, Nurefşan | Actors, external systems and in/out-of-scope areas clear; consistent with vision |
| S1-05 | Draft OpenAPI YAML | Arda | YAML parses; validated against selected OpenAPI version; requirements mapping and draft limitations documented |
| S1-06 | Roles and RACI | Azra, Mert | All six members included; one A per row; CSV/Markdown match; team approval recorded |
| S1-07 | Organization/repository access | Barış, Mert | Organization decision made; six members' accounts/access and repository URL verified |
| S1-08 | Git-Flow and review policy | Mert, Barış | Branch, commit, PR, review, merge, conflict and protection rules reviewed; develop decision recorded |
| S1-09 | Initial Product Backlog | Nurefşan, Mert | Stories, Acceptance Criteria, priorities, estimates and dependencies reviewed by PO/team; draft/approved distinction clear |
| S1-10 | Projects, Issues and sprint plan | Mert, Azra | Board and actual Issue links available after permission; owners, sprint goal and statuses verified |
| S1-11 | Issue/PR templates and AGENTS | Mert | All fields in three Issue templates and one PR template complete; security and approval boundaries clear; review performed |
| S1-12 | Process records | Azra, Mert | Actual meeting/attendance/decision/action records supported by evidence; events that have not occurred explicitly blank/planned |
| S1-13 | Quality and submission compliance | Ahmet, Arda, Mert | All six Sprint 1 deliverable headings and links checked; gaps and results recorded |
| S1-14 | Individual contribution evidence | All six members | Each member's actual account, Issue, PR/review and commit evidence mapped |
| S1-15 | Release/tag | Barış, Mert | Reviewed commit versioned after user approval; URL and SHA recorded |
| S1-16 | Final submission tracking | Mert, Azra, Barış | Checklist completed; submission links and course-channel submission evidence recorded |

## Verified Issue and PR mapping — 3 November 2026

| Sprint 1 work | Existing Issue | Existing PR / evidence | Remaining coordination |
| --- | --- | --- | --- |
| Quality checks | [#3](https://github.com/mert494/student-information-system/issues/3), Ahmet | [PR #2](https://github.com/mert494/student-information-system/pull/2) references #3; Mert requested as reviewer | Independent review and affected rechecks pending |
| Repository setup | [#5](https://github.com/mert494/student-information-system/issues/5), Barış | [PR #6](https://github.com/mert494/student-information-system/pull/6) references #5; Mert/Arda requested | Issue #5 still has a PR TODO; owner update and review pending |
| Proposal, combined Vision/Boundary and Initial Backlog | [TODO] | [PR #7](https://github.com/mert494/student-information-system/pull/7); no linked Issue evidenced | Nurefşan confirms scope/content; Mert coordinates Issue coverage and backlog mapping |
| OpenAPI / Boundary draft tracking | [TODO] | [PR #8](https://github.com/mert494/student-information-system/pull/8); no linked Issue evidenced | Arda/Nurefşan reconcile shared-file scope; Mert tracks links only |
| Roles/process records | [TODO] | [PR #4](https://github.com/mert494/student-information-system/pull/4); no linked Issue evidenced | Azra coordinates RACI approval; agree integration with PR #1 |
| Mert's process templates, guides and QA checklist corrections | [TODO] | [PR #1](https://github.com/mert494/student-information-system/pull/1); correction [b7e8655](https://github.com/mert494/student-information-system/commit/b7e865574ff87f9ae303d390307fb8317c5569c3) has no PR | Agree task Issue and PR target before any publication |
| Sprint planning, Projects and submission tracking; PB-01–PB-07 mapping | [TODO] | [Submission checklist](Sprint1_Submission_Checklist.md); board URL [TODO] | Confirm real sprint facts, PO-approved stories, team estimates/owners and board status; no implementation commitment inferred |

All six PRs are open and have zero submitted reviews. A requested reviewer is not a completed review. Proposed board statuses above have not been verified on a live board. Missing Issue, dependency and board mappings remain [TODO]; create/update operations require separate approval. Mert coordinates tracking without editing the Product Owner's backlog or approving another member's deliverable.

## GitHub interface steps — only after approval

1. Check existing Organization/Projects and repository access; do not unnecessarily duplicate the board. Organization creation or repository transfer requires a separate team/authorization decision.
2. Under the appropriate owner, open a new board through Projects or select an existing board. Link it to the repository.
3. Configure Status with the five options above. Add required fields; group the Board by Status.
4. Barış verifies member access. After team approval, create S1 tasks with the Issue templates; add actual assignees, Acceptance Criteria and dependency links.
5. Add Issues to the board. Select S1 tasks as Sprint 1 scope; do not automatically turn PB product examples into implementation commitments.
6. Review Projects Workflows settings. Check default automations that set Done when an Issue closes/a PR merges; do not mistakenly mark unaccepted or canceled work complete. Initially verify transitions manually.
7. Mert updates progress/impediment tracking; Azra updates actual meeting and decision records. At submission, check actual Issue → PR → commit → release/tag links.

## Read-only CLI check examples when available

No installation or login was performed in this task. The following PowerShell commands check current status after the CLI is installed and the account authorized. If the Project owner is an Organization, replace the example personal owner with the verified Organization name.

```powershell
gh --version
gh auth status
gh repo view mert494/student-information-system
gh issue list --repo mert494/student-information-system --state all --limit 100
gh pr list --repo mert494/student-information-system --state all --limit 100
gh project list --owner mert494
```

Once the Project number is known, use `gh project view <NUMBER> --owner <OWNER>` and `gh project item-list <NUMBER> --owner <OWNER>`; do not run them until `<...>` placeholders have been replaced with actual values. Pagination/limits mean the first results must not be assumed to include all records. Do not interpret an access error as “no board exists”. Verify account permissions needed for Project reading against CLI help; expanding permissions and remote changes are outside this preparation's scope.

Do not execute commands here that change Issues, Projects, releases, branch protection or other remote resources. Explicit push approval is required, followed by separate approval to open a PR. If `develop` does not exist, ask the user for the PR target.

## Sources

- [GitHub Projects single-select fields](https://docs.github.com/en/issues/planning-and-tracking-with-projects/understanding-fields/about-single-select-fields)
- [GitHub Projects built-in automations](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/using-the-built-in-automations)
- [GitHub CLI project commands](https://cli.github.com/manual/gh_project)
