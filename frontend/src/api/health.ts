export interface HealthResponse {
  status: 'UP';
  service: 'sis-foundation';
  uptimeSeconds: number;
}

function isHealthResponse(value: unknown): value is HealthResponse {
  if (typeof value !== 'object' || value === null) return false;
  const data = value as Record<string, unknown>;
  return data.status === 'UP'
    && data.service === 'sis-foundation'
    && typeof data.uptimeSeconds === 'number'
    && Number.isSafeInteger(data.uptimeSeconds)
    && data.uptimeSeconds >= 0;
}

export async function fetchHealth(signal: AbortSignal): Promise<HealthResponse> {
  const response = await fetch('/api/health', {
    headers: { Accept: 'application/json' },
    credentials: 'omit',
    signal,
  });
  if (!response.ok) throw new Error('Health request failed (' + response.status + ')');
  const data: unknown = await response.json();
  if (!isHealthResponse(data)) throw new Error('Unexpected health response');
  return data;
}
