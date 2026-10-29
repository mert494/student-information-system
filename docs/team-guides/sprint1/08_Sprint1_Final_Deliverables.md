# Sprint 1 — final deliverable and submission mapping

[Return to the main guide](00_Team_Overview.md). This document is a **preparation and review guide**, not a new completion record. Record actual status and evidence in the existing [Sprint1_Submission_Checklist.md](../../Sprint1_Submission_Checklist.md); do not maintain two separate status tables.

## Interpreting requirements

Sprint 1 is due at the end of Week 2 and accounts for 15% of the total grade. Five specification items are expanded into six headings in Teams. Required content is below. OpenAPI must be YAML; other file names and Markdown source format are proposals. No PDF/Word requirement has been verified. Detailed Teams Files instructions and exact submission format/deadline [TODO].

## Content and acceptance checks for the six headings

| Deliverable / proposed owner | Content to check | File / evidence location |
| --- | --- | --- |
| Project Proposal and Problem Definition — Nurefşan | Problem and supporting evidence, stakeholder analysis, solution/expected outcomes, feasibility/initial scope, assumptions/risks, open-source license and rationale | New proposal `docs/Project_Proposal.md`; existing `LICENSE`; review/decision link |
| System Vision and Boundary — Vision Nurefşan, Boundary Arda | Purpose/target users, system responsibilities/core functions, context/external interactions, in/out of scope, constraints/assumptions | New shared proposal `docs/System_Vision_and_Boundary.md`; section owners and review |
| OpenAPI Draft — Arda | Valid OpenAPI YAML; resources/paths/HTTP operations; request/response schemas; representative success/error responses; alignment with the proposed system | New proposal `api/openapi.yaml`; tool/version/command and actual validation result |
| Team Roles and RACI — Azra, supported by Mert | All six people and product/process/architecture/quality/DevOps/implementation responsibilities; R/A/C/I and one A per row; approval status | Existing [RACI](../../RACI_Matrix.md) and [CSV](../../RACI_Matrix.csv) |
| GitHub Repository and Git-Flow — Barış infrastructure, Mert process | Organized repository/Organization and access; main/develop/task branches; actual Issues/PRs; independent review/protection; preserved contribution history | [Git_Workflow](../../Git_Workflow.md), [Projects guide](../../GitHub_Projects_Setup.md), actual GitHub URLs |
| Initial Product Backlog — Nurefşan, supported by Mert | Prioritized epics/features/stories, Acceptance Criteria, initial team estimates, dependencies and owners; example/approved distinction | Existing [Product Backlog](../../Initial_Backlog_Draft.md); approval record and actual Issue/board mapping |

Listing a proposed file path in a guide does not mean the deliverable is ready if the file does not yet exist. Reuse an equivalent existing file; do not create unnecessary copies just to change its name.

## Supporting documents and actual process evidence

- Ahmet's `docs/Sprint1_Quality_Report.md` is a proposed quality role output in this work package; it is not claimed as an additional official course deliverable beyond the six headings.
- Barış's `docs/Repository_Setup.md` is proposed setup/infrastructure evidence; if no application exists yet, it must say so explicitly.
- Complete existing [process records](../../Sprint1_Process_Records.md) with actual Planning/Stand-up/impediment/decision/Review/Retrospective and action data; template existence does not prove the event occurred.
- These nine team guides and existing Issue/PR templates support work; they do not replace members' own deliverables/contributions.

## Submission package links

Mert completes the following fields in the existing checklist; do not create another empty submission table here:

1. Team number, project name, all six members' names/roles and actual GitHub usernames.
2. GitHub repository and Organization/board URLs if applicable; access verification.
3. Actual document links for all six headings and a direct link to the OpenAPI YAML file.
4. Actual Issue, PR/review, commit SHA/URL mappings for each deliverable and person; preserved repository history.
5. Sprint 1 release/tag name, URL and the reviewed commit SHA it points to. Example name `sprint1-v0.1.0` is only a proposal; do not create tags automatically.
6. Course-designated submission channel, exact date/time and receipt evidence.

## Final review sequence

1. Authors complete their files and scope mappings; clarify assumption/approval status.
2. Ahmet checks file existence, content, Markdown/local links, RACI parity and OpenAPI validation against actual versions.
3. Return findings to owners; rerun affected checks after fix commits/PRs.
4. Perform required merges after independent review and separate user approval. If `develop` does not exist, clarify the target with the user; do not automatically select `main`.
5. Barış prepares release/tag on the correct commit only with explicit permission; Mert verifies all contribution/submission links. Also check whether new process documents have been integrated into the default branch.
6. Mert compares against the actual Teams Files instructions and completes submission through the course-designated channel.

## Open decisions and gaps

Exact schedule/submission format/team number; all six accounts' access; Organization; `develop` base and PR target; Mert–Azra division/RACI; scope and role permissions; license rationale; OpenAPI version/tool; Product Backlog estimate/owner approvals; merge/protection policy; release/tag name [TODO].

Detailed SRS/C4/UML belong to Sprint 2, MVP and CI/50% unit-test coverage to Sprint 3, and single-command Docker startup and final quality/demo work to later submissions. Do not produce evidence of application/tests/deployment that have not occurred in Sprint 1.
