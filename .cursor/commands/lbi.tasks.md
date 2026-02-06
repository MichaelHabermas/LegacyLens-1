---
description: "Create and manage implementation tasks"
---

# Tasks

Create a detailed task breakdown for implementation.

## Purpose

Convert plans into discrete, trackable implementation tasks.

## Prerequisites

- Plan at `.lbi/specs/{feature}/plan.md`

## Instructions

1. Review the implementation plan
2. Break down into atomic tasks
3. Estimate and prioritize
4. Track progress

## Task Template

Create `.lbi/specs/{feature}/tasks.md`:

```markdown
# Tasks: {Feature Name}

## Summary

| Metric | Value |
|--------|-------|
| Total Tasks | {N} |
| Completed | {X} |
| In Progress | {Y} |
| Blocked | {Z} |
| Progress | {%} |

## Phase 1: Setup

- [x] **S** Create feature branch
- [x] **S** Set up development environment
- [ ] **M** Configure dependencies

## Phase 2: Core Implementation

- [ ] **L** Implement {component A}
  - [ ] Create data models
  - [ ] Add business logic
  - [ ] Write unit tests
- [ ] **M** Implement {component B}
- [ ] **M** Add validation logic

## Phase 3: Integration

- [ ] **M** Connect to existing services
- [ ] **S** Add API endpoints
- [ ] **M** Implement error handling

## Phase 4: Testing

- [ ] **M** Write integration tests
- [ ] **S** Add e2e tests
- [ ] **S** Performance testing

## Phase 5: Documentation

- [ ] **S** Update README
- [ ] **S** Add inline documentation
- [ ] **S** Update API docs

## Task Sizing

| Size | Time | Description |
|------|------|-------------|
| S | < 30 min | Single file, simple change |
| M | 30-60 min | Few files, moderate complexity |
| L | 1-2 hours | Multiple files, complex logic |
| XL | > 2 hours | Consider breaking down |

## Blocked Items

| Task | Blocker | Owner | ETA |
|------|---------|-------|-----|
| {Task} | {Blocker} | {Who} | {When} |

## Notes

- {Important consideration}
- {Technical debt to track}
```

## Task Management

### Daily Updates

```markdown
## Progress Log

### {Date}

**Completed**:
- Task 1
- Task 2

**In Progress**:
- Task 3 (50%)

**Blockers**:
- {Blocker description}
```

## Next Steps

After tasks:
1. Run `/lbi.implement` to begin coding
2. Update task status as you progress