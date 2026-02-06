---
description: "Set up development environment for a project"
---

# Project Setup

Configure the development environment and project dependencies.

## Instructions

1. Review project requirements and tech stack
2. Set up the development environment
3. Install required dependencies
4. Configure development tools

## Setup Checklist

### 1. Environment Setup

- [ ] Verify required runtime versions (Python, Node, etc.)
- [ ] Set up virtual environment or package manager
- [ ] Configure environment variables
- [ ] Set up IDE/editor configuration

### 2. Dependencies

- [ ] Install project dependencies
- [ ] Install development dependencies
- [ ] Verify all dependencies resolve correctly
- [ ] Check for security vulnerabilities

### 3. Configuration Files

Review and update configuration files:

- [ ] `.env.example` → `.env` (with actual values)
- [ ] IDE settings (`.vscode/`, `.idea/`)
- [ ] Git hooks (pre-commit, etc.)
- [ ] Linter configuration

### 4. Database Setup (if applicable)

- [ ] Install database server
- [ ] Create development database
- [ ] Run migrations
- [ ] Seed initial data

### 5. External Services (if applicable)

- [ ] Configure API keys
- [ ] Set up service connections
- [ ] Verify connectivity

## Setup Commands Template

Create a setup script or document the commands:

```bash
# Example setup commands
# Python project
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -e ".[dev]"

# Node project
npm install
npm run setup

# Run initial checks
make test
make lint
```

## Verification

Ensure setup is complete by running:

- [ ] Tests pass: `make test` or `npm test`
- [ ] Linter passes: `make lint` or `npm run lint`
- [ ] Application starts: `make run` or `npm start`

## Troubleshooting

Document common setup issues and solutions:

| Issue | Solution |
|-------|----------|
| {Issue 1} | {Solution 1} |
| {Issue 2} | {Solution 2} |

## Next Steps

After completing setup, you can start developing with the SDD workflow:
- Run `/lbi.request` to start a new feature
- Run `/lbi.status` to check project status