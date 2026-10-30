---
applyTo: "app/**/*.py"
description: "OWASP API Top 10 security standards, input sanitization, and SOLID architecture."
---

# Security & Architecture Standards

## 1. OWASP API Top 10 Mitigations
- **Broken Object Level Authorization (BOLA):** Every endpoint operating on a specific resource ID must verify that the requesting user/tenant owns that resource.
- **Mass Assignment Prevention:** Always use Pydantic models with `extra="forbid"` for mutable update and creation payloads.
- **Injection Prevention:** Use SQLAlchemy async queries with parameterized bounds or ORM constructs. Raw SQL string concatenation is strictly banned.
- **Error Sanitization:** Never leak internal database stack traces, file paths, or raw driver errors to API clients. Catch internal exceptions and return structured `HTTPException(status_code=..., detail=...)`.

## 2. SOLID Implementation
- **Single Responsibility:** Routers do not execute database queries directly; they delegate to repository or service layers.
- **Dependency Inversion:** Depend on abstractions via FastAPI dependencies (`Depends()`), enabling frictionless swapping with mock sessions in unit tests.
