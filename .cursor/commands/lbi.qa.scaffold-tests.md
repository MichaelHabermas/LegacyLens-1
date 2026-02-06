---
description: "Generate test file scaffolding based on test plan"
---

# Scaffold Tests

Create the test file structure and boilerplate.

## Purpose

Generate empty test files with proper structure, imports, and placeholder test cases based on the test plan.

## Prerequisites

- Test plan at `.lbi/specs/{feature}/qa/test-plan.md`
- QA tasks at `.lbi/specs/{feature}/qa/tasks.md`

## Instructions

1. Review test plan and tasks
2. Create test directory structure
3. Generate test file scaffolds
4. Add placeholder test functions

## Directory Structure

```
tests/
├── unit/
│   └── {feature}/
│       ├── test_{component_a}.py
│       └── test_{component_b}.py
├── integration/
│   └── {feature}/
│       ├── test_{endpoint_a}.py
│       └── test_{endpoint_b}.py
└── e2e/
    └── {feature}/
        └── test_{workflow}.py
```

## Scaffold Templates

### Unit Test Scaffold

```python
"""
Unit tests for {Component}.

Tests cover:
- {functionality 1}
- {functionality 2}
"""

import pytest
from {module} import {Component}


class Test{Component}:
    """Tests for {Component} class."""

    @pytest.fixture
    def instance(self):
        """Create test instance."""
        return {Component}()

    def test_{function}_success(self, instance):
        """Test {function} with valid input."""
        # Arrange
        # Act
        # Assert
        pytest.skip("TODO: Implement test")

    def test_{function}_invalid_input(self, instance):
        """Test {function} with invalid input."""
        pytest.skip("TODO: Implement test")

    def test_{function}_edge_case(self, instance):
        """Test {function} edge case."""
        pytest.skip("TODO: Implement test")
```

### Integration Test Scaffold

```python
"""
Integration tests for {Feature} API.

Tests cover:
- {endpoint 1}
- {endpoint 2}
"""

import pytest
from fastapi.testclient import TestClient
from {app} import app


class Test{Feature}API:
    """Integration tests for {Feature} endpoints."""

    @pytest.fixture
    def client(self):
        """Create test client."""
        return TestClient(app)

    @pytest.fixture
    def auth_headers(self):
        """Create authenticated headers."""
        return {"Authorization": "Bearer test-token"}

    def test_{endpoint}_success(self, client, auth_headers):
        """Test {endpoint} returns success."""
        pytest.skip("TODO: Implement test")

    def test_{endpoint}_unauthorized(self, client):
        """Test {endpoint} requires auth."""
        pytest.skip("TODO: Implement test")

    def test_{endpoint}_validation(self, client, auth_headers):
        """Test {endpoint} validates input."""
        pytest.skip("TODO: Implement test")
```

### E2E Test Scaffold

```python
"""
End-to-end tests for {Workflow}.

Tests cover complete user workflow:
- {step 1}
- {step 2}
- {step 3}
"""

import pytest


class Test{Workflow}E2E:
    """E2E tests for {Workflow}."""

    @pytest.fixture(autouse=True)
    def setup(self, test_db):
        """Set up test environment."""
        pass

    def test_complete_workflow(self):
        """Test complete {workflow} from start to finish."""
        pytest.skip("TODO: Implement test")

    def test_workflow_error_recovery(self):
        """Test workflow handles errors gracefully."""
        pytest.skip("TODO: Implement test")
```

## Conftest Template

```python
"""
Shared fixtures for {feature} tests.
"""

import pytest


@pytest.fixture
def test_db():
    """Provide test database."""
    # Setup
    yield db
    # Teardown


@pytest.fixture
def sample_data():
    """Provide sample test data."""
    return {
        "field": "value",
    }
```

## Next Steps

After scaffolding:
1. Run `/lbi.qa.generate-fixtures` to create test data
2. Run `/lbi.qa.implement` to fill in test implementations