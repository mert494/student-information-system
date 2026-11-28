package com.example.sis.health;

import static org.junit.jupiter.api.Assertions.assertSame;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;

import org.junit.jupiter.api.Test;

class HealthControllerTest {
    @Test
    void returnsTheCurrentServiceSnapshotWithoutFabricatingHealth() {
        HealthService service = mock(HealthService.class);
        HealthResponse expected = new HealthResponse("UP", "sis-foundation", 72);
        when(service.current()).thenReturn(expected);

        assertSame(expected, new HealthController(service).health());
        verify(service).current();
    }
}
