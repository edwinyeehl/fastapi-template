---
applyTo: "app/agents/**/*.py"
description: "LangGraph state management, reducers, persistent checkpointing, and HITL patterns."
---

# LangGraph Backend Engineering Standards

## 1. State Definition & Reducers
- Model agent state explicitly:
  ```python
  from typing import Annotated
  from typing_extensions import TypedDict
  from langchain_core.messages import BaseMessage
  from langgraph.graph.message import add_messages


  class AgentState(TypedDict):
      messages: Annotated[list[BaseMessage], add_messages]
      user_id: str
      step_count: int
  ```
- Use `add_messages` or explicit reducer functions (`operator.add`) for lists to avoid state overwrites across turns.

## 2. Checkpointing & Multi-Tenancy
- In production, graphs must compile with a persistent async checkpointer (`AsyncPostgresSaver` backed by PostgreSQL + pgvector).
- Thread isolation is mandatory: always supply a unique `thread_id` under `configurable` in `RunnableConfig`.
- Never reuse a `thread_id` across different user sessions.

## 3. Human-in-the-Loop (HITL) Interruption
- Use `interrupt()` for approval gates before dangerous actions.
- Expose resume routes via `graph.invoke(Command(resume=payload), config)`.
- Stream execution progress to frontend clients via Server-Sent Events (`fastapi.sse.EventSourceResponse`).
