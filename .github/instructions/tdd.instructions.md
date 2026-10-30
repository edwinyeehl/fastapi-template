---
applyTo: "tests/**/*.py"
description: "Test-Driven Development (TDD) guidelines, AAA structure, and async test client fixtures."
---

# Test-Driven Development (TDD) Standards

## 1. The Red-Green-Refactor Loop
- **Red:** Agree on the public seam, write one failing test verifying expected behavior, and run it (`uv run pytest tests/path/to/test.py`).
- **Green:** Implement the minimal code required to pass that single test.
- **Refactor:** Clean up code, remove duplication, and run lint checks while keeping the suite green.

## 2. Test Structure: Arrange-Act-Assert (AAA)
Every test function must follow the AAA structure clearly:
```python
import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app


@pytest.mark.asyncio
async def test_create_item_success():
    # Arrange
    payload = {"name": "Test Item", "price": 49.99}
    transport = ASGITransport(app=app)

    # Act
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.post("/api/v1/items", json=payload)

    # Assert
    assert response.status_code == 201
    assert response.json()["name"] == "Test Item"
```

## 3. Anti-Pattern Rules
- **No Implementation Coupling:** Never assert on internal helper calls or mock private methods. Test observable HTTP/service responses.
- **No Tautological Assertions:** Assert against concrete expected literals, never duplicate the implementation logic in the assert statement.
- **Vertical Slices:** Deliver behavior one slice at a time.
