---
description: "Create detailed specifications"
---

# Specification

Create detailed technical specifications from the feature request.

## Prerequisites

- Complete `/lbi.request` first
- Request file exists at `.lbi/specs/{feature}/request.md`

## Instructions

1. Read the request at `.lbi/specs/{feature}/request.md`
2. Create `spec.md` with detailed technical requirements
3. Define acceptance criteria and test scenarios

## Specification Template

Create `.lbi/specs/{feature}/spec.md`:

```markdown
# Specification: {Feature Name}

## Overview
{Technical summary of what will be built}

## Requirements

### Functional Requirements
1. {FR-1}: {Description}
2. {FR-2}: {Description}

### Non-Functional Requirements
1. {NFR-1}: {Performance, security, etc.}

## Technical Design

### Components
- {Component 1}: {Purpose}
- {Component 2}: {Purpose}

### Data Model
{Describe any data structures or database changes}

### API Contracts
{Define any API endpoints or interfaces}

## Test Scenarios

| Scenario | Given | When | Then |
|----------|-------|------|------|
| {Name} | {Precondition} | {Action} | {Expected Result} |

## Dependencies
- {Dependency 1}
- {Dependency 2}
```

## Next Steps

After completing specifications, run `/lbi.plan` to create the implementation plan.