package com.example.sis.health;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;

import java.lang.management.RuntimeMXBean;
import org.junit.jupiter.api.Test;

class HealthServiceTest {
    @Test
    void reportsWholeSecondsFromTheLiveRuntime() {
        RuntimeMXBean runtime = mock(RuntimeMXBean.class);
        when(runtime.getUptime()).thenReturn(12_999L);

        HealthResponse response = new HealthService(runtime).current();

        assertEquals("UP", response.status());
        assertEquals("sis-foundation", response.service());
        assertEquals(12, response.uptimeSeconds());
        verify(runtime).getUptime();
    }

    @Test
    void supportsTheFirstSecondAfterProcessStartup() {
        RuntimeMXBean runtime = mock(RuntimeMXBean.class);
        when(runtime.getUptime()).thenReturn(999L);

        assertEquals(0, new HealthService(runtime).current().uptimeSeconds());
    }

    @Test
    void readsFreshUptimeOnEveryHealthRequest() {
        RuntimeMXBean runtime = mock(RuntimeMXBean.class);
        when(runtime.getUptime()).thenReturn(1_000L, 5_000L);
        HealthService service = new HealthService(runtime);

        assertEquals(1, service.current().uptimeSeconds());
        assertEquals(5, service.current().uptimeSeconds());
    }
}
