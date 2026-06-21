# Claude Code Test-Driven Development Prompt

Commands Claude Code to strictly follow TDD principles—writing test assertions first before modifying application logic.

> Part of **[Prompt Bazaar](../../README.md)** · [Mega AI Bazaar](https://drvivek34.github.io/Mega-AI-Bazaar/)

## Details
- **Target Tool / Agent**: `Claude Code`
- **Source URL**: [https://docs.anthropic.com/en/docs](https://docs.anthropic.com/en/docs)
- **Author**: Agile Practictioners
- **License**: MIT
- **Date Added**: 2026-06-21

## Prompt Instructions
```markdown
Always write the test first when creating a new feature or fixing a bug. First, create a failing test file in the appropriate directory. Run the test suite and verify that the test fails for the expected reasons. Then, write the minimum implementation code necessary to pass the test. Finally, refactor while keeping tests green.
```
