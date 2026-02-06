---
description: "Commit and push changes"
---

# Push Changes

Commit reviewed changes and push to the remote repository.

## Prerequisites

- Complete `/lbi.review` first
- All review items addressed

## Instructions

1. Stage all relevant files
2. Create descriptive commit message
3. Push to feature branch
4. Create pull request if needed

## Commit Message Format

```
{type}: {brief description}

{Longer description if needed}

Refs: {feature-slug}
```

### Commit Types

- `feat`: New feature
- `fix`: Bug fix
- `refactor`: Code refactoring
- `test`: Adding tests
- `docs`: Documentation changes
- `chore`: Maintenance tasks

## Git Commands

```bash
# Check status
git status

# Stage changes
git add .

# Commit with message
git commit -m "feat: {description}"

# Push to remote
git push origin {branch-name}
```

## Pull Request

If creating a PR:

1. Use feature name as PR title
2. Link to specification in description
3. Add reviewers
4. Wait for CI checks

## Completion

After pushing, the feature workflow is complete. Update the spec folder:

```markdown
## Status: Complete
- Completed: {Date}
- PR: #{PR number}
```

## Workflow Complete

Congratulations! You've completed the SDD workflow:

1. `/lbi.request` - Defined the feature
2. `/lbi.specify` - Created specifications
3. `/lbi.plan` - Made implementation plan
4. `/lbi.implement` - Wrote the code
5. `/lbi.tests` - Added tests
6. `/lbi.review` - Reviewed changes
7. `/lbi.push` - Committed and pushed