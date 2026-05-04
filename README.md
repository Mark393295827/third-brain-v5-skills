# Third Brain V5 Skills

**A curated set of Agent Skills for knowledge compounding, behavior design, and creativity — turning AI agents into a persistent cognitive operating system.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

---

## Overview

These skills transform any AI coding agent (Claude Code, Codex, Gemini CLI) into a **personal knowledge compounding system**. Instead of treating each conversation as a one-off chat, these skills create a persistent, interlinked knowledge base that grows richer with every session.

Inspired by the [Third Brain V5.0](https://github.com/your-repo) architecture — a synthesis of:

- **STOW pattern** (Source → Think → Organize → Write) — Karpathy's LLM wiki approach
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

## Architecture

```
                    ┌─────────────┐
                    │  External   │
                    │  Sources    │
                    └──────┬──────┘
                           ▼
              ┌──────────────────────┐
              │    wiki-ingest       │
              │  (STOW pipeline)     │
              └──────┬──────┬───────┘
                     │      │
              ┌──────▼      └──────┐
              │  wiki/              │
              │  ├ entities/        │
              │  ├ concepts/        │
              │  ├ sources/         │
              │  ├ outputs/         │
              │  └ decisions/       │
              └─────────────────────┘
                     │
        ┌────────────┼────────────┬──────────────┐
        ▼            ▼            ▼              ▼
┌─────────────┐ ┌──────────┐ ┌──────────┐ ┌────────────┐
│ daily-okr   │ │cognitive │ │ behavior │ │ creativity │
│ (7 KR loop) │ │ -compile │ │ -design  │ │ -engine    │
└─────────────┘ └──────────┘ └──────────┘ └────────────┘
        │            │            │              │
        └────────────┼────────────┼──────────────┘
                     ▼
           ┌─────────────────┐
           │ session-learn   │ ← continuous extraction
           │ verify-before-  │
           │ claim           │ ← quality gate
           │ wiki-lint       │ ← periodic health
           └─────────────────┘
```

## Quick Start

### With Claude Code

```bash
# Copy skills to your Claude Code skills directory
cp -r skills/* ~/.claude/skills/

# Or use a project-specific setup
cp -r skills/* .claude/skills/
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
