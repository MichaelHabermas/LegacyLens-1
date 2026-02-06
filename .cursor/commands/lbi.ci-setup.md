---
description: "Set up CI/CD pipeline for the project"
---

# CI/CD Setup

Configure continuous integration and deployment pipelines.

## Purpose

Establish automated build, test, and deployment workflows for consistent quality and fast feedback.

## Prerequisites

- Git repository initialized
- Test suite available
- Deployment targets identified

## Instructions

1. Choose CI/CD platform
2. Configure build pipeline
3. Set up test automation
4. Configure deployment stages

## Platform Selection

| Platform | Best For | Pricing |
|----------|----------|---------|
| GitHub Actions | GitHub repos | Free tier available |
| GitLab CI | GitLab repos | Free tier available |
| CircleCI | Any repo | Free tier available |
| Jenkins | Self-hosted | Free (self-managed) |

## GitHub Actions Setup

### Basic Workflow

Create `.github/workflows/ci.yml`:

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -e ".[dev]"
      
      - name: Run linter
        run: ruff check src/ tests/
      
      - name: Run type checker
        run: mypy src/
      
      - name: Run tests
        run: pytest tests/ --cov=src --cov-report=xml
      
      - name: Upload coverage
        uses: codecov/codecov-action@v4
        with:
          file: ./coverage.xml

  build:
    needs: test
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Build package
        run: python -m build
      
      - name: Upload artifact
        uses: actions/upload-artifact@v4
        with:
          name: dist
          path: dist/
```

### Deployment Workflow

Create `.github/workflows/deploy.yml`:

```yaml
name: Deploy

on:
  push:
    tags:
      - 'v*'

jobs:
  deploy:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Build and publish
        env:
          TWINE_USERNAME: __token__
          TWINE_PASSWORD: ${{ secrets.PYPI_TOKEN }}
        run: |
          python -m build
          twine upload dist/*
```

## Quality Gates

```yaml
# Add to CI workflow
- name: Check coverage threshold
  run: |
    coverage report --fail-under=85

- name: Check for security issues
  run: |
    pip install safety
    safety check

- name: Check dependencies
  run: |
    pip install pip-audit
    pip-audit
```

## Branch Protection

Configure in GitHub Settings → Branches:

- [ ] Require pull request before merging
- [ ] Require status checks to pass
- [ ] Require conversation resolution
- [ ] Require signed commits (optional)

## Secrets Management

Required secrets for deployment:

| Secret | Purpose | Location |
|--------|---------|----------|
| `PYPI_TOKEN` | Package publishing | PyPI account |
| `CODECOV_TOKEN` | Coverage reports | Codecov account |
| `DEPLOY_KEY` | Server access | Target server |

## Output

Create `.github/workflows/` directory with workflow files.

## Next Steps

After CI setup:
1. Run `/lbi.ci-matrix` for multi-version testing
2. Run `/lbi.security-setup` for security scanning