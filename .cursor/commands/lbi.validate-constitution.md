---
description: "Validate project compliance with constitution principles"
---

# Validate Constitution Compliance

Check that the current codebase adheres to constitutional principles.

## Purpose

Verify that code changes, pull requests, or the entire codebase comply with the non-negotiable principles defined in the project constitution.

## Prerequisites

- Constitution exists at `.lbi/memory/constitution.md`
- Codebase or changes to validate

## Instructions

1. Load the constitution from `.lbi/memory/constitution.md`
2. Extract all principles and quality standards
3. Validate codebase against each principle
4. Report compliance status

## Validation Process

### Step 1: Load Constitution

Read and parse the constitution file:

```markdown
# Constitution Check

**Constitution Version**: [version]
**Last Amended**: [date]
**Principles Found**: [count]
```

### Step 2: Extract Validation Rules

For each principle, identify:

- **Principle Name**: What it's called
- **Requirement**: What must be true
- **Validation Method**: How to check compliance

### Step 3: Run Validations

Check each principle against the codebase:

#### Code Quality Checks

| Check | Expected | Command | Status |
|-------|----------|---------|--------|
| Test Coverage | ≥ X% | `pytest --cov` | ✅/❌ |
| Linter | 0 errors | `ruff check .` | ✅/❌ |
| Type Check | 0 errors | `mypy src/` | ✅/❌ |

#### Principle-Specific Checks

For each constitutional principle:

```markdown
### Principle: [Name]

**Requirement**: [What must be true]

**Validation**:
- [ ] [Specific check 1]
- [ ] [Specific check 2]
- [ ] [Specific check 3]

**Status**: ✅ Compliant | ❌ Violation | ⚠️ Warning

**Evidence**: [Files checked, results found]
```

### Step 4: Generate Report

Create a compliance report:

```markdown
# Constitution Compliance Report

**Date**: [YYYY-MM-DD]
**Constitution Version**: [version]
**Scope**: [Full codebase / PR #X / Feature Y]

## Summary

| Category | Total | Passing | Failing |
|----------|-------|---------|---------|
| Principles | X | Y | Z |
| Quality Gates | X | Y | Z |
| Total | X | Y | Z |

## Principle Compliance

### ✅ Passing Principles

1. **[Principle Name]**: [Brief status]
2. **[Principle Name]**: [Brief status]

### ❌ Failing Principles

1. **[Principle Name]**
   - **Violation**: [What's wrong]
   - **Location**: [File/line]
   - **Required Action**: [How to fix]

### ⚠️ Warnings

1. **[Principle Name]**
   - **Issue**: [What's concerning]
   - **Recommendation**: [Suggested action]

## Quality Gate Status

| Gate | Threshold | Actual | Status |
|------|-----------|--------|--------|
| Test Coverage | ≥85% | 87% | ✅ |
| Linter Errors | 0 | 0 | ✅ |
| Type Errors | 0 | 3 | ❌ |

## Recommendations

1. [First priority fix]
2. [Second priority fix]
3. [Third priority fix]
```

## Common Validations

### Testing Principles

- TDD requirement: Check commit history for test-first patterns
- Coverage threshold: Run coverage report
- Required test types: Check for unit/integration test directories

### Code Quality Principles

- Type safety: Run type checker
- Linting: Run configured linter
- Documentation: Check docstring coverage

### Architecture Principles

- Layer separation: Check import patterns
- Dependency direction: Validate no circular imports
- Module boundaries: Check cross-module access

## Validation Commands

Common commands to run:

```bash
# Python projects
pytest --cov=src --cov-report=term-missing
ruff check src/ tests/
mypy src/ --strict

# JavaScript/TypeScript projects
npm test -- --coverage
npm run lint
npm run typecheck
```

## Output Format

Save report to `.lbi/reports/constitution-compliance-[date].md`

## Exit Status

- **Exit 0**: All principles compliant
- **Exit 1**: One or more violations found
- **Exit 2**: Constitution file not found

## Next Steps

After validation:
- If compliant: Proceed with `/lbi.review` or `/lbi.push`
- If violations: Fix issues and re-validate
- If warnings: Consider addressing before merge