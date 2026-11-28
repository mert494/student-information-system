export function LoadingState() {
  return (
    <div className="course-state">
      <p className="course-state__title" role="status">Loading courses…</p>
      <p>Waiting for course information.</p>
      <div className="course-skeleton" aria-hidden="true">
        <span /><span /><span />
      </div>
    </div>
  );
}

export function EmptyState() {
  return (
    <div className="course-state">
      <p className="course-state__title" role="status">No courses to display.</p>
      <p>Courses will appear here when they are available.</p>
    </div>
  );
}

export interface ErrorStateProps {
  /** Caller-supplied, user-safe text. Never pass raw server errors or credentials. */
  message?: string;
  onRetry?: () => void;
}

export function ErrorState({ message = 'Courses could not be loaded.', onRetry }: ErrorStateProps) {
  return (
    <div className="course-state course-state--error">
      <p className="course-state__title" role="alert">{message}</p>
      <p>The course list is unavailable. Please try again.</p>
      {onRetry && <button className="course-button" type="button" onClick={onRetry}>Try again</button>}
    </div>
  );
}
