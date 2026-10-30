---
name: grilling
description: Conduct a structured pre-build grilling interview on a feature or architecture. Use when starting a new task or clarifying intentions.
---
# Grilling Skill

Interview the developer to clarify intentions, boundaries, and acceptance criteria before writing production code.

## Rules
1. Map the plan as a decision tree.
2. Group unsettled prerequisites into rounds (maximum 3 rounds).
3. For every question, always offer a **concrete recommendation** so the developer reacts to a proposal rather than a blank prompt.
4. **ADR Governance Gate:** When an architectural change or decision is required, **STOP** and ask:
   > *"This architectural decision requires alignment. Has this decision already been reviewed and approved in Confluence or the team's official ADR records?"*
   Never generate or assume an ADR without explicit team confirmation.
