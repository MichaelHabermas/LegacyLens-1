---
description: "Implement the planned changes"
---

# Implementation

Execute the implementation plan, writing code according to specifications.

## Prerequisites

- Complete `/lbi.plan` first
- Plan file exists at `.lbi/specs/{feature}/plan.md`

## Instructions

1. Read the plan at `.lbi/specs/{feature}/plan.md`
2. Implement each task in order
3. Mark tasks complete as you progress
4. Follow the project's coding standards

## Implementation Guidelines

### Code Quality

- Follow SOLID principles
- Use meaningful names
- Keep functions focused (single responsibility)
- Add type hints to all functions
- Write self-documenting code

### Commit Strategy

- Commit after completing each logical unit
- Use descriptive commit messages
- Reference the feature in commits

### Progress Tracking

Update `.lbi/specs/{feature}/plan.md` as you complete tasks:

```markdown
### Phase 2: Core Implementation
- [x] Task 2.1: Completed 2024-01-15
- [ ] Task 2.2: In progress
```

## Quality Checklist

Before moving to tests:

- [ ] All planned tasks completed
- [ ] Code follows project standards
- [ ] No linter errors
- [ ] Type hints added
- [ ] Basic error handling in place

## Next Steps

After implementation, run `/lbi.tests` to write and run tests.