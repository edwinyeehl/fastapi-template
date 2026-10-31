---
applyTo: "tests/**/*.py"
description: "Strict Test-Driven Development (TDD) rules, Iron Law, red-green loop, and rationalization blockers."
---

# Test-Driven Development (TDD) — The Iron Law

Write the test first. Watch it fail. Write minimal code to pass.

**Core principle:** If you didn't watch the test fail, you don't know if it tests the right thing.
**Violating the letter of the rules is violating the spirit of the rules.**

---

## The Iron Law

```
NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST
```

Write code before the test? **Delete it. Start over.**
- Don't keep it as "reference"
- Don't "adapt" it while writing tests
- Don't look at it
- Delete means delete. Implement fresh from tests. Period.

---

## When to Use

**Always:**
- New features
- Bug fixes
- Refactoring
- Behavior changes

**Exceptions (ask your human partner):**
- Throwaway prototypes
- Generated migration files
- Pure configuration files

Thinking *"skip TDD just this once"*? **Stop. That's rationalization.**

---

## The Red-Green-Refactor Loop

```
  ┌─────────────────────────┐
  │  RED: Write Failing Test │
  └────────────┬────────────┘
               ▼
  ┌─────────────────────────┐     Wrong failure
  │   Verify RED (Fails?)   │ ────────────────────► (Fix test)
  └────────────┬────────────┘
               ▼ Yes
  ┌─────────────────────────┐
  │   GREEN: Minimal Code   │
  └────────────┬────────────┘
               ▼
  ┌─────────────────────────┐     Fails / Breaks others
  │  Verify GREEN (Passes?) │ ────────────────────► (Fix code)
  └────────────┬────────────┘
               ▼ Yes
  ┌─────────────────────────┐
  │   REFACTOR: Clean Up    │
  └────────────┬────────────┘
               ▼
         (Next Slice)
```

### 1. RED — Write Failing Test
Write one minimal test showing what should happen using the **Arrange-Act-Assert (AAA)** pattern:
```python
import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app

@pytest.mark.asyncio
async def test_rejects_empty_email():
    # Arrange
    payload = {"email": ""}
    transport = ASGITransport(app=app)

    # Act
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.post("/api/v1/auth/register", json=payload)

    # Assert
    assert response.status_code == 422
    assert response.json()["status"] == 422
```
- **Requirements:** One behavior, clear name describing intent, real code (no mocks unless unavoidable).

### 2. Verify RED — Watch It Fail (**MANDATORY**)
Execute:
```bash
uv run pytest tests/path/to/test.py -k test_name
```
**Confirm:**
- Test fails (does not error out with syntax/import crashes).
- Failure message is the exact expected assertion error.
- Fails because feature is missing (not due to a typo).

*Test passes?* You're testing existing behavior. Fix test.  
*Test errors out?* Fix import/fixture error, re-run until it fails on assertion.

### 3. GREEN — Minimal Code
Write the simplest code to pass the test.
- Don't add speculative features (YAGNI).
- Don't refactor other code.
- Don't "improve" beyond what satisfies the test.

### 4. Verify GREEN — Watch It Pass (**MANDATORY**)
Execute:
```bash
uv run pytest tests/path/to/test.py -k test_name
```
**Confirm:**
- Test passes.
- **Run the whole test suite:** `uv run pytest`. Other tests must still pass.
- Output is pristine (zero warnings, zero errors).

### 5. REFACTOR — Clean Up
After green only:
- Remove duplication, improve variable names, extract helpers.
- Run `uv run ruff check --fix .` and `uv run ruff format .`.
- Keep tests green. Never add behavior during refactor.

---

## Common Rationalizations & Red Flags

| Excuse | Reality |
| :--- | :--- |
| *"Too simple to test"* | Simple code breaks. Test takes 30 seconds. |
| *"I'll test after"* | Tests written after pass immediately — proving nothing. You never proved it can catch the bug. |
| *"Already manually tested"* | Manual testing is ad-hoc, unrepeatable, and forgotten under pressure. |
| *"Deleting X hours is wasteful"* | Sunk cost fallacy. Keeping unverified code is technical debt. Delete and rewrite test-first. |
| *"Need to explore first"* | Fine. Throw away exploration code, start fresh with TDD. |

### Red Flags — STOP and Start Over:
- Code written before test
- Test added "later"
- Test passes immediately on first run
- Can't explain why test failed
- "Just this once" rationalization

**All of these mean: Delete code. Start over with TDD.**
