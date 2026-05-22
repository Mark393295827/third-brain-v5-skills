# Third Brain V5 Skills — Codex CLI

This repository contains Agent Skills for the Codex CLI environment. Place skills in `~/.agents/skills/`.

## Skills

### 📥 Knowledge Pipeline
- **wiki-ingest** — STOW pipeline for ingesting sources into an interlinked wiki.
- **knowledge-ops** — Multi-layer knowledge management with vector storage.
- **wiki-lint** — 8-dimension wiki health check.

### 🔄 Daily Loop
- **daily-okr** — 7 Key Results daily knowledge compound cycle.
- **cognitive-compile** — 8-section deep learning compile framework.

### 🎨 Behavior & Creativity
- **behavior-design** — Behavior change system with HAS framework.
- **creativity-engine** — Combinatorial ideation + minimum experiments.

### 🔬 Research & Quality
- **deep-research** — Multi-source research with evidence standards.
- **verify-before-claim** — Verification-first quality gate.

### 🔄 Learning
- **session-learn** — Knowledge extraction with Closure Protocol.
- **project-flow-ops** — Project triage and tracking.

### 📊 Cost
- **context-manager** — Context window and token budget management.
- **token-cost-tracker** — Token usage estimation and tracking.

### 🏗️ Engineering
- **agentic-engineering** — Agent-as-process workflow refactoring with autonomy defaults, state checkpoints, write-back, and verification gates.
- **harness-engineering** — Agent runtime kernel design: permissions, tools as system calls, observability, and recovery.
- **agent-teams-command** — Multi-agent process orchestration with ownership, IPC, integration, cleanup, and evidence gates.

### 💼 Strategy
- **startup-evaluation** — MIT 24-step startup evaluation framework.
- **anthropic-os** — Self-evolving work method engine.

## Compatibility

All skills follow the [Agent Skills](https://agentskills.io) open format. Skills are model-agnostic markdown files compatible with Codex CLI.

## Skill Contract

When selecting a skill, read its frontmatter before executing:

- `assumes` — required operating assumptions.
- `conflicts_with` — boundaries that must not be silently overridden.
- `## Success Metrics` — the minimum observable result for one successful run.
- `## Quality Gates` — checks that must pass before claiming completion.

For wiki-writing skills, resolve paths from `system/config.md` when available. Defaults include `SOURCES_DIR=sources/`, `CONCEPTS_DIR=wiki/concepts/`, `ENTITIES_DIR=wiki/entities/`, and `LOG_FILE=system/log.md`.

## Adoption Ladder

1. Start with `wiki-ingest` + `verify-before-claim`.
2. Add `daily-okr` + `session-learn` after daily ingest and evidence checks are working.
3. Add `cognitive-compile`, `behavior-design`, and `creativity-engine` when the wiki has enough material to synthesize.
4. Add `knowledge-ops`, `harness-engineering`, `agentic-engineering`, and `agent-teams-command` only when scale, reliability, or multi-agent ownership requires them.

## Karpathy LLM OS

LLM=CPU · Context=RAM · Storage=Disk · Tools=System Calls · Skills=Programs · Harness=Kernel · Agent Teams=Processes
