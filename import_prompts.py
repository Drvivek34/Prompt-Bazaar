#!/usr/bin/env python3
import os
from datetime import datetime

PROMPT_BAZAAR_DIR = "/root/bazaars/Prompt-Bazaar"

CURATED_PROMPTS = [
    {
        "name": "Claude Code Conventional Commits Prompt",
        "slug": "claude-code-conventional-commits",
        "category": "claude-code",
        "desc": "Instructs Claude Code to write structured, semantic conventional commits whenever saving changes.",
        "tool": "Claude Code",
        "author": "Claude Code Community",
        "source": "https://github.com/anthropics/claude-code",
        "prompt_text": "Before staging changes or running a commit, run 'git diff'. Generate a conventional commit message following this format: <type>(<scope>): <short description>. Types allowed: feat, fix, docs, style, refactor, perf, test, build, ci, chore. Keep the description under 60 characters and in the imperative mood."
    },
    {
        "name": "Claude Code Test-Driven Development Prompt",
        "slug": "claude-code-tdd-focus",
        "category": "claude-code",
        "desc": "Commands Claude Code to strictly follow TDD principles—writing test assertions first before modifying application logic.",
        "tool": "Claude Code",
        "author": "Agile Practictioners",
        "source": "https://docs.anthropic.com/en/docs",
        "prompt_text": "Always write the test first when creating a new feature or fixing a bug. First, create a failing test file in the appropriate directory. Run the test suite and verify that the test fails for the expected reasons. Then, write the minimum implementation code necessary to pass the test. Finally, refactor while keeping tests green."
    },
    {
        "name": "Aider Refactoring & Clean Code Rules",
        "slug": "aider-refactoring-rules",
        "category": "aider",
        "desc": "Guidelines that direct Aider to refactor existing code, optimize nested branches, and follow SOLID principles.",
        "tool": "Aider",
        "author": "Aider Community",
        "source": "https://aider.chat/docs/usage.html",
        "prompt_text": "Analyze the codebase for SOLID design principles. Look for complex nested branches and reduce cyclomatic complexity. Extract long functions into smaller, single-responsibility functions. Keep comments aligned with functional behavior. Ensure no formatting regressions are committed."
    },
    {
        "name": "Codex Project Structure Builder",
        "slug": "codex-structure-builder",
        "category": "codex",
        "desc": "A system instruction that directs Codex to map project layouts and generate code skeletons with clean interfaces.",
        "tool": "Codex",
        "author": "Codex Devs",
        "source": "https://github.com/google-gemini/gemini-cli",
        "prompt_text": "When starting a project, first draft a file map showcasing all folders, interfaces, and APIs. Write skeleton files containing classes, interfaces, and function signatures with docstrings. Do not implement details until the structure is approved by the user."
    },
    {
        "name": "Open REST API Design Prompt",
        "slug": "open-rest-api-design",
        "category": "open-code",
        "desc": "A generic prompt for designing clean RESTful API endpoints with standard response shapes and error handling.",
        "tool": "Generic / Agnostic",
        "author": "API Best Practices",
        "source": "https://restfulapi.net/",
        "prompt_text": "Design all API endpoints to follow RESTful standards. Use plural nouns for resources (e.g., /api/v1/users). Return standard JSON envelopes: { status: 'success', data: [...] } for success and { status: 'error', message: '...' } for errors. Implement standard HTTP status codes (200 OK, 201 Created, 400 Bad Request, 401 Unauthorized, 404 Not Found, 500 Internal Error)."
    }
]

def main():
    today_str = datetime.today().strftime("%Y-%m-%d")
    count = 0

    for item in CURATED_PROMPTS:
        cat_dir = os.path.join(PROMPT_BAZAAR_DIR, item["category"], item["slug"])
        os.makedirs(cat_dir, exist_ok=True)

        readme_content = f"""# {item['name']}

{item['desc']}

> Part of **[Prompt Bazaar](../../README.md)** · [Mega AI Bazaar](https://drvivek34.github.io/Mega-AI-Bazaar/)

## Details
- **Target Tool / Agent**: `{item['tool']}`
- **Source URL**: [{item['source']}]({item['source']})
- **Author**: {item['author']}
- **License**: MIT
- **Date Added**: {today_str}

## Prompt Instructions
```markdown
{item['prompt_text']}
```
"""
        with open(os.path.join(cat_dir, "README.md"), "w") as f:
            f.write(readme_content)
        count += 1
        print(f"Imported Prompt: {item['name']} -> {item['category']}/{item['slug']}")

    print(f"Successfully imported {count} prompts.")

if __name__ == "__main__":
    main()
