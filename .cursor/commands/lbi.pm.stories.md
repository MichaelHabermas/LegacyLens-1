---
description: "Break down PRD into user stories"
---

# User Stories

Convert PRD requirements into detailed user stories.

## Purpose

Create granular, estimable user stories that engineering can implement.

## Prerequisites

- Approved PRD at `.lbi/specs/{feature}/prd.md`

## Instructions

1. Review PRD requirements
2. Identify story themes
3. Write detailed stories
4. Define acceptance criteria

## User Story Format

```markdown
## Story: {Title}

**ID**: US-{XXX}
**Epic**: {Epic name}
**Priority**: P0/P1/P2
**Points**: {Estimate}

### Description

As a {user type},
I want to {action/capability},
So that {benefit/value}.

### Acceptance Criteria

Given {precondition}
When {action}
Then {expected result}

- [ ] AC1: {Specific, testable criterion}
- [ ] AC2: {Specific, testable criterion}
- [ ] AC3: {Specific, testable criterion}

### Technical Notes

- {Implementation consideration}
- {API endpoint needed}
- {Database changes}

### Dependencies

- Blocked by: {US-XXX}
- Blocks: {US-YYY}

### Out of Scope

- {What this story doesn't include}
```

## Story Breakdown Template

```markdown
# User Stories: {Feature Name}

## Epic: {Epic Name}

### Theme 1: {Theme Name}

#### US-001: {Story Title}

As a {user}, I want to {action}, so that {benefit}.

**Acceptance Criteria**:
- [ ] {Criterion}
- [ ] {Criterion}

**Points**: {X}

---

#### US-002: {Story Title}

As a {user}, I want to {action}, so that {benefit}.

**Acceptance Criteria**:
- [ ] {Criterion}
- [ ] {Criterion}

**Points**: {X}

---

### Theme 2: {Theme Name}

[Continue pattern...]

## Story Map

| Theme | Must Have | Should Have | Could Have |
|-------|-----------|-------------|------------|
| {Theme 1} | US-001, US-002 | US-005 | US-008 |
| {Theme 2} | US-003 | US-006, US-007 | - |

## Estimation Summary

| Priority | Stories | Total Points |
|----------|---------|--------------|
| P0 | {N} | {X} |
| P1 | {N} | {X} |
| P2 | {N} | {X} |
| **Total** | **{N}** | **{X}** |
```

## Story Writing Tips

### Good Story Characteristics (INVEST)

- **I**ndependent: Can be developed alone
- **N**egotiable: Details can be discussed
- **V**aluable: Delivers user value
- **E**stimable: Team can estimate effort
- **S**mall: Fits in a sprint
- **T**estable: Has clear criteria

### Story Splitting Strategies

1. **By workflow steps**: Login → Dashboard → Action
2. **By data variations**: Create, Read, Update, Delete
3. **By user roles**: Admin vs. User
4. **By platform**: Web vs. Mobile
5. **By operations**: Happy path vs. Error handling

## Output

Create `.lbi/specs/{feature}/stories/`

## Next Steps

After stories:
1. Run `/lbi.pm.align` for stakeholder review
2. Run `/lbi.pm.handoff` to hand off to engineering