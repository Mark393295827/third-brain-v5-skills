# Third Brain V6 Skills — Codex CLI

This repository contains Agent Skills for the Codex CLI environment. Place skills in `~/.agents/skills/`.

V6 treats Obsidian as the agent's durable disk and governance layer. Do not turn wiki signals into skill or schema rules until they pass the promotion gate: repeated source support or local verification, bounded macro action, no provenance relaxation, and a cheap objective check.

## Skills

### 📥 Knowledge Pipeline
- **wiki-ingest** — V6 STOW pipeline with source-risk classification, Trigger-Context-Steering scope, block refs, clipping archive, understanding gate, governance notes, and post-ingest lint.
- **knowledge-ops** — Multi-layer knowledge management with Markdown-first retrieval, optional vector storage, evidence hierarchy, deduplication, Agent/Wiki flywheel, and knowledge debt queues.
- **wiki-lint** — Wiki health check for P0/P1 graph health, source refs, frontmatter, links, provenance debt, clipping lifecycle, understanding integrity, and V6 promotion readiness.

### 🔄 Daily Loop
- **daily-okr** — 7 Key Results daily knowledge compound cycle; may consume the scheduled daily knowledge-loop note when present.
- **cognitive-compile** — 8-section deep learning compile framework.

### 🎨 Behavior & Creativity
- **behavior-design** — Behavior change system with HAS framework.
- **creativity-engine** — Combinatorial ideation + minimum experiments.

### 🔬 Research & Quality
- **deep-research** — STOW-compatible research harness with ChatGPT-style preflight, source/claim ledgers, activity trace, citations, privacy checks, and wiki-ingest handoff.
- **verify-before-claim** — Verification-first quality gate.

### 🔄 Learning
- **session-learn** — Knowledge extraction with Closure Protocol.
- **project-flow-ops** — Project triage and tracking.

### 📊 Cost
- **context-manager** — Context window and token budget management.
- **token-cost-tracker** — Token usage estimation and tracking.

### 🏗️ Engineering
- **agentic-engineering** — Agent-as-process workflow refactoring with autonomy defaults, delegated-action boundaries, state checkpoints, write-back, and verification gates.
- **loop-engineering** — Bounded Trigger -> Execute -> Verify -> State loop design with durable contracts, independent verification, hard budgets, stop/recovery rules, and topology selection.
- **harness-engineering** — Agent runtime kernel design: permissions, tools as system calls, MCP/Skills/Hooks selection, provenance ledgers, delegated-action gates, observability, and recovery.
- **agent-teams-command** — Multi-agent process orchestration with ownership, IPC, worktree isolation, async budget envelopes, integration, cleanup, and evidence gates.

### 💼 Strategy & Operations
- **startup-evaluation** — Startup health diagnosis with entrepreneurship, VC 5T, PMF, runway, team, and next-test frameworks.
- **anthropic-os** — Self-evolving work method engine.
- **ai-six-sigma-property-os** — AI + Ontology + DMAIC Black Belt operating model for property work orders, dispatch, quotes, evidence, CTQ dashboards, and MVP quality control.

## Compatibility

All skills follow the [Agent Skills](https://agentskills.io) open format. Skills are model-agnostic markdown files compatible with Codex CLI.

## Skill Contract

When selecting a skill, read its frontmatter before executing:

- `assumes` — required operating assumptions.
- `conflicts_with` — boundaries that must not be silently overridden.
- `## Success Metrics` — the minimum observable result for one successful run.
- `## Quality Gates` — checks that must pass before claiming completion.

For wiki-writing skills, resolve paths from `system/config.md` when available. Defaults include `SOURCES_DIR=sources/`, `CONCEPTS_DIR=wiki/concepts/`, `ENTITIES_DIR=wiki/entities/`, and `LOG_FILE=system/log.md`.

## V6 Promotion Gate

Promote wiki knowledge into a skill, SOP, schema rule, or automation only when:

- At least two durable wiki/source pages support it, or one high-quality source plus local verification supports it.
- The rule can be expressed as Trigger -> Execute -> Verify -> State with owner, budget, stop condition, recovery, and write-back.
- Source immutability, block refs, clipping lifecycle, review queues, permissions, and human approval boundaries are preserved.
- The change has a cheap check: skill lint, wiki lint, link check, script receipt, test output, dashboard metric, or review receipt.

## Adoption Ladder

1. Start with `wiki-ingest` + `verify-before-claim`.
2. Add `daily-okr` + `session-learn` after daily ingest and evidence checks are working.
3. Add `cognitive-compile`, `behavior-design`, and `creativity-engine` when the wiki has enough material to synthesize.
4. Add `knowledge-ops`, `harness-engineering`, `agentic-engineering`, and `agent-teams-command` only when scale, reliability, or multi-agent ownership requires them.

## Karpathy LLM OS

LLM=CPU · Context=RAM · Storage=Disk · Tools=System Calls · Skills=Programs · Harness=Kernel · Agent Teams=Processes
