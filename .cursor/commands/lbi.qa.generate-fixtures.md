---
description: "Generate test fixtures and sample data"
---

# Generate Test Fixtures

Create reusable test data and fixtures.

## Purpose

Generate consistent, realistic test data that can be used across all test types.

## Prerequisites

- Data architecture documentation (entity catalog)
- Test plan defining data requirements

## Instructions

1. Review entity catalog from architecture docs
2. Identify required test data
3. Generate fixtures for each entity
4. Create factory functions for dynamic data

## Fixture Types

### Static Fixtures (JSON/YAML)

For unchanging reference data:

```yaml
# tests/fixtures/users.yaml
valid_user:
  email: "test@example.com"
  name: "Test User"
  role: "user"

admin_user:
  email: "admin@example.com"
  name: "Admin User"
  role: "admin"

invalid_users:
  - email: ""
    name: "Missing Email"
  - email: "invalid"
    name: "Bad Email Format"
```

### Factory Fixtures (Python)

For dynamic test data:

```python
# tests/fixtures/factories.py
"""Test data factories."""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional
import uuid


@dataclass
class UserFactory:
    """Factory for creating test users."""

    @staticmethod
    def create(
        email: Optional[str] = None,
        name: str = "Test User",
        role: str = "user",
    ) -> dict:
        """Create a user dict with optional overrides."""
        return {
            "id": str(uuid.uuid4()),
            "email": email or f"user-{uuid.uuid4().hex[:8]}@test.com",
            "name": name,
            "role": role,
            "created_at": datetime.utcnow().isoformat(),
        }

    @staticmethod
    def create_batch(count: int) -> list:
        """Create multiple users."""
        return [UserFactory.create() for _ in range(count)]


@dataclass
class OrderFactory:
    """Factory for creating test orders."""

    @staticmethod
    def create(
        user_id: Optional[str] = None,
        status: str = "pending",
        total: float = 100.00,
    ) -> dict:
        """Create an order dict."""
        return {
            "id": str(uuid.uuid4()),
            "user_id": user_id or str(uuid.uuid4()),
            "status": status,
            "total": total,
            "items": [],
            "created_at": datetime.utcnow().isoformat(),
        }
```

### Pytest Fixtures

```python
# tests/conftest.py
"""Shared pytest fixtures."""

import pytest
from tests.fixtures.factories import UserFactory, OrderFactory


@pytest.fixture
def sample_user():
    """Provide a sample user."""
    return UserFactory.create()


@pytest.fixture
def sample_users():
    """Provide multiple sample users."""
    return UserFactory.create_batch(5)


@pytest.fixture
def sample_order(sample_user):
    """Provide a sample order with user."""
    return OrderFactory.create(user_id=sample_user["id"])


@pytest.fixture
def admin_user():
    """Provide an admin user."""
    return UserFactory.create(role="admin")
```

### Database Fixtures

```python
# tests/fixtures/database.py
"""Database fixtures for integration tests."""

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.models import Base


@pytest.fixture(scope="session")
def db_engine():
    """Create test database engine."""
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    yield engine
    engine.dispose()


@pytest.fixture
def db_session(db_engine):
    """Provide database session with rollback."""
    Session = sessionmaker(bind=db_engine)
    session = Session()
    yield session
    session.rollback()
    session.close()


@pytest.fixture
def seeded_db(db_session, sample_users):
    """Provide database with seed data."""
    from src.models import User
    for user_data in sample_users:
        user = User(**user_data)
        db_session.add(user)
    db_session.commit()
    return db_session
```

## Fixture Organization

```
tests/
├── conftest.py              # Shared fixtures
├── fixtures/
│   ├── __init__.py
│   ├── factories.py         # Factory classes
│   ├── database.py          # DB fixtures
│   ├── users.yaml           # Static user data
│   ├── orders.yaml          # Static order data
│   └── responses/           # API response mocks
│       ├── success.json
│       └── error.json
```

## Best Practices

1. **Isolation**: Each test gets fresh data
2. **Realism**: Data should be realistic
3. **Determinism**: Same inputs = same outputs
4. **Documentation**: Document fixture purpose
5. **Scoping**: Use appropriate pytest scopes

## Next Steps

After generating fixtures:
1. Run `/lbi.qa.implement` to use fixtures in tests
2. Verify fixtures work: `pytest tests/ -v --collect-only`