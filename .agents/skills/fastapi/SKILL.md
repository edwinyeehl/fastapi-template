---
name: fastapi
description: Official FastAPI best practices. Use when building RESTful endpoints, Annotated dependencies, and Pydantic models.
---
# FastAPI Best Practices

- Use `Annotated[..., Depends(...)]` for dependencies.
- Use `Annotated` with `Query`, `Path`, `Header` for route parameters.
- Do not use `...` as default values or Pydantic `RootModel`.
- Prefer explicit return types over redundant `response_model` when types match.
- Keep routers thin: validation, service dispatch, return response.
