---
description: "Configure test matrix for multiple environments"
---

# CI Matrix Configuration

Set up testing across multiple Python versions, OS, and configurations.

## Purpose

Ensure compatibility across supported environments using matrix builds.

## Prerequisites

- Basic CI/CD setup via `/lbi.ci-setup`
- Understanding of supported environments

## Instructions

1. Define supported environments
2. Configure matrix strategy
3. Set up caching
4. Handle platform-specific tests

## Matrix Strategy

### Python Version Matrix

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ['3.9', '3.10', '3.11', '3.12']
      fail-fast: false
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
      
      - name: Install dependencies
        run: pip install -e ".[dev]"
      
      - name: Run tests
        run: pytest tests/
```

### OS Matrix

```yaml
jobs:
  test:
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
        python-version: ['3.11']
    
    runs-on: ${{ matrix.os }}
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
      
      - name: Install dependencies
        run: pip install -e ".[dev]"
      
      - name: Run tests
        run: pytest tests/
```

### Full Matrix

```yaml
jobs:
  test:
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
        python-version: ['3.10', '3.11', '3.12']
        exclude:
          # Exclude specific combinations
          - os: macos-latest
            python-version: '3.10'
      fail-fast: false
    
    runs-on: ${{ matrix.os }}
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
          cache: 'pip'
      
      - name: Install dependencies
        run: pip install -e ".[dev]"
      
      - name: Run tests
        run: pytest tests/ -v
```

## Caching Strategies

### Pip Cache

```yaml
- uses: actions/setup-python@v5
  with:
    python-version: '3.11'
    cache: 'pip'
    cache-dependency-path: '**/pyproject.toml'
```

### Custom Cache

```yaml
- name: Cache dependencies
  uses: actions/cache@v4
  with:
    path: ~/.cache/pip
    key: ${{ runner.os }}-pip-${{ hashFiles('**/pyproject.toml') }}
    restore-keys: |
      ${{ runner.os }}-pip-
```

## Conditional Jobs

```yaml
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: pip install ruff && ruff check .
  
  test:
    needs: lint  # Only run if lint passes
    strategy:
      matrix:
        python-version: ['3.10', '3.11', '3.12']
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: pytest tests/
  
  deploy:
    needs: test  # Only run if all tests pass
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - run: echo "Deploy!"
```

## Matrix Configuration Template

```markdown
## Supported Environments

| Dimension | Values | Notes |
|-----------|--------|-------|
| Python | 3.10, 3.11, 3.12 | 3.9 EOL Dec 2025 |
| OS | Linux, Windows, macOS | Primary: Linux |
| Database | PostgreSQL 14, 15, 16 | If applicable |

## Matrix Size

- Total combinations: {N}
- Estimated CI time: {X} minutes
- Parallel jobs: {Y}
```

## Next Steps

After matrix setup:
1. Run `/lbi.security-setup` for security scanning
2. Run `/lbi.telemetry-check` for observability