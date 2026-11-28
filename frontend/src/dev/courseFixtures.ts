import type { CourseSummary } from '../courses/CourseSummary';

/** Synthetic records for the separate review page only. No business service uses these. */
export const syntheticCourses: readonly CourseSummary[] = [
  { courseId: 'synthetic-course-1', courseCode: 'DEMO 101', title: 'Introduction to Computer Science' },
  { courseId: 'synthetic-course-2', courseCode: 'DEMO 202', title: 'Software Engineering' },
  { courseId: 'synthetic-course-3', courseCode: 'DEMO 303', title: 'Databases and Information Systems' },
  { courseId: 'synthetic-course-4', courseCode: 'DEMO 404', title: 'Special Topics in Human–Computer Interaction and Accessible Interface Design' },
];
