---
description: "Hand off product requirements to engineering"
---

# Engineering Handoff

Transfer product requirements to engineering for implementation.

## Purpose

Ensure engineering has everything needed to begin development without ambiguity.

## Prerequisites

- Approved PRD
- User stories written
- Stakeholder alignment complete
- Design assets ready

## Instructions

1. Prepare handoff package
2. Conduct handoff session
3. Answer questions
4. Track implementation kickoff

## Handoff Package Checklist

```markdown
## Handoff Checklist: {Feature Name}

### Documentation

- [ ] PRD (approved version)
- [ ] User stories (pointed)
- [ ] Acceptance criteria (complete)
- [ ] Technical notes (reviewed by eng)

### Design

- [ ] Wireframes/mockups (all states)
- [ ] Design specs (spacing, colors, etc.)
- [ ] Prototype (interactive)
- [ ] Asset exports (icons, images)

### Data

- [ ] Data requirements documented
- [ ] API contracts defined
- [ ] Sample data available
- [ ] Migration plan (if needed)

### Context

- [ ] User research summary
- [ ] Competitive context
- [ ] Business metrics targets
- [ ] Launch criteria

### Access

- [ ] Test accounts ready
- [ ] Staging environment access
- [ ] Third-party credentials
- [ ] Analytics setup
```

## Handoff Document Template

```markdown
# Engineering Handoff: {Feature Name}

**Date**: {Date}
**PM**: {Name}
**Eng Lead**: {Name}

## Quick Links

| Document | Link | Status |
|----------|------|--------|
| PRD | {Link} | ✅ Final |
| Stories | {Link} | ✅ Pointed |
| Designs | {Link} | ✅ Complete |
| Technical Spec | {Link} | 🔄 In Progress |

## Feature Summary

{2-3 sentence overview of what we're building}

## Success Criteria

| Metric | Target | Measurement |
|--------|--------|-------------|
| {Metric} | {Target} | {How measured} |

## Scope

### In Scope

- {Feature component 1}
- {Feature component 2}

### Out of Scope

- {Explicitly excluded}

### Edge Cases

| Scenario | Expected Behavior |
|----------|-------------------|
| {Edge case} | {What happens} |

## Implementation Notes

### Priority Order

1. {First thing to build}
2. {Second thing to build}
3. {Third thing to build}

### Technical Considerations

- {Consideration from eng discussion}
- {Performance requirement}
- {Security requirement}

### Known Risks

| Risk | Mitigation |
|------|------------|
| {Risk} | {Plan} |

## Open Questions

| Question | Owner | Due |
|----------|-------|-----|
| {Question} | {Who} | {When} |

## Timeline

| Milestone | Date | Owner |
|-----------|------|-------|
| Sprint planning | {Date} | Eng Lead |
| Development start | {Date} | Team |
| Code complete | {Date} | Team |
| QA complete | {Date} | QA |
| Launch | {Date} | Team |

## Contact

- **Product questions**: {PM name/slack}
- **Design questions**: {Designer name/slack}
- **Technical questions**: {Tech lead name/slack}
```

## Handoff Meeting Agenda

```markdown
## Handoff Session

**Duration**: 60 minutes

1. **Overview** (10 min)
   - Problem context
   - User needs
   - Business goals

2. **Walk-through** (20 min)
   - User flows
   - Key screens
   - Edge cases

3. **Technical Discussion** (15 min)
   - Architecture approach
   - Dependencies
   - Risks

4. **Q&A** (10 min)
   - Clarifying questions
   - Scope concerns

5. **Next Steps** (5 min)
   - Sprint planning date
   - Follow-up items
```

## Output

Create `.lbi/specs/{feature}/handoff/`

## Next Steps

After handoff:
1. Run `/lbi.request` to capture the feature in SDD workflow
2. Engineering runs `/lbi.specify` to create technical spec