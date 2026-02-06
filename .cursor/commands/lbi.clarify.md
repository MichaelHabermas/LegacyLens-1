---
description: "Ask clarifying questions about specifications"
---

# Clarify Specifications

Review the current specification and identify ambiguities or missing details.

## Prerequisites

- Complete `/lbi.specify` first
- Spec file exists at `.lbi/specs/{feature}/spec.md`

## Instructions

1. Read the specification at `.lbi/specs/{feature}/spec.md`
2. Identify unclear or ambiguous requirements
3. Generate clarifying questions
4. Update the spec with answers when received

## Question Categories

Review the specification for gaps in these areas:

### Scope Questions

- What is explicitly in scope?
- What is explicitly out of scope?
- Are there any boundary conditions unclear?

### Technical Questions

- Are all data types and formats specified?
- Are API contracts fully defined?
- Are error handling requirements clear?

### Edge Cases

- What happens when inputs are invalid?
- How should the system behave under load?
- What are the failure modes?

### Dependencies

- What must exist before this feature?
- Are there external service dependencies?
- What are the integration points?

### Acceptance Criteria

- How do we know the feature is complete?
- What are the measurable success criteria?
- Who will validate acceptance?

## Clarification Template

Document questions in `.lbi/specs/{feature}/clarifications.md`:

```markdown
# Clarifications: {Feature Name}

## Open Questions

1. **Question**: {Your question here}
   **Context**: {Why this is unclear}
   **Answer**: {To be filled when answered}

2. **Question**: {Another question}
   **Context**: {Why this matters}
   **Answer**: {Pending}

## Resolved Questions

- {Question that was answered}
  - **Answer**: {The answer}
  - **Impact**: {How this affects the spec}
```

## Next Steps

After clarifications are resolved:
1. Update `spec.md` with clarified requirements
2. Run `/lbi.plan` to create the implementation plan