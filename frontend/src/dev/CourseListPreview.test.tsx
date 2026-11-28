import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { describe, expect, it, vi } from 'vitest';
import { CourseListPreview } from './CourseListPreview';

describe('synthetic Course List review page', () => {
  it('labels the records as synthetic and displays courses without contacting a service', () => {
    const request = vi.fn();
    vi.stubGlobal('fetch', request);
    render(<CourseListPreview />);
    expect(screen.getByRole('heading', { level: 1, name: 'Course list' })).toBeVisible();
    expect(screen.getByText('Synthetic data')).toBeVisible();
    expect(screen.getByRole('combobox', { name: 'Preview state' })).toHaveAccessibleDescription(/Switch states/);
    expect(screen.getAllByRole('listitem')).toHaveLength(4);
    expect(request).not.toHaveBeenCalled();
  });

  it('switches between distinct states and restores samples through the working retry control', async () => {
    const user = userEvent.setup();
    const request = vi.fn();
    vi.stubGlobal('fetch', request);
    render(<CourseListPreview />);
    const selector = screen.getByRole('combobox', { name: 'Preview state' });
    await user.selectOptions(selector, 'loading');
    expect(screen.getByRole('status')).toHaveTextContent('Loading courses…');
    await user.selectOptions(selector, 'empty');
    expect(screen.getByRole('status')).toHaveTextContent('No courses to display.');
    await user.selectOptions(selector, 'error');
    expect(screen.getByRole('alert')).toHaveTextContent('Sample error:');
    expect(screen.queryByRole('list')).not.toBeInTheDocument();
    await user.click(screen.getByRole('button', { name: 'Try again' }));
    expect(screen.getAllByRole('listitem')).toHaveLength(4);
    expect(selector).toHaveValue('success');
    expect(selector).toHaveFocus();
    expect(request).not.toHaveBeenCalled();
  });

  it('keeps controls keyboard reachable and returns focus after a Space-key retry', async () => {
    const user = userEvent.setup();
    render(<CourseListPreview />);
    const selector = screen.getByRole('combobox', { name: 'Preview state' });
    await user.tab();
    expect(selector).toHaveFocus();
    await user.selectOptions(selector, 'error');
    await user.tab();
    expect(screen.getByRole('button', { name: 'Try again' })).toHaveFocus();
    await user.keyboard(' ');
    expect(screen.getByRole('status')).toHaveTextContent('4 courses shown');
    expect(selector).toHaveFocus();
    expect(screen.queryByRole('alert')).not.toBeInTheDocument();
  });
});
