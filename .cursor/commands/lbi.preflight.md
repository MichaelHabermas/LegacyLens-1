---
description: "Run pre-deployment checks"
---

# Preflight Check

Run comprehensive checks before deployment.

## Purpose

Verify everything is ready for deployment to catch issues early.

## Prerequisites

- Feature complete and tested
- CI passing

## Instructions

1. Run all automated checks
2. Verify manual requirements
3. Document any exceptions
4. Get sign-off

## Preflight Checks

### Code Quality

```bash
# Linting
ruff check src/ tests/

# Type checking
mypy src/ --strict

# Formatting
black --check src/ tests/
```

### Tests

```bash
# Unit tests
pytest tests/unit/ -v

# Integration tests
pytest tests/integration/ -v

# Coverage check
pytest --cov=src --cov-fail-under=85
```

### Security

```bash
# Dependency vulnerabilities
pip-audit

# Security linting
bandit -r src/ -ll

# Secret scanning
detect-secrets scan
```

### Build

```bash
# Clean build
rm -rf dist/ build/
python -m build

# Verify package
twine check dist/*
```

## Preflight Checklist

```markdown
## Preflight: {Feature/Release}

**Date**: {YYYY-MM-DD}
**Deployer**: {Name}

### Automated Checks

| Check | Command | Status |
|-------|---------|--------|
| Lint | `ruff check .` | ✅/❌ |
| Types | `mypy src/` | ✅/❌ |
| Unit Tests | `pytest tests/unit/` | ✅/❌ |
| Integration Tests | `pytest tests/integration/` | ✅/❌ |
| Coverage | `pytest --cov-fail-under=85` | ✅/❌ |
| Security | `pip-audit` | ✅/❌ |
| Build | `python -m build` | ✅/❌ |

### Manual Checks

- [ ] CHANGELOG updated
- [ ] Version bumped
- [ ] Documentation current
- [ ] Migration scripts tested
- [ ] Rollback plan documented

### Environment Checks

- [ ] Environment variables documented
- [ ] Secrets in vault/secrets manager
- [ ] Database migrations ready
- [ ] Feature flags configured

### Stakeholder Sign-off

| Role | Name | Approved | Date |
|------|------|----------|------|
| Engineering | {Name} | ✅/❌ | {Date} |
| QA | {Name} | ✅/❌ | {Date} |
| Product | {Name} | ✅/❌ | {Date} |

### Exceptions

| Item | Reason | Approved By |
|------|--------|-------------|
| {Item} | {Reason} | {Name} |
```

## Automated Preflight Script

```bash
#!/bin/bash
set -e

echo "🔍 Running preflight checks..."

echo "📝 Linting..."
ruff check src/ tests/

echo "🔤 Type checking..."
mypy src/

echo "🧪 Running tests..."
pytest tests/ --cov=src --cov-fail-under=85

echo "🔒 Security scan..."
pip-audit
bandit -r src/ -ll

echo "📦 Building..."
python -m build
twine check dist/*

echo "✅ All preflight checks passed!"
```

## Next Steps

After preflight:
1. Run `/lbi.ready-to-push` for final verification
2. Proceed with deployment