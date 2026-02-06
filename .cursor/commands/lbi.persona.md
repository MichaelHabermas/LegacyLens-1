---
description: "Set or view the active development persona"
---

# Persona

Manage your development persona for role-specific guidance.

## Purpose

Set your role to receive tailored guidance and workflow suggestions.

## Available Personas

| ID | Role | Focus |
|----|------|-------|
| `backend_engineer` | Backend Engineer | APIs, services, databases |
| `frontend_engineer` | Frontend Engineer | UI, UX, components |
| `fullstack_engineer` | Fullstack Engineer | End-to-end development |
| `qa_engineer` | QA Engineer | Testing, quality assurance |
| `data_engineer` | Data Engineer | Pipelines, ETL, data models |
| `data_scientist` | Data Scientist | ML, analytics, notebooks |
| `ml_engineer` | ML Engineer | Model deployment, MLOps |
| `sre` | Site Reliability Engineer | Infrastructure, monitoring |
| `security_compliance` | Security Engineer | Security, compliance |
| `architect` | Software Architect | System design, ADRs |
| `product_manager` | Product Manager | Requirements, stakeholders |
| `maintainer` | Maintainer | Open source, releases |

## View Current Persona

Check the current persona setting:

```bash
lbi personas show
```

Or read `.lbi/config/personas.yaml`:

```yaml
default_persona: backend_engineer
personas:
  - backend_engineer
  - frontend_engineer
  # ... etc
```

## Set Persona

```bash
lbi personas set-default {persona_id}
```

Or edit `.lbi/config/personas.yaml` directly.

## Persona Effects

Setting a persona affects:

### 1. Command Guidance

Each persona gets tailored sections in commands:

```markdown
## Backend Engineer Considerations

- API design patterns
- Database optimization
- Service architecture
```

### 2. Required Sections

Some personas require specific sections:

| Persona | Required in Spec | Required in Plan |
|---------|------------------|------------------|
| Backend | API design, Data model | Database migration |
| Frontend | Component design, State | Accessibility |
| QA | Test strategy | Test environments |
| SRE | Monitoring, SLOs | Deployment strategy |

### 3. Workflow Recommendations

```markdown
## Recommended Workflow

### Backend Engineer
1. /lbi.constitution
2. /lbi.architecture
3. /lbi.request
4. /lbi.specify (API contracts)
5. /lbi.plan (with data model)
6. /lbi.implement
7. /lbi.tests (integration focus)
8. /lbi.review
9. /lbi.push

### QA Engineer
1. /lbi.qa.plan
2. /lbi.qa.tasks
3. /lbi.qa.scaffold-tests
4. /lbi.qa.generate-fixtures
5. /lbi.qa.implement
6. /lbi.qa.review-tests
```

## Persona Configuration

### Custom Persona

Create custom persona in `.lbi/personas/{id}.yaml`:

```yaml
id: custom_role
name: Custom Role
description: Description of the role
focus_areas:
  - Area 1
  - Area 2
required_sections:
  specify:
    - Custom Section
  plan:
    - Custom Planning Section
workflow_hints:
  - Hint 1
  - Hint 2
```

### Persona Switching

Switch personas for different tasks:

```bash
# Set for backend work
lbi personas set-default backend_engineer

# Do backend work...

# Switch for QA work
lbi personas set-default qa_engineer
```

## Output

Updates `.lbi/config/personas.yaml`

## Next Steps

After setting persona:
1. Run `/lbi.constitution` to establish principles
2. Follow persona-specific workflow