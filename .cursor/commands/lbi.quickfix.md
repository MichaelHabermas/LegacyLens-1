---
description: "Quick bug fix without full SDD workflow"
---

# Quick Fix

Apply a targeted bug fix without the full Spec-Driven Development workflow.

## When to Use

Use `/lbi.quickfix` for:

- Small, isolated bug fixes
- Typo corrections
- Minor configuration changes
- Simple refactoring (< 20 lines)

**Do NOT use for**:

- New features (use full SDD workflow)
- Changes affecting multiple files
- Architectural changes
- Changes requiring design decisions

## Instructions

1. Identify the bug or issue
2. Locate the affected code
3. Implement the fix
4. Write or update tests
5. Verify the fix works
6. Commit with conventional format

## Quick Fix Template

Document your fix in the commit message:

```
fix: {brief description}

Problem: {what was broken}
Cause: {why it was broken}
Solution: {how you fixed it}

Tested: {how you verified the fix}
```

## Checklist

Before committing your quickfix:

- [ ] Fix is isolated (single responsibility)
- [ ] No new features introduced
- [ ] Tests pass
- [ ] No linter errors
- [ ] Change is < 50 lines total

## Example

```bash
# Find the bug
grep -r "broken_function" src/

# Fix it (small, targeted change)
# Edit the file...

# Verify
uv run pytest tests/ -v

# Commit
git add .
git commit -m "fix: correct null check in user validation

Problem: User validation crashed on empty email
Cause: Missing null check before regex match
Solution: Added early return for null/empty values

Tested: Added unit test, verified manually"
```

## After Quick Fix

If the fix reveals larger issues:

1. Create a proper feature request with `/lbi.request`
2. Document the technical debt
3. Schedule follow-up work

Quick fixes are for quick wins - don't let them grow into features.