import { useId } from 'react';
import { CourseCard } from './CourseCard';
import { EmptyState, ErrorState, LoadingState } from './CourseStates';
import type { CourseListState } from './CourseSummary';
import './course-list.css';

export interface CourseListProps {
  state: CourseListState;
  heading?: string;
  /** Supplied by the host; omitted when retry is unavailable. No request is made here. */
  onRetry?: () => void;
}

/** Props-only presentation. The host owns requests, cancellation and permissions. */
export function CourseList({ state, heading = 'Courses', onRetry }: CourseListProps) {
  const headingId = useId();

  return (
    <section className="course-list" aria-labelledby={headingId}>
      <div className="course-list__heading">
        <h2 id={headingId}>{heading}</h2>
        <span className="course-list__type">Course catalog</span>
      </div>
      {state.status === 'loading' && <LoadingState />}
      {state.status === 'error' && <ErrorState message={state.message} onRetry={onRetry} />}
      {state.status === 'success' && (
        state.courses.length === 0 ? <EmptyState /> : (
          <>
            <p className="course-list__count" role="status">
              {state.courses.length} {state.courses.length === 1 ? 'course' : 'courses'} shown
            </p>
            <ul className="course-list__items" role="list" aria-label={heading}>
              {state.courses.map((course) => <CourseCard key={course.courseId} course={course} />)}
            </ul>
          </>
        )
      )}
    </section>
  );
}
