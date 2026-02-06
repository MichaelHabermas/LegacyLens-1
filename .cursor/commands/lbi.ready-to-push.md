---
description: "Final verification before pushing changes"
---

# Ready to Push

Final verification checklist before pushing code.

## Purpose

Last check before pushing to ensure code quality and completeness.

## Prerequisites

- All development work complete
- Tests passing locally

## Instructions

1. Verify all changes are staged
2. Run final checks
3. Review commit message
4. Push with confidence

## Quick Checks

```bash
# Check git status
git status

# Check what will be pushed
git log origin/main..HEAD --oneline

# Run tests one more time
pytest tests/ -v

# Check linting
ruff check .
```

## Ready to Push Checklist

```markdown
## Pre-Push Verification

### Code Changes

- [ ] All intended changes staged
- [ ] No unintended files included
- [ ] No debug code left (print, console.log)
- [ ] No commented-out code
- [ ] No TODO comments for this PR

### Tests

- [ ] All tests passing
- [ ] New code has tests
- [ ] No skipped tests without reason
- [ ] Coverage maintained

### Quality

- [ ] Linter passing (0 errors)
- [ ] Type checker passing
- [ ] No new warnings introduced

### Commit

- [ ] Commit message follows convention
- [ ] Commit message explains "why"
- [ ] Related issue referenced

### Documentation

- [ ] Code is self-documenting
- [ ] Complex logic has comments
- [ ] Public APIs have docstrings

### Final Review

- [ ] Re-read the diff one more time
- [ ] Nothing sensitive in commit
- [ ] Changes match PR description
```

## Commit Message Format

```
type(scope): brief description

Longer description if needed, explaining:
- What changed
- Why it changed
- Any important details

Fixes #123
```

### Types

| Type | Use For |
|------|---------|
| feat | New feature |
| fix | Bug fix |
| docs | Documentation only |
| style | Formatting, no code change |
| refactor | Code change that neither fixes nor adds |
| test | Adding tests |
| chore | Maintenance tasks |

## Danger Signs

Stop and reconsider if you see:

- ❌ Large number of changed files unexpectedly
- ❌ Changes in files you didn't intend to modify
- ❌ Failing tests
- ❌ `.env` or credential files in diff
- ❌ Binary files you didn't expect
- ❌ Merge conflict markers

## Push Commands

```bash
# Standard push
git push origin HEAD

# Push and set upstream
git push -u origin HEAD

# Force push (DANGER - use carefully)
git push --force-with-lease origin HEAD
```

## After Push

- [ ] CI pipeline started
- [ ] PR created/updated
- [ ] Reviewers assigned
- [ ] PR description complete

## Next Steps

After pushing:
1. Create PR if not exists
2. Request code review
3. Run `/lbi.review` for self-review