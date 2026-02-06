---
description: "Create a comprehensive QA test plan for a feature"
---

# QA Test Plan

Create a structured test plan for quality assurance.

## Purpose

Define the testing strategy, scope, and approach for a feature before implementation begins.

## Prerequisites

- Feature specification at `.lbi/specs/{feature}/spec.md`
- Architecture documentation (recommended)

## Instructions

1. Review the feature specification
2. Identify testable requirements
3. Define test categories and coverage goals
4. Create the test plan document

## Test Plan Template

Create `.lbi/specs/{feature}/qa/test-plan.md`:

```markdown
# Test Plan: {Feature Name}

## Overview

**Feature**: {Feature name}
**Version**: 1.0
**Created**: {Date}
**QA Owner**: {Name}

## Scope

### In Scope

- {Functionality to test}
- {Integration points}
- {User workflows}

### Out of Scope

- {What won't be tested}
- {Deferred testing}

## Test Strategy

### Test Levels

| Level | Coverage Target | Tools |
|-------|-----------------|-------|
| Unit | 85% | pytest |
| Integration | Key paths | pytest |
| E2E | Critical flows | playwright |

### Test Types

- [ ] Functional testing
- [ ] Integration testing
- [ ] Performance testing
- [ ] Security testing
- [ ] Accessibility testing

## Test Cases Overview

### Happy Path

| ID | Scenario | Priority |
|----|----------|----------|
| TC-001 | {Main success flow} | High |
| TC-002 | {Secondary flow} | Medium |

### Edge Cases

| ID | Scenario | Priority |
|----|----------|----------|
| TC-010 | {Boundary condition} | Medium |
| TC-011 | {Error handling} | High |

### Negative Tests

| ID | Scenario | Expected Result |
|----|----------|-----------------|
| TC-020 | Invalid input | Error message |
| TC-021 | Unauthorized access | 403 response |

## Environment Requirements

- Test database with seed data
- Mock external services
- Test user accounts

## Success Criteria

- All high-priority tests pass
- Coverage meets targets
- No critical bugs open

## Timeline

| Phase | Duration | Deliverable |
|-------|----------|-------------|
| Test Design | X days | Test cases |
| Implementation | X days | Test code |
| Execution | X days | Results |
```

## Next Steps

After creating the test plan:
1. Run `/lbi.qa.tasks` to break down into tasks
2. Run `/lbi.qa.scaffold-tests` to create test structure