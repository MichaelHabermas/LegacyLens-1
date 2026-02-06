---
description: "Break down plan into discrete tasks"
---

# Analyze & Create Tasks

Break down the implementation plan into discrete, actionable tasks.

## Prerequisites

- Complete `/lbi.plan` first
- Plan file exists at `.lbi/specs/{feature}/plan.md`

## Instructions

1. Read the plan at `.lbi/specs/{feature}/plan.md`
2. Break each phase into specific tasks
3. Add time estimates and priorities
4. Create task checklist for tracking

## Task Analysis Process

### Step 1: Identify Work Units

For each phase in the plan, identify:

- Individual code changes
- Files to create or modify
- Tests to write
- Documentation to update

### Step 2: Estimate Complexity

Rate each task:

- **S (Small)**: < 30 minutes, single file change
- **M (Medium)**: 30-60 minutes, few files
- **L (Large)**: 1-2 hours, multiple components
- **XL (Extra Large)**: > 2 hours, consider breaking down

### Step 3: Prioritize

Order tasks by:

1. Dependencies (what must come first)
2. Risk (tackle unknowns early)
3. Value (core functionality first)

## Tasks Template

Create `.lbi/specs/{feature}/tasks.md`:

```markdown
# Tasks: {Feature Name}

## Overview
Total: {X} tasks | Estimated: {Y} hours

## Phase 1: Setup
- [ ] **S** Create directory structure
- [ ] **S** Add configuration file
- [ ] **M** Set up dependencies

## Phase 2: Core Implementation
- [ ] **L** Implement main logic in `src/module.py`
- [ ] **M** Add data models
- [ ] **M** Implement validation

## Phase 3: Integration
- [ ] **M** Connect to existing services
- [ ] **S** Update API routes
- [ ] **M** Add error handling

## Phase 4: Testing
- [ ] **M** Write unit tests
- [ ] **M** Write integration tests
- [ ] **S** Add test fixtures

## Phase 5: Polish
- [ ] **S** Add logging
- [ ] **S** Update documentation
- [ ] **S** Code review prep

## Dependencies Graph
- Phase 2 depends on Phase 1
- Phase 3 depends on Phase 2
- Phase 4 can start after Phase 2
- Phase 5 after all phases complete

## Progress Tracking
- Started: {date}
- Current Phase: {1-5}
- Blocked: {none or description}
```

## Task Checklist Rules

1. Each task should be completable in one session
2. Mark tasks complete immediately when done
3. Note blockers as they arise
4. Update estimates based on actuals

## Next Steps

After creating tasks, run `/lbi.implement` to begin implementation.