import { describe, expect, it, vi } from 'vitest';
import { fetchHealth } from './health';

describe('health API boundary', () => {
  it('requests the same-origin proxy with cancellation and validates a healthy response', async () => {
    const data = { status: 'UP', service: 'sis-foundation', uptimeSeconds: 12 };
    const request = vi.fn().mockResolvedValue({ ok: true, json: async () => data });
    vi.stubGlobal('fetch', request);
    const controller = new AbortController();

    await expect(fetchHealth(controller.signal)).resolves.toEqual(data);
    expect(request).toHaveBeenCalledWith('/api/health', {
      headers: { Accept: 'application/json' }, credentials: 'omit', signal: controller.signal,
    });
  });

  it('rejects failed HTTP responses instead of treating them as healthy', async () => {
    vi.stubGlobal('fetch', vi.fn().mockResolvedValue({ ok: false, status: 503 }));
    await expect(fetchHealth(new AbortController().signal)).rejects.toThrow('503');
  });

  it.each([null, [], { status: 'DOWN' }, { status: 'UP', service: 'other', uptimeSeconds: 1 },
    { status: 'UP', service: 'sis-foundation', uptimeSeconds: -1 },
    { status: 'UP', service: 'sis-foundation', uptimeSeconds: 1.5 }])(
    'rejects an invalid health payload: %j', async (data) => {
      vi.stubGlobal('fetch', vi.fn().mockResolvedValue({ ok: true, json: async () => data }));
      await expect(fetchHealth(new AbortController().signal)).rejects.toThrow('Unexpected health response');
    },
  );

  it('preserves network failures for the UI to handle', async () => {
    vi.stubGlobal('fetch', vi.fn().mockRejectedValue(new TypeError('Network unavailable')));
    await expect(fetchHealth(new AbortController().signal)).rejects.toThrow('Network unavailable');
  });
});
