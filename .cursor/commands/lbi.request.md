---
description: "Start a new feature request"
---

# Feature Request

Start the Spec-Driven Development workflow by defining what you want to build.

## Instructions

1. Read the project constitution at `.lbi/memory/constitution.md`
2. Create a new feature directory: `.lbi/specs/{feature-slug}/`
3. Generate `request.md` with the following structure:

## Request Template

Create `.lbi/specs/{feature-slug}/request.md`:

```markdown
# Feature Request: {Feature Name}

## Summary
{Brief one-sentence description of the feature}

## User Goals
- {Goal 1: What the user wants to achieve}
- {Goal 2: Expected outcome}
- {Goal 3: Success criteria}

## Context
{Background information and motivation for this feature}

## Scope
- **In Scope**: {What this feature includes}
- **Out of Scope**: {What this feature explicitly excludes}

## Acceptance Criteria
- [ ] {Criterion 1}
- [ ] {Criterion 2}
- [ ] {Criterion 3}
```

## Next Steps

After completing the request, run `/lbi.specify` to create detailed specifications.