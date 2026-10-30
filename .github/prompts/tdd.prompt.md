You are executing a disciplined Test-Driven Development (TDD) loop for the current slice:

1. **Confirm the Seam:** Ask/confirm with the user: *"What is the public interface and seam under test?"*
2. **Write the Failing Test First (Red):**
   - Use Pytest and the Arrange-Act-Assert (AAA) structure.
   - Use `httpx.AsyncClient` with `ASGITransport(app=app)`.
   - Run the test to confirm it fails for the expected reason.
3. **Write the Minimal Implementation (Green):**
   - Write only enough code to pass the current test.
   - Avoid horizontal slicing (writing multiple tests before implementation).
4. Run the suite to verify all tests pass.
