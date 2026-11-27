package com.example.sis.health;

import java.lang.management.RuntimeMXBean;
import org.springframework.stereotype.Service;

@Service
public class HealthService {
    private final RuntimeMXBean runtime;

    public HealthService(RuntimeMXBean runtime) {
        this.runtime = runtime;
    }

    public HealthResponse current() {
        return new HealthResponse("UP", "sis-foundation", runtime.getUptime() / 1_000);
    }
}
