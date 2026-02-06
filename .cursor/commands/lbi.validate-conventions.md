---
description: "Validate project follows coding conventions"
---

# Validate Coding Conventions

Check that the codebase follows established coding conventions, style guides,
and best practices defined in the project constitution.

## Instructions

1. Review the project constitution at `.lbi/memory/constitution.md`
2. Check code against established conventions
3. Identify and report violations
4. Suggest fixes for non-compliant code

## Convention Categories

### 1. Code Style

Check for consistent code style:

- [ ] Consistent indentation (spaces vs tabs, width)
- [ ] Line length limits respected
- [ ] Consistent naming conventions (camelCase, snake_case, etc.)
- [ ] Proper use of whitespace
- [ ] Consistent bracket/brace style

### 2. File Organization

Verify file structure conventions:

- [ ] Files in correct directories
- [ ] Consistent file naming
- [ ] Proper module organization
- [ ] Import ordering (standard → third-party → local)

### 3. Documentation

Check documentation standards:

- [ ] All public APIs documented
- [ ] Docstrings follow project style (Google, NumPy, etc.)
- [ ] README files present and up-to-date
- [ ] CHANGELOG maintained

### 4. Type Safety

Verify type annotations (if applicable):

- [ ] Function parameters typed
- [ ] Return types specified
- [ ] No `Any` types without justification
- [ ] Type errors resolved

### 5. Testing Standards

Check test conventions:

- [ ] Test files follow naming convention
- [ ] Tests organized by unit/integration/e2e
- [ ] Sufficient test coverage
- [ ] Test documentation present

### 6. Error Handling

Verify error handling patterns:

- [ ] Consistent error types used
- [ ] Proper exception handling
- [ ] User-friendly error messages
- [ ] No silent failures

## Validation Commands

Run automated checks:

```bash
# Linting
make lint
# or
ruff check .
flake8 .
eslint .

# Type checking
mypy .
# or
tsc --noEmit

# Formatting
make format-check
# or
black --check .
prettier --check .

# All checks
make check
```

## Violation Report Template

When violations are found, document them:

```markdown
## Convention Violations Found

### {Category}

| Location | Violation | Severity | Fix |
|----------|-----------|----------|-----|
| `file.py:42` | {Description} | High/Medium/Low | {Fix suggestion} |

### Summary
- **Total violations**: X
- **High severity**: X
- **Medium severity**: X
- **Low severity**: X
```

## Auto-Fix Options

Many violations can be auto-fixed:

```bash
# Format code
make format
# or
black .
prettier --write .

# Sort imports
isort .

# Fix linting issues
ruff check --fix .
eslint --fix .
```

## Next Steps

After validating conventions:
- Fix any violations found
- Run `/lbi.review` for code review
- Run `/lbi.tests` to ensure fixes don't break functionality