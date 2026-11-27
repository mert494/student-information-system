import { useEffect, useState } from 'react';
import { fetchHealth, type HealthResponse } from './api/health';

type HealthState =
  | { kind: 'loading' }
  | { kind: 'ready'; health: HealthResponse }
  | { kind: 'error' };

export default function App() {
  const [attempt, setAttempt] = useState(0);
  const [state, setState] = useState<HealthState>({ kind: 'loading' });

  useEffect(() => {
    const controller = new AbortController();
    let active = true;
    setState({ kind: 'loading' });
    const timeout = window.setTimeout(() => {
      controller.abort();
      if (active) setState({ kind: 'error' });
    }, 5_000);
    void fetchHealth(controller.signal)
      .then((health) => {
        window.clearTimeout(timeout);
        if (active && !controller.signal.aborted) setState({ kind: 'ready', health });
      })
      .catch(() => {
        window.clearTimeout(timeout);
        if (active) setState({ kind: 'error' });
      });
    return () => {
      active = false;
      window.clearTimeout(timeout);
      controller.abort();
    };
  }, [attempt]);

  return (
    <main>
      <p className="eyebrow">SPRINT 3 · LOCAL CANDIDATE</p>
      <h1>SIS technical foundation</h1>
      <p>Architecture and product approval are pending.</p>
      <section aria-labelledby="health-title">
        <h2 id="health-title">Backend connection</h2>
        {state.kind === 'loading' && <p role="status">Checking backend…</p>}
        {state.kind === 'ready' && (
          <div role="status">
            <p className="connected">Backend connected</p>
            <p>Process uptime: {state.health.uptimeSeconds} seconds</p>
          </div>
        )}
        {state.kind === 'error' && (
          <p role="alert">Backend unavailable. Start the backend and try again.</p>
        )}
        <button disabled={state.kind === 'loading'} onClick={() => setAttempt((value) => value + 1)}>
          Check again
        </button>
      </section>
      <p className="note">Health confirms process availability only. SIS features and database checks are not implemented.</p>
    </main>
  );
}
