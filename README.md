# student-information-system
BM321 Software Engineering - Student Information System

## Repository documentation

- [Contributions](CONTRIBUTIONS.md)
- [Sprint 2 SRS draft](docs/sprint2/SRS_Draft.md)
- [Sprint 2 architecture](docs/sprint2/Architecture_Decisions_and_Contract_Mapping.md)
- [Provisional OpenAPI](api/openapi.yaml)

## Sprint 3 candidate foundation

**Draft technical scaffold; architecture and product approval pending. Related Issues: [#53 — S3-02 scaffold/test harness](https://github.com/mert494/student-information-system/issues/53) and [#54 — S3-03 CI/coverage](https://github.com/mert494/student-information-system/issues/54).**

This candidate contains a Java 21/Spring Boot process-health endpoint, a React/TypeScript connection screen, unit tests and a GitHub Actions workflow in Draft PR #69. It is **not a working SIS MVP**. Authentication, Students, Courses, registrations, grades, database mappings and migrations are not implemented. Sprint 2 source and its OpenAPI contract are unchanged.

The explicitly authorized scope is an isolated scaffold while Arda and Nurefşan review the stack and product scope. Nothing here records their approval. See [decision/integration notes](docs/sprint3/Candidate_Foundation.md), [measured test report](docs/sprint3/Test_Report.md), [file inventory](docs/sprint3/File_Inventory.md) and [historical PR preparation](docs/sprint3/Proposed_Initial_PR.md).

### Candidate tool versions

| Tool | Candidate version |
| --- | --- |
| Java | 21 |
| Spring Boot | 4.2.0 |
| Maven / Wrapper | 3.9.16 / 3.3.4 only-script distribution |
| Backend tests | Spring Boot managed `spring-boot-starter-test`; JaCoCo 0.8.16 |
| Node / npm | Tested with 24.13.1 / 11.8.0; Node 24.x required |
| React / TypeScript | 19.3.1 / 7.0.2 |
| Vite / Vitest | 8.3.8 / 5.1.2; V8 provider 5.1.2 |
| DOM test environment | happy-dom 21.0.4, compatible with the available Node version |
| Optional PostgreSQL | 18.7 container candidate; not connected or runtime-tested |

Versions were checked against official release metadata and registry engine/peer requirements. The current POM uses Spring Boot managed test dependencies through `spring-boot-starter-test`; the former explicit JUnit 5 override was removed in `a9f4014`. Historical test versions are recorded in the technical report. Maven distribution SHA-256 is pinned and the bootstrap archive was checked against its published SHA-512.

### Verify on Windows

Prerequisites: JDK 21, Node 24.x/npm and Python 3. Open PowerShell at the checkout root and pass your JDK 21 installation path:

~~~powershell
.\scripts\verify-local.ps1 -JavaHome $env:JAVA_HOME
~~~

The verifier runs Maven clean/verify, locked frontend installation, production build, frontend unit tests, coverage-tool tests and separate report checks. Logs and caches stay under `_local`; process environment changes are restored on exit. Use a supported JDK 21 patch. Machine-specific historical troubleshooting is preserved in the [Sprint 3 technical report](docs/sprint3/Test_Report.md#windows-troubleshooting-historical-environment).

### Standard build commands on Linux/macOS

Prerequisites: JDK 21, Node 24.x/npm, Python 3, and network access for the first dependency download. The historical hosted Ubuntu run is linked below; this local review runs on Windows.

~~~bash
cd backend
./mvnw -B -ntp clean verify
cd ../frontend
npm ci --no-fund --no-audit
npm run build
npm run test:coverage
cd ..
python3 -B -m unittest discover -s scripts/tests -v
python3 scripts/verify_coverage.py backend --coverage backend/target/site/jacoco/jacoco.xml --tests backend/target/surefire-reports
python3 scripts/verify_coverage.py frontend --coverage frontend/coverage/unit/coverage-summary.json --tests frontend/reports/unit-junit.xml
~~~

### Run the candidate locally

After the verified package build, in terminal 1:

~~~powershell
# Set JAVA_HOME to your JDK 21 installation before starting this terminal.
& "$env:JAVA_HOME\bin\java.exe" -jar .\backend\target\sis-foundation-0.0.1-SNAPSHOT.jar
~~~

In terminal 2, from this candidate directory:

~~~powershell
cd frontend
npm.cmd run dev
~~~

Open [the local frontend](http://127.0.0.1:5173). Query [backend health](http://127.0.0.1:8080/health):

~~~powershell
Invoke-RestMethod 'http://127.0.0.1:8080/health'
~~~

Expected shape: `{"status":"UP","service":"sis-foundation","uptimeSeconds":12}`; uptime varies. This checks the **process only**, not PostgreSQL or any FR-01–FR-07 feature. Both servers bind to loopback. Stop each with Ctrl+C.

The browser requests `/api/health` on the Vite origin. The dev proxy forwards to `http://127.0.0.1:8080/health`; no broad backend CORS configuration is added. The frontend has loading, validated-success, failure, retry and five-second timeout behavior.

To override the backend port, set `SERVER_PORT` in terminal 1 and `VITE_BACKEND_URL` in terminal 2 before starting Vite. [Frontend configuration example](frontend/.env.example) contains only a public proxy target. Never put secrets in `VITE_` variables. The built frontend needs a separately approved hosting/reverse-proxy arrangement; `vite preview` alone does not provide this backend proxy.

### Optional database configuration

Docker/PostgreSQL execution remains unverified; see the technical report for the historical environment limitation. The backend has no database driver, mappings or DB health assertion. After architecture approval, optional isolated container startup can be evaluated:

~~~powershell
docker compose --env-file .env.example config
docker compose --env-file .env.example up -d postgres
docker compose --env-file .env.example ps
docker compose --env-file .env.example down
~~~

The [.env.example](.env.example) password is deliberately dummy/local-only. Replace it through an ignored local environment file or environment variables before any shared use. Never commit a real `.env` file. The database port is loopback-only and data uses a named volume; `down` preserves it. No deletion command is needed. No institution/student data is seeded.

### Coverage and CI

Backend JaCoCo gates bundle **line coverage ≥50%** at Maven verify. Frontend V8 independently gates **line coverage ≥50%**. Formula per component: covered executable lines / total executable lines. No combined percentage is calculated.

Backend includes every handwritten production class, including the uncovered application entry/configuration. Frontend explicitly includes all `src/**/*.ts(x)`, including its uncovered bootstrap. Only test files/setup and type declarations are excluded; CSS/assets are not executable TS. No handwritten production package is excluded and no generated API code exists. JaCoCo's own compiler-generated-record filtering is normal tool behavior.

Report formats and recorded local results are described in the tracked [integration validation report](docs/sprint3/Test_Report.md#measured-denominator). Reproduce them with the verification commands above. Generated local paths are `backend/target/site/jacoco/index.html` (backend HTML), `backend/target/site/jacoco/jacoco.xml` (backend XML), `frontend/coverage/unit/index.html` (frontend HTML) and `frontend/coverage/unit/coverage-summary.json` (frontend JSON). These ignored outputs are absent from a clean checkout and must not be added to Git to make links work. Coverage describes this tiny scaffold and must not be represented as future MVP coverage.

The [workflow](.github/workflows/ci.yml) handles PRs to develop/main and pushes to both branches, uses a read-only repository token and pinned actions, fails on builds/tests/gates and retains diagnostics for 30 days. It rejects missing reports, zero executed tests and empty denominators. No database integration job is claimed. PR runs may cancel older runs for the same PR; each branch push has its own concurrency group and cannot displace another push run.

[SIS foundation CI run #1](https://github.com/mert494/student-information-system/actions/runs/46047276557) completed successfully for the original `11d6291a8c7b134d0f15e8ebf28a33c563b522ac` revision. GitHub reports Backend unit, Frontend unit and CI result successful, including both diagnostic-upload steps. This is historical hosted evidence, not a run of the newer baseline or this local patch. Artifact contents/downloads and deliberate hosted failure cases remain unverified.

### Integration boundary

Do not copy `_local`, node_modules, target, dist, coverage, reports, logs, downloaded tools or local caches into Git. The inventory identifies exact source candidates. Preserve the repository identity, legacy documents and existing ignore rules when preparing further changes.

Arda must approve stack, package/health-contract/proxy choices and CI tooling; Nurefşan must accept scope and confirm the feature decisions before real MVP work. Preserve JWT `sid`/server revocation, Registration→Student/CourseOffering, unique pair, Grade→Registration, separate Instructor GET and inactive-login/enrollment behavior when those features are implemented.

[Draft PR #69](https://github.com/mert494/student-information-system/pull/69) was published from commit `11d6291a8c7b134d0f15e8ebf28a33c563b522ac` on 27 November 2026. The reviewed baseline is now `a9f4014c939635773778b8fbb6586e1b94b59c1e`; Arda's follow-up changes only the backend test dependencies to Spring Boot management. This local DevOps correction preserves that change. Architecture/product acceptance and independent review remain pending.

Further staging, commits, pushes, PR metadata edits, review requests, merge, settings and release actions require separate applicable authorization. This review prepares a local patch only; it does not complete either Issue.
