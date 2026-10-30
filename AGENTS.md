# ==============================================================================
# AGENTS.md: UNIVERSAL CROSS-AGENT SPECIFICATION (2026 EDITION)
# Recognized natively by VS Code Copilot, Claude Code, Codex, and Hermes
# ==============================================================================

You are working on `fastapi-template`, an enterprise-grade agentic FastAPI & LangGraph backend.

## Non-Negotiable Directives
1. **Never Vibe Code:** Do not generate speculative features, ungrounded helper functions, or phantom dependencies.
2. **5-Step Autonomous Lifecycle:**
   - **Phase 1 (Frontier Clarification):** Maximum 3 rounds of questions with recommendations (`➡️ Recommended: ...`). Verify ADR alignment with Confluence before committing architectural decisions.
   - **Phase 2 (Vertical-Slice TDD):** State agreed seam, write failing test (AAA), verify failure with `uv run pytest`, write minimal passing code.
   - **Phase 3 (Slice Progression):** Build tracer-bullet slices iteratively.
   - **Phase 4 (Refactor & Security Pass):** Verify SOLID, enforce OWASP API Top 10 (BOLA checks, `extra="forbid"`), run `uv run ruff check --fix .`.
   - **Phase 5 (Handoff):** Summarize verified state without hallucination.
3. **Response Envelopes:**
   - Success: `ResponseEnvelope[T]` with `data` and `meta` (request_id, pagination).
   - Error: RFC 9457 `ProblemDetails` (`application/problem+json`).
4. **Tooling & Commands:**
   - Package manager: `uv` (do not use pip or poetry directly).
   - Tests: `uv run pytest`
   - Migrations: `uv run alembic upgrade head`
   - Lint & format: `uv run ruff check --fix . && uv run ruff format .`
