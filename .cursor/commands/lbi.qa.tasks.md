---
description: "Break down QA test plan into actionable tasks"
---

# QA Tasks

Convert the test plan into discrete, trackable tasks.

## Purpose

Transform the test plan into a checklist of implementable test tasks.

## Prerequisites

- Test plan at `.lbi/specs/{feature}/qa/test-plan.md`

## Instructions

1. Review the test plan
2. Break down each test category into tasks
3. Estimate effort and set priorities
4. Create task checklist

## Task Breakdown Template

Create `.lbi/specs/{feature}/qa/tasks.md`:

```markdown
# QA Tasks: {Feature Name}

## Overview

**Total Tasks**: {count}
**Estimated Effort**: {hours}

## Phase 1: Test Infrastructure

- [ ] **S** Set up test database fixtures
- [ ] **S** Configure test environment variables
- [ ] **M** Create mock services for external APIs
- [ ] **S** Set up test data factories

## Phase 2: Unit Tests

- [ ] **M** Test {Component A} business logic
- [ ] **M** Test {Component B} validation
- [ ] **S** Test utility functions
- [ ] **M** Test error handling paths

## Phase 3: Integration Tests

- [ ] **L** Test API endpoint {endpoint 1}
- [ ] **L** Test API endpoint {endpoint 2}
- [ ] **M** Test database operations
- [ ] **M** Test service integrations

## Phase 4: E2E Tests

- [ ] **L** Test complete user workflow
- [ ] **M** Test error recovery flows
- [ ] **M** Test edge case scenarios

## Phase 5: Quality Gates

- [ ] **S** Verify coverage thresholds
- [ ] **S** Run security scan
- [ ] **S** Performance baseline check

## Task Sizing

- **S (Small)**: < 30 min, single test file
- **M (Medium)**: 30-60 min, multiple tests
- **L (Large)**: 1-2 hours, complex scenarios

## Dependencies

- Phase 2 can start after Phase 1
- Phase 3 requires Phase 2 completion
- Phase 4 requires Phase 3 completion

## Progress

- Started: {date}
- Current Phase: {1-5}
- Blocked: {none}
```

## Next Steps

After creating tasks:
1. Run `/lbi.qa.scaffold-tests` to create test file structure
2. Run `/lbi.qa.implement` to write the tests