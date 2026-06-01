# Agent Skills Standard

This repository follows the Agent Skills open format described in the Obsidian note
`wiki/concepts/Skills and Agents`.

## Contract

Each skill is a portable folder under `skills/`:

```text
skill-name/
└── SKILL.md
```

Optional resources may be added only when they directly support execution:

```text
skill-name/
├── SKILL.md
├── scripts/
├── references/
└── assets/
```

Do not add auxiliary `README.md`, changelogs, installation guides, or narrative
process notes inside skill folders. Put repo-level documentation under `docs/`.

## Required SKILL.md Shape

Every `SKILL.md` must have:

- YAML frontmatter at the top.
- `name` matching the folder name.
- `description` that says what the skill does and when to use it.
- `assumes` stating required operating assumptions.
- `conflicts_with` stating boundaries that should not be silently overridden.
- A top-level title.
- A `## Usage Template` section.
- A `## Success Metrics` section.
- A `## Quality Gates` section.

Recommended description pattern:

```yaml
description: Do the core job in one sentence. Use when the user asks for trigger condition, task class, or workflow.
```

The description is the discovery layer. Keep it specific enough for an agent to
choose the skill without reading the whole file.

## Progressive Disclosure

Use three loading levels:

1. Discovery: `name` and `description` only.
2. Activation: concise `SKILL.md` workflow.
3. Execution: load `references/`, run `scripts/`, or use `assets/` only when needed.

Keep `SKILL.md` concise. If it approaches 500 lines, move detailed examples,
schemas, or long checklists into `references/` and link them from `SKILL.md`.

## Design Rules

- Single responsibility: one skill should own one coherent workflow.
- Concise first: include only instructions the model cannot infer.
- Freedom matches risk: use prose for judgment-heavy tasks, scripts for fragile or repeated operations.
- Verification is mandatory: every skill should say how output is checked.
- Portable by default: avoid project-specific absolute paths inside skill instructions.
- Write-back when useful: knowledge workflows should update durable notes or logs.

## Validation

Run:

```powershell
python tools\lint-agent-skills.py
```

The linter checks the open-format contract, trigger descriptions, section
presence, folder hygiene, and oversized skill files.
