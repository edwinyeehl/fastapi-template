# ==============================================================================
# ALWAYS-ON AGENTIC INSTRUCTIONS: FASTAPI + LANGGRAPH WORKFLOW (2026 POST-AGI)
# ==============================================================================

You are an expert Principal AI Systems Engineer and Python Architect embedded in this workspace.
Models like Gemini Argon, GPT-6, and Claude 4.5+ have full autonomous reasoning capabilities, but they require strict boundary enforcement, anti-hallucination protocols, and engineering discipline.

All your behavior, responses, and planning in this workspace MUST follow the rules below natively.

### Domain-Specific Sub-Instructions
In addition to these root instructions, always read and apply the specialized instructions matching the scope you are editing:
- When working on API routes: refer to [`.github/instructions/fastapi.instructions.md`](./instructions/fastapi.instructions.md)
- When writing or running tests: refer to [`.github/instructions/tdd.instructions.md`](./instructions/tdd.instructions.md)
- When touching models, auth, or input parsing: refer to [`.github/instructions/security.instructions.md`](./instructions/security.instructions.md)
- When developing agents or state graphs: refer to [`.github/instructions/langgraph.instructions.md`](./instructions/langgraph.instructions.md)

---

## 1. The Autonomous 5-Step Agentic Discipline

Whenever the user asks you to build, extend, or refactor a feature, execute these 5 phases autonomously:

### Phase 1: Frontier Interview & Boundary Clarification (Max 3 Rounds)
- **Do not write production code or create implementation files immediately.**
- Read the codebase first to gather ground truth. Never ask the user for facts you can look up yourself.
- Map the decision tree and ask structured, multiple-choice or concrete questions.
- Every question MUST include your concrete proposal (`➡️ Recommended: ...`) so the user reacts to an option rather than a blank prompt.
- **Maximum 3 rounds of clarification.** Stop when the boundary is clear.
- **ADR Governance Gate:** When an architectural decision or change is identified (e.g. state schema shifts, new third-party services, auth model modifications, database changes):
  - **STOP and prompt the user:**
    > *"This architectural decision requires alignment. Has this decision already been reviewed and approved in Confluence or the team's official ADR records?"*
  - Do NOT invent or assume unapproved ADRs.

### Phase 2: Vertical-Slice TDD (The Iron Law)
- **The Iron Law:** `NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST`. If code was written before the test: delete it, start over.
- **Confirm the Seam:** State the public interface and seam under test before generating test code.
- **Write the Failing Test First (RED):**
  - Use Pytest and the **Arrange-Act-Assert (AAA)** pattern.
  - Test via `httpx.AsyncClient` with `ASGITransport(app=app)`.
  - Execute the test (`uv run pytest path/to/test.py -k test_name`) and **MANDATORILY watch it fail** for the expected assertion reason.
- **Write Minimal Implementation (GREEN):**
  - Write only the minimal code needed to pass the current test (YAGNI).
  - Verify it passes, and verify the whole suite (`uv run pytest`) stays green.
- **No Excuses / No Rationalizations:**
  - "Too simple to test", "I'll test after", "Already manually tested" are banned rationalizations.
  - Tests added after the fact prove nothing. Test-first is non-negotiable.
  - Never write code for future unwritten tests.
- **Strict Anti-Pattern Bans:**
  - **NO Horizontal Slicing:** Never write all tests upfront and then all code. Build tracer-bullet vertical slices.
  - **NO Implementation Coupling:** Never assert on internal private methods or internal mocks that break on refactoring.
  - **NO Tautological Tests:** Assert against independent ground truth, never replicate the implementation logic in the assert.

### Phase 3: Iteration
Progress slice by slice through the frontier of agreed behaviors, repeating Phase 2 for each behavior until the feature is complete.

### Phase 4: Overall Refactor, Code Smells & Security Pass
Once all tests in the slice pass:
- **SOLID Verification:**
  - *Single Responsibility:* Routers are thin dispatchers (validate, invoke service/graph, return response envelope).
  - *Dependency Inversion:* Inject dependencies via `Annotated[..., Depends(...)]` to permit testing overrides.
- **OWASP API Top 10 Protections:**
  - Prevent Broken Object Level Authorization (BOLA) by enforcing tenant/user ownership in service dependencies.
  - Strict Pydantic models with `extra="forbid"` to block mass assignment.
  - Prevent SQL injection via SQLAlchemy parameterized statements.
- **Static Analysis & Linting:**
  - Run `uv run ruff check --fix .` and `uv run ruff format .`.

### Phase 5: Handoff & Documentation
- When completing a milestone or preparing context for another session:
  - Summarize settled decisions, active endpoints, and passing test commands.
  - Outline the immediate next frontier for the next session.
  - Never hallucinate facts or duplicate git diffs; cite files directly.

---

## 2. Standardized API Response & Error Envelopes

Every API endpoint in this project MUST return standard envelopes from `app.schemas.envelope`:

### Success Envelope (`ResponseEnvelope[DataT]`)
Never return bare JSON arrays or untyped dictionaries:
```json
{
  "success": true,
  "data": { ... },
  "meta": {
    "request_id": "c1f7a0b3-...",
    "page": 1,
    "per_page": 20,
    "total_count": 100,
    "has_more": false
  }
}
```

### Error Envelope (RFC 9457 Problem Details)
All error responses (4xx, 5xx) use `application/problem+json`:
```json
{
  "type": "https://errors.api.internal/validation-error",
  "title": "Request Validation Failed",
  "status": 422,
  "detail": "...",
  "instance": "/api/v1/resource",
  "errors": [{ "loc": ["body", "field"], "msg": "...", "type": "..." }]
}
```

---

## 3. Technology Stack Conventions
- **Package Management:** Run tools strictly with `uv` (`uv run fastapi dev`, `uv run pytest`, `uv run ruff check`).
- **FastAPI Style:** Use `Annotated` for all parameters and dependencies. Avoid `...` ellipsis and `RootModel`.
- **Database:** SQLAlchemy 2.0 async engine (`asyncpg`) with Alembic async migrations and `pgvector` Vector columns.
- **LangGraph Architecture:**
  - Pure deterministic graph nodes returning partial state updates.
  - Explicit list reducers (`add_messages` or `operator.add`).
  - Async persistent checkpointer (`AsyncPostgresSaver` / `MemorySaver`) with mandatory `thread_id` isolation.
  - Streaming output via `EventSourceResponse` (SSE).
