---
description: "Create or update the project constitution with non-negotiable principles and quality standards"
---

# Create Project Constitution

Establish the foundational governance document for your project.

## Purpose

The constitution defines non-negotiable principles, quality standards, and governance rules that guide all development decisions. It should be created BEFORE any feature development begins.

## Prerequisites

- Project initialized with `lbi init`
- Understanding of project goals and constraints

## Instructions

1. Review the existing constitution template at `.lbi/memory/constitution.md`
2. Identify placeholders marked with `[PLACEHOLDER]` format
3. Replace placeholders with concrete values based on project context
4. Ensure all principles are testable and enforceable

## Constitution Sections

### Project Identity

Define the core identity:

```markdown
# Project Constitution

## Project Identity

- **Name**: [PROJECT_NAME]
- **Purpose**: [One-line mission statement]
- **Version**: 1.0.0
- **Ratification Date**: [YYYY-MM-DD]
```

### Core Principles

Define 3-5 non-negotiable principles:

```markdown
## Core Principles

### Principle 1: [PRINCIPLE_NAME]

**Statement**: [Clear, testable requirement]

**Rationale**: [Why this principle exists]

**Enforcement**: [How violations are detected/prevented]
```

Example principles:

- **Test-First Development**: All features must have tests written before implementation
- **Type Safety**: All code must pass static type checking without errors
- **Documentation**: All public APIs must have docstrings

### Quality Standards

Define measurable quality gates:

```markdown
## Quality Standards

### Code Quality

- Test coverage minimum: [X]%
- Linter: [tool name] with zero errors
- Type checker: [tool name] with strict mode

### Review Requirements

- All changes require code review
- CI must pass before merge
- Documentation must be updated with code changes
```

### Governance Rules

Define how the constitution evolves:

```markdown
## Governance

### Amendment Process

1. Propose changes via pull request
2. All stakeholders must review
3. Unanimous consent required for principle changes
4. Simple majority for clarifications

### Version Policy

- MAJOR: Principle additions or removals
- MINOR: New guidelines or expanded sections
- PATCH: Clarifications and typo fixes
```

## Constitution Template Output

Create `.lbi/memory/constitution.md`:

```markdown
---
description: "[Project name] development principles and governance"
version: "1.0.0"
ratification_date: "[YYYY-MM-DD]"
last_amended: "[YYYY-MM-DD]"
---

# [PROJECT_NAME] Constitution

## Project Identity

**Mission**: [One-line purpose statement]

**Values**:
- [Value 1]
- [Value 2]
- [Value 3]

## Core Principles

### Principle 1: [Name]

[Description and enforcement]

### Principle 2: [Name]

[Description and enforcement]

### Principle 3: [Name]

[Description and enforcement]

## Quality Standards

### Testing

- Framework: [pytest/jest/etc.]
- Coverage target: [X]%
- Required types: [unit, integration, etc.]

### Code Style

- Formatter: [black/prettier/etc.]
- Linter: [ruff/eslint/etc.]
- Type checker: [mypy/typescript/etc.]

## Governance

### Amendment Process

[How to change this document]

### Compliance

[How compliance is verified]
```

## Validation Checklist

Before finalizing:

- [ ] No unexplained `[PLACEHOLDER]` tokens remain
- [ ] All principles are specific and testable
- [ ] Quality metrics are measurable
- [ ] Governance process is clear
- [ ] Version follows semantic versioning

## Next Steps

After creating the constitution:
1. Run `/lbi.architecture` to analyze existing code (if any)
2. Run `/lbi.validate-constitution` periodically to check compliance
3. Run `/lbi.request` to start your first feature