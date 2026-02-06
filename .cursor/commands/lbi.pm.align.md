---
description: "Align stakeholders on product decisions"
---

# Stakeholder Alignment

Ensure all stakeholders are aligned on product direction.

## Purpose

Get explicit buy-in from stakeholders before proceeding to development.

## Prerequisites

- PRD or user stories ready for review
- Identified stakeholder list

## Instructions

1. Identify stakeholders
2. Prepare alignment materials
3. Conduct alignment sessions
4. Document decisions

## Stakeholder Map

```markdown
## Stakeholder Analysis

| Stakeholder | Role | Interest | Influence | Engagement |
|-------------|------|----------|-----------|------------|
| {Name} | Sponsor | High | High | Manage Closely |
| {Name} | User Rep | High | Medium | Keep Informed |
| {Name} | Tech Lead | Medium | High | Keep Satisfied |

### RACI Matrix

| Decision | Responsible | Accountable | Consulted | Informed |
|----------|-------------|-------------|-----------|----------|
| Scope | PM | VP Product | Eng Lead | Team |
| Timeline | Eng Lead | PM | Design | Stakeholders |
| Launch | PM | VP Product | Legal, Marketing | All |
```

## Alignment Meeting Template

```markdown
# Alignment Meeting: {Feature Name}

**Date**: {Date}
**Attendees**: {List}
**Duration**: {Time}

## Agenda

1. Context & Background (5 min)
2. Proposed Solution (10 min)
3. Trade-offs & Alternatives (10 min)
4. Open Discussion (15 min)
5. Decision & Next Steps (5 min)

## Pre-Read Materials

- [ ] PRD: {Link}
- [ ] User Stories: {Link}
- [ ] Research Summary: {Link}

## Discussion Points

### Point 1: {Topic}

**Options**:
- A: {Option and trade-offs}
- B: {Option and trade-offs}

**Recommendation**: {A/B} because {rationale}

### Point 2: {Topic}

[Same structure]

## Decisions Made

| Decision | Choice | Rationale | Owner |
|----------|--------|-----------|-------|
| {Decision} | {Choice} | {Why} | {Who} |

## Action Items

| Action | Owner | Due Date |
|--------|-------|----------|
| {Action} | {Name} | {Date} |

## Parking Lot

- {Item for future discussion}
```

## Alignment Checklist

```markdown
## Alignment Status

### Business Alignment

- [ ] Goals align with company strategy
- [ ] Success metrics approved
- [ ] Budget allocated
- [ ] Resources committed

### Technical Alignment

- [ ] Architecture reviewed
- [ ] Security approved
- [ ] Infrastructure planned
- [ ] Dependencies identified

### Design Alignment

- [ ] UX approved
- [ ] Design resources allocated
- [ ] Accessibility reviewed

### Go-to-Market Alignment

- [ ] Marketing informed
- [ ] Sales enablement planned
- [ ] Support training scheduled
- [ ] Documentation planned

## Sign-Off

| Stakeholder | Role | Status | Date |
|-------------|------|--------|------|
| {Name} | VP Product | ✅ Approved | {Date} |
| {Name} | Eng Lead | ✅ Approved | {Date} |
| {Name} | Design Lead | 🔄 Pending | - |
```

## Output

Create `.lbi/specs/{feature}/alignment/`

## Next Steps

After alignment:
1. Run `/lbi.pm.handoff` to hand off to engineering
2. Run `/lbi.request` to begin implementation workflow