---
description: "Check feature branch status and progress"
---

# Branch Status

Review the current state of your feature branch.

## Purpose

Understand where you are in the development process and what's left to do.

## Prerequisites

- Git repository
- Feature branch checked out

## Instructions

1. Check git status
2. Review commit history
3. Compare with main
4. Identify pending work

## Status Commands

```bash
# Current branch
git branch --show-current

# Branch status vs remote
git status

# Commits ahead/behind main
git rev-list --left-right --count main...HEAD

# Recent commits on this branch
git log main..HEAD --oneline

# Files changed vs main
git diff --stat main...HEAD

# Uncommitted changes
git diff --stat
```

## Branch Status Report

```markdown
## Branch Status: {branch-name}

**Date**: {YYYY-MM-DD}
**Developer**: {Name}

### Git Status

| Metric | Value |
|--------|-------|
| Branch | `{branch-name}` |
| Base | `main` |
| Commits Ahead | {N} |
| Commits Behind | {N} |
| Files Changed | {N} |

### Commit History

| Hash | Message | Date |
|------|---------|------|
| abc123 | feat: add X | 2 days ago |
| def456 | fix: resolve Y | 1 day ago |
| ghi789 | test: add tests for X | today |

### Changed Files

| File | Changes | Status |
|------|---------|--------|
| `src/feature.py` | +50/-10 | Modified |
| `tests/test_feature.py` | +100/-0 | Added |
| `docs/feature.md` | +20/-5 | Modified |

### Uncommitted Changes

| File | Status |
|------|--------|
| `src/wip.py` | Modified |
| `notes.txt` | Untracked |

### SDD Workflow Progress

| Step | Status | Artifact |
|------|--------|----------|
| Request | ✅ | `request.md` |
| Specify | ✅ | `spec.md` |
| Plan | ✅ | `plan.md` |
| Tasks | ✅ | `tasks.md` |
| Implement | 🔄 | In progress |
| Tests | ⏳ | Pending |
| Review | ⏳ | Pending |
| Push | ⏳ | Pending |

### Blocking Issues

| Issue | Description | Owner |
|-------|-------------|-------|
| {Issue} | {Description} | {Who} |

### Next Actions

1. {Next thing to do}
2. {After that}
3. {Then}
```

## Health Checks

```bash
# Check for merge conflicts with main
git merge --no-commit --no-ff main
git merge --abort  # if conflicts

# Check if rebasing is needed
git fetch origin
git log HEAD..origin/main --oneline

# Check branch age
git log -1 --format="%ci" $(git merge-base main HEAD)
```

## Branch Hygiene

### Signs of Healthy Branch

- ✅ Small, focused commits
- ✅ Up-to-date with main
- ✅ Tests passing
- ✅ Clear commit messages

### Signs of Unhealthy Branch

- ❌ Many days since last rebase
- ❌ Large number of commits
- ❌ Mixed concerns in single branch
- ❌ Failing tests

## Next Steps

After reviewing status:
1. Address any blocking issues
2. Continue with current workflow step
3. Run `/lbi.status` for feature progress