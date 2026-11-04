# Arda — architecture and technical lead execution package

Status: Task guide for team approval; not a completed technical deliverable. Follow the [main guide](00_Team_Overview.md) and [RACI](../../RACI_Matrix.md). Related work: S1-02, S1-03, S1-04, S1-05, S1-13, S1-14.

## A. Purpose of the role

Translate product needs into consistent system responsibilities and a verifiable API contract; preserve the rationale for technical decisions and review quality. Sprint 1 does not mean a working backend or detailed architecture package has been delivered.

## B. Sprint 1 responsibilities

1. Clarify scope, actors and System Boundary with Nurefşan; serve as primary owner of the Boundary section.
2. Distinguish approved/proposed operations for students, academic staff and administrators; prepare a draft OpenAPI YAML from them.
3. Design request/response models, representative success/error responses and authorization needs; validate the contract.
4. Support Nurefşan on feasibility, data/technology assumptions and license selection; record decisions.
5. Resolve validation findings with Ahmet; independently review technical PRs and add contribution evidence.

Detailed C4/UML, architecture documentation and expanded database design are Sprint 2 preparation. The MVP belongs to Sprint 3; full implementation is not expected in Sprint 1.

## C. Step-by-step implementation

1. Use Git and a Markdown editor to follow the [shared workflow](00_Team_Overview.md); inspect README, AGENTS, the Product Backlog, RACI and existing API files. If `develop` is missing, do not create it automatically; wait for a base decision.
2. Obtain from Nurefşan which roles can access which data through which operations. Example resource candidates: user/session, student, course, registration and grade. All await scope approval; do not assume screens/features map one-to-one to API resources.
3. In the shared vision/boundary file, edit only the agreed Boundary sections: actors, external systems, responsibilities, in/out-of-scope features, data and trust boundaries. Leave unknown actual integrations as `[TODO]`.
4. Select and record an OpenAPI version based on tool compatibility; for example, 3.1.0 is a candidate, not an agreed version. Establish version, `info`, proposed server information, `paths` and reusable `components` in YAML. Do not present an unknown live URL as an actual server.
5. For each in-scope operation, specify HTTP method/path, unique `operationId`, parameters, body where needed, required fields/types/constraints and response schemas. Select listing, individual-record and modification operations according to requirements; do not assume all CRUD operations.
6. Model appropriate success statuses and relevant errors such as 400/401/403/404/409. If the session/role mechanism is undecided, do not present JWT/OAuth as a final decision; state the draft security assumption and open question. Examples must match schemas and contain entirely dummy data.
7. Jointly record requirement/PB ID → `operationId` mapping in Nurefşan's Product Backlog. Add license and architectural rationale to the existing Decision Log with Azra; do not create a separate, duplicate decision log.
8. Use a validator compatible with the selected OpenAPI version to check parsing, `$ref`, schemas and example consistency. Ahmet repeats the checks with the same version/rules. Include results, command, tool version, file commit and open findings in the PR.
9. Show the diff; obtain separate user approval for commit, push and PR. Nurefşan reviews scope and Ahmet validation. Merging requires separate approval.

Tool suggestion: If Redocly CLI is already installed locally with approval, run `redocly lint api/openapi.yaml` from the repository root. If not installed, do not download dependencies without permission; submit tool selection/installation for approval. Distinguish lint warnings from specification errors; validator success does not prove requirements are correct. Do not present the results as tests against a running API.

## D. Files to produce or update

Paths are proposals; reuse an equivalent existing file. Requirements concern content; file names/Markdown format other than YAML are team preferences.

| File / format / location | Required content | Requirement status | Completion criterion |
| --- | --- | --- | --- |
| `api/openapi.yaml` — YAML, new proposal | Version/info, resources/paths/HTTP operations, parameters/body, request/response schemas, representative success/error responses, security definition if applicable | OpenAPI YAML required | Selected-version validator result recorded; scope mapped; errors resolved and draft limitations explicit |
| `docs/System_Vision_and_Boundary.md` — Markdown, shared new proposal | Boundary: context, external interactions, system responsibilities, in/out of scope, constraints/assumptions | Boundary content required | Consistent with Nurefşan's Vision section; both section owners have reviewed |
| `docs/Sprint1_Process_Records.md` — existing Markdown | Technical decision, alternatives, rationale and approval status in Decision Log | Process evidence support; no separate technical decision file proposed | Coordinated with Azra; drafts not recorded as decisions |

## E. Prompt to paste into Codex

```text
I am Arda, the Lead Software Architect and Technical Lead of the BM321 SIS team.
First inspect git status/branch/remote, README, all applicable AGENTS.md files,
docs/Git_Workflow.md, docs/RACI_Matrix.md, docs/Initial_Backlog_Draft.md and existing
proposal/vision/API files. Read docs/team-guides/sprint1/01_Arda_Architecture_Lead.md.
Summarize the current work; do not touch another person's uncommitted changes.
If equivalent files do not exist, prepare a draft api/openapi.yaml and the Boundary
section of docs/System_Vision_and_Boundary.md shared with Nurefşan.
Do not take over Vision/proposal ownership; first clarify section boundaries in the
shared file. Map student/academic staff/administrator needs, resources, HTTP operations,
request/response schemas and representative success/error responses to scope.
Label unapproved role/technology/security decisions as proposals. Mark missing information
[TODO]; use comments/extensions rather than placeholders that would produce invalid YAML.
Specify the OpenAPI version and validator; validate with installed tools and request
permission if dependencies need installation. Do not mark unrun checks as passed.
Coordinate technical decisions with Azra in the existing Decision Log; separate C4/UML
as Sprint 2 preparation. Do not delete or modify another person's files without
permission or perform refactoring. Present local files and check results. Wait for
approval to create/switch branches or commit; obtain separate explicit approval for
push, PR and merge. Do not commit directly to main/develop or force push.
If develop does not exist, ask the user for the base/target.
```

## F. GitHub workflow

Example branch: `docs/arda-sprint1-openapi` (adapt with the actual Issue ID). Example commit: `docs(api): draft sprint 1 OpenAPI contract`. Add only an actual `Refs #...` in the body. In the [PR template](../../../.github/pull_request_template.md), state the Issue, changed resources, version/validator result and open decisions. If an approved `develop` target is unavailable, ask for the target. Nurefşan and Ahmet can review; do not be the sole approver of your own PR. Follow the [shared approval sequence](00_Team_Overview.md) at every Git stage.

## G. Collaboration

Nurefşan: roles/scope and domain rules; Barış: local setup requirements for selected tools; Ahmet: validator and negative scenarios; Azra: decision records; Mert: Issues, dependencies and submission evidence. Do not edit the same section of the shared vision file concurrently; use separate sections/diffs or sequential PRs.

## H. Submission checklist

- [ ] Boundary and role permissions reviewed with Nurefşan.
- [ ] OpenAPI YAML, schemas, success/error examples and references consistent.
- [ ] Validator version/command, results and requirements mapping recorded.
- [ ] Technical proposals distinguished from approved decisions.
- [ ] Independent review and actual Issue/PR/commit links added.
- [ ] Detailed C4/UML or backend implementation not presented as completed Sprint 1 work.

Technical sources: [OpenAPI 3.1.0 specification](https://spec.openapis.org/oas/v3.1.0), [Redocly lint command](https://redocly.com/docs/cli/commands/lint). These links do not automatically settle version selection.
