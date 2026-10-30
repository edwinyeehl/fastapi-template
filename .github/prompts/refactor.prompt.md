Perform a disciplined refactoring and cleanup pass on the recently completed feature:

1. **Smell Check:** Check for Fowler code smells (feature envy, duplicated logic, bloated functions).
2. **SOLID Verification:**
   - Single Responsibility: Are routers thin?
   - Dependency Inversion: Are database sessions and dependencies injected via `Annotated[..., Depends(...)]`?
3. **OWASP API Top 10 Review:**
   - Are schemas using `extra="forbid"` to prevent mass assignment?
   - Are resource ownership checks in place to prevent BOLA?
4. **Code Quality:** Run `uv run ruff check --fix` and `uv run ruff format`.
5. Ensure all existing tests remain green.
