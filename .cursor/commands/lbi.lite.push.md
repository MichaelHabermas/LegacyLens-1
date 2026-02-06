---
description: "Quick push and PR for lite workflow"
---

# Lite Push

Finalize and push changes for lite workflow.

## Purpose

Complete the lite workflow with minimal ceremony.

## Prerequisites

- Implementation complete
- Tests passing

## Quick Push Process

### Step 1: Final Checks

```bash
# Verify all tests pass
pytest tests/ -v

# Check linting
ruff check src/ tests/

# Check for uncommitted changes
git status
```

### Step 2: Commit

```bash
# Stage changes
git add .

# Commit with lite workflow reference
git commit -m "feat: {description}

Lite workflow implementation.

- {Change 1}
- {Change 2}

Acceptance criteria:
- [x] {Criterion 1}
- [x] {Criterion 2}"
```

### Step 3: Push

```bash
# Push to remote
git push -u origin HEAD
```

### Step 4: Create PR

```bash
# Using GitHub CLI
gh pr create --title "{Title}" --body "$(cat <<EOF
## Summary

{Brief description of changes}

## Changes

- {Change 1}
- {Change 2}

## Testing

- [x] Unit tests added
- [x] Manual testing complete

## Lite Workflow

This PR follows the lite workflow for small, well-understood changes.

**Request**: {link to lite-request.md if committed}
EOF
)"
```

## Lite PR Template

```markdown
## Summary

{One paragraph summary}

## Changes

- {Change 1}
- {Change 2}

## Testing

- [x] Unit tests pass
- [x] Manual testing done

## Checklist

- [x] Code follows project style
- [x] Tests added/updated
- [x] Documentation updated (if needed)
- [x] Self-review completed

## Lite Workflow

- **Effort**: {S/M}
- **Risk**: Low
- **Files Changed**: {N}
```

## Quick PR Review Checklist

For reviewers:

- [ ] Changes match PR description
- [ ] Tests are meaningful
- [ ] No obvious bugs
- [ ] Code is readable
- [ ] No security issues

## Completion Checklist

```markdown
## Lite Workflow Complete

- [x] Request documented
- [x] Plan created
- [x] Implementation complete
- [x] Tests passing
- [x] PR created
- [ ] Review approved
- [ ] Merged
```

## When to Escalate

If during lite workflow you discover:

- Scope is larger than expected → Switch to full workflow
- Architecture changes needed → Run `/lbi.architecture`
- Stakeholder input needed → Run `/lbi.pm.align`
- Complex testing required → Run `/lbi.qa.plan`

## Output

PR created and ready for review.

## Next Steps

After push:
1. Request code review
2. Address feedback
3. Merge when approved