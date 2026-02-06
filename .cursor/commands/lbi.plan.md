---
description: "Create implementation plan"
---

# Implementation Plan

Break down the specification into actionable implementation steps.

## Prerequisites

- Complete `/lbi.specify` first
- Spec file exists at `.lbi/specs/{feature}/spec.md`

## Instructions

1. Read the specification at `.lbi/specs/{feature}/spec.md`
2. Break down into phases and tasks
3. Identify dependencies and order of implementation

## Plan Template

Create `.lbi/specs/{feature}/plan.md`:

```markdown
# Implementation Plan: {Feature Name}

## Overview
{Brief summary of implementation approach}

## Phases

### Phase 1: Setup
- [ ] {Task 1.1}: {Description}
- [ ] {Task 1.2}: {Description}

### Phase 2: Core Implementation
- [ ] {Task 2.1}: {Description}
- [ ] {Task 2.2}: {Description}

### Phase 3: Integration
- [ ] {Task 3.1}: {Description}
- [ ] {Task 3.2}: {Description}

### Phase 4: Testing
- [ ] {Task 4.1}: Write unit tests
- [ ] {Task 4.2}: Write integration tests

### Phase 5: Documentation
- [ ] {Task 5.1}: Update README
- [ ] {Task 5.2}: Add code comments

## Files to Create/Modify

| File | Action | Purpose |
|------|--------|---------|
| {path} | Create | {Description} |
| {path} | Modify | {Description} |

## Risk Assessment

| Risk | Mitigation |
|------|------------|
| {Risk 1} | {How to handle} |

## Estimated Effort
{T-shirt size: S/M/L/XL}
```

## Next Steps

After planning, run `/lbi.implement` to begin implementation.