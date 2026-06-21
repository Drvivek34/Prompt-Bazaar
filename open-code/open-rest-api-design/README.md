# Open REST API Design Prompt

A generic prompt for designing clean RESTful API endpoints with standard response shapes and error handling.

> Part of **[Prompt Bazaar](../../README.md)** · [Mega AI Bazaar](https://drvivek34.github.io/Mega-AI-Bazaar/)

## Details
- **Target Tool / Agent**: `Generic / Agnostic`
- **Source URL**: [https://restfulapi.net/](https://restfulapi.net/)
- **Author**: API Best Practices
- **License**: MIT
- **Date Added**: 2026-06-21

## Prompt Instructions
```markdown
Design all API endpoints to follow RESTful standards. Use plural nouns for resources (e.g., /api/v1/users). Return standard JSON envelopes: { status: 'success', data: [...] } for success and { status: 'error', message: '...' } for errors. Implement standard HTTP status codes (200 OK, 201 Created, 400 Bad Request, 401 Unauthorized, 404 Not Found, 500 Internal Error).
```
