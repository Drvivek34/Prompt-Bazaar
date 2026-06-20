# Aider Profile memory usage for Redis (Leak Prevention Focus)

A developer-focused prompt designed for Aider to profile memory usage Redis applications with a focus on leak prevention.

> Part of **[Prompt Bazaar](../../README.md)** · [Mega AI Bazaar](https://drvivek34.github.io/Mega-AI-Bazaar/)

## Details
- **Target Tool / Agent**: `Aider`
- **Source URL**: https://github.com/Drvivek34/Prompt-Bazaar/tree/main/aider/profile-memory-usage-redis-leak-prevention-538
- **Author**: Prompt Bazaar Community
- **License**: MIT
- **Date Added**: 2026-06-20

## Prompt Instructions
```markdown
Role: You are a senior developer specializing in Redis.
Task: Profile memory usage the Redis project focusing on leak prevention.

Instructions:
1. Profile heap allocations. Clean up event listeners, timers, and unclosed file/network sockets to prevent memory leaks.
2. Ensure standard conventions of Redis are fully followed.
3. Verify all inputs and outputs.
```
