# STUDENT INFORMATION SYSTEM (SIS)

## INITIAL PRODUCT BACKLOG

**Document status:** Draft – Pending Product Owner and team approval.

The user stories in this document are prepared to evaluate the initial requirements of the system. They must not be treated as approved requirements or Sprint commitments until reviewed and approved by the Product Owner and the team.

All PB-01–PB-07 priorities, Story Point values, and proposed owners are unapproved proposals unless explicitly approved by the Product Owner and team. Story Point values are relative estimates, not hours, and must be reassessed by the development team. Proposed owners do not represent confirmed assignments.

# PB-01 – User Login

- **Epic:** Identity and Access
- **User Story:** As a user, I want to log in with my account so that I can access the operations I am authorized to perform.

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
- **User Story:** As a system administrator, I want to restrict students', instructors', and administrators' operations according to their roles so that users can access only the functions they are authorized to use.

**Acceptance Criteria:**

1. User permissions must follow the role-and-permission matrix approved by the Product Owner.
2. An unauthenticated request to a protected operation must return HTTP `401 Unauthorized`.
3. An authenticated user who lacks the permission required for an operation must receive HTTP `403 Forbidden`, including when the operation is attempted through a direct API request.
4. A student who attempts to access another student's protected academic information must receive HTTP `403 Forbidden`; no protected information belonging to the other student must be returned.
5. The response-code mapping (`401` for missing/invalid authentication and `403` for insufficient permission) is proposed for measurable testing; Arda and the team must confirm it in the API contract before it is treated as approved.

- **Priority:** P1 – High (proposed)
- **Story Points:** 5 (proposed)
- **Dependencies:** PB-01 and approval of the role-and-permission matrix.
- **Proposed Owner:** Arda
- **Quality Reviewer:** Ahmet
- **Status:** Pending approval of the role-and-permission matrix.

# PB-03 – Student Management

- **Epic:** Student Affairs
- **User Story:** As an authorized administrator, I want to create, list, and update student records so that student information can be managed.

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
- **User Story:** As an authorized administrator, I want to create courses and update existing course information so that course records can be maintained.

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
- **User Story:** As a student, I want to enroll in a course when I meet the enrollment conditions and view my current course enrollments.

**Acceptance Criteria:**

1. A student must be able to enroll in a course when the approved enrollment conditions are met and the enrollment period is open.
2. A second enrollment record for the same student, course, and term must be prevented; the API must return HTTP `409 Conflict`.
3. A new enrollment request submitted while the enrollment period is closed must be rejected with HTTP `409 Conflict`.
4. A student must be able to view only their own course enrollments; a request to view another student's enrollments must return HTTP `403 Forbidden` and must not disclose those records.
5. When an enrollment condition formally approved by the Product Owner and team is not met, the API must reject the request with HTTP `422 Unprocessable Content`.
6. For a successful enrollment, the system must create one enrollment record for the requested student, course, and term and make it visible in that student's enrollment list.
7. The response-code mapping (`409` for duplicate enrollment or a closed enrollment period, and `422` for a failed eligibility condition that the Product Owner and team have approved) is proposed for measurable testing; Arda and the team must confirm it in the API contract before it is treated as approved.

**Open Decisions:**

- Is active student status required for enrollment?
- Must course capacity be checked?
- Do course prerequisites apply?
- Who defines the enrollment dates for each term?

These rules must be finalized by the Product Owner and the team. Unapproved conditions must not be treated as established system requirements.

- **Priority:** P1 – High (proposed)
- **Story Points:** 8 (proposed)
- **Dependencies:** PB-03, PB-04, and approval of enrollment conditions.
- **Business Rules Advisor:** Nurefşan
- **Validation Advisor:** Ahmet
- **Status:** Pending clarification of enrollment conditions and team estimation.

# PB-06 – Instructor Grade Entry

- **Epic:** Grade Management
- **User Story:** As an instructor, I want to enter grades for students enrolled in a course assigned to me.

**Acceptance Criteria:**

1. Only an instructor assigned to the relevant course must be able to enter grades for that course.
2. Values outside the approved grading range must be rejected.
3. Entering a grade for a student who is not enrolled in the relevant course must be prevented.
4. A successfully saved grade must be retrievable later.
5. An unauthorized user must not be able to perform grade-entry operations.

- **Priority:** P2 – Medium (proposed)
- **Story Points:** 8 (proposed)
- **Dependencies:** PB-02, PB-05, instructor/course assignment, and approval of the grading scale.
- **Proposed Owner:** To be determined by the implementation team.
- **Acceptance Criteria Advisors:** Nurefşan and Ahmet
- **Status:** Pending approval of grading scale and publication rules.

# PB-07 – Student Grade Viewing

- **Epic:** Grade Management
- **User Story:** As a student, I want to view the grades published for my courses.

**Acceptance Criteria:**

1. A student must be able to view only their own published grades.
2. Grades that have not yet been published must not be displayed to the student.
3. If the student has no published grades, the system must display the message: "No published grades are available."
4. If a student attempts to access another student's grade information through a direct request, access must be denied.
5. When a grade-viewing request is successful, only information the student is authorized to access must be displayed.

- **Priority:** P2 – Medium (proposed)
- **Story Points:** 3 (proposed)
- **Dependencies:** PB-06 and approval of the grade publication rule.
- **Proposed Owner:** To be determined by the implementation team.
- **Validation Advisor:** Ahmet
- **Status:** Pending approval of the empty-state message proposal and publication rule.

# 8. Prioritization and Estimation Notes

P1, P2, and P3 values are initial priority proposals.

Story Point values represent relative effort and uncertainty; they must not be interpreted as working hours.

Priorities should be reviewed by the Product Owner together with team input. Story Point values must be estimated by the development team.

# 9. Dependencies and Responsibilities

The dependencies of PB-01–PB-07 are listed above.

Proposed owners are not confirmed assignments. Implementation tasks should be assigned by the team according to capacity and expertise.

# 10. Approval and Tracking

- **Product Owner approval:** [TODO]
- **Team estimates:** [TODO]
- **Implementation assignments:** [TODO]
- **API mapping with Arda:** [TODO]
- **GitHub Issue mapping with Mert:** [TODO]
- **Quality review by Ahmet:** [TODO]

Approved backlog items should later be mapped to actual GitHub Issues.

A backlog item should be considered complete only after its acceptance criteria have been verified, relevant tests have passed, required documentation has been updated, and the independent review process has been completed.
