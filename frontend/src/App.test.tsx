import { act, render, screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import App from './App';
import { fetchHealth } from './api/health';

vi.mock('./api/health', () => ({ fetchHealth: vi.fn() }));
const request = vi.mocked(fetchHealth);
const healthy = { status: 'UP', service: 'sis-foundation', uptimeSeconds: 7 } as const;

beforeEach(() => { request.mockReset(); });

describe('connection screen', () => {
  it('shows loading until a validated response arrives, then reports connection', async () => {
    let resolve!: (value: typeof healthy) => void;
    request.mockReturnValue(new Promise((done) => { resolve = done; }));
    render(<App />);

    expect(screen.getByRole('status')).toHaveTextContent('Checking backend');
    expect(screen.getByRole('button', { name: 'Check again' })).toBeDisabled();
    await act(async () => resolve(healthy));
    expect(await screen.findByRole('status')).toHaveTextContent('Backend connected');
    expect(screen.getByRole('status')).toHaveTextContent('7 seconds');
    expect(screen.getByRole('button')).toBeEnabled();
  });

  it('shows a real request failure and retries successfully', async () => {
    request.mockRejectedValueOnce(new Error('HTTP 503')).mockResolvedValueOnce(healthy);
    render(<App />);
    expect(await screen.findByRole('alert')).toHaveTextContent('Backend unavailable');

    await userEvent.click(screen.getByRole('button', { name: 'Check again' }));
    await waitFor(() => expect(screen.getByRole('status')).toHaveTextContent('Backend connected'));
    expect(request).toHaveBeenCalledTimes(2);
    expect(screen.queryByRole('alert')).not.toBeInTheDocument();
  });

  it('cancels an outstanding request when unmounted', () => {
    request.mockReturnValue(new Promise(() => {}));
    const view = render(<App />);
    const signal = request.mock.calls[0][0];
    expect(signal.aborted).toBe(false);
    view.unmount();
    expect(signal.aborted).toBe(true);
  });

  it('ends loading and cancels a backend request after five seconds', () => {
    vi.useFakeTimers();
    request.mockReturnValue(new Promise(() => {}));
    render(<App />);
    const signal = request.mock.calls[0][0];

    act(() => vi.advanceTimersByTime(5_000));

    expect(signal.aborted).toBe(true);
    expect(screen.getByRole('alert')).toHaveTextContent('Backend unavailable');
    expect(screen.getByRole('button')).toBeEnabled();
  });
});
