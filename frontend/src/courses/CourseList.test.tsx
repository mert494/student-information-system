import { render, screen, within } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { describe, expect, it, vi } from 'vitest';
import { CourseList } from './CourseList';
import type { CourseSummary } from './CourseSummary';

const courses: readonly CourseSummary[] = [
  { courseId: 'synthetic-a', courseCode: 'DEMO 101', title: 'Introduction to Computer Science' },
  { courseId: 'synthetic-b', courseCode: 'DEMO 202', title: 'Software Engineering' },
];

describe('CourseList presentation', () => {
  it('renders multiple courses in a named semantic list with headings and codes', () => {
    render(<CourseList state={{ status: 'success', courses }} />);
    const region = screen.getByRole('region', { name: 'Courses' });
    expect(within(region).getByRole('heading', { level: 2 })).toHaveTextContent('Courses');
    const items = within(screen.getByRole('list', { name: 'Courses' })).getAllByRole('listitem');
    expect(items).toHaveLength(2);
    courses.forEach((course, index) => {
      expect(within(items[index]).getByRole('heading', { level: 3 })).toHaveTextContent(course.title);
      expect(within(items[index]).getByText(course.courseCode)).toBeVisible();
    });
    expect(screen.getByRole('status')).toHaveTextContent('2 courses shown');
    expect(screen.queryByRole('button')).not.toBeInTheDocument();
  });

  it('announces successful empty results without presenting a failure or loading message', () => {
    render(<CourseList state={{ status: 'success', courses: [] }} />);
    expect(screen.getByRole('status')).toHaveTextContent('No courses to display.');
    expect(screen.queryByRole('list')).not.toBeInTheDocument();
    expect(screen.queryByRole('alert')).not.toBeInTheDocument();
    expect(screen.queryByText('Loading courses…')).not.toBeInTheDocument();
  });

  it('announces loading separately from an empty response', () => {
    render(<CourseList state={{ status: 'loading' }} />);
    expect(screen.getByRole('status')).toHaveTextContent('Loading courses…');
    expect(screen.queryByText('No courses to display.')).not.toBeInTheDocument();
    expect(screen.queryByRole('list')).not.toBeInTheDocument();
    expect(screen.queryByRole('alert')).not.toBeInTheDocument();
  });

  it('announces an injected user-safe API error and does not mistake it for an empty list', () => {
    render(<CourseList state={{ status: 'error', message: 'Course information is temporarily unavailable.' }} />);
    expect(screen.getByRole('alert')).toHaveTextContent('Course information is temporarily unavailable.');
    expect(screen.queryByRole('status')).not.toBeInTheDocument();
    expect(screen.queryByRole('list')).not.toBeInTheDocument();
    expect(screen.queryByRole('button')).not.toBeInTheDocument();
  });

  it('uses a safe default error and invokes the real retry callback by keyboard', async () => {
    const user = userEvent.setup();
    const retry = vi.fn();
    render(<CourseList state={{ status: 'error' }} onRetry={retry} />);
    expect(screen.getByRole('alert')).toHaveTextContent('Courses could not be loaded.');
    await user.tab();
    expect(screen.getByRole('button', { name: 'Try again' })).toHaveFocus();
    await user.keyboard('{Enter}');
    expect(retry).toHaveBeenCalledTimes(1);
  });

  it('preserves a long Unicode title and an unbroken title without truncating their text', () => {
    const title = 'İleri düzey İnsan–Bilgisayar Etkileşimi ve Erişilebilir Arayüz Tasarımı — '.repeat(5);
    const unbroken = 'SyntheticLongCourseTitle'.repeat(12);
    render(<CourseList state={{ status: 'success', courses: [
      { ...courses[0], title }, { ...courses[1], title: unbroken },
    ] }} />);
    const headings = screen.getAllByRole('heading', { level: 3 });
    expect(headings[0].textContent).toBe(title);
    expect(headings[1].textContent).toBe(unbroken);
    expect(headings[0]).toBeVisible();
    expect(headings[1]).toBeVisible();
  });

  it('removes stale course data during loading and failure, then displays a fresh result', () => {
    const view = render(<CourseList state={{ status: 'success', courses }} />);
    view.rerender(<CourseList state={{ status: 'loading' }} />);
    expect(screen.queryByText(courses[0].title)).not.toBeInTheDocument();
    view.rerender(<CourseList state={{ status: 'error' }} />);
    expect(screen.queryByRole('list')).not.toBeInTheDocument();
    view.rerender(<CourseList state={{ status: 'success', courses: [courses[1]] }} />);
    expect(screen.getByRole('status')).toHaveTextContent('1 course shown');
    expect(screen.queryByRole('alert')).not.toBeInTheDocument();
    expect(screen.getAllByRole('listitem')).toHaveLength(1);
  });

  it('supports separately named instances without duplicate heading IDs', () => {
    render(<><CourseList heading="First sample" state={{ status: 'loading' }} />
      <CourseList heading="Second sample" state={{ status: 'success', courses }} /></>);
    const first = screen.getByRole('region', { name: 'First sample' });
    const second = screen.getByRole('region', { name: 'Second sample' });
    expect(first.getAttribute('aria-labelledby')).not.toBe(second.getAttribute('aria-labelledby'));
    expect(within(second).getByRole('list', { name: 'Second sample' })).toBeVisible();
  });
});
