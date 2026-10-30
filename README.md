# FastAPI Agentic & LangGraph Backend Template (2026 Edition)

Modern, test-driven, agent-ready **FastAPI** backend template configured with **uv**, **Alembic**, **PostgreSQL + pgvector**, **Pytest**, **Ruff**, and **VS Code Copilot / Agentic Skills**.

---

## ⚡ Tech Stack & Architecture

- **Runtime & Framework:** Python 3.11+, FastAPI (Pydantic v2, `Annotated` dependency injection).
- **Package Manager:** [`uv`](https://github.com/astral-sh/uv) (blazing-fast resolution & environments).
- **Database & Vectors:** PostgreSQL 17 with `pgvector` extension.
- **ORM & Migrations:** SQLAlchemy 2.0 (asyncio + `asyncpg`) + Alembic async runner.
- **Standardized API Envelopes:** JSend-style `ResponseEnvelope` for successful payloads and RFC 9457 `ProblemDetails` (`application/problem+json`) for errors.
- **Testing & Quality:** Pytest (`pytest-asyncio`, `httpx` ASGI transport), Ruff (linter & formatter).
- **Git Hooks:** `pre-commit` and `pre-push` hooks running unit tests and linters automatically to block invalid commits/pushes.
- **Observability & Logging:** Structured JSON logging (`structlog`) with request IDs, plus integrated **Langfuse** tracing callback support for LangGraph workflows.
- **Agentic Infrastructure:** LangGraph ready with persistent thread checkpointing and vector store schema.
- **VS Code Copilot Engine:** Hierarchical agent instructions (`.github/copilot-instructions.md`), path-specific rules (`.github/instructions/`), and universal cross-agent rules (`AGENTS.md`).

---

## 🚀 Quick Start

### 1. Prerequisites
Ensure you have `uv` installed and a PostgreSQL instance running with `pgvector`:
```bash
brew install uv
# or curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Environment Configuration
Copy the environment file:
```bash
cp .env.example .env
```
Update your `POSTGRES_*` credentials in `.env` to point to your PostgreSQL instance.

### 3. Database Migrations
Run Alembic async migrations to provision `pgvector` and initial tables:
```bash
uv run alembic upgrade head
```

### 4. Run the Dev Server
```bash
uv run fastapi dev main.py
```
Visit the interactive Swagger API documentation at: [http://localhost:8000/docs](http://localhost:8000/docs)

### 5. Run Tests & Linter
```bash
# Run test suite
uv run pytest

# Check code format and linting
uv run ruff check .
uv run ruff format .
```

---

## 🤖 VS Code Copilot & Agentic Workflow

This repository enforces a strict **5-Step Agentic Discipline** for developers and AI pair programmers:

1. **Frontier Grilling Interview (Max 3 Rounds):**
   - Use `/grill` in Copilot Chat.
   - The agent reads codebase context first, maps a decision tree, and asks clarifying questions with concrete recommendations.
   - **ADR Governance Gate:** When an architectural decision is required, the agent **stops and prompts the user** to verify whether it has been approved in Confluence/team ADR records before proceeding.
2. **Vertical-Slice TDD (Red ➔ Green):**
   - Use `/tdd`.
   - Agree on the public seam, write one failing test using the **Arrange-Act-Assert (AAA)** structure, and verify failure (**Red**).
   - Write minimal implementation code to pass (**Green**).
3. **Iterative Build:** Progress slice by slice through the feature frontier.
4. **Refactor & Security Review:**
   - Use `/refactor`.
   - Check Fowler code smells, verify SOLID boundaries, and enforce OWASP API Top 10 (preventing BOLA, mass assignment, injection).
5. **Handoff:**
   - Use `/handoff` to summarize settled decisions, open frontiers, and active commands into a structured document.

---

## 📂 Project Structure

```text
fastapi-template/
├── .github/
│   ├── copilot-instructions.md      # Always-on master workflow rules
│   └── instructions/                # Path-specific rules (applyTo)
│       ├── fastapi.instructions.md  # FastAPI & Annotated standards
│       ├── tdd.instructions.md      # Pytest & AAA pattern
│       ├── security.instructions.md # OWASP API Top 10 & SOLID
│       └── langgraph.instructions.md# LangGraph state & checkpointing
├── .agents/skills/                  # Universal agent skills (Codex, Claude, Hermes)
│   ├── grilling/SKILL.md
│   ├── tdd/SKILL.md
│   ├── fastapi/SKILL.md
│   └── handoff/SKILL.md
├── AGENTS.md                        # Universal root spec for modern IDE agents
├── alembic/                         # Database migrations
│   ├── versions/
│   │   └── 0001_initial_pgvector.py # pgvector extension & base schema
│   └── env.py                       # Async Alembic runner
├── app/
│   ├── core/
│   │   ├── config.py                # Pydantic v2 settings & Langfuse config
│   │   ├── database.py              # Async SQLAlchemy engine & session
│   │   ├── logging.py               # Structured JSON logging (structlog)
│   │   └── observability.py         # Langfuse callback generator
│   ├── api/                         # RESTful API routers
│   ├── models/                      # SQLAlchemy & pgvector ORM entities
│   ├── schemas/
│   │   └── envelope.py              # ResponseEnvelope & RFC 9457 ProblemDetails
│   └── services/                    # Domain logic & LangGraph agent workflows
├── tests/
│   └── test_main.py                 # Async integration test with envelope assertion
├── .pre-commit-config.yaml          # Pre-commit & pre-push hooks (ruff + pytest)
├── pyproject.toml                   # Project dependencies & tool configs
└── main.py                          # FastAPI application entrypoint with middleware
```
