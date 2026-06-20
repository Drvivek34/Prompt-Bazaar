#!/usr/bin/env bash
# Scaffolds the Prompt-Bazaar repository structure.
set -euo pipefail

ROOT=/root/bazaars/Prompt-Bazaar
GH=Drvivek34
WEBSITE="https://drvivek34.github.io/Mega-AI-Bazaar/"
R=Prompt-Bazaar; T="Prompt Bazaar"; NOUN="prompt"
submit="https://github.com/$GH/$R/issues/new/choose"

mkdir -p "$ROOT/.github/ISSUE_TEMPLATE"

mkcat () {
  local slug="$1" title="$2" desc="$3"
  local d="$ROOT/$slug"; mkdir -p "$d"
  cat > "$d/README.md" <<EOF
# $title

$desc

> Part of **[$T](../README.md)** · [Mega AI Bazaar]($WEBSITE)

Each prompt lives in its own sub-folder with a \`README.md\` recording name, author, target tool, prompt instructions, and source URL.

Add via [CONTRIBUTING.md](../CONTRIBUTING.md) or the [submission form]($submit).

## Entries
_No entries yet._
EOF
  touch "$d/.gitkeep"
}

mkdir -p "$ROOT/featured"
cat > "$ROOT/featured/README.md" <<EOF
# ⭐ Featured — Top Prompt Picks

The most popular, optimized, and effective coding agent prompts, surfaced at the very front of $T.

> [Mega AI Bazaar]($WEBSITE)
EOF
touch "$ROOT/featured/.gitkeep"

mkcat claude-code "Claude Code Prompts" "Curated prompts optimized for Anthropic's Claude Code CLI."
mkcat aider       "Aider Prompts"       "Effective prompts and system instructions for the Aider coding tool."
mkcat open-code   "Open Code Prompts"   "Open source and generic code prompts designed for LLM code generation."
mkcat codex       "Codex Prompts"       "Prompts and instructions tailored for Codex CLI and similar tools."
mkcat misc        "Miscellaneous"       "Other useful developer and prompt engineering templates."

# ---------- LICENSE ----------
cat > "$ROOT/LICENSE" <<EOF
MIT License

Copyright (c) 2026 Dr. Vivek Trivedi ($T)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND. SEE FULL MIT TEXT.

----------------------------------------------------------------------
Each prompt in this bazaar retains its original author's license and attribution.
EOF

# ---------- CONTRIBUTING ----------
cat > "$ROOT/CONTRIBUTING.md" <<EOF
# Contributing to $T

Add a $NOUN via the [submission form]($submit) or a Pull Request.

## Layout
\`\`\`
<category>/
└── <prompt-name>/
    └── README.md   # name, description, author, target tool, prompt text, source
\`\`\`

## Each entry must record
- Prompt name + target tool
- Original Author / credit
- Prompt instructions/text
- Source URL of the prompt
- License (if specified)

Part of the [Mega AI Bazaar]($WEBSITE).
EOF

# ---------- CODE_OF_CONDUCT ----------
cat > "$ROOT/CODE_OF_CONDUCT.md" <<EOF
# Code of Conduct
Be respectful and constructive. Maintainers may edit or remove non-compliant content.
Part of the [Mega AI Bazaar]($WEBSITE).
EOF

# ---------- issue config ----------
cat > "$ROOT/.github/ISSUE_TEMPLATE/config.yml" <<EOF
blank_issues_enabled: true
contact_links:
  - name: 🌐 Mega AI Bazaar (browse & search all bazaars)
    url: $WEBSITE
    about: The front door to every bazaar.
EOF

# ---------- submit form ----------
cat > "$ROOT/.github/ISSUE_TEMPLATE/submit.yml" <<'EOF'
name: "➕ Submit a Prompt"
description: "Add a custom prompt to the Prompt Bazaar."
title: "[Prompt] <name>"
labels: ["submission", "prompt"]
body:
  - type: input
    id: name
    attributes:
      label: Prompt Name
    validations:
      required: true
  - type: dropdown
    id: category
    attributes:
      label: Category
      options:
        - claude-code
        - aider
        - open-code
        - codex
        - misc
    validations:
      required: true
  - type: dropdown
    id: tool
    attributes:
      label: Target Tool / Agent
      options:
        - Claude Code
        - Aider
        - Codex
        - Generic / Agnostic
    validations:
      required: true
  - type: input
    id: author
    attributes:
      label: Author / credit
    validations:
      required: true
  - type: input
    id: source
    attributes:
      label: Source URL
    validations:
      required: false
  - type: textarea
    id: prompt_text
    attributes:
      label: Prompt Text / Instructions
    validations:
      required: true
  - type: checkboxes
    id: confirm
    attributes:
      label: Confirmation
      options:
        - label: I have not posted any secret API keys.
          required: true
EOF

# ---------- README ----------
cat > "$ROOT/README.md" <<EOF
# ⚡ Prompt Bazaar

> A categorized library of high-quality developer prompts for coding agents (Claude Code, Aider, Codex, Open Code, and more).

[![Mega AI Bazaar](https://img.shields.io/badge/🌐_Mega_AI_Bazaar-browse_all-6C5CE7)]($WEBSITE) [![Submit](https://img.shields.io/badge/➕_Submit-a_prompt-2ecc71)]($submit) [![License](https://img.shields.io/badge/License-MIT-blue)](LICENSE)

Prompt Bazaar compiles optimized system prompts, developer rules, and workflow shortcuts for automated coding tools. The top picks are highlighted in **featured/**.

## 📂 Categories

**[⭐ Featured](featured/)** — best prompts, at the very front.

| Category | About |
|---|---|
| [Claude Code Prompts](claude-code/) | Curated prompts optimized for Claude Code CLI. |
| [Aider Prompts](aider/) | System instructions for the Aider tool. |
| [Open Code Prompts](open-code/) | Open/generic coding prompts. |
| [Codex Prompts](codex/) | Custom scripts and prompts for Codex. |
| [Miscellaneous](misc/) | Other prompt templates. |

## ➕ Contribute
**[Submit via the form]($submit)** or open a PR — see [CONTRIBUTING.md](CONTRIBUTING.md).

---
Part of the **[Mega AI Bazaar]($WEBSITE)** — the front door to all the bazaars.
EOF

echo "Prompt-Bazaar scaffold complete."
