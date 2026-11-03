# STUDENT INFORMATION SYSTEM (SIS)

## INITIAL PRODUCT BACKLOG

**Document status:** Draft – Pending Product Owner and team approval.

The user stories in this document are prepared to evaluate the initial requirements of the system. They must not be treated as approved requirements or Sprint commitments until reviewed and approved by the Product Owner and the team.

Priorities are initial proposals. Story Point values are not hours and must be reassessed by the development team. Proposed owners do not represent confirmed assignments.

# PB-01 – User Login

- **Epic:** Identity and Access
- **User Story:** As a user with an assigned system role, I want to log in with my account so that I can access the operations I am authorized to perform.

**Acceptance Criteria:**

1. A user must be able to log in with valid credentials.
2. Access must be denied when invalid credentials are provided.
3. An invalid-login message must not reveal whether the account exists in the system.
4. After logging out, a user must be required to authenticate again before performing a protected operation.

- **Priority:** P1 – High (proposed)
- **Story Points:** 5 (proposed)
- **Dependencies:** Approval of authentication requirements and test-account policy.
- **Proposed Owner:** Arda
- **Quality Reviewer:** Ahmet
- **Status:** Pending Product Owner and team approval.

# PB-02 – Role-Based Authorization

- **Epic:** Identity and Access
- **User Story:** As a Student Affairs Staff member, I want to restrict operations performed by Students, Instructors, Administrators, and Student Affairs Staff members according to their roles so that each user can access only the functions they are authorized to use.

**Acceptance Criteria:**

1. User permissions must follow the role-and-permission matrix approved by the Product Owner.
2. An unauthenticated request to a protected API operation must return **401 Unauthorized**.
3. An authenticated user who lacks permission for an operation must receive **403 Forbidden** with an error response containing a code and message.
4. A Student must not be able to access another Student's protected academic information, including through a direct API request; such an authenticated unauthorized request must return **403 Forbidden** with an error code and message.
5. The same authorization rules must be enforced by the API, not only by hiding or disabling interface elements.

- **Priority:** P1 – High (proposed)
- **Story Points:** 5 (proposed)
- **Dependencies:** PB-01 and approval of the role-and-permission matrix.
- **Proposed Owner:** Arda
- **Quality Reviewer:** Ahmet
- **Status:** Pending approval of the role-and-permission matrix and API response mapping.

# PB-03 – Student Management

- **Epic:** Student Affairs
- **User Story:** As an authorized Student Affairs Staff member, I want to create, list, and update student records so that student information can be managed.

**Acceptance Criteria:**

1. Required fields must be validated when a student record is created.
2. Creating a second record with the same student number must be prevented.
3. Unauthorized users must not be able to modify student records.
4. After a successful update, the updated information must be visible in the student list.
5. A student record request containing missing or invalid information must be rejected.

- **Priority:** P1 – High (proposed)
- **Story Points:** 5 (proposed)
- **Dependencies:** PB-02 and approval of student data fields.
- **Proposed Owner:** To be determined by the implementation team.
- **Acceptance Criteria Advisor:** Nurefşan
- **Status:** Pending approval of data fields and owner assignment.

# PB-04 – Course Management

- **Epic:** Course Catalog
- **User Story:** As an authorized Student Affairs Staff member, I want to create courses and update existing course information so that course records can be maintained.

**Acceptance Criteria:**

1. Required fields must be validated when a course is created.
2. Creating a second course with the same course code within the approved uniqueness scope must be prevented.
3. Unauthorized users must not be able to modify course information.
4. A newly created course must be visible in the course list.
5. A course creation request containing missing or invalid information must be rejected.

- **Priority:** P1 – High (proposed)
- **Story Points:** 5 (proposed)
- **Dependencies:** PB-02 and approval of the course/term data model.
- **Proposed Owner:** To be determined by the implementation team.
- **Quality Reviewer:** Ahmet
- **Status:** Pending clarification of course-code uniqueness scope and owner assignment.

# PB-05 – Course Enrollment

- **Epic:** Course Enrollment
- **User Story:** As a Student, I want to enroll in courses and view my current course enrollments so that I can plan and track my studies.

**Acceptance Criteria:**

1. Only a student with active student status may enroll in a course. Enrollment is allowed only when the enrollment period is open and all approved enrollment conditions are met.
2. A second enrollment record for the same student, course, and term must be prevented. The API should return **409 Conflict** with a defined error code for a duplicate enrollment.
3. A new enrollment request made while the enrollment period is closed must be rejected with **409 Conflict** and a defined error code.
4. A Student must be able to view only their own course enrollments.
5. The system must check course capacity and applicable course prerequisites before accepting an enrollment. If the course is full or a prerequisite is not met, the API must reject the request with **409 Conflict** and an error response containing a specific code and message identifying the unmet condition.
6. If the student does not have active student status, the API must reject the request with **409 Conflict** and an error response containing a specific code and message identifying the unmet condition. The exact error-code names and response schema must be documented with the API implementation.
7. A rejected enrollment request must not create or modify an enrollment record.
8. A successful enrollment request must create exactly one enrollment record for the requested student, course, and term, and that enrollment must appear in the student's own enrollment list.

**Enrollment Business Rules:**

- Enrollment requires active student status.
- Course capacity must be checked.
- Applicable course prerequisites must be checked.
- University Management is responsible for defining the enrollment dates for each term.

These enrollment rules are Product Owner decisions and are included as the business-rule basis for this backlog item. The detailed business rules and API error-code mapping should be documented with the team before implementation.

- **Priority:** P1 – High (proposed)
- **Story Points:** 8 (proposed)
- **Dependencies:** PB-03 and PB-04.
- **Business Rules Advisor:** Nurefşan
- **Validation Advisor:** Ahmet
- **Status:** Business rules defined; detailed API error mapping and team estimation remain to be documented.

# PB-06 – Instructor Grade Entry

- **Epic:** Grade Management
- **User Story:** As an Instructor, I want to enter grades for students enrolled in a course assigned to me so that I can record and maintain the academic results for my course.

**Acceptance Criteria:**

1. Only an instructor assigned to the relevant course must be able to enter grades for that course.
2. Values outside the approved grading range must be rejected.
3. Entering a grade for a student who is not enrolled in the relevant course must be prevented.
4. A successfully saved grade must be retrievable later.
5. An unauthorized user must not be able to perform grade-entry operations; an authenticated user without the required permission must receive **403 Forbidden**.
6. A rejected grade-entry request must not create or modify a grade record.

- **Priority:** P2 – Medium (proposed)
- **Story Points:** 8 (proposed)
- **Dependencies:** PB-02, PB-05, instructor/course assignment, and approval of the grading scale.
- **Proposed Owner:** To be determined by the implementation team.
- **Acceptance Criteria Advisors:** Nurefşan and Ahmet
- **Status:** Pending approval of grading scale, publication rules, and API response mapping.

# PB-07 – Student Grade Viewing

- **Epic:** Grade Management
- **User Story:** As a Student, I want to view the grades published for my courses so that I can monitor my academic performance and progress.

**Acceptance Criteria:**

1. A Student must be able to view only their own published grades.
2. Grades that have not yet been published must not be displayed to the student.
3. If the student has no published grades, the system must display the message: "No published grades are available."
4. If a Student attempts to access another Student's grade information through a direct request, access must be denied. An authenticated Student making such a request must receive **403 Forbidden** with an error code and message.
5. When a grade-viewing request is successful, only information the student is authorized to access must be displayed.
6. A request for another student's grades must not disclose the grades or other protected academic information.

- **Priority:** P2 – Medium (proposed)
- **Story Points:** 3 (proposed)
- **Dependencies:** PB-06 and approval of the grade publication rule.
- **Proposed Owner:** To be determined by the implementation team.
- **Validation Advisor:** Ahmet
- **Status:** Pending approval of the empty-state message proposal, publication rule, and API response mapping.

# 8. Prioritization and Estimation Notes

P1, P2, and P3 values are initial priority proposals.

Story Point values represent relative effort and uncertainty; they must not be interpreted as working hours.

Priorities should be reviewed by the Product Owner together with team input. Story Point values must be estimated by the development team.

# 9. Dependencies and Responsibilities

The dependencies of PB-01–PB-07 are listed above.

Proposed owners are not confirmed assignments. Implementation tasks should be assigned by the team according to capacity and expertise.

# 10. Approval and Tracking

- **Product Owner approval:** Pending
- **Team estimates:** Pending
- **Implementation assignments:** Pending
- **API mapping with Arda:** Proposed in api/openapi.yaml via x-backlog-reference (PB-01…PB-07); see PR #8 / Issue #13.
- **GitHub Issue mapping with Mert:** Deliverable Issues #11 (Proposal), #12 (Vision/Boundary), #15 (Backlog); per-PB Issues [TODO].
- **Quality review by Ahmet:** In review via PR #7.
- **Confirmed user roles:** Student, Instructor, Administrators, and Student Affairs Staff.
- **Role-and-permission matrix:** Pending technical review by the Architecture Lead and team.
- **Enrollment rules and API error-code mapping:** To be documented with the implementation details.

Approved backlog items should later be mapped to actual GitHub Issues.

A backlog item should be considered complete only after its acceptance criteria have been verified, relevant tests have passed, required documentation has been updated, and the independent review process has been completed.
