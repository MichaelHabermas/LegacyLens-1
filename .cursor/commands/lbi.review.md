---
description: "Review changes before committing"
---

# Code Review

Review all changes for quality, completeness, and adherence to standards.

## Prerequisites

- Complete `/lbi.tests` first
- All tests passing

## Instructions

1. Review all changed files
2. Check against specification requirements
3. Verify coding standards compliance
4. Ensure documentation is complete

## Review Checklist

### Code Quality

- [ ] Code follows SOLID principles
- [ ] Functions are focused and small
- [ ] Meaningful variable and function names
- [ ] No code duplication
- [ ] Proper error handling

### Type Safety

- [ ] All functions have type hints
- [ ] No `Any` types unless necessary
- [ ] Return types specified

### Documentation

- [ ] Docstrings on all public functions
- [ ] Complex logic has explanatory comments
- [ ] README updated if needed

### Testing

- [ ] All tests pass
- [ ] Coverage meets threshold
- [ ] Edge cases covered

### Security

- [ ] No hardcoded secrets
- [ ] Input validation in place
- [ ] No SQL injection vulnerabilities

### Performance

- [ ] No obvious performance issues
- [ ] Efficient algorithms used
- [ ] No unnecessary loops

## Files Changed

Review each file in `.lbi/specs/{feature}/plan.md` "Files to Create/Modify" section.

## Sign-Off

Once review is complete, update the plan:

```markdown
## Review Status
- Reviewer: {Your name}
- Date: {Date}
- Status: Approved
```

## Next Steps

After review approval, run `/lbi.push` to commit and push changes.