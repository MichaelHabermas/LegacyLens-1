---
description: "Document a specific component or decision"
---

# Document

Create documentation for a specific component, decision, or process.

## Purpose

Create focused documentation for a single topic.

## Prerequisites

- Component or topic to document
- Context and background

## Instructions

1. Identify documentation type
2. Gather information
3. Write documentation
4. Review for accuracy

## Documentation Templates

### Component Documentation

```markdown
# {Component Name}

## Overview

**Purpose**: {What this component does}
**Location**: `src/{path}/`
**Owner**: {Team/Person}

## Responsibilities

- {Responsibility 1}
- {Responsibility 2}
- {Responsibility 3}

## Architecture

```mermaid
graph TD
    A[Input] --> B[{Component}]
    B --> C[Output]
```

## Interface

### Public Methods

#### `method_name(param) -> return_type`

{Description}

### Configuration

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| {name} | {type} | {value} | {description} |

## Usage Examples

```python
# Example 1: Basic usage
component = Component()
result = component.method()

# Example 2: With configuration
component = Component(config={"key": "value"})
```

## Error Handling

| Error | Cause | Resolution |
|-------|-------|------------|
| {Error} | {Why it happens} | {How to fix} |

## Testing

```bash
pytest tests/unit/test_{component}.py -v
```

## Related Components

- [{Related 1}](path/to/doc.md)
- [{Related 2}](path/to/doc.md)
```

### ADR (Architecture Decision Record)

```markdown
# ADR-{NNN}: {Title}

## Status

{Proposed | Accepted | Deprecated | Superseded}

## Context

{What is the issue we're addressing?}

## Decision

{What decision did we make?}

## Consequences

### Positive

- {Good outcome 1}
- {Good outcome 2}

### Negative

- {Trade-off 1}
- {Trade-off 2}

### Neutral

- {Side effect}

## Alternatives Considered

### Option A: {Name}

{Description}

**Pros**: {List}
**Cons**: {List}

### Option B: {Name}

{Description}

**Pros**: {List}
**Cons**: {List}

## References

- {Link to related discussion}
- {Link to documentation}
```

### Runbook

```markdown
# Runbook: {Process Name}

## Overview

**Purpose**: {What this runbook is for}
**Audience**: {Who uses this}
**Last Updated**: {Date}

## Prerequisites

- [ ] {Prerequisite 1}
- [ ] {Prerequisite 2}

## Procedure

### Step 1: {Action}

```bash
# Command to run
command --flag value
```

**Expected Output**:
```
{What you should see}
```

### Step 2: {Action}

{Instructions}

### Step 3: {Action}

{Instructions}

## Verification

- [ ] {How to verify step 1}
- [ ] {How to verify step 2}

## Rollback

If something goes wrong:

1. {Rollback step 1}
2. {Rollback step 2}

## Troubleshooting

| Symptom | Cause | Solution |
|---------|-------|----------|
| {Symptom} | {Cause} | {Solution} |
```

## Output

Create documentation in appropriate location.

## Next Steps

After documenting:
1. Request review from stakeholders
2. Add to documentation index