---
description: "Implement the actual test code from scaffolds"
---

# Implement Tests

Write the actual test implementations.

## Purpose

Fill in the scaffolded test files with real test logic, assertions, and coverage.

## Prerequisites

- Test scaffolds created via `/lbi.qa.scaffold-tests`
- Test fixtures available via `/lbi.qa.generate-fixtures`
- Understanding of the feature being tested

## Instructions

1. Review scaffolded test files
2. Implement each test case
3. Run tests to verify
4. Ensure coverage targets met

## Implementation Guidelines

### Test Structure (AAA Pattern)

```python
def test_user_creation_success(self, client, sample_user):
    """Test successful user creation."""
    # Arrange - Set up test data and conditions
    user_data = {
        "email": "test@example.com",
        "name": "Test User",
    }

    # Act - Execute the code under test
    response = client.post("/users", json=user_data)

    # Assert - Verify the results
    assert response.status_code == 201
    assert response.json()["email"] == user_data["email"]
```

### Assertion Best Practices

```python
# Good - Specific assertions
assert result.status == "active"
assert len(result.items) == 3
assert "error" not in response.json()

# Better - With messages
assert result.status == "active", f"Expected active, got {result.status}"

# Use pytest helpers
pytest.approx(result.value, 0.1)  # For floats
pytest.raises(ValueError)  # For exceptions
```

### Testing Edge Cases

```python
class TestValidation:
    """Test input validation."""

    @pytest.mark.parametrize("invalid_email", [
        "",
        "not-an-email",
        "@missing-local.com",
        "missing-domain@",
        None,
    ])
    def test_rejects_invalid_email(self, client, invalid_email):
        """Test that invalid emails are rejected."""
        response = client.post("/users", json={"email": invalid_email})
        assert response.status_code == 422
```

### Mocking External Services

```python
from unittest.mock import Mock, patch

def test_payment_processing(self, client):
    """Test payment with mocked payment gateway."""
    with patch("services.payment.PaymentGateway") as mock_gateway:
        mock_gateway.return_value.charge.return_value = {
            "id": "charge_123",
            "status": "succeeded",
        }

        response = client.post("/payments", json={"amount": 100})

        assert response.status_code == 200
        mock_gateway.return_value.charge.assert_called_once()
```

### Database Testing

```python
def test_user_persistence(self, db_session, sample_user):
    """Test user is persisted correctly."""
    # Create user
    user = User(**sample_user)
    db_session.add(user)
    db_session.commit()

    # Verify persistence
    saved_user = db_session.query(User).filter_by(
        email=sample_user["email"]
    ).first()

    assert saved_user is not None
    assert saved_user.name == sample_user["name"]
```

## Coverage Requirements

Run coverage check:

```bash
pytest --cov=src --cov-report=term-missing --cov-fail-under=85
```

### Coverage Report Analysis

```
Name                    Stmts   Miss  Cover   Missing
-----------------------------------------------------
src/services/user.py      50      5    90%    42-46
src/services/order.py     80     12    85%    67-78
-----------------------------------------------------
TOTAL                    130     17    87%
```

Focus on:
- Missing lines in critical paths
- Untested error handling
- Edge case branches

## Test Quality Checklist

For each test file:

- [ ] All TODO placeholders replaced
- [ ] Tests are independent (no shared state)
- [ ] Tests are deterministic (no flaky tests)
- [ ] Meaningful assertion messages
- [ ] Proper cleanup in teardown
- [ ] Edge cases covered
- [ ] Error paths tested

## Next Steps

After implementation:
1. Run full test suite: `pytest tests/ -v`
2. Check coverage: `pytest --cov`
3. Run `/lbi.qa.review-tests` for test quality review