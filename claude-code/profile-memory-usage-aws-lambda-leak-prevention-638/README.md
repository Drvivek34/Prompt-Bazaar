# Claude Code Profile memory usage for AWS Lambda (Leak Prevention Focus)

A developer-focused prompt designed for Claude Code to profile memory usage AWS Lambda applications with a focus on leak prevention.

> Part of **[Prompt Bazaar](../../README.md)** · [Mega AI Bazaar](https://drvivek34.github.io/Mega-AI-Bazaar/)

## Details
- **Target Tool / Agent**: `Claude Code`
- **Source URL**: https://github.com/Drvivek34/Prompt-Bazaar/tree/main/claude-code/profile-memory-usage-aws-lambda-leak-prevention-638
- **Author**: Prompt Bazaar Community
- **License**: MIT
- **Date Added**: 2026-06-20

## Prompt Instructions
```markdown
Role: You are a senior developer specializing in AWS Lambda.
Task: Profile memory usage the AWS Lambda project focusing on leak prevention.

Instructions:
1. Profile heap allocations. Clean up event listeners, timers, and unclosed file/network sockets to prevent memory leaks.
2. Ensure standard conventions of AWS Lambda are fully followed.
3. Verify all inputs and outputs.
```
