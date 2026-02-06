---
description: "Create a Product Requirements Document"
---

# Product Requirements Document

Create a comprehensive PRD for a validated feature.

## Purpose

Document product requirements clearly so engineering, design, and stakeholders share a common understanding.

## Prerequisites

- Problem validated via `/lbi.pm.validate-problem`
- Stakeholder alignment on goals

## Instructions

1. Define the problem and goals
2. Specify requirements
3. Define success metrics
4. Document constraints

## PRD Template

```markdown
# PRD: {Feature Name}

## Document Info

| Field | Value |
|-------|-------|
| Author | {Name} |
| Status | Draft / Review / Approved |
| Version | 1.0 |
| Last Updated | {Date} |

## Executive Summary

{2-3 sentence summary of what we're building and why}

## Problem Statement

### User Problem

{Description of the user problem we're solving}

### Business Problem

{How this problem affects the business}

### Evidence

- {Quantified evidence point 1}
- {Quantified evidence point 2}

## Goals & Success Metrics

### Goals

| Goal | Description | Priority |
|------|-------------|----------|
| {Goal 1} | {Description} | P0 |
| {Goal 2} | {Description} | P1 |

### Success Metrics

| Metric | Current | Target | Timeframe |
|--------|---------|--------|-----------|
| {Metric 1} | {X} | {Y} | 90 days |
| {Metric 2} | {X} | {Y} | 90 days |

### Non-Goals

- {What we're explicitly not doing}
- {Scope exclusions}

## User Stories

### Primary Persona: {Name}

As a {user type}, I want to {action} so that {benefit}.

**Acceptance Criteria**:
- [ ] {Criterion 1}
- [ ] {Criterion 2}

### Secondary Persona: {Name}

As a {user type}, I want to {action} so that {benefit}.

## Requirements

### Functional Requirements

| ID | Requirement | Priority | Notes |
|----|-------------|----------|-------|
| FR-1 | {Requirement} | Must | {Notes} |
| FR-2 | {Requirement} | Should | {Notes} |
| FR-3 | {Requirement} | Could | {Notes} |

### Non-Functional Requirements

| Category | Requirement |
|----------|-------------|
| Performance | Response time < {X}ms |
| Scalability | Support {N} concurrent users |
| Security | {Security requirement} |
| Accessibility | WCAG 2.1 AA compliance |

## User Experience

### User Flow

```
[Entry Point] → [Step 1] → [Step 2] → [Success State]
                    ↓
              [Error State]
```

### Wireframes

{Link to wireframes or embed images}

## Technical Considerations

### Dependencies

- {External service}
- {Internal system}

### Constraints

- {Technical constraint}
- {Business constraint}

### Risks

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| {Risk} | Medium | High | {Mitigation} |

## Timeline

| Milestone | Target Date | Owner |
|-----------|-------------|-------|
| PRD Approved | {Date} | PM |
| Design Complete | {Date} | Design |
| Dev Complete | {Date} | Engineering |
| Launch | {Date} | Team |

## Open Questions

1. {Question that needs resolution}
2. {Question that needs resolution}

## Appendix

### Research Links

- {Link to research}
- {Link to competitive analysis}

### Changelog

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | {Date} | {Name} | Initial draft |
```

## Output

Create `.lbi/specs/{feature}/prd.md`

## Next Steps

After PRD:
1. Run `/lbi.pm.stories` to break down into user stories
2. Run `/lbi.pm.align` for stakeholder alignment