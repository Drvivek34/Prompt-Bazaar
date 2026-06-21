# Claude Code Conventional Commits Prompt

Instructs Claude Code to write structured, semantic conventional commits whenever saving changes.

> Part of **[Prompt Bazaar](../../README.md)** · [Mega AI Bazaar](https://drvivek34.github.io/Mega-AI-Bazaar/)

## Details
- **Target Tool / Agent**: `Claude Code`
- **Source URL**: [https://github.com/anthropics/claude-code](https://github.com/anthropics/claude-code)
- **Author**: Claude Code Community
- **License**: MIT
- **Date Added**: 2026-06-21

## Prompt Instructions
```markdown
Before staging changes or running a commit, run 'git diff'. Generate a conventional commit message following this format: <type>(<scope>): <short description>. Types allowed: feat, fix, docs, style, refactor, perf, test, build, ci, chore. Keep the description under 60 characters and in the imperative mood.
```
