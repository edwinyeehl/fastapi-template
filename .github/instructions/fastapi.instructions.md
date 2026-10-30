---
applyTo: "app/api/**/*.py"
description: "FastAPI RESTful API design standards, routing, and Annotated dependency injection."
---

# FastAPI Development Standards

## 1. Routing & Organization
- Routers must declare their `prefix` and `tags` directly on the `APIRouter` instance:
  ```python
  router = APIRouter(prefix="/users", tags=["users"])
  ```
- Keep routers razor-thin: validation, permission check, dispatch to domain service or LangGraph runner, and return response.
- Use one HTTP operation per function (e.g. `get_item`, `create_item`).

## 2. Parameter Declarations & Dependencies
- Strictly use `Annotated` for all query params, path params, headers, and dependency injections:
  ```python
  from typing import Annotated
  from fastapi import APIRouter, Depends, Query, Path

  SessionDep = Annotated[AsyncSession, Depends(get_db_session)]
  ```
- Never use `...` as default parameter values.

## 3. Request & Response Models
- Define separate schemas for input requests and output responses.
- Enforce strict schemas:
  ```python
  class ItemCreate(BaseModel):
      name: str
      price: float
      model_config = ConfigDict(extra="forbid")
  ```
- Always provide an explicit return type on path operations.
