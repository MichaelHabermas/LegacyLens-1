---
description: "Write and run tests"
---

# Testing

Write tests for the implemented feature and ensure quality.

## Prerequisites

- Complete `/lbi.implement` first
- Implementation is complete

## Instructions

1. Review the specification test scenarios
2. Write unit tests for new functions
3. Write integration tests for workflows
4. Run all tests and fix failures

## Testing Guidelines

### Test Structure

```python
def test_feature_does_expected_behavior():
    """
    Test that feature produces expected result.
    
    Given: {precondition}
    When: {action}
    Then: {expected outcome}
    """
    # Arrange
    ...
    
    # Act
    ...
    
    # Assert
    ...
```

### Coverage Requirements

- Minimum 80% code coverage for new code
- All public functions must have tests
- Edge cases and error conditions tested

### Test Categories

1. **Unit Tests**: Test individual functions in isolation
2. **Integration Tests**: Test component interactions
3. **End-to-End Tests**: Test complete workflows

## Running Tests

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=src/lbi

# Run specific test file
uv run pytest tests/unit/test_feature.py
```

## Quality Checklist

- [ ] All tests pass
- [ ] Coverage meets minimum threshold
- [ ] Edge cases covered
- [ ] Error conditions tested
- [ ] No flaky tests

## Next Steps

After tests pass, run `/lbi.review` for code review.