---
description: "Get help on LBI commands and workflows"
---

# Help

Get help on LBI commands, workflows, and concepts.

## Usage

```bash
lbi help [topic]
```

## Available Topics

### Commands

| Topic | Description |
|-------|-------------|
| `overview` | Introduction to LBI |
| `workflow` | SDD workflow steps |
| `commands` | All available commands |
| `personas` | Role-based guidance |
| `getting-started` | Quick start guide |

### Workflows

| Topic | Description |
|-------|-------------|
| `sdd` | Spec-Driven Development |
| `qa` | QA workflow |
| `pm` | Product Management workflow |
| `lite` | Simplified workflow |

### Concepts

| Topic | Description |
|-------|-------------|
| `constitution` | Project governance |
| `architecture` | Architecture documentation |
| `testing` | Testing approaches |
| `quality-gates` | Quality standards |

## Topic: overview

LBI (Lets-Build-It) is a CLI tool for Spec-Driven Development.

**Core Workflow**:

```
Constitution → Architecture → Request → Specify → Plan → Implement → Tests → Review → Push
```

**Key Concepts**:
- **Constitution**: Project principles and governance
- **Architecture**: Codebase structure documentation
- **Specs**: Feature specifications and plans
- **Personas**: Role-based workflow guidance

## Topic: workflow

### Full SDD Workflow

1. **`/lbi.constitution`** - Establish project principles
2. **`/lbi.architecture`** - Document codebase structure
3. **`/lbi.request`** - Capture feature request
4. **`/lbi.specify`** - Write detailed specification
5. **`/lbi.clarify`** - Resolve ambiguities
6. **`/lbi.plan`** - Create implementation plan
7. **`/lbi.analyze`** - Break into tasks
8. **`/lbi.implement`** - Write the code
9. **`/lbi.tests`** - Write tests
10. **`/lbi.review`** - Self-review
11. **`/lbi.push`** - Create PR

### Lite Workflow

For small changes:

```
/lbi.lite.request → /lbi.lite.plan → /lbi.lite.implement → /lbi.lite.push
```

## Topic: commands

### Core Commands

| Command | Purpose |
|---------|---------|
| `init` | Initialize LBI in project |
| `upgrade` | Upgrade LBI version |
| `status` | Show workflow progress |
| `config` | Manage configuration |
| `personas` | Manage personas |
| `help` | Show help |
| `version` | Show version |

### Workflow Commands

| Command | Purpose |
|---------|---------|
| `/lbi.request` | Capture feature request |
| `/lbi.specify` | Write specification |
| `/lbi.plan` | Create plan |
| `/lbi.implement` | Implementation guide |
| `/lbi.tests` | Testing guide |
| `/lbi.review` | Review checklist |
| `/lbi.push` | Push guidelines |

## Topic: getting-started

### Quick Start

```bash
# Install
pip install lbi

# Initialize in your project
lbi init . --ai cursor

# Set your persona
lbi personas set-default backend_engineer

# Start with constitution
# Use: /lbi.constitution

# Then architecture (for existing code)
# Use: /lbi.architecture

# Start a feature
# Use: /lbi.request
```

### File Structure

After init:

```
your-project/
├── .lbi/
│   ├── manifest.json
│   ├── memory/constitution.md
│   ├── config/personas.yaml
│   └── specs/  # Feature artifacts go here
├── .cursor/commands/  # Agent commands
│   ├── lbi.request.md
│   ├── lbi.specify.md
│   └── ...
```

## Topic: quality-gates

Quality gates are checkpoints that must pass:

| Gate | Command | Requirement |
|------|---------|-------------|
| Lint | `ruff check .` | 0 errors |
| Types | `mypy src/` | 0 errors |
| Tests | `pytest` | All pass |
| Coverage | `pytest --cov` | ≥ 85% |
| Security | `pip-audit` | No high/critical |

## More Help

- Run `lbi help {topic}` for specific help
- Check documentation at `.lbi/docs/`
- View command templates in `.cursor/commands/`