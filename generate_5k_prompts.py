#!/usr/bin/env python3
import os
import re

PROMPT_BAZAAR_DIR = "/root/bazaars/Prompt-Bazaar"

tools = {
    "claude-code": "Claude Code",
    "aider": "Aider",
    "codex": "Codex",
    "open-code": "Generic / Agnostic",
    "misc": "Generic / Agnostic"
}

technologies = [
    "Python", "JavaScript", "TypeScript", "React", "Node.js", "Django", "Flask", "FastAPI",
    "Spring Boot", "Rust", "Go", "Java", "C++", "Ruby on Rails", "Laravel", "Vue.js",
    "Angular", "Express.js", "PostgreSQL", "MongoDB", "MySQL", "Redis", "Docker", "Kubernetes",
    "Terraform", "AWS Lambda", "GitHub Actions", "Svelte", "TailwindCSS", "PyTorch", "TensorFlow",
    "Next.js", "Nuxt.js", "GraphQL", "Elasticsearch", "Apache Kafka", "RabbitMQ", "Webpack",
    "Vite", "Jest", "Cypress", "Selenium", "Pandas", "NumPy", "Swift", "Kotlin", "Flutter",
    "React Native", "Ansible", "Jenkins"
]

tasks = [
    ("Refactor", "clean-code", "Analyze the file for cognitive complexity. Refactor deeply nested if-else structures into early return guards. Extract utility helper functions."),
    ("Write unit tests", "test-coverage", "Write comprehensive unit tests using standard testing libraries. Cover edge cases, empty states, and invalid inputs. Mock network requests."),
    ("Optimize performance", "execution-speed", "Review database queries or loops. Identify N+1 query problems and optimize index usage. Minimize memory allocations and CPU overhead."),
    ("Implement security checks", "threat-mitigation", "Scan code for OWASP Top 10 vulnerabilities. Prevent SQL injection, XSS, and command injection. Ensure input validation is strict."),
    ("Create API endpoints", "api-design", "Design standard endpoints. Return clear status codes and standard JSON envelope format. Handle exceptions gracefully."),
    ("Configure CI/CD pipeline", "automation-flow", "Draft a build/test pipeline. Cache dependencies to speed up runs. Run linters, security scanners, and test suites."),
    ("Document code", "readability", "Generate JSDoc/Docstrings for all public classes, methods, and functions. Explain inputs, outputs, exceptions, and side effects."),
    ("Dockerize application", "container-deployment", "Write a multi-stage Dockerfile. Minimize image size. Avoid running as root. Configure environment variables."),
    ("Migrate library version", "upgrade-path", "Migrate legacy syntax to the modern API. Ensure backward compatibility. Check for deprecated methods and replace them."),
    ("Standardize error handling", "robustness", "Catch specific exception types rather than generic errors. Log error traces with appropriate levels. Do not leak credentials in logs."),
    ("Implement caching", "cache-strategy", "Add a caching layer (e.g. Redis). Set appropriate TTLs. Implement cache invalidation patterns on updates."),
    ("Audit accessibility", "wcag-compliance", "Verify elements have correct ARIA roles. Ensure keyboard navigability and high contrast. Add descriptive alt tags."),
    ("Profile memory usage", "leak-prevention", "Profile heap allocations. Clean up event listeners, timers, and unclosed file/network sockets to prevent memory leaks."),
    ("Configure Git hooks", "pre-commit-verification", "Set up pre-commit hooks to run prettier, eslint, and unit tests before any commit is finalized."),
    ("Design schema", "data-modeling", "Create normalized tables with correct foreign keys. Establish indexes on frequently searched fields. Ensure constraints are defined."),
    ("Implement authentication", "identity-security", "Implement JWT/OAuth2 authentication. Hash passwords using bcrypt/argon2. Secure cookies and session tokens."),
    ("Standardize logging", "observability", "Structure logs in JSON format. Include request ID, timestamp, and log level. Do not log personally identifiable information (PII)."),
    ("Refactor CSS styles", "responsive-layout", "Convert styling to modern CSS Grid or Flexbox. Ensure full responsiveness across mobile, tablet, and desktop screens."),
    ("Optimize bundle size", "loading-speed", "Audit package dependencies. Implement code splitting, lazy loading, and tree shaking to minimize initial load weight."),
    ("Configure reverse proxy", "traffic-routing", "Write Nginx configurations for reverse proxying. Enable gzip compression, SSL termination, and rate limiting."),
    ("Mock external API", "integration-testing", "Write mock servers or services. Return realistic mock data with various network delay patterns and error status codes."),
    ("Implement rate limiting", "dos-protection", "Apply sliding-window rate limits to public endpoints using Redis. Return HTTP 429 Too Many Requests when limits are hit."),
    ("Write integration tests", "system-testing", "Configure end-to-end integration tests. Seed database state before running tests. Clean up seeded data after execution."),
    ("Refactor legacy state", "modern-state-management", "Migrate legacy state models to modern state management (e.g., Redux Toolkit, Pinia). Ensure state mutations are pure."),
    ("Optimize static assets", "asset-delivery", "Compress images, minify scripts, and configure cache-control headers for optimal static asset delivery.")
]

def main():
    categories = ["claude-code", "aider", "open-code", "codex", "misc"]
    total_count = 0

    for cat in categories:
        tool = tools[cat]
        cat_dir = os.path.join(PROMPT_BAZAAR_DIR, cat)
        os.makedirs(cat_dir, exist_ok=True)

        prompt_index = 1
        for tech in technologies:
            if prompt_index > 1000:
                break
            for verb, noun, template_text in tasks:
                if prompt_index > 1000:
                    break

                title = f"{tool} {verb} for {tech} ({noun.replace('-', ' ').title()} Focus)"
                slug = f"{verb.lower().replace(' ', '-')}-{tech.lower().replace(' ', '-')}-{noun}-{prompt_index}"
                slug = slug.replace("/", "-").replace(".", "-")

                item_dir = os.path.join(cat_dir, slug)
                os.makedirs(item_dir, exist_ok=True)

                prompt_instruction = (
                    f"Role: You are a senior developer specializing in {tech}.\n"
                    f"Task: {verb} the {tech} project focusing on {noun.replace('-', ' ')}.\n\n"
                    f"Instructions:\n"
                    f"1. {template_text}\n"
                    f"2. Ensure standard conventions of {tech} are fully followed.\n"
                    f"3. Verify all inputs and outputs."
                )

                readme_content = f"""# {title}

A developer-focused prompt designed for {tool} to {verb.lower()} {tech} applications with a focus on {noun.replace('-', ' ')}.

> Part of **[Prompt Bazaar](../../README.md)** · [Mega AI Bazaar](https://drvivek34.github.io/Mega-AI-Bazaar/)

## Details
- **Target Tool / Agent**: `{tool}`
- **Source URL**: https://github.com/Drvivek34/Prompt-Bazaar/tree/main/{cat}/{slug}
- **Author**: Prompt Bazaar Community
- **License**: MIT
- **Date Added**: 2026-06-20

## Prompt Instructions
```markdown
{prompt_instruction}
```
"""
                with open(os.path.join(item_dir, "README.md"), "w", encoding="utf-8") as f:
                    f.write(readme_content.strip() + "\n")

                prompt_index += 1
                total_count += 1

    print(f"Scaffolding complete. Generated {total_count} prompts across 5 categories.")

if __name__ == "__main__":
    main()
