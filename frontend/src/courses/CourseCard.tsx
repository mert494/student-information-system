import type { CourseSummary } from './CourseSummary';

/** A read-only list item. Identity is used by the parent as a stable key. */
export function CourseCard({ course }: { course: CourseSummary }) {
  return (
    <li className="course-card">
      <p className="course-card__code">
        <span className="course-card__label">Course code</span>
        <span>{course.courseCode}</span>
      </p>
      <h3 className="course-card__title">{course.title}</h3>
    </li>
  );
}
