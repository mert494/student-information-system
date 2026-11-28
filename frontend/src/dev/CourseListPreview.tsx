import { useRef, useState } from 'react';
import { CourseList } from '../courses/CourseList';
import type { CourseListState } from '../courses/CourseSummary';
import { syntheticCourses } from './courseFixtures';
import './course-preview.css';

type PreviewScenario = 'success' | 'loading' | 'empty' | 'error';
const scenarios: Record<PreviewScenario, CourseListState> = {
  success: { status: 'success', courses: syntheticCourses },
  loading: { status: 'loading' },
  empty: { status: 'success', courses: [] },
  error: { status: 'error', message: 'Sample error: course information could not be loaded.' },
};

/** Isolated review adapter. No network, authenticated identity or academic actions. */
export function CourseListPreview() {
  const [scenario, setScenario] = useState<PreviewScenario>('success');
  const selector = useRef<HTMLSelectElement>(null);

  function restoreSamples() {
    setScenario('success');
    selector.current?.focus();
  }

  return (
    <div className="course-preview">
      <header className="course-preview__masthead">
        <span className="course-preview__brand">SIS <span>/ Component preview</span></span>
        <span className="course-preview__badge">Synthetic data</span>
      </header>
      <main className="course-preview__main">
        <div className="course-preview__intro">
          <p className="course-preview__eyebrow">SPRINT 3 · LOCAL UI CANDIDATE</p>
          <h1>Course list</h1>
          <p>Explore the course list with sample records. These courses are synthetic.</p>
        </div>
        <div className="course-preview__controls">
          <div>
            <label htmlFor="preview-state">Preview state</label>
            <p id="preview-state-help">Switch states to review the interface. Try again restores the sample courses.</p>
          </div>
          <select id="preview-state" ref={selector} value={scenario} aria-describedby="preview-state-help"
            onChange={(event) => setScenario(event.currentTarget.value as PreviewScenario)}>
            <option value="success">Loaded courses</option>
            <option value="loading">Loading</option>
            <option value="empty">Empty list</option>
            <option value="error">Error</option>
          </select>
        </div>
        <CourseList state={scenarios[scenario]} onRetry={restoreSamples} />
        <p className="course-preview__footer">Synthetic preview · No live course data</p>
      </main>
    </div>
  );
}
