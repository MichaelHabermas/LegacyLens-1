---
description: "Generate a checklist for a process or review"
---

# Checklist

Create structured checklists for processes, reviews, or validation.

## Purpose

Ensure nothing is missed during complex processes.

## Prerequisites

- Process or review to systematize
- Understanding of requirements

## Instructions

1. Identify all required steps
2. Organize logically
3. Add verification criteria
4. Format as checklist

## Checklist Templates

### Code Review Checklist

```markdown
## Code Review: {PR/Feature}

### Functionality
- [ ] Code does what it's supposed to do
- [ ] Edge cases handled
- [ ] Error handling appropriate
- [ ] No obvious bugs

### Code Quality
- [ ] Code is readable and self-documenting
- [ ] No unnecessary complexity
- [ ] DRY principle followed
- [ ] SOLID principles applied
- [ ] No magic numbers/strings

### Testing
- [ ] Unit tests added/updated
- [ ] Tests cover happy path
- [ ] Tests cover edge cases
- [ ] Tests are deterministic
- [ ] Coverage maintained/improved

### Security
- [ ] No hardcoded secrets
- [ ] Input validation present
- [ ] SQL injection prevented
- [ ] XSS prevented (if applicable)

### Performance
- [ ] No obvious performance issues
- [ ] Database queries optimized
- [ ] No N+1 queries
- [ ] Appropriate caching

### Documentation
- [ ] Code comments where needed
- [ ] Docstrings complete
- [ ] README updated if needed
- [ ] API docs updated if needed
```

### Release Checklist

```markdown
## Release: v{X.Y.Z}

### Pre-Release
- [ ] All PRs merged
- [ ] CI passing on main
- [ ] Version bumped in pyproject.toml
- [ ] CHANGELOG updated
- [ ] Documentation updated

### Testing
- [ ] Unit tests passing
- [ ] Integration tests passing
- [ ] Manual testing complete
- [ ] Performance regression check

### Deployment
- [ ] Staging deployment successful
- [ ] Staging smoke tests passing
- [ ] Production deployment scheduled
- [ ] Rollback plan documented

### Post-Release
- [ ] Production smoke tests
- [ ] Monitoring alerts reviewed
- [ ] Release notes published
- [ ] Team notified
```

### Feature Completion Checklist

```markdown
## Feature: {Name}

### Requirements
- [ ] All acceptance criteria met
- [ ] Edge cases handled
- [ ] Error scenarios covered

### Code
- [ ] Implementation complete
- [ ] Code reviewed and approved
- [ ] No TODO comments left
- [ ] Technical debt documented

### Testing
- [ ] Unit tests: {X}% coverage
- [ ] Integration tests written
- [ ] Manual QA passed
- [ ] Performance tested

### Documentation
- [ ] User documentation
- [ ] API documentation
- [ ] Architecture diagrams updated

### Deployment
- [ ] Feature flag configured
- [ ] Monitoring/alerting set up
- [ ] Rollback plan documented
```

### Sprint Planning Checklist

```markdown
## Sprint: {Name/Number}

### Preparation
- [ ] Backlog groomed
- [ ] Stories pointed
- [ ] Dependencies identified
- [ ] Team capacity calculated

### Planning Meeting
- [ ] Sprint goal defined
- [ ] Stories selected
- [ ] Tasks broken down
- [ ] Assignments made

### Definition of Done
- [ ] Code complete
- [ ] Tests passing
- [ ] Code reviewed
- [ ] Documentation updated
- [ ] Deployed to staging
```

## Custom Checklist Builder

```markdown
## {Checklist Name}

### Section 1: {Name}
- [ ] {Item}
- [ ] {Item}
- [ ] {Item}

### Section 2: {Name}
- [ ] {Item}
- [ ] {Item}

### Sign-off
- [ ] All items complete
- [ ] Reviewer: {Name}
- [ ] Date: {YYYY-MM-DD}
```

## Next Steps

After creating checklist:
1. Use during the relevant process
2. Update based on lessons learned