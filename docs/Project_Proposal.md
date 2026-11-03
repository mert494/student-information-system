# STUDENT INFORMATION SYSTEM (SIS)

## PROJECT PROPOSAL

# 1. Project Overview

The Student Information System (SIS) is a software system intended to support the centralized management of academic information within a university.

Its main purpose is to enable students, academic staff, and authorized administrative personnel to access the academic information they need in a more organized and controlled manner.

The SIS aims to support essential academic processes such as student records, course information, course enrollment, and grade management. Managing these processes through a single system is intended to improve information accessibility, data consistency, and administrative efficiency.

# 2. Problem Definition

Universities manage various types of academic information, including student records, course details, enrollment information, and grades. When these processes are handled through separate tools or manual procedures, accessing and updating information may become difficult.

Potential problems include:

* Student information being stored in different locations.
* Difficulties accessing up-to-date course and enrollment information.
* Delays in recording or viewing grades.
* Inconsistencies or duplicate records in academic data.
* Insufficient control over who can access or modify sensitive information.

These problems may lead to unnecessary administrative work, communication difficulties, and risks to data consistency.

**Evidence and validation:** These problems are initial project assumptions. They have not yet been validated through formal interviews, surveys, or institutional data. However, a preliminary review of the existing university Student Information System (OBS) was conducted to observe its visible academic functions.

### Preliminary Review of the Existing Student Information System

The existing university Student Information System (OBS) was briefly examined to understand how academic processes are presented through its interface. The following observations were recorded:

* The Course Registration screen lists selected courses with information such as course code, course name, credits, ECTS, and academic year.
* The registration status section displays the student's finalization status and academic advisor approval status.
* The Add/Drop Courses screen provides access to course selection and modification functions.
* The Grade List screen provides separate sections for courses, including fields for exam name, grade, announcement date, and class average.
* Other academic functions, such as transcripts and semester GPA information, are presented under separate menu sections.

These observations show that the existing OBS provides access to essential academic processes, including course registration, course management, and grade viewing. They also indicate that different academic functions are presented through separate menus and screens.

This review is limited to observations of the existing system's interface and visible functionality. No student survey or interview was conducted. Therefore, these observations should not be interpreted as evidence of confirmed user dissatisfaction or specific user problems.


### QA Evidence Register — Preliminary OBS Review

| Ref. | Observation recorded in this proposal | Evidence status for QA |
| --- | --- | --- |
| OBS-01 | Course Registration lists selected courses with course code, course name, credits, ECTS, and academic year. | Observation is recorded as a text-based interface observation in this proposal; no image attachment is included or required for this draft. |
| OBS-02 | Registration status displays finalization status and academic advisor approval status. | Observation is recorded as a text-based interface observation in this proposal; no image attachment is included or required for this draft. |
| OBS-03 | Add/Drop Courses provides course selection and modification functions. | Observation is recorded as a text-based interface observation in this proposal; no image attachment is included or required for this draft. |
| OBS-04 | Grade List contains sections for courses and fields including exam name, grade, announcement date, and class average. | Observation is recorded as a text-based interface observation in this proposal; no image attachment is included or required for this draft. |
| OBS-05 | Transcript and semester GPA functions appear under separate menu sections. | Observation is recorded as a text-based interface observation in this proposal; no image attachment is included or required for this draft. |

**QA limitation:** This proposal records the OBS review as text-based observations. No screenshots or other visual attachments are planned for this document. QA may review the wording and, if OBS access is available, check whether the listed screens and fields are visible. The observations do not establish user dissatisfaction, process failure, or measured performance.

# 3. Stakeholder Analysis

The initial stakeholder groups are listed below. Their needs and expectations should be validated during the project.

| Stakeholder               | Potential Needs and Expectations                                                                          |
| ------------------------- | --------------------------------------------------------------------------------------------------------- |
| Students                  | Access their own academic information, courses, enrollment status, and grades.                            |
| Academic Staff            | Access information about their assigned courses and students, and perform authorized academic operations. |
| Student Affairs Personnel | Manage student and course enrollment records efficiently.                                                 |
| University Management     | Access relevant academic information to monitor administrative processes.                                 |

### Stakeholder → System Role

| Stakeholder | System Role |
| --- | --- |
| Students | Student |
| Academic Staff | Instructor |
| Student Affairs Personnel | Student Affairs Staff |
| University Management | Administrators |

University Management remains a stakeholder, but dedicated University Management functions (such as institution-level dashboards, management reports, and management-specific access workflows) are outside the Sprint 1 scope. The Administrators role is retained as a system role; this does not make those University Management-specific capabilities part of Sprint 1.

The detailed responsibilities and access permissions of each system role must be clarified by the team.

# 4. Proposed Solution

The proposed solution is to develop a centralized Student Information System that supports essential academic information management processes.

The initially proposed capabilities include:

* User authentication and access control.
* Student information management.
* Course information management.
* Course enrollment.
* Grade management.
* Academic information viewing according to user permissions.

These capabilities are initial proposals. The final feature list must be compared with the existing Product Backlog items PB-01–PB-07 and aligned with team decisions.

# 5. Expected Outcomes

The project aims to achieve the following outcomes:

* Provide centralized access to academic information.
* Reduce unnecessary manual work in academic information management.
* Improve the consistency and accessibility of student records.
* Support course and enrollment management processes.
* Provide controlled access to academic information.
* Make relevant information easier for authorized users to retrieve.

These are intended project benefits, not outcomes that have already been achieved.

# 6. Feasibility Analysis

## 6.1 Technical Feasibility

The project is planned to be implemented using software development technologies and tools selected by the team.

Technical feasibility depends on the technologies selected, the system architecture, and the development resources available.

Technical details and external integrations that have not yet been decided must be evaluated separately by the team.

## 6.2 Operational Feasibility

The proposed system is intended to support students, academic staff, and authorized administrative personnel.

Its operational feasibility depends on whether the implemented functions meet the actual needs of these users and whether the proposed workflows are practical.

Stakeholder needs and operational assumptions must be validated.

## 6.3 Schedule and Team Feasibility

The project will be developed collaboratively by the project team. Its schedule feasibility depends on the approved scope, sprint capacity, task distribution, and the time available to team members.

The team should estimate the effort required for backlog items before creating an implementation plan.

# 7. Initial Project Scope

The following features are proposed for consideration in the initial scope.

## 7.1 Potentially In Scope

* User authentication and authorization.
* Student information management.
* Course information management.
* Course enrollment information management.
* Grade management.
* Access to academic information according to user permissions.

## 7.2 Potentially Out of Scope

The following features are proposed exclusions from the current project scope. They must not be treated as final scope decisions without team approval:

* Dedicated University Management functions, including institution-level dashboards, management reports, and management-specific access workflows, are outside Sprint 1 scope. University Management remains a stakeholder; its mapping to the Administrators system role does not add these capabilities to Sprint 1.

* Online payment processing.
* Employee payroll and salary management.
* Full Learning Management System (LMS) functionality.
* A separate mobile application.
* Integrations with external university systems.

The final scope must be consistent with the System Vision and Boundary document and team decisions.

# 8. Assumptions and Constraints

## 8.1 Assumptions

* The system will support multiple user groups.
* User access permissions will differ according to their roles.
* Academic information will be managed through a centralized system.
* The initial release will focus on essential academic information management functions.

These assumptions must be validated during the project.

## 8.2 Constraints

* The project must be completed according to the schedule defined for the course.
* Development tasks must follow the responsibilities agreed upon by the team.
* The system scope must remain consistent with the approved project requirements.
* Technical decisions must be made collaboratively and documented.

# 9. Initial Risks

| Risk                                        | Potential Impact                                  | Proposed Mitigation                                        |
| ------------------------------------------- | ------------------------------------------------- | ---------------------------------------------------------- |
| Unclear or frequently changing requirements | Rework and delays                                 | Review and document requirements before implementation.    |
| Unclear project boundaries                  | Scope expansion                                   | Agree on in-scope and out-of-scope features as a team.     |
| Inconsistent academic data                  | Incorrect or unreliable information               | Define appropriate data validation rules.                  |
| Unauthorized access                         | Exposure or modification of sensitive information | Define roles and access permissions.                       |
| Insufficient development time               | Incomplete functionality                          | Prioritize essential features and monitor sprint progress. |
| Communication problems                      | Misunderstandings and duplicated work             | Document decisions and responsibilities.                   |

# 10. Open-Source License Consideration

The repository already contains an MIT License file. Retaining the existing license is recommended unless the team agrees on a different approach.

The MIT License is a permissive open-source license that allows software to be used, modified, and distributed subject to its conditions. These conditions include preserving the copyright and license notices.

Retaining the existing MIT License is suitable for this project because it is simple and permissive, allowing others to use, modify, and distribute the project with minimal restrictions. This supports collaboration and future development while requiring the original copyright and license notice to be preserved.


The team should review whether the existing license is appropriate for the project's purpose and intended distribution. No license change is proposed in this document.


**QA/review note:** This proposal records the rationale for retaining the MIT License already present in the repository; it does not claim that the team has formally approved the license decision. Reviewers should verify that the repository's `LICENSE` file is present and that its text matches the license identified in this section. Team approval remains pending.

# 11. Initial Success Criteria

The project may be considered successful if it:

* Provides the academic information management functions included in the approved scope.
* Supports the agreed user roles and access permissions.
* Enables authorized users to access and manage relevant information.
* Maintains the accuracy and consistency of stored academic data.
* Meets the functional and quality requirements approved by the team.
* Is completed according to the agreed schedule and submission requirements.

The final success criteria should be refined as the requirements become more specific.

# 12. Conclusion

The Student Information System aims to provide a centralized and controlled environment for managing essential academic information within a university.

This proposal presents the initial problem definition, stakeholder groups, proposed solution, feasibility considerations, and potential project scope.

These points will be refined through stakeholder analysis, team discussions, and the development of the System Vision, Boundary, and Product Backlog documents.
