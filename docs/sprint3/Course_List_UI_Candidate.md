# Course List UI — local candidate

Prepared 28 November 2026 on exact foundation commit `27f7d6e6c6194b7bfc5908402ce322a85a826099` in a separate detached checkout. Related to [Issue #58](https://github.com/mert494/student-information-system/issues/58) and preparation for S3-10/S3-11. #58 is S3-07 Course maintenance; this presentation component does not complete that Issue, the frontend slices or any API/business acceptance criterion. [Issue #52](https://github.com/mert494/student-information-system/issues/52) decisions remain pending. No remote mutation is authorized by this document.

## Run the working preview

From the candidate's `frontend` directory:

```powershell
npm ci --no-fund --no-audit
npm run dev -- --port 61281 --strictPort
```

Open `http://127.0.0.1:61281/course-preview.html`. The existing foundation remains at `/`. For a production-build review, run `npm run build` followed by `npm run preview -- --port 61281 --strictPort` and open the same path. The additional Vite HTML entry builds a clearly labeled synthetic review page; it does not replace or import fixtures into the existing application screen or a business service. No backend is needed for this page.

The native **Preview state** select switches between loaded, loading, empty and injected error states. **Try again** restores the synthetic samples and returns focus to the state selector. It is a preview action, not a claimed network retry. The reusable error component only shows retry when the host provides an actual callback. There are no login, identity, permission, enrollment or maintenance controls.

## Component contracts

| Contract | Proposed local behavior |
| --- | --- |
| `CourseSummary` | Read-only UI model: `courseId: string`, `courseCode: string`, `title: string`. These candidate fields do not approve API requiredness or a CourseOffering model. |
| `CourseList` | Props: `state: CourseListState`, optional `heading` (default `Courses`), optional `onRetry: () => void`. Pure presentation; no fetch, state cache, authorization or persistence. |
| `CourseListState` | Discriminated union: `{ status: 'loading' }`, `{ status: 'success', courses: readonly CourseSummary[] }`, or `{ status: 'error', message?: string }`. Empty is a successful response with zero courses. Loading/error never render stale rows as current results. |
| `CourseCard` | Receives one `course`. Renders a semantic list item with visible course code and an h3 title; course ID is used as the stable React key by the list. No fake click action. |
| `LoadingState` / `EmptyState` | Reusable status announcements with distinct copy. Loading has static decorative skeletons hidden from assistive technology. |
| `ErrorState` | A user-safe message in an alert and optional native retry button. Omitted message uses safe generic copy. Host owns error translation and retry/focus behavior. Never pass raw response dumps or credentials. |
| `CourseListPreview` | Separate review adapter; imports only synthetic fixtures and feeds props. The state selector has a visible label/help text. No requests, fake authenticated identity or assumed role. |

Use the list below a page-level h1; it supplies h2/h3 hierarchy. Multiple instances receive distinct heading IDs. Native list semantics, count/status announcements and error alerts distinguish each state. Titles and codes wrap without ellipsis, including long unbroken strings. Scoped component styles, 44px controls and visible focus support narrow layouts and keyboard operation. These checks do not establish full WCAG conformance or screen-reader acceptance.

## Proposed API response mapping — not implemented

The provisional [OpenAPI](../../api/openapi.yaml) describes `GET /courses` as an array of `Course`. `courseId` and `courseCode` are candidate strings; `title` has no approved JSON type/requiredness. The shared document also has unresolved authentication and role visibility. No endpoint is called, contract type generated, schema changed or default policy selected here.

After Arda/Nurefşan approve the affected slice, a separate host adapter should validate the real response, then map approved fields to `CourseSummary`. A possible mapping is `Course.courseId → courseId`, `Course.courseCode → courseCode`, and an approved display title → `title`; field names and missing/null/duplicate handling still require agreement. Do not treat a Course ID as a CourseOffering ID or silently invent a title for malformed data.

Replace the review adapter at the application composition boundary with a real data owner that supplies loading, validated success and user-safe error states. That owner must implement the approved request/cancellation/retry behavior, permissions and error semantics. Keep fixtures confined to the review entry/tests. An empty response, transport failure and unauthorized response must not become interchangeable. No future contract or authorization behavior is implemented by this candidate.

Pending decisions include Course fields/types/requiredness and uniqueness (OQ-04), approved offering identifiers/lookup (OQ-05), role/record visibility (OQ-01), error schema/copy (OQ-08), PATCH policy (OQ-13), and stack/scope acceptance under #52. Sorting, pagination, search, credits, terms, enrollment and actions are deliberately outside this component's contract.

## Reference and QA review

- [Figma prototype](https://www.figma.com/design/n5jM7D19uV3Yj2rQRkoV6F/SENG321---OBS-prototype?node-id=142-238): reviewed publicly in the browser, including course code/name presentation, white/gray panels and indigo accents. Its role-specific chrome and academic actions are outside this candidate. This responsive list is a local design proposal, not a claim of pixel-identical implementation or an approved screen. No design file was edited or Figma tracking session created.
- [PR #68 matrix at exact reviewed revision](https://github.com/mert494/student-information-system/blob/3aed7aa509c474191b5666f6117e0da5f8e79e43/docs/sprint3/Sprint3_Test_Strategy_and_Matrix.md): remains a draft. Applied its synthetic-data, visible labels/focus and distinct-state principles; FR-04 API/create/PATCH/permission cases remain blocked and are not claimed as passed. The FR-07 loading/error examples are analogous UI guidance, not Course feature acceptance tests. #67's full axe/manual screen-reader/usability protocol is separate.

Suggested independent reviewers: **Azra** for UI/layout/focus, **Ahmet** for test value/coverage/accessibility, **Arda** for view-model/API compatibility. No review request or acceptance is recorded.

## Validation and inventory

Actual commands, measured coverage and browser observations are recorded below after execution. Existing foundation tests are preserved byte-for-byte; no coverage exclusion or threshold change is introduced. Component and preview source remain inside the existing full `src/**/*.{ts,tsx}` denominator. The preview bootstrap remains included even if not executed by unit tests. Backend coverage stays separate.

Exact source changes:

- `frontend/vite.config.ts` — additional isolated preview HTML build entry; existing proxy preserved.
- `frontend/course-preview.html`
- `frontend/src/courses/CourseSummary.ts`
- `frontend/src/courses/CourseList.tsx`
- `frontend/src/courses/CourseCard.tsx`
- `frontend/src/courses/CourseStates.tsx`
- `frontend/src/courses/course-list.css`
- `frontend/src/courses/CourseList.test.tsx`
- `frontend/src/dev/CourseListPreview.tsx`
- `frontend/src/dev/CourseListPreview.test.tsx`
- `frontend/src/dev/courseFixtures.ts`
- `frontend/src/dev/course-preview.tsx`
- `frontend/src/dev/course-preview.css`
- `docs/sprint3/Course_List_UI_Candidate.md` — this integration/readiness record.

No staging, commit, push, Issue/PR creation, merge, release or settings action is performed. Publication/integration actions require separate applicable Mert authorization; product/API decisions require their owners. Original work and both existing PRs remain protected.

## Executed validation — 28 November 2026

Environment: Windows, Oracle JDK 21.0.1, Node 24.13.1, npm 11.8.0 and bundled Python 3.12.14. Dependency caches/tools were copied into this isolated checkout; prior application reports were not copied. All results here were obtained from this candidate. The existing PR #69 checkout was not used as a build location.

| Executed check | Actual result |
| --- | --- |
| `npm ci --no-fund --no-audit` through the existing local verifier | PASS; 88 packages installed, lockfile unchanged. |
| `npm run typecheck` | PASS; strict TypeScript validation. |
| `npm run build` | PASS; foundation and synthetic preview HTML/JS/CSS entries built. Existing dev proxy configuration unchanged. |
| `npm run test:coverage` (Vitest) | PASS; 24 tests across 4 files: original 13 plus 8 CourseList tests and 3 preview tests. Zero failures/skips. |
| Frontend V8 coverage | 43/49 lines = **87.75%** (report validator: 87.7551%); 38/45 branches = **84.44%**; 19/19 functions = **100%**. Existing independent 50% line gate passes. |
| New list/state components | CourseList, CourseCard and CourseStates each have **100%** reported line/function coverage; CourseList and CourseStates also have 100% reported branches. Preview component is covered; both old/new bootstraps remain included and uncovered by unit tests. Type-only model has no executable lines. |
| Maven Wrapper `clean verify`, JDK 21, via `scripts/verify-local.ps1` | PASS; 4 backend tests, zero failures/errors/skips; JaCoCo 9/13 lines = **69.23%**; executable package. Backend source/POM unchanged. |
| `python -B -m unittest discover -s scripts/tests -v` | PASS; 7 gate-tool tests, outside application metrics. Backend/frontend report validators also passed. |
| Production preview in the browser | PASS; success/loading/empty/error states, native keyboard selection, Tab → retry → Enter, visible focus and focus return verified. Browser console reported no errors. |
| Responsive review | PASS at desktop 1280px and narrow 320px. Four complete course titles remain readable and wrap; no horizontal overflow observed. Select ~45.8px and retry ~47.6px tall. Temporary viewport override reset. |
| Static/preservation checks | PASS; `git diff --check` plus every new file checked; full patch applies cleanly to the exact baseline; 14 source paths (13 additions, 1 modification), no deletions/generated artifacts/secrets; documented paths, 2 tables and the local OpenAPI link verified. All 96 other tracked paths, original tests, package/lockfile, OpenAPI and backend configuration retain their baseline blobs. Normal index remains unchanged; original and PR #69 checkout file/index/ref/config/status fingerprints match. |

The initial sandboxed backend attempt could not complete because Mockito/JVM attach was denied access to its pipe; that attempt was stopped. The unchanged verifier then passed outside the sandbox. Its usual dynamic-agent warning remains non-failing; no agent flags, POM dependencies or coverage settings were changed. Frontend tests/build were repeated after adding the explicit native-list role to preserve list semantics with list-style removal across browsers.

Checked CSS contrast pairs by relative luminance: body 13.66:1, secondary text 7.58:1, accent/focus on white 7.90:1, error on white 7.55:1, badge 8.88:1, select border on white 4.76:1. These are limited color checks, not a WCAG audit. No axe scan, live screen-reader session, usability study, real Course API, persistence/authentication test or hosted CI run was performed. FR-04 business/API matrix cases remain blocked.

Readiness: ready for **Azra's local UI review**, with **Ahmet** reviewing tests/accessibility and **Arda** reviewing the candidate view model. Integration/acceptance remains pending #52 decisions and the later real-data adapter; no Issue is marked complete. Review the exact 14-file inventory above before any separately authorized publication.
