package com.example.sis.health;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HealthController {
    private final HealthService health;

    public HealthController(HealthService health) {
        this.health = health;
    }

    @GetMapping(value = "/health", produces = "application/json")
    public HealthResponse health() {
        return health.current();
    }
}
