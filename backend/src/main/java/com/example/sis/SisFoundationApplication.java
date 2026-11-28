package com.example.sis;

import java.lang.management.ManagementFactory;
import java.lang.management.RuntimeMXBean;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
public class SisFoundationApplication {
    public static void main(String[] args) {
        SpringApplication.run(SisFoundationApplication.class, args);
    }

    @Bean
    RuntimeMXBean runtimeMxBean() {
        return ManagementFactory.getRuntimeMXBean();
    }
}
