package com.example.sis.health;

/** Process availability only; no database, authentication or SIS feature readiness. */
public record HealthResponse(String status, String service, long uptimeSeconds) {
}
