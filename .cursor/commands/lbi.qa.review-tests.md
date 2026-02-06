---
description: "Review test quality and coverage"
---

# Review Tests

Evaluate test quality, coverage, and completeness.

## Purpose

Ensure tests are high-quality, maintainable, and provide adequate coverage before merging.

## Prerequisites

- Tests implemented via `/lbi.qa.implement`
- All tests passing

## Instructions

1. Run test suite with coverage
2. Analyze coverage report
3. Review test quality
4. Document findings and recommendations

## Review Process

### Step 1: Run Tests with Coverage

```bash
# Run all tests with coverage
pytest tests/ -v --cov=src --cov-report=html --cov-report=term-missing

# Run specific test categories
pytest tests/unit/ -v --cov=src
pytest tests/integration/ -v --cov=src
pytest tests/e2e/ -v
```

### Step 2: Coverage Analysis

```markdown
## Coverage Report

**Overall Coverage**: X%
**Target**: 85%
**Status**: ✅ Met / ❌ Below Target

### By Module

| Module | Statements | Covered | Missing | Coverage |
|--------|------------|---------|---------|----------|
| services/user.py | 50 | 45 | 5 | 90% |
| services/order.py | 80 | 68 | 12 | 85% |
| api/endpoints.py | 100 | 82 | 18 | 82% |

### Uncovered Lines

| File | Lines | Reason |
|------|-------|--------|
| services/user.py | 42-46 | Error handling path |
| api/endpoints.py | 78-82 | Edge case not tested |
```

### Step 3: Test Quality Review

```markdown
## Test Quality Checklist

### Structure
- [ ] Tests follow AAA pattern (Arrange-Act-Assert)
- [ ] Test names describe behavior being tested
- [ ] One assertion concept per test
- [ ] Tests are independent and isolated

### Maintainability
- [ ] No hardcoded magic values
- [ ] Fixtures used for test data
- [ ] No duplicate test code
- [ ] Clear failure messages

### Completeness
- [ ] Happy path covered
- [ ] Edge cases covered
- [ ] Error paths covered
- [ ] Boundary conditions tested

### Performance
- [ ] Tests run in reasonable time
- [ ] No unnecessary sleeps/waits
- [ ] Database fixtures properly scoped
- [ ] Mocks used for external services
```

### Step 4: Identify Issues

```markdown
## Issues Found

### Critical

1. **Missing Error Handling Tests**
   - Location: `test_user_service.py`
   - Issue: No tests for database connection errors
   - Recommendation: Add tests for exception scenarios

### Warnings

1. **Flaky Test Detected**
   - Location: `test_api_integration.py::test_concurrent_requests`
   - Issue: Fails intermittently due to timing
   - Recommendation: Add proper synchronization

### Suggestions

1. **Improve Test Names**
   - Current: `test_user_1`, `test_user_2`
   - Better: `test_user_creation_with_valid_data`, `test_user_creation_rejects_duplicate_email`
```

## Review Report Template

Create `.lbi/specs/{feature}/qa/review-report.md`:

```markdown
# Test Review Report: {Feature Name}

**Date**: {YYYY-MM-DD}
**Reviewer**: {Name}
**Status**: ✅ Approved / ❌ Changes Required

## Summary

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Coverage | X% | 85% | ✅/❌ |
| Tests Passing | X/Y | 100% | ✅/❌ |
| Test Quality | Good/Fair/Poor | Good | ✅/❌ |

## Coverage Analysis

[Coverage details here]

## Quality Assessment

[Quality findings here]

## Issues

### Must Fix Before Merge

1. [Critical issue]
2. [Critical issue]

### Should Fix

1. [Important improvement]
2. [Important improvement]

### Nice to Have

1. [Optional enhancement]

## Recommendations

[Summary of recommended actions]

## Approval

- [ ] Coverage targets met
- [ ] All critical issues resolved
- [ ] Tests pass consistently
- [ ] Code review approved
```

## Quality Gates

Tests must pass these gates:

| Gate | Requirement | Check Command |
|------|-------------|---------------|
| Coverage | ≥ 85% | `pytest --cov-fail-under=85` |
| All Pass | 100% | `pytest --tb=short` |
| No Skips | 0 skipped | `pytest -v \| grep -c SKIP` |
| Performance | < 60s | `pytest --timeout=60` |

## Next Steps

After review:
- If approved: Proceed to `/lbi.review` for code review
- If changes required: Address issues and re-run `/lbi.qa.review-tests`