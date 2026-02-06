---
description: "Verify telemetry and observability configuration"
---

# Telemetry Check

Verify logging, metrics, and tracing are properly configured.

## Purpose

Ensure the application has adequate observability for debugging and monitoring in production.

## Prerequisites

- Application with logging/metrics code
- Observability requirements defined

## Instructions

1. Check logging configuration
2. Verify metrics collection
3. Validate tracing setup
4. Review alerting rules

## Logging Checklist

### Configuration

```markdown
## Logging Status

### Log Levels

- [ ] DEBUG: Development only
- [ ] INFO: Normal operations
- [ ] WARNING: Unexpected but handled
- [ ] ERROR: Failures requiring attention
- [ ] CRITICAL: System failures

### Log Format

- [ ] Timestamp included
- [ ] Log level included
- [ ] Request ID / Trace ID
- [ ] Structured format (JSON)

### Log Output

- [ ] Console output configured
- [ ] File output (if needed)
- [ ] Log aggregation service
```

### Python Logging Setup

```python
# logging_config.py
import logging
import json

class JsonFormatter(logging.Formatter):
    def format(self, record):
        return json.dumps({
            "timestamp": self.formatTime(record),
            "level": record.levelname,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
        })

# Configuration
LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "json": {
            "()": JsonFormatter,
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "json",
        },
    },
    "root": {
        "level": "INFO",
        "handlers": ["console"],
    },
}
```

## Metrics Checklist

```markdown
## Metrics Status

### Application Metrics

- [ ] Request count
- [ ] Request latency (p50, p95, p99)
- [ ] Error rate
- [ ] Active connections

### Business Metrics

- [ ] Key action counts
- [ ] Conversion rates
- [ ] User activity

### System Metrics

- [ ] CPU usage
- [ ] Memory usage
- [ ] Disk I/O
- [ ] Network I/O

### Metric Collection

- [ ] Prometheus endpoint exposed
- [ ] StatsD integration
- [ ] Custom metrics library
```

## Tracing Checklist

```markdown
## Tracing Status

### Distributed Tracing

- [ ] Trace ID propagation
- [ ] Span creation for key operations
- [ ] Cross-service correlation

### Instrumentation

- [ ] HTTP requests traced
- [ ] Database queries traced
- [ ] External API calls traced
- [ ] Background jobs traced

### Tracing Backend

- [ ] Jaeger / Zipkin configured
- [ ] Sampling rate set
- [ ] Trace retention policy
```

## Alerting Checklist

```markdown
## Alerting Status

### Critical Alerts

| Alert | Condition | Notification |
|-------|-----------|--------------|
| Error Rate High | > 1% | PagerDuty |
| Latency High | p99 > 2s | Slack |
| Service Down | Health check fail | PagerDuty |

### Warning Alerts

| Alert | Condition | Notification |
|-------|-----------|--------------|
| Error Rate Elevated | > 0.1% | Slack |
| Memory High | > 80% | Slack |

### Alert Configuration

- [ ] PagerDuty integration
- [ ] Slack integration
- [ ] Email notifications
- [ ] Escalation policy
```

## Verification Commands

```bash
# Check logging output
python -c "import logging; logging.basicConfig(level='INFO'); logging.info('test')"

# Check metrics endpoint
curl http://localhost:8000/metrics

# Check health endpoint
curl http://localhost:8000/health

# Verify tracing
curl -H "X-Request-ID: test-123" http://localhost:8000/api/endpoint
```

## Observability Report

```markdown
# Telemetry Verification Report

**Date**: {YYYY-MM-DD}
**Environment**: {dev/staging/prod}

## Summary

| Category | Status | Coverage |
|----------|--------|----------|
| Logging | ✅ | 100% |
| Metrics | ⚠️ | 70% |
| Tracing | ❌ | 0% |
| Alerting | ✅ | 90% |

## Issues Found

1. **{Issue}**: {Description}
   - **Impact**: {Impact}
   - **Recommendation**: {Fix}

## Action Items

- [ ] {Action 1}
- [ ] {Action 2}
```

## Next Steps

After telemetry check:
1. Address any gaps found
2. Run `/lbi.preflight` before deployment