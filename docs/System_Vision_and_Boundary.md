# STUDENT INFORMATION SYSTEM (SIS)

## SYSTEM VISION AND BOUNDARY

**Document Status:** Draft – Pending Product Owner, Architecture Lead, and Team Approval.

---

# 1. System Vision

The Student Information System (SIS) aims to provide a centralized platform for managing essential academic information within a university.

The system is intended to make academic information more accessible, organized, and manageable for students, academic staff, and authorized administrative personnel.

The initial vision focuses on supporting essential academic processes such as student information management, course information management, course enrollment, and grade management.

The system's exact capabilities and boundaries will be clarified according to the approved Product Backlog and team decisions.

# 2. Target Users and Candidate Actors

The following user groups are identified as initial stakeholder and candidate actor groups.

| User Group                | Description                                                         | Expected Needs                                                                             |
| ------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| Students                  | Individuals enrolled at the university.                             | Access their own academic information, courses, enrollment status, and grades.             |
| Academic Staff            | Instructors and other academic personnel.                           | Access relevant course and student information and perform authorized academic operations. |
| Student Affairs Personnel | Administrative personnel responsible for student-related processes. | Access and manage authorized student and enrollment records.                               |
| University Management     | Authorized university administrators.                               | Access academic information within their permissions.                                      |

## 2.1 Proposed System Roles

The four system roles selected by the Product Owner for the initial SIS role model are:

* **Student:** A user who accesses their own academic information and performs authorized student operations.
* **Instructor:** An academic staff member who accesses relevant course and student information and performs authorized academic operations.
* **Administrators:** Users who perform authorized administrative operations within the scope approved for the system.
* **Student Affairs Staff:** Personnel responsible for authorized student-related administrative processes.

The stakeholder-to-system-role mapping is documented in the Project Proposal. University Management maps to the Administrators role as a stakeholder relationship; dedicated University Management functions remain outside Sprint 1 scope.

The detailed permissions and responsibilities of these roles still require technical review by the Architecture Lead and team.

**[TODO – Nurefşan / Arda / Team]:** Confirm the role-to-operation and role-to-data permission matrix.

# 3. System Responsibilities and Main Functions

The system is initially expected to support the following responsibilities:

| Function                       | Description                                                                             |
| ------------------------------ | --------------------------------------------------------------------------------------- |
| User Authentication            | Allow users to authenticate themselves and access the system.                           |
| Access Control                 | Restrict system operations according to approved user roles and permissions.            |
| Student Information Management | Support viewing and authorized management of student information.                       |
| Course Management              | Support the management and viewing of course information.                               |
| Course Enrollment              | Support student course enrollment processes.                                            |
| Grade Management               | Support grade management by authorized academic staff and access to grades by students. |

These functions are initial proposals. They must be compared with PB-01–PB-07 in the Initial Product Backlog and validated by the Product Owner and the team.

# 4. System Boundary

**Responsible: Arda – Architecture Lead**

## 4.1 Purpose and Responsibilities

The repository identifies the project as a BM321 Student Information System.

The proposed purpose is to support student-information and academic-information workflows through a centralized system.

The backlog contains examples for account access, student records, course records, course registration, and grades. These are candidate responsibilities only; none is an approved in-scope capability until confirmed by the Product Owner and the team.

## 4.2 Candidate Actors and Permissions

The requirements guide identifies students, academic staff, and student affairs or administration personnel as stakeholder candidates.

The example backlog also refers to an administrator.

These candidates and their status as actual system actors require confirmation.

No role-permission mapping has been approved.

Which actor may read or modify which data, and which operations each actor may perform, remain unresolved.

**[TODO – Nurefşan / Arda]:** Define and validate the role-to-operation and role-to-data permission mapping.

## 4.3 Candidate System Scope

The following capabilities appear in the initial Product Backlog as examples:

* Account sign-in and access control (PB-01 and PB-02).
* Student record management (PB-03).
* Course management (PB-04).
* Course registration and viewing registrations (PB-05).
* Academic staff grade entry and student grade viewing (PB-06 and PB-07).

These capabilities must not be considered approved product commitments until reviewed and approved.

The approved in-scope capability set is **[TODO]**.

Sprint 1 delivers documentation and an API contract draft, not a working backend. Detailed C4/UML work is identified as Sprint 2 preparation, and the MVP as Sprint 3 work.

## 4.4 System Context and External Interactions

The conceptual system is the Student Information System.

The expected interactions include:

* Students accessing their own academic information.
* Academic staff accessing information about relevant courses and students.
* Student affairs personnel managing authorized student and enrollment records.
* Administrators performing authorized administrative operations.

The repository does not identify any confirmed external systems, integrations, deployment environments, or system interfaces.

Potential integrations such as identity providers, academic calendars, payment systems, and notification services must not be assumed to be part of the system.

No external systems are in scope for Sprint 1 (proposed; pending team confirmation). This is consistent with section 5.2, which lists integrations with external university systems as out of scope.

| Actor | Interaction with SIS | Related API operations |
| --- | --- | --- |
| Student | Access their own academic information and perform authorized student operations. | pending role–permission matrix |
| Instructor | Access relevant course and student information and perform authorized academic operations. | pending role–permission matrix |
| Administrators | Perform authorized administrative operations within the scope approved for the system. | pending role–permission matrix |
| Student Affairs Staff | Perform authorized student-related administrative processes. | pending role–permission matrix |

Channel: HTTPS REST API defined in api/openapi.yaml (proposed). No user interface is defined in Sprint 1.

No actual user interface, client application, or running service is established by this draft.

**Pending team confirmation:** The external-systems decision and the actor interaction table above are proposals by the Architecture Lead.

## 4.5 Data and Trust Boundaries

Candidate information areas inferred from the example user stories include:

* Student records.
* Course records.
* Course registrations.
* Grades.

Their fields, sources of truth, ownership, retention, sensitivity classification, and lifecycle have not yet been specified.

Authentication and authorization policies, session mechanisms, and trust boundaries between users, clients, the SIS, and any external systems remain unresolved.

This document does not establish that any operation is public or select a final security mechanism.

Real student data must not be used in project examples.

**[TODO – Team]:** Define data classification, sources of truth, data ownership, lifecycle, and trust boundaries.

## 4.6 Constraints and Assumptions

The following initial constraints and assumptions should be considered:

* The project must follow the course schedule and submission requirements.
* Development activities must follow the responsibilities agreed upon by the team.
* The system scope must remain consistent with approved requirements.
* Access to academic information must be controlled.
* Technical architecture and integration decisions must be documented.
* OpenAPI YAML is required for the API draft; the specification version and validator are not yet team-approved.
* Product requirements, priorities, assignments, RACI, and process decisions in the inspected drafts are proposals awaiting their respective approvals.
* Unknown behavior, integrations, data fields, and policies remain unresolved until confirmed.
* No live server URL, implementation, or deployment is known from the inspected repository.

# 5. Initial Scope

The following scope is preliminary and subject to Product Owner and team approval.

## 5.1 Proposed In-Scope Features

* User authentication and access control.
* Student information management.
* Course information management.
* Course enrollment processes.
* Grade-related operations.

The final feature list must be aligned with the approved Product Backlog.

## 5.2 Proposed Out-of-Scope Features

The following features are proposed to remain outside the initial project scope:

* Online payment processing.
* Employee payroll and salary management.
* Full Learning Management System (LMS) functionality.
* A separate mobile application.
* Integrations with external university systems.

These are proposed exclusions from the initial Vision draft. They have not yet been formally approved by the team.

**[TODO – Nurefşan / Arda / Team]:** Confirm the final in-scope and out-of-scope feature lists.

# 6. Assumptions and Open Decisions

## 6.1 Initial Assumptions

* The system will support multiple user groups.
* Different user groups will have different access permissions.
* Academic information will be managed through a centralized platform.
* The initial system release will focus on essential academic information management functions.

These assumptions require validation.

## 6.2 Decisions Needed

| Decision                                               | Responsible Person(s)  | Status  |
| ------------------------------------------------------ | ---------------------- | ------- |
| Product purpose and approved system responsibilities   | Nurefşan / Team        | Pending |
| Final target users and system actors                   | Nurefşan / Team        | Pending |
| Exact system roles and permissions                     | Nurefşan / Arda        | Pending |
| Role-to-operation and role-to-data mapping             | Nurefşan / Arda        | Pending |
| Final system boundary                                  | Arda / Team            | Pending |
| Confirmed external systems and integrations            | Arda / Team            | Proposed: none for Sprint 1 |
| Domain entities, fields, lifecycle, and business rules | Nurefşan / Arda        | Pending |
| Data classification and trust boundaries               | Team                   | Pending |
| Authentication and session approach                    | Arda / Team            | Pending |
| API specification version and validation tool          | Arda / Team            | Pending |
| Approval of in-scope and out-of-scope features         | Nurefşan / Arda / Team | Pending |
| Alignment with PB-01–PB-07                             | Nurefşan / Team        | Pending |

# 7. Conclusion

The Student Information System aims to provide a centralized platform for managing essential academic information within a university.

This document combines the initial System Vision and the proposed System Boundary into a single working draft.

The Vision section defines the intended purpose, target users, and expected system responsibilities.

The Boundary section describes candidate actors, responsibilities, system context, data and trust boundaries, constraints, and unresolved technical decisions.

The final system scope, user roles, permissions, external interactions, and business rules remain subject to Product Owner, Architecture Lead, and team review.

This document must not be considered an approved specification until the relevant decisions have been reviewed and approved.
