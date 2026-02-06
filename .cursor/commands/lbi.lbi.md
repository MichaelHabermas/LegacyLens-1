---
description: "LBI command overview and quick reference"
---

# LBI Quick Reference

Quick reference for all LBI commands and workflows.

## Overview

LBI (Lets-Build-It) provides Spec-Driven Development workflows for AI-assisted coding.

## Command Reference

### CLI Commands

```bash
lbi init [path]           # Initialize project
lbi upgrade [path]        # Upgrade LBI version
lbi status [path]         # Show workflow status
lbi config show [path]    # Show configuration
lbi personas list         # List personas
lbi personas show         # Show current persona
lbi personas set-default  # Set default persona
lbi version               # Show version
lbi help [topic]          # Get help
```

### Workflow Commands (Slash Commands)

Use these as slash commands in your AI agent:

#### Governance

| Command | Purpose |
|---------|---------|
| `/lbi.constitution` | Create project governance |
| `/lbi.architecture` | Document codebase |
| `/lbi.validate-constitution` | Check compliance |
| `/lbi.validate-architecture` | Check boundaries |

#### Core SDD Workflow

| Command | Purpose |
|---------|---------|
| `/lbi.request` | Capture feature request |
| `/lbi.specify` | Write specification |
| `/lbi.clarify` | Resolve ambiguities |
| `/lbi.plan` | Create implementation plan |
| `/lbi.analyze` | Break into tasks |
| `/lbi.implement` | Implementation guide |
| `/lbi.tests` | Testing guide |
| `/lbi.review` | Review checklist |
| `/lbi.push` | Push and PR guide |

#### QA Workflow

| Command | Purpose |
|---------|---------|
| `/lbi.qa.plan` | Create test plan |
| `/lbi.qa.tasks` | Break into test tasks |
| `/lbi.qa.scaffold-tests` | Create test scaffolds |
| `/lbi.qa.implement` | Write tests |
| `/lbi.qa.generate-fixtures` | Create test data |
| `/lbi.qa.review-tests` | Review test quality |

#### PM Workflow

| Command | Purpose |
|---------|---------|
| `/lbi.pm.discover` | Product discovery |
| `/lbi.pm.interview` | User interviews |
| `/lbi.pm.research` | Market research |
| `/lbi.pm.validate-problem` | Problem validation |
| `/lbi.pm.prd` | Create PRD |
| `/lbi.pm.stories` | Write user stories |
| `/lbi.pm.align` | Stakeholder alignment |
| `/lbi.pm.handoff` | Engineering handoff |

#### Lite Workflow

| Command | Purpose |
|---------|---------|
| `/lbi.lite.request` | Quick request |
| `/lbi.lite.plan` | Quick plan |
| `/lbi.lite.implement` | Quick implement |
| `/lbi.lite.push` | Quick push |

#### CI/CD & Quality

| Command | Purpose |
|---------|---------|
| `/lbi.ci-setup` | Configure CI/CD |
| `/lbi.ci-matrix` | Test matrix setup |
| `/lbi.security-setup` | Security scanning |
| `/lbi.telemetry-check` | Observability check |

#### Utilities

| Command | Purpose |
|---------|---------|
| `/lbi.tasks` | Manage tasks |
| `/lbi.docs` | Generate docs |
| `/lbi.document` | Document component |
| `/lbi.checklist` | Create checklist |
| `/lbi.preflight` | Pre-deploy checks |
| `/lbi.ready-to-push` | Final push checks |
| `/lbi.branch-status` | Branch status |
| `/lbi.fact-check` | Verify claims |
| `/lbi.quickfix` | Quick bug fix |

#### Meta

| Command | Purpose |
|---------|---------|
| `/lbi.persona` | Set/view persona |
| `/lbi.help` | Get help |
| `/lbi` | This reference |

## Workflow Decision Tree

```
New Project?
├── Yes → /lbi.constitution → /lbi.request
└── No → Existing Code?
    ├── Yes → /lbi.architecture → /lbi.request
    └── No → /lbi.request

Simple Change (< 2 days)?
├── Yes → /lbi.lite.request → lite workflow
└── No → /lbi.request → full workflow

QA Focus?
├── Yes → /lbi.qa.plan → QA workflow
└── No → Continue SDD workflow

PM Focus?
├── Yes → /lbi.pm.discover → PM workflow
└── No → Continue SDD workflow
```

## Quick Start

```bash
# 1. Install
pip install lbi

# 2. Initialize
lbi init . --ai cursor

# 3. Set persona
lbi personas set-default backend_engineer

# 4. Start workflow (use slash commands in AI agent)
# /lbi.constitution
# /lbi.architecture
# /lbi.request
```

## More Information

- `/lbi.help overview` - Introduction
- `/lbi.help workflow` - Workflow details
- `/lbi.help commands` - All commands
- `/lbi.help getting-started` - Detailed setup