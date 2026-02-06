---
description: "Configure security scanning and compliance"
---

# Security Setup

Set up security scanning, vulnerability detection, and compliance checks.

## Purpose

Integrate security into the CI/CD pipeline to catch vulnerabilities early.

## Prerequisites

- CI/CD pipeline configured
- Understanding of security requirements

## Instructions

1. Configure dependency scanning
2. Set up code security analysis
3. Enable secret detection
4. Configure compliance checks

## Dependency Scanning

### Python Projects

```yaml
# Add to CI workflow
- name: Install security tools
  run: |
    pip install safety pip-audit bandit

- name: Check for known vulnerabilities
  run: safety check

- name: Audit dependencies
  run: pip-audit

- name: Run security linter
  run: bandit -r src/ -ll
```

### Automated Dependabot

Create `.github/dependabot.yml`:

```yaml
version: 2
updates:
  - package-ecosystem: "pip"
    directory: "/"
    schedule:
      interval: "weekly"
    open-pull-requests-limit: 10
    labels:
      - "dependencies"
      - "security"
```

## Code Security Analysis

### Bandit Configuration

Create `bandit.yaml`:

```yaml
skips:
  - B101  # assert_used (OK in tests)
  - B104  # hardcoded_bind_all_interfaces (review needed)

exclude_dirs:
  - tests
  - .venv
```

### GitHub Code Scanning

```yaml
name: Security Scan

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  schedule:
    - cron: '0 0 * * 0'  # Weekly

jobs:
  codeql:
    runs-on: ubuntu-latest
    permissions:
      security-events: write
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Initialize CodeQL
        uses: github/codeql-action/init@v3
        with:
          languages: python
      
      - name: Perform CodeQL Analysis
        uses: github/codeql-action/analyze@v3
```

## Secret Detection

### Pre-commit Hooks

Create `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/Yelp/detect-secrets
    rev: v1.4.0
    hooks:
      - id: detect-secrets
        args: ['--baseline', '.secrets.baseline']
```

### GitHub Secret Scanning

Enable in repository settings:
- Settings → Security → Secret scanning ✓

### Gitleaks

```yaml
- name: Scan for secrets
  uses: gitleaks/gitleaks-action@v2
  env:
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

## Security Headers

For web applications:

```yaml
- name: Check security headers
  run: |
    pip install securityheaders
    securityheaders https://your-app.com
```

## Compliance Checks

### OWASP Dependency Check

```yaml
- name: OWASP Dependency Check
  uses: dependency-check/Dependency-Check_Action@main
  with:
    project: 'my-project'
    path: '.'
    format: 'HTML'
```

## Security Checklist

```markdown
## Security Configuration Status

### Automated Scanning

- [ ] Dependency vulnerability scanning (safety/pip-audit)
- [ ] Static code analysis (bandit)
- [ ] Secret detection (detect-secrets/gitleaks)
- [ ] Container scanning (if applicable)

### GitHub Security Features

- [ ] Dependabot alerts enabled
- [ ] Dependabot security updates enabled
- [ ] Code scanning enabled
- [ ] Secret scanning enabled

### Process

- [ ] Security review in PR checklist
- [ ] Dependency update process
- [ ] Incident response plan
```

## Output

Create security scanning configuration files.

## Next Steps

After security setup:
1. Run `/lbi.telemetry-check` for observability
2. Run `/lbi.preflight` before deployment