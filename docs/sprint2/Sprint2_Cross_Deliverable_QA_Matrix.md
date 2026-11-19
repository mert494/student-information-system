# Sprint 2 Cross-Deliverable QA Matrix - Initial Draft

Related Issue: [#38 - S2-13][I38]. Prepared by Mert (`mert494`) as a coordination draft, not Ahmet's completed or signed QA report. Deadline: 24 November 2026, as supplied by Mert; official assignment timezone/format still require confirmation.

**Status: INITIAL / INCOMPLETE. No final deliverable acceptance, owner assignment, PO approval, team estimate, runtime test, release or submission is established by this matrix. Issue #38 remains open.**

## Snapshot and evidence boundaries

- Evidence snapshot: 19 November 2026, 22:30 Europe/Istanbul (19:30 UTC). GitHub states are observations at that time, not permanent facts.
- Integration baseline: develop `ee5c64b0730551e8d5a1699a209fdfaef1cb380f`; this draft branch starts from that exact commit.
- [PR #43][PR43] is open at `a9b6b4819ca18146e4e2b72346405283dbdd0c60`: SRS/backlog source drafts.
- [PR #45][PR45] is open at `63ca3e8c8efc57637185808a6f1981a7561c09d5`: NFR/quality source draft.
- [PR #44][PR44] is open at `479e68b96def3f348c737fcb7537a616abd26e2c`: process/contribution source draft.
- Source PR files were read through GitHub at the above SHAs; they are not assumed to exist on develop. Main, Sprint 1 records, colleague files and branches are not edited.
- [Traceability][TRACE] and [OpenAPI][API] were read at the pinned baseline. The traceability document's 16 November inventory is historical; its old 'no output' statements are not current evidence that drafts or external work do not exist.
- Current inspected architecture evidence: develop tree, remote branch/PR inventory and #34/#35/#36 comments. No new S2 source/export was supplied there. External model files are NOT VERIFIED, not declared nonexistent.
- Figma links/messages were inspected. A read-only connector session attempt failed because the connector required edit access; account diagnostic showed a View seat. No file content, interaction or intended-audience permission was verified. No access escalation or design edit was performed. This does not establish that browser view access fails.
- Methods below are static source/record checks unless explicitly marked otherwise. No live API, product, performance, security, accessibility, prototype interaction or UML/C4 semantic test is claimed. The independent reviewer has not yet verified this matrix; all row rechecks are pending.

## Result and severity conventions

- **PASS:** the narrowly stated static observation was actually checked; never whole-deliverable, PO, implementation or submission acceptance.
- **FAIL:** an observed document/record defect at the cited version, not an asserted running-product defect.
- **PENDING:** missing input, decision, artifact or owner evidence prevents acceptance/recheck.
- **NOT VERIFIED:** the specified check has not been performed or access prevented inspection; no quality result inferred.
- Severity: BLOCKER (verified issue preventing even draft review), MAJOR (material evidence/consistency gap), MINOR (limited documentation gap), INFORMATIONAL (bounded observation). Missing mandatory architecture evidence blocks final package acceptance, not publication of this draft. No BLOCKER is asserted in this first snapshot.
- Responsible Owner is a follow-up route based on existing proposals/role expertise, not a new assignment. Azra's Figma acceptance is supported by [actual comments][F32A]; other unconfirmed assignments/estimates remain Pending. No colleague decision is made here.

## Snapshot counts

| Result | Rows |
| --- | ---: |
| PASS | 11 |
| FAIL | 11 |
| PENDING | 15 |
| NOT VERIFIED | 3 |
| Total | 40 |

| Severity | Rows |
| --- | ---: |
| BLOCKER | 0 |
| MAJOR | 26 |
| MINOR | 3 |
| INFORMATIONAL | 11 |

Counts describe matrix rows, not independent defects, a readiness percentage, test coverage or a completion score. Related rows can refer to the same source finding.

## Detailed SRS and refined backlog

| ID | Artifact / Deliverable | Source PR / Commit / Version | Requirement / Acceptance Criterion | Verification Method | Result | Severity | Finding / Evidence | Responsible Owner | Recheck Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| S-01 | SRS / backlog | [SRS], [BACKLOG] @ a9b6b48 | FR-01..07 and PB-01..07 map in both directions (#38, #29) | Read seven FR/PB IDs and forward/reverse tables | PASS | INFORMATIONAL | Seven ID pairs exist; this does not establish complete AC or implementation coverage. | Nurefşan; Ahmet recheck | Static observation recorded; independent recheck pending |
| S-02 | Hierarchy / tasks / decisions | [BACKLOG] @ a9b6b48; [R43] MAJOR 1 | Explicit Epic > Feature > PB > Task, dependencies and OQ links | Read hierarchy and T-01..09 register | FAIL | MAJOR | Task dependencies and parent/OQ references remain incomplete; T-09 is absent from the hierarchy. Keep unconfirmed NFR applicability Pending. | Nurefşan; team for estimates | Open; owner evidence and independent recheck pending |
| S-03 | SRS cross-document links | [BACKLOG] @ a9b6b48; [R43] MAJOR 4 | Backlog links resolve to actual SRS file and headings | Compare seven targets with PR #43 tree | FAIL | MAJOR | Lines 54, 68, 83, 98, 114, 128, 141 point to absent SRS_Draft_Revision1.md. Actual file is SRS_Draft.md; anchors also need checking. | Nurefşan | Open; owner evidence and independent recheck pending |
| S-04 | Backlog Markdown / names | [BACKLOG] @ a9b6b48; [R43] MINOR | Readable tables and consistent identifiers/names | Count table cells; compare Epic/NFR names | FAIL | MINOR | Separator lines 13, 33, 177 have 6/7/5 cells for 7/9/6-column tables. Enrollment/Course Enrollment and abbreviated NFR IDs remain inconsistent. | Nurefşan | Open; owner evidence and independent recheck pending |
| S-05 | SRS / OpenAPI comparison | [SRS], [BACKLOG] @ a9b6b48; [API]; [R43] MAJOR 2 | Record concrete method/path/operationId/schema, FR/PB/OQ and decision status | Compare generic alignment topics with actual API text | FAIL | MAJOR | Topic lists do not yet record the concrete observations in A-01..A-04. Recording an observation is not authorizing a contract change. | Nurefşan + Arda | Open; owner evidence and independent recheck pending |
| S-06 | FR-03 / FR-04 update AC | [SRS] lines 88-102; [BACKLOG]; [R43] MAJOR 3 | Testable missing-record, omitted/null, immutable/unknown and duplicate-update scenarios | Static scenario and AC comparison | FAIL | MAJOR | Not-found and allowlist were added, but omitted vs null, duplicate-update vs unchanged-value cases and precise expected outcomes remain incomplete; unresolved policies need OQ links. | Nurefşan; Arda contract mapping | Open; owner evidence and independent recheck pending |
| S-07 | FR-07 empty/error states | [SRS] lines 120-126; [BACKLOG] PB-07 | Successful zero results differ from loading/API failure | Read revised precondition, alternate path and AC | PASS | INFORMATIONAL | Draft explicitly limits empty-state text to a successful zero-results response and treats errors separately; no live UI test performed. | Nurefşan; Azra downstream UX | Static observation recorded; independent recheck pending |
| S-08 | Role / business / data decisions | [SRS] OQ-01..11; [API]; [I38] | Permissions, enrollment, grades and field rules supported by owner decisions | Inspect open-decision and approval trackers | PENDING | MAJOR | Required fields, permission matrix, enrollment/grading policies and owner approvals remain open. Proposed values are not approved facts. | PO Nurefşan + Arda + team | Open; owner evidence and independent recheck pending |

## SRS / API consistency

| ID | Artifact / Deliverable | Source PR / Commit / Version | Requirement / Acceptance Criterion | Verification Method | Result | Severity | Finding / Evidence | Responsible Owner | Recheck Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A-01 | Authentication / student fields | [API] createSession, SessionResponse, bearerAuth, StudentInput; [SRS] | FR-01/PB-01 OQ-02 and FR-03/PB-03 OQ-03 aligned | Static schema / requirement comparison; owner decision not verified | PENDING | MAJOR | API returns sessionId and proposes JWT bearer; their relationship/logout is unresolved. SRS proposes first/last name while API has fullName; requiredness/types are unresolved. | Arda + Nurefşan | Open; owner evidence and independent recheck pending |
| A-02 | Enrollment identifiers / errors | [API] createRegistration / RegistrationInput; [SRS] FR-05 | FR-05/PB-05, BR-01..05 and OQ-05/06/08 aligned | Read request fields, errors and SRS rules | PENDING | MAJOR | courseId, term and status exist; term/status semantics and offering/identity mapping remain open. Generic 409 is not evidence of every business rule or no-side-effect behavior. | Arda + Nurefşan | Open; owner evidence and independent recheck pending |
| A-03 | Published-grade response example | [API] listMyPublishedGrades; [SRS] FR-07; [TRACE] G-08 | Only own published grades (FR-07/PB-07) | Read GET /grades success example | FAIL | MAJOR | Example includes published:false despite published-only intent. Static mismatch only; no running-service disclosure is asserted. | Arda; Nurefşan publication decision | Open; owner evidence and independent recheck pending |
| A-04 | Instructor later grade retrieval | [API] recordGrade; [SRS] FR-06; [TRACE] G-07 | Saved grade retrievable later by authorized Instructor | Compare operation inventory with FR-06/PB-06 | PENDING | MAJOR | PUT returns Grade, but a later instructor read/list flow is not explicitly mapped. Student listMyPublishedGrades must not be assumed to cover it; no new endpoint is selected here. | Arda + Nurefşan | Open; owner evidence and independent recheck pending |

## NFR and quality measures

| ID | Artifact / Deliverable | Source PR / Commit / Version | Requirement / Acceptance Criterion | Verification Method | Result | Severity | Finding / Evidence | Responsible Owner | Recheck Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| N-01 | NFR / quality-measure draft structure | [NFR] @ 63ca3e8 | Requirements have scenario and metric/method/pass-fail/stage fields | Read requirement and measure tables | PASS | INFORMATIONAL | Nine SRS NFR IDs are retained and nine additions are marked QA proposals. Proposed/Open and S2-doc/Impl distinctions exist; no measurement result is claimed. | Ahmet; independent reviewer | Static observation recorded; independent recheck pending |
| N-02 | Protected operation coverage | [NFR] NFR-SEC-01; [API]; [R45] MAJOR 1 | Correct operation-level security / role / response coverage | Compare 0 of 12 target with API inventory | FAIL | MAJOR | 12 is total operations, not the protected subset. createSession has security: []; deleteCurrentSession has no 403 response. Need per-operation matrix; do not require 401+403 on every operation. | Ahmet; Arda security review | Open; owner evidence and independent recheck pending |
| N-03 | Accessibility acceptance scope | [NFR] NFR-ACCESS-01; [R45] MAJOR 2 | Claimed WCAG target consistent with verification coverage | Compare target, pass/fail rule and stages | FAIL | MAJOR | Contrast plus no critical/serious axe findings does not cover the claimed full WCAG 2.2 AA target. Separate prototype checks from implemented UI/manual checks; no conformance decision here. | Ahmet; Arda/team and prototype owner | Open; owner evidence and independent recheck pending |
| N-04 | Targets / verification evidence | [NFR] sections 4-7; [R45] | PO priority/target acceptance and technical feasibility evidenced | Inspect Proposed/Open targets and review tracker | PENDING | MAJOR | No target approval or real performance/security/usability measurement is established. Open targets/missing methods cannot be unconditionally accepted; future Impl tests are not S2 results. | Ahmet; Nurefşan decisions; Arda feasibility | Open; owner evidence and independent recheck pending |
| N-05 | SRS / NFR / backlog alignment | [SRS], [BACKLOG] @ a9b6b48; [NFR] @ 63ca3e8 | Accepted additional NFRs linked bidirectionally; full IDs used | Compare declared ID origins and trace tables | PENDING | MINOR | Nine extra NFRs await owner acceptance before adding scope. Reconcile full IDs, open decisions, prototype availability and assignment tracker without inventing approval. | Nurefşan + Ahmet; Azra UX inputs | Open; owner evidence and independent recheck pending |

## Figma and user flows

| ID | Artifact / Deliverable | Source PR / Commit / Version | Requirement / Acceptance Criterion | Verification Method | Result | Severity | Finding / Evidence | Responsible Owner | Recheck Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F-01 | Responsibility and URL declarations | [F32A], [F32S], [F33S] | Real acceptance and design/prototype sharing evidence | Read comments authored by azrayy | PASS | INFORMATIONAL | Acceptance and supplied file/node URLs are recorded. This proves the messages, not prototype quality, ownership history or reviewer permissions. | Azra; Mert coordination | Static observation recorded; independent recheck pending |
| F-02 | Independent file access | [FIGMA-D], [FIGMA-P], node 1:1681; file version unknown | Reviewer can inspect exact intended version/audience | Figma connector create_session attempted; account access diagnostic | NOT VERIFIED | MAJOR | 2026-11-19 connector refused session: edit access unavailable; diagnostic showed View seat. This tool limitation does not prove missing/invalid file or lack of ordinary browser view access. No design content was read. | Azra sharing support; independent reviewer | Open; owner evidence and independent recheck pending |
| F-03 | Role / flow / error coverage | [F32S], [F33S]; [SRS] FR-01..07 | Selected roles/flows map to FR/PB, permissions and success/error/empty paths | Required walkthrough and trace inspection not performed | NOT VERIFIED | MAJOR | No independent role-flow coverage check recorded. Confirm selected scope with PO; do not infer an Administrators dashboard or completed user-flow diagrams from a URL. | Azra; Nurefşan product validation; Ahmet QA | Open; owner evidence and independent recheck pending |
| F-04 | Click-through prototype | [FIGMA-P]; no frozen version supplied | Primary journeys navigate end to end; loading errors differ from empty state | Required interactive test not performed | NOT VERIFIED | MAJOR | No click-through or interaction result is available from this review. URL format/existence in a comment is not a working-prototype test. | Azra; independent reviewer | Open; owner evidence and independent recheck pending |
| F-05 | Version ownership / editable source / exports | [PROCESS] verification table; [I32], [I33] | Version owner, reviewer access and agreed readable exports evidenced | Inspect supplied GitHub declarations only | PENDING | MAJOR | File key/node ID is not a frozen version or ownership proof. Independent access and agreed export integrity still need evidence; no mandatory PDF format is inferred. | Azra; Mert submission coordination | Open; owner evidence and independent recheck pending |

## Architecture, C4, UML, database and interfaces

| ID | Artifact / Deliverable | Source PR / Commit / Version | Requirement / Acceptance Criterion | Verification Method | Result | Severity | Finding / Evidence | Responsible Owner | Recheck Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AR-01 | Architecture rationale document | [I34]; [TREE] develop ee5c64b | Versioned architecture choices, responsibilities and NFR trade-offs | Inspect develop tree, current branch/PR list and #34 comments | PENDING | MAJOR | No new S2 architecture artifact/version found in inspected sources. Historical Sprint 1 Boundary is input, not completed S2 design. External work remains unknown. | Arda (proposed lead); independent QA | Open; owner evidence and independent recheck pending |
| AR-02 | C4 views and sources | [I35]; [TREE] | Agreed C4 levels, boundaries, labeled relationships and readable exports | Repository/evidence inventory; diagram review not performed | PENDING | MAJOR | No S2 C4 source/export supplied in inspected evidence. Sprint1_System_Context.svg does not establish S2 completion; no additional C4 level is mandated. | Arda (proposed lead); team scope confirmation | Open; owner evidence and independent recheck pending |
| AR-03 | UML views / scenarios | [I36]; [SRS] FR/PB scenarios | Agreed structural/behavioral diagrams consistent with requirements and interfaces | Repository/evidence inventory; UML semantic check not performed | PENDING | MAJOR | No S2 UML source/export/version available to review. Type selection, relationships, multiplicities and scenario messages await owner evidence. | Arda (proposed lead); independent QA | Open; owner evidence and independent recheck pending |
| AR-04 | Proposed database schema | [I34], [I36]; [SRS] section 6; [API] schemas | Entities, keys, relationships, cardinality and basic constraints explicit | Compare candidate data lists to required schema evidence | PENDING | MAJOR | Candidate SRS fields and OpenAPI shapes do not establish an approved relational/domain schema. Student/course/offering/enrollment/grade relationships, uniqueness and lifecycle remain unresolved. | Arda + Nurefşan | Open; owner evidence and independent recheck pending |
| AR-05 | Component / interface / NFR mappings | [I34]; [API]; [NFR] | Responsibilities, provided/consumed interfaces, dependencies and API/data/security behavior linked | Required architecture-to-contract comparison not yet possible | PENDING | MAJOR | No owner-supplied component/interface map found. Link actual operations, inputs/outputs/errors/auth and relevant NFRs after architecture versions exist. | Arda; Ahmet consistency review | Open; owner evidence and independent recheck pending |

## Process / review evidence

| ID | Artifact / Deliverable | Source PR / Commit / Version | Requirement / Acceptance Criterion | Verification Method | Result | Severity | Finding / Evidence | Responsible Owner | Recheck Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P-01 | Six-member inventory structure | [PROCESS] @ 479e68b | All six member records present; unknown evidence stays Pending | Read member list and status disclaimers | PASS | INFORMATIONAL | All six accounts/names represented; open PRs labeled draft/in review; Arda S2 evidence remains Pending. Structure is not complete contribution acceptance. | Azra; Mert coordination | Static observation recorded; independent recheck pending |
| P-02 | Review-state accuracy | [PROCESS] line 20; [R44] | COMMENTED is not REQUEST_CHANGES | Compare log text with GitHub review 5981223436 | FAIL | MAJOR | COMMENTED (Changes Requested) is inaccurate as a formal state; actual review is COMMENTED. Record open findings separately. | Azra | Open; owner evidence and independent recheck pending |
| P-03 | Merge attribution | [PROCESS] line 40; [M42] | Actual author and merger distinguished | Read GitHub PR #42 merged_by and log wording | FAIL | MAJOR | Barış authored/revised; mert494 merged. The contribution line currently attributes merge to Barış despite the event row naming Mert. | Azra | Open; owner evidence and independent recheck pending |
| P-04 | Existing review history | [PROCESS] lines 32/38; [R44] MAJOR 3; [AZ24], [AZ25], [AZ41], [AH24], [AH25], [AH41] | Include real review states/commits, including dismissed history | Compare current review records with Pending placeholders | FAIL | MAJOR | Azra/Ahmet review evidence still missing; Mert COMMENTED reviews need direct links. Azra #42 review is DISMISSED, not a current approval; #41 merge event and timezone also need recording. | Azra; members confirm their evidence | Open; owner evidence and independent recheck pending |
| P-05 | Peer-assessment source / timing | [PROCESS] lines 63-69; [I37]; [R44] MINOR | Official method/source verified or explicitly Pending; no invented window/results | Read tracking fields and limitations | PENDING | MINOR | Fields/results are Pending, but 'until official submission window' has no supplied official source. Method/form/timing stay Pending; no assessment result is asserted. | Azra + Mert; course source required | Open; owner evidence and independent recheck pending |

## Six-member contribution evidence

| ID | Artifact / Deliverable | Source PR / Commit / Version | Requirement / Acceptance Criterion | Verification Method | Result | Severity | Finding / Evidence | Responsible Owner | Recheck Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C-01 | Mert / mert494 | [M24], [M25], [M41], [M42], [R43], [R44], [R45] | Real author/review/merge evidence distinguished from PO acceptance | Read GitHub author, head and review/merge records | PASS | INFORMATIONAL | Authored planning/traceability/checker; merged #41/#42; COMMENTED on #43/#44/#45. Current matrix is Mert's coordination draft, not independent approval of his work. | Mert; independent reviewer | Static observation recorded; independent recheck pending |
| C-02 | Nurefşan / nsnkcc | [SRS], [BACKLOG]; [PR43] @ a9b6b48 | Draft authorship / revisions evidenced | Read PR author and commit/version records | PASS | INFORMATIONAL | f27e169 and a9b6b48 are requirements/backlog contributions; PR open and owner/QA acceptance pending. Do not count submission as accepted delivery. | Nurefşan; Azra evidence record | Static observation recorded; independent recheck pending |
| C-03 | Ahmet / ahmetserdar41 | [NFR]; [PR45] @ 63ca3e8; [AH24], [AH25], [AH41] | Draft writing and review contributions evidenced | Read PR author and review submissions | PASS | INFORMATIONAL | NFR draft and reviews exist; Mert review on #45 is COMMENTED. Ahmet cannot independently accept his own NFR measures. | Ahmet; Arda/another independent NFR reviewer | Static observation recorded; independent recheck pending |
| C-04 | Barış / baryyss-001 | [M42], head 6a6446b3b957633bb3da902644308871cbb1b45c | Release-preparation authorship and fixes evidenced | Read five author commits and merged PR metadata | PASS | INFORMATIONAL | Draft preparation contribution is real; merge performed by Mert. No actual S2 tag/release is evidenced by this document. | Barış; Azra record accuracy | Static observation recorded; independent recheck pending |
| C-05 | Azra / azrayy | [PR44] @ 479e68b; [F32A], [F32S], [F33S], [AZ24], [AZ25], [AZ41] | Process authorship, acceptance messages and reviews evidenced | Read GitHub authors/messages/review records | PASS | INFORMATIONAL | Process revisions, acceptance/sharing messages and PR reviews are real. Figma version ownership/content is still unverified; historical dismissed #42 review is not current approval. | Azra; independent reviewer | Static observation recorded; independent recheck pending |
| C-06 | Arda / ardaberkkara1 | [I34], [I35], [I36]; [BRANCHES] | Real S2 architecture/model ownership evidence | Inspect current sources; do not infer from assignment | PENDING | MAJOR | No new S2 artifact/PR found in inspected sources; historical #8/#19 are Sprint 1 only. Ask for actual source/export/version links; do not claim no work exists elsewhere. | Arda; Mert follow-up | Open; owner evidence and independent recheck pending |

## Integration and final QA boundary

| ID | Artifact / Deliverable | Source PR / Commit / Version | Requirement / Acceptance Criterion | Verification Method | Result | Severity | Finding / Evidence | Responsible Owner | Recheck Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| I-01 | Supporting tooling / release preparation | [M41], [M42] | Keep support merges separate from final artifact acceptance | Read merged states and commit parents | PASS | INFORMATIONAL | #41 merged ee5c64b; #42 merged 98f9b5a, by mert494. They do not complete #38/#39/#40 or authorize release/submission. | Mert + Barış | Static observation recorded; independent recheck pending |
| I-02 | Final cross-deliverable recheck | [I38]; [CHECKLIST] | Actual accepted versions consistent across SRS, NFR, UX, API, C4/UML, schema and contributions | End-to-end package/document QA not yet completed | PENDING | MAJOR | Source PRs are open; no integrated accepted four-output package or completed owner rechecks exists in this matrix. No runtime/product tests or final Teams acceptance claimed. | Ahmet proposed QA lead; independent reviewer for own work | Open; owner evidence and independent recheck pending |

## Prior review findings and exact versions

| Source review | Reviewed source | Matrix follow-up |
| --- | --- | --- |
| [Mert COMMENTED on #43][R43] | `a9b6b4819ca18146e4e2b72346405283dbdd0c60` | S-02..S-06; A-01..A-04. FR-07 correction is a bounded static PASS (S-07), not prototype acceptance. |
| [Mert COMMENTED on #45][R45] | `63ca3e8c8efc57637185808a6f1981a7561c09d5` | N-02..N-05. Proposed targets remain proposals; no REQUEST_CHANGES state or measured conformance is invented. |
| [Mert COMMENTED on #44][R44] | `479e68b96def3f348c737fcb7537a616abd26e2c` | P-02..P-05. Formal state is COMMENTED, not REQUEST_CHANGES. |
| Azra review on #42 | [Historical review](https://github.com/mert494/student-information-system/pull/42#pullrequestreview-5965490511), `f20aa7afe57e44938e78a6d82b113d0e95adae12` | DISMISSED; contribution history only, not current approval. |
| Mert approval on #42 | [APPROVED](https://github.com/mert494/student-information-system/pull/42#pullrequestreview-5965667751), `6a6446b3b957633bb3da902644308871cbb1b45c` | Draft release-preparation scope only; subsequent merge `98f9b5ac41d24fa1139492c52a043e5773f8a6b4` by mert494. |

GitHub review submission time, commit time and merge time are different events. Preserve original UTC timestamps and optionally show Europe/Istanbul alongside them. #42 opened 18 November 2026 22:51:36 +03:00 and merged 19 November 00:47:44 +03:00; #41 merged 19 November 21:56:20 +03:00 as `ee5c64b0730551e8d5a1699a209fdfaef1cb380f`. The #44 source currently combines some events and omits the explicit #41 merge event; no timeline completion is claimed.

## Recheck and independent-review handoff

1. Keep row IDs stable. The artifact owner supplies the fix commit or exact Figma/model version, response to the finding and any real decision evidence. Do not silently replace old source SHAs or mark a row closed because a PR is open/merged.
2. On a source change, compare old vs new versions, recheck affected rows and their downstream FR/PB/NFR/UX/API/model/data relationships. Add reviewer/date/method/expected-vs-observed evidence. A prior PASS does not carry to a different artifact version automatically.
3. Suggested independent reviewer for this Mert-authored matrix: Ahmet, subject to availability/acceptance. Ahmet's authored NFR and measurement rows require Arda or another independent reviewer; Ahmet must not accept his own work. PO decisions remain with Nurefşan and technical decisions with Arda/team.
4. For architecture, obtain actual editable sources and readable exports before semantic review. For Figma, confirm intended reviewer account/audience, exact version, roles, paths, error/empty states and ownership/export evidence; URL presence alone cannot close F-02..F-05.
5. Recheck individual contributions from author/commit/review/ownership evidence. Assignment alone is insufficient. Preserve DISMISSED history; do not convert COMMENTED into APPROVED or REQUEST_CHANGES.
6. Final #38 acceptance requires actual four-output versions, owner corrections and independent rechecks against its acceptance criteria. This coordination draft neither performs those checks nor closes #38. #39/#40 release and Teams steps remain separately authorized and Pending.

| Row IDs / source finding | Owner fix version / response | Independent reviewer and date | Recheck method / result / evidence | Closure |
| --- | --- | --- | --- | --- |
| S-02..S-06 / #43 review | Pending owner commit | Pending | Pending | Open |
| A-01..A-04 / API decisions | Pending owner decisions/contract evidence | Pending | Pending | Open |
| N-02..N-05 / #45 review | Pending owner commit/target decisions | Pending independent NFR reviewer | Pending | Open |
| F-02..F-05 / #32/#33 | Pending actual version/access/export evidence | Pending | NOT VERIFIED | Open |
| AR-01..AR-05 / #34..#36 | Pending actual artifact sources/exports | Pending | Pending | Open |
| P-02..P-05 / #44 review | Pending owner commit | Pending | Pending | Open |
| C-06 / Arda S2 evidence | Pending source/ownership links | Pending | Pending | Open |
| I-02 / final package | Pending integrated reviewed versions | Pending | Pending | Open |

## Validation record for this matrix

Initial content/record observations were made by Mert with assistant support at the pinned sources. On 19 November 2026, document validation confirmed 40 unique row IDs, allowed result values, consistent columns in all 12 tables, and 37 defined/used HTTPS reference labels. GitHub source paths and review/comment links were checked against the inspected records; Figma access remains NOT VERIFIED. Whitespace/conflict-marker and single-file scope checks passed. These are static checks, not semantic acceptance of every linked artifact.

The unchanged supporting checker was also executed with Python 3.13.5 against the exact local develop snapshot `ee5c64b0730551e8d5a1699a209fdfaef1cb380f`, using the baseline manifest: exit code 2, overall PENDING, 24 PASS / 0 ERROR / 232 PENDING, all four categories PENDING. That manifest intentionally contains no technical-output or member evidence; this run does not audit the open PR documents or this new matrix, and does not mean members made no contributions. No manifest was edited. No runtime/product/prototype or final QA test is represented by these checks; checker unit tests were not rerun for this documentation-only change.

## Evidence references

[I38]: https://github.com/mert494/student-information-system/issues/38
[I37]: https://github.com/mert494/student-information-system/issues/37
[I32]: https://github.com/mert494/student-information-system/issues/32
[I33]: https://github.com/mert494/student-information-system/issues/33
[I34]: https://github.com/mert494/student-information-system/issues/34
[I35]: https://github.com/mert494/student-information-system/issues/35
[I36]: https://github.com/mert494/student-information-system/issues/36
[SRS]: https://github.com/mert494/student-information-system/blob/a9b6b4819ca18146e4e2b72346405283dbdd0c60/docs/sprint2/SRS_Draft.md
[BACKLOG]: https://github.com/mert494/student-information-system/blob/a9b6b4819ca18146e4e2b72346405283dbdd0c60/docs/sprint2/Refined_Backlog_Draft.md
[NFR]: https://github.com/mert494/student-information-system/blob/63ca3e8c8efc57637185808a6f1981a7561c09d5/docs/sprint2/NFR_Quality_Measures.md
[PROCESS]: https://github.com/mert494/student-information-system/blob/479e68b96def3f348c737fcb7537a616abd26e2c/docs/sprint2/Sprint2_Process_and_Contribution_Log.md
[API]: https://github.com/mert494/student-information-system/blob/ee5c64b0730551e8d5a1699a209fdfaef1cb380f/api/openapi.yaml
[TRACE]: https://github.com/mert494/student-information-system/blob/ee5c64b0730551e8d5a1699a209fdfaef1cb380f/docs/sprint2/Sprint2_Requirements_Traceability.md
[CHECKLIST]: https://github.com/mert494/student-information-system/blob/ee5c64b0730551e8d5a1699a209fdfaef1cb380f/docs/sprint2/Sprint2_Submission_Checklist.md
[TREE]: https://github.com/mert494/student-information-system/tree/ee5c64b0730551e8d5a1699a209fdfaef1cb380f
[BRANCHES]: https://github.com/mert494/student-information-system/branches
[PR43]: https://github.com/mert494/student-information-system/pull/43
[PR44]: https://github.com/mert494/student-information-system/pull/44
[PR45]: https://github.com/mert494/student-information-system/pull/45
[R43]: https://github.com/mert494/student-information-system/pull/43#pullrequestreview-5965776469
[R44]: https://github.com/mert494/student-information-system/pull/44#pullrequestreview-5981606023
[R45]: https://github.com/mert494/student-information-system/pull/45#pullrequestreview-5981094098
[M24]: https://github.com/mert494/student-information-system/pull/24
[M25]: https://github.com/mert494/student-information-system/pull/25
[M41]: https://github.com/mert494/student-information-system/pull/41
[M42]: https://github.com/mert494/student-information-system/pull/42
[F32A]: https://github.com/mert494/student-information-system/issues/32#issuecomment-6992432115
[F32S]: https://github.com/mert494/student-information-system/issues/32#issuecomment-6996130573
[F33S]: https://github.com/mert494/student-information-system/issues/33#issuecomment-6996146017
[FIGMA-D]: https://www.figma.com/design/n5jM7D19uV3Yj2rQRkoV6F/Untitled?node-id=1-1681
[FIGMA-P]: https://www.figma.com/proto/n5jM7D19uV3Yj2rQRkoV6F/Untitled?node-id=1-1681
[AZ24]: https://github.com/mert494/student-information-system/pull/24#pullrequestreview-5924357973
[AZ25]: https://github.com/mert494/student-information-system/pull/25#pullrequestreview-5943656924
[AZ41]: https://github.com/mert494/student-information-system/pull/41#pullrequestreview-5960127871
[AH24]: https://github.com/mert494/student-information-system/pull/24#pullrequestreview-5937084529
[AH25]: https://github.com/mert494/student-information-system/pull/25#pullrequestreview-5943542094
[AH41]: https://github.com/mert494/student-information-system/pull/41#pullrequestreview-5970428075
