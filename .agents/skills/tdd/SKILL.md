---
name: tdd
description: Test-driven development with Pytest. Use when building features or fixing bugs test-first in a vertical-slice red-green loop.
---
# Test-Driven Development (TDD)

TDD is the strict Red ➔ Green ➔ Refactor loop.

## Rules of the Loop
- **Agree on Seam:** Agree with the user which public interface or seam is being tested.
- **Red before Green:** Write one failing test first using Arrange-Act-Assert (AAA), and run it to verify failure.
- **One slice at a time:** Write minimal code to pass the current test.
- **Banned:** Horizontal slicing (bulk tests first), implementation coupling (testing internals), tautological assertions.
