---
description: "Create design documentation for a feature"
---

# Design Documentation

Create comprehensive design documentation for a feature including architecture,
data models, and technical decisions.

## Instructions

1. Ensure the feature has a completed specification (`spec.md`)
2. Review the project architecture at `.lbi/specs/architecture/`
3. Create design documentation in the feature directory

## Design Template

Create `.lbi/specs/{feature-slug}/design.md`:

```markdown
# Design Document: {Feature Name}

## Overview
{Brief summary of the feature design approach}

## Architecture

### Component Diagram
{Describe or diagram the main components and their relationships}

### Data Flow
{Describe how data flows through the feature}

## Technical Decisions

### Decision 1: {Decision Title}
- **Context**: {Why this decision was needed}
- **Options Considered**: {List alternatives evaluated}
- **Decision**: {What was decided and why}
- **Consequences**: {Positive and negative outcomes}

### Decision 2: {Decision Title}
- **Context**: {Why this decision was needed}
- **Options Considered**: {List alternatives evaluated}
- **Decision**: {What was decided and why}
- **Consequences**: {Positive and negative outcomes}

## Data Models

### {Model Name}
```
{Model definition with fields and types}
```

**Relationships**:
- {Relationship to other models}

## API Design

### Endpoints
| Method | Path | Description |
|--------|------|-------------|
| GET | /api/... | {Description} |
| POST | /api/... | {Description} |

### Request/Response Examples
{Include example payloads}

## Security Considerations
- {Security consideration 1}
- {Security consideration 2}

## Performance Considerations
- {Performance consideration 1}
- {Performance consideration 2}

## Testing Strategy
- **Unit Tests**: {What will be unit tested}
- **Integration Tests**: {What will be integration tested}
- **E2E Tests**: {What will be end-to-end tested}
```

## Next Steps

After completing the design, run `/lbi.plan` to create an implementation plan.