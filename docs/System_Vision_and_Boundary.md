# System Vision and Boundary — Draft

**Status:** Proposed working draft. Product scope, actors, permissions, domain rules, and external integrations have not been approved in the inspected repository. This file does not record team approval.

## System Vision — owned by Nurefşan

Reserved for the Product Owner's Vision content. It has not been drafted here. Purpose, target users, and core product functions require product scope decisions. [TODO]

## System Boundary — owned by Arda

### Purpose and responsibilities

The repository identifies the project as a BM321 Student Information System. A possible purpose is to support student-information workflows. The product purpose and responsibilities remain subject to Product Owner scope approval. [TODO]

The backlog contains examples for account access, student records, course records, course registration, and grades. These are candidate responsibilities only; none is an approved in-scope capability.

### Candidate actors

The requirements guide names students, academic staff, and student affairs/administration as stakeholder candidates, and cautions that stakeholders are not automatically product roles. The example backlog also refers to an administrator. These candidates and their status as system actors require confirmation. [TODO]

No role-permission mapping is approved. Which actor may read or change which data and perform which operation remains [TODO].

### Candidate scope

The following capabilities appear only as examples in `docs/Initial_Backlog_Draft.md`; none is an approved product commitment:

- Account sign-in and access control (PB-01 and PB-02).
- Student record management (PB-03).
- Course management (PB-04).
- Course registration and viewing registrations (PB-05).
- Academic staff grade entry and student grade viewing (PB-06 and PB-07).

The approved in-scope capability set is [TODO]. Explicit out-of-scope capabilities have not been recorded and are [TODO]. Sprint 1 delivers documentation and an API contract draft, not a working backend. Detailed C4/UML work is identified as Sprint 2 preparation, and the MVP as Sprint 3 work.

### System context and external interactions

The conceptual system is the Student Information System. The repository identifies no confirmed external systems, integrations, deployment environments, or system interfaces. Identity provider, academic calendar, payment, notification, and other integrations must not be assumed; confirmed external interactions are [TODO].

Users may be candidate external actors, pending product confirmation. No actual user interface, client application, or running service is established by this draft.

### Data and trust boundaries

Candidate information areas inferred from the example stories are student records, course records, registrations, and grades. Their fields, sources of truth, ownership, retention, sensitivity classification, and lifecycle are unspecified and [TODO]. Do not use real student data in examples.

Authentication and authorization policy, session mechanism, and trust boundaries between users, clients, the SIS, and any external system are unresolved. This draft does not assert that any operation is public or select a security mechanism. [TODO]

### Constraints and assumptions

- OpenAPI YAML is required for the API draft; the specification version and validator are not team-approved.
- Product requirements, priorities, assignments, RACI, and process decisions in the inspected drafts are proposals awaiting their respective approvals.
- Unknown behavior, integrations, data fields, and policies remain [TODO] until confirmed with the responsible teammates.
- No live server URL, implementation, or deployment is known from the inspected repository.

### Decisions needed

- Product purpose, approved target users/actors, and initial scope: [TODO — Nurefşan / team]
- Role-to-operation and role-to-data permissions: [TODO — Nurefşan]
- Domain entities, fields, lifecycle, and business rules: [TODO — Nurefşan]
- Confirmed external systems and integrations: [TODO — Nurefşan / team]
- Data classification, source of truth, and trust boundaries: [TODO — team]
- Authentication/session approach and authorization policy: [TODO — team]
- API specification version, validation tool, and any server information: [TODO — Arda / team]
