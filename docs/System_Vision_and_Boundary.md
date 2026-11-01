# STUDENT INFORMATION SYSTEM (SIS)

## SYSTEM VISION AND BOUNDARY

# 1. System Vision

The Student Information System (SIS) aims to provide a centralized platform for managing essential academic information within a university.

The system is intended to make academic information more accessible, organized, and manageable for students, academic staff, and authorized administrative personnel.

The initial vision focuses on supporting essential academic processes such as student information, course information, course enrollment, and grade management.

The system's exact capabilities and boundaries will be clarified according to the approved Product Backlog and team decisions.

# 2. Target Users

The initial target user groups are:

| User Group | Description | Expected Needs |
|---|---|---|
| Students | Individuals enrolled at the university. | Access their own academic information, courses, enrollment status, and grades. |
| Academic Staff | Instructors and other academic personnel. | Access relevant course and student information and perform authorized academic operations. |
| Student Affairs Personnel | Administrative personnel responsible for student-related processes. | Access and manage authorized student and enrollment records. |
| University Management | Authorized university administrators. | Access academic information within their permissions. |

The exact roles and permissions of each user group must be validated by the team.

# 3. System Responsibilities and Main Functions

The system is initially expected to support the following responsibilities:

| Function | Description |
|---|---|
| User Authentication | Allow users to authenticate themselves and access the system. |
| Access Control | Restrict system operations according to user roles and permissions. |
| Student Information Management | Support viewing and authorized management of student information. |
| Course Management | Support the management and viewing of course information. |
| Course Enrollment | Support student course enrollment processes. |
| Grade Management | Support grade management by authorized academic staff and access to grades by students. |

These functions are initial proposals. They must be compared with PB-01–PB-07 in the existing Product Backlog and validated by the team.

# 4. System Context

The SIS is envisioned as a centralized system through which different user groups interact with academic information.

The expected interactions include:

- Students accessing their own academic information.
- Academic staff accessing information about their assigned courses and students.
- Student affairs personnel managing authorized student and course enrollment records.
- University management accessing relevant information according to its permissions.

It has not yet been determined whether the system will communicate with other university systems or third-party services.

**[TODO – Arda]:** Define the system boundaries, external actors, external systems, interfaces, and relevant interactions.

# 5. System Boundary Specification

**Responsible: Arda – Architecture Lead**

The detailed system boundary must be defined by the Architecture Lead in coordination with the team.

The following topics require clarification:

- Which functions are the responsibility of the SIS?
- Which activities will remain outside the system?
- Which external actors will interact with the system?
- Are integrations with external university systems or third-party services required?
- Which APIs or interfaces are needed?
- What are the technical and operational constraints?

**[TODO – Arda / Team]:** The system boundary must not be considered approved until these decisions have been clarified.

# 6. Initial Scope

The following scope is preliminary and subject to team approval.

## 6.1 Proposed In-Scope Features

- User authentication and access control.
- Student information management.
- Course information management.
- Course enrollment processes.
- Grade-related operations.

The final feature list must be aligned with the existing Product Backlog.

## 6.2 Proposed Out-of-Scope Features

The following features are proposed to remain outside the initial project scope:

- Online payment processing.
- Employee payroll and salary management.
- Full Learning Management System (LMS) functionality.
- A separate mobile application.
- Integrations with external university systems.

These features must not be treated as final exclusions unless approved by the team.

# 7. Constraints

The following initial constraints should be considered during system development:

- The project must follow the course schedule and submission requirements.
- Development activities must follow the responsibilities agreed upon by the team.
- The system scope must remain consistent with approved requirements.
- Access to academic information must be controlled.
- Technical architecture and integration decisions must be documented.

# 8. Assumptions and Open Decisions

## 8.1 Initial Assumptions

- The system will support multiple user groups.
- Different user groups will have different access permissions.
- Academic information will be managed through a centralized platform.
- The initial system release will focus on essential academic information management functions.

These assumptions require validation.

## 8.2 Open Decisions

| Decision | Related Responsibility | Status |
|---|---|---|
| Exact user roles and permissions | Team | Pending |
| Final system boundary | Arda / Team | Pending |
| External system interactions | Arda / Team | Pending |
| Required API operations | Arda / Nurefşan | Pending |
| Approval of in-scope and out-of-scope features | Arda / Nurefşan / Team | Pending |
| Alignment with PB-01–PB-07 | Nurefşan / Team | Pending |

# 9. Conclusion

The Student Information System aims to provide a centralized platform for managing essential academic information.

This document defines the initial system vision, target users, and expected responsibilities.

The detailed system boundaries, external interactions, and final scope will be clarified through the Architecture Lead's analysis and team approval.
