# Third Brain V5 Skills

**A curated set of Agent Skills for knowledge compounding, behavior design, and creativity — turning AI agents into a persistent cognitive operating system.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Compatible-8A2BE2)](https://claude.ai/code)
[![Codex CLI](https://img.shields.io/badge/Codex%20CLI-Compatible-000000)](https://github.com/openai/codex)
[![Gemini CLI](https://img.shields.io/badge/Gemini%20CLI-Compatible-4285F4)](https://github.com/google-gemini/gemini-cli)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-Format-2ea44f)](https://agentskills.io)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](CONTRIBUTING.md)
![Skills](https://img.shields.io/badge/skills-16-FF6B6B)
![Karpathy LLM OS](https://img.shields.io/badge/Karpathy%20LLM%20OS-Compatible-8A2BE2)
![Context Management](https://img.shields.io/badge/context--manager-F0DB4F)
![Token Tracking](https://img.shields.io/badge/token--tracking-00D1B2)
![Startup Evaluation](https://img.shields.io/badge/startup--evaluation-FF9900)
![Anthropic OS](https://img.shields.io/badge/anthropic--os-8A2BE2)

---

## Overview

These skills transform any AI coding agent (Claude Code, Codex, Gemini CLI) into a **personal knowledge compounding system**. Instead of treating each conversation as a one-off chat, these skills create a persistent, interlinked knowledge base that grows richer with every session.

Inspired by the [Third Brain V5.0](https://github.com/your-repo) architecture — a synthesis of:

- **STOW pattern** (Source → Think → Organize → Write) — Karpathy's LLM wiki approach
- **Schema §5.3** — standardized page structure: quote → mechanism → tables → connections → timeline
- **Karpathy LLM OS framework** — LLM=CPU, Context=RAM, Storage=Disk, Tools=System Calls
- **Andreessen Horowitz** AI capital-to-labor thesis — software that replaces labor
- **ECC continuous-learning v2.1** — automatic knowledge extraction from sessions
- **Superpowers verification** — evidence-before-claims discipline

## Skills

| Skill | Description |
|-------|-------------|
| [wiki-ingest](skills/wiki-ingest/SKILL.md) | Ingest sources into a persistent interlinked wiki. Creates source notes, entity pages, concept pages, updates navigation. |
| [daily-okr](skills/daily-okr/SKILL.md) | Daily knowledge compound closed loop — 7 Key Results from input to feedback, with scoring. |
| [cognitive-compile](skills/cognitive-compile/SKILL.md) | Deep learning 7-step framework: Question → Facts → Concepts → Patterns → Conflicts → Judgment → Action. |
| [behavior-design](skills/behavior-design/SKILL.md) | Transform goals into behavior systems: decompose → minimum habits → triggers → SOPs → review → identity. |
| [creativity-engine](skills/creativity-engine/SKILL.md) | Generate novel ideas by combining knowledge across domains. Combinatorial ideation + minimum experiments. |
| [session-learn](skills/session-learn/SKILL.md) | Extract knowledge patterns from sessions — new concepts, entities, corrections, decisions, gaps. |
| [verify-before-claim](skills/verify-before-claim/SKILL.md) | Iron rule: No completion claims without fresh verification evidence. |
| [wiki-lint](skills/wiki-lint/SKILL.md) | Health-check the wiki across 8 dimensions: frontmatter, links, orphans, stale content, contradictions, drift. |
| [knowledge-ops](skills/knowledge-ops/SKILL.md) | Multi-layer knowledge management — classify, deduplicate, sync, retrieve. |
| [deep-research](skills/deep-research/SKILL.md) | Multi-source deep research with confidence-based evidence standards. |
| [project-flow-ops](skills/project-flow-ops/SKILL.md) | Execution flow — triage, plan, track, review across projects. |
| [harness-engineering](skills/harness-engineering/SKILL.md) | Design the runtime infrastructure around AI agents — permissions, tools, feedback loops, observability, constraints. |
| [context-manager](skills/context-manager/SKILL.md) | Manage the LLM's context window — token budgeting, prompt assembly, truncation strategies, cache optimization. |
| [startup-evaluation](skills/startup-evaluation/SKILL.md) | Evaluate startups using the 24-step disciplined entrepreneurship framework. Market identification, customer understanding, business model analysis. |
| [anthropic-os](skills/anthropic-os/SKILL.md) | Anthropic OS — Self-Evolving Work Method Engine. CASH growth, 70/30, two-week rule, hive mind, working backwards. Built-in self-evolution mechanism. |
| [agent-teams-command](skills/agent-teams-command/SKILL.md) | Ender's Game approach to commanding Claude Code Agent Teams. Karpathy Agentic Engineering — Plan→Act→Observe→Iterate. L1-L5 commander progression. |

## Architecture

```
  ┌────────────────────────────────────────────────────────────────────┐
  │                Karpathy LLM OS Layer                                │
  │  LLM=CPU │ Context=RAM │ Storage=Disk │ Tools=System Calls         │
  │  ┌────────────────────────────────────────────────────────────┐    │
  │  │ context-manager: Token Budget → Prompt Assembly→ Truncation │    │
  │  │ token-cost-tracker: Estimate → Log → Report (weekly burn)   │    │
  │  └────────────────────────────────────────────────────────────┘    │
  └────────────────────────────────────────────────────────────────────┘
                                   │
                    ┌──────────────────┐
                    │   External       │
                    │   Sources        │
                    └────────┬─────────┘
                             ▼
             ┌──────────────────────────────┐
             │   wiki-ingest                │
             │   knowledge-ops (+VectorDB) │
             │ (STOW pipeline + RAG sync)  │
             └──────┬──────────┬───────────┘
                    │          │
             ┌──────▼          └─────────────┐
             │  Knowledge Layers              │
             │  ├ Active (GitHub/Linear)      │
             │  ├ Memory (quick access)       │
             │  ├ Wiki (durable, interlinked) │
             │  ├ Vector (ChromaDB, semantic)⭐│
             │  └ External (DBs, APIs)        │
             └────────────────────────────────┘
                    │
        ┌───────────┼──────────┬──────────────┬──────────────┐
        ▼           ▼          ▼              ▼              ▼
┌────────────┐ ┌─────────┐ ┌──────────┐ ┌───────────┐ ┌──────────────┐
│ daily-okr  │ │cognitive│ │ behavior │ │ creativity│ │ project-flow │
│ (7 KR loop)│ │-compile │ │ -design  │ │ -engine   │ │ -ops         │
└────────────┘ └─────────┘ └──────────┘ └───────────┘ └──────────────┘
        │           │          │              │              │
        └───────────┼──────────┼──────────────┼──────────────┘
                    ▼
           ┌──────────────────────────────────────────────────────────┐
           │ session-learn (+Closure Protocol) ← continuous + feedback│
           │ verify-before-claim               ← quality gate         │
           │ wiki-lint                         ← health check         │
           │ deep-research                     ← synthesis            │
           │ harness-engineering (+GAN pattern) ← safety + multi-agent│
           │ startup-evaluation (24-step)      ← VC evaluation        │
           └──────────────────────────────────────────────────────────┘
```

## Quick Start

### One-line Install

```bash
# Clone and install all skills
git clone https://github.com/Mark393295827/third-brain-v5-skills.git
cp -r third-brain-v5-skills/skills/* ~/.claude/skills/
```

### With Claude Code

```bash
# Personal skills (available across all projects)
cp -r skills/* ~/.claude/skills/

# Project skills (shared with team)
cp -r skills/* .claude/skills/
```

### With Codex CLI

```bash
cp -r skills/* ~/.agents/skills/
```

### With Gemini CLI

```bash
cp -r skills/* ~/.gemini/skills/
```

Then use in conversation:

```
"I just read an interesting article about X. Ingest it into my wiki."
"Run my daily OKR."
"Help me think deeply about Y — run a cognitive compile."
"I want to build a habit of Z."
"Generate 10 new ideas about W."
"Extract what we learned from this session."
"Verify before I claim this is done."
"Lint my wiki."
```

### With Other Agents

These skills follow the [Agent Skills](https://agentskills.io) open format. Compatible agents include:
- **Claude Code** — reads `CLAUDE.md`
- **Codex CLI** — reads `AGENTS.md`
- **Gemini CLI** — reads `GEMINI.md`

## Wiki Structure

These skills assume the following wiki layout:

```
sources/          ← Immutable source notes (READ ONLY)
wiki/
├── concepts/     ← Ideas, frameworks, methods
├── entities/     ← People, companies, products
├── atomic-notes/ ← Single knowledge atoms
├── outputs/      ← Reusable outputs (reports, analyses)
├── decisions/    ← Architecture and strategy decisions
└── sops/         ← Standard operating procedures
maps/             ← Navigation / Maps of Content
system/
├── schema.md     ← Constitution
├── log.md        ← Evolution log
├── review-queue.md ← Human review queue
├── lint-report.md  ← Health check reports
└── templates/    ← Templates
08_behaviors/     ← Behavior system (goals/habits/SOPs/reviews)
09_creativity/    ← Creativity system (ideas/experiments/prototypes/analogies)
```

## Related Projects

- [llm-wiki-agent](https://github.com/SamurAIGPT/llm-wiki-agent) — Original STOW pattern implementation
- [Superpowers](https://github.com/your-link) — TDD-for-skills and verification-first development
- [Agent Skills](https://agentskills.io) — Open format specification

## License

MIT — see [LICENSE](LICENSE).
