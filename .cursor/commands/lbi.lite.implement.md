---
description: "Quick implementation for lite workflow"
---

# Lite Implement

Implement the feature following the lite plan.

## Purpose

Execute the implementation for small, well-understood changes.

## Prerequisites

- Lite plan at `.lbi/specs/{feature}/lite-plan.md`
- Development environment ready

## Implementation Process

### Step 1: Create Branch

```bash
git checkout -b feature/{name}
```

### Step 2: Implement Changes

Follow the plan and implement each step:

```markdown
## Implementation Checklist

- [ ] Step 1: {Description}
- [ ] Step 2: {Description}
- [ ] Step 3: {Description}
- [ ] Write tests
- [ ] Run tests
- [ ] Manual verification
```

### Step 3: Quality Checks

```bash
# Run linter
ruff check src/ tests/

# Run type checker
mypy src/

# Run tests
pytest tests/ -v

# Check coverage
pytest --cov=src
```

### Step 4: Self-Review

Before committing, verify:

- [ ] Code matches the plan
- [ ] All acceptance criteria met
- [ ] Tests pass
- [ ] No debug code left
- [ ] Code is clean and readable

## Commit Format

```
type: brief description

- Change 1
- Change 2

Lite workflow: {feature-name}
```

## Implementation Notes Template

```markdown
# Implementation Notes: {Title}

## Changes Made

### {File 1}

- Added {functionality}
- Modified {existing code}

### {File 2}

- Created {new component}

## Deviations from Plan

{Any changes from the original plan and why}

## Test Results

```
pytest results here
```

## Manual Testing

- [ ] Tested {scenario 1}
- [ ] Tested {scenario 2}

## Known Issues

{Any issues discovered during implementation}
```

## Output

Create implementation and tests per the plan.

## Next Steps

After implementation:
1. Run `/lbi.lite.push` to complete