# Third Brain V5 Skills — Agent Guidelines

This repository contains Agent Skills for knowledge compounding, behavior design, and creativity. Use these skills when the user wants to build or maintain a personal knowledge system.

## Skill Format

All skills follow the [Agent Skills specification](https://agentskills.io):

```
skill-name/
├── SKILL.md       # Required: YAML frontmatter + Markdown instructions
```

Every SKILL.md starts with:
```yaml
---
name: skill-name
description: One-line description of what this skill does and when to use it.
---
```

## Skill Organization

- **Knowledge operations**: wiki-ingest, cognitive-compile, session-learn, wiki-lint, knowledge-ops
- **Daily workflow**: daily-okr
- **Behavior & creativity**: behavior-design, creativity-engine
- **Quality**: verify-before-claim, harness-engineering
- **Context & cost**: context-manager (token budget), token-cost-tracker (usage log)

## Key Principles

1. **Knowledge compounds** — every operation should make the wiki richer
2. **Evidence before claims** — never assert completion without verification
3. **TDD for SOPs** — define failure mode before writing the SOP
4. **Progressive disclosure** — SKILL.md loads on demand, not at startup
5. **≥2 links per page** — every wiki page needs at least 2 outgoing `[[wikilinks]]`
6. **Schema §5.3 structure** — concept pages follow: quote → mechanism → tables → data → connections → timeline
7. **Karpathy LLM OS mapping** — LLM=CPU, Context=RAM, Wiki=Disk, Tools=System Calls, Loop=Process Scheduler

## Tags Reference

| Tag | Meaning |
|-----|---------|
| `domain/ai` | Artificial Intelligence |
| `domain/strategy` | Business strategy |
| `domain/cognition` | Cognitive science |
| `domain/meta` | Meta knowledge |
| `type/concept` | Concept page |
| `type/entity` | Entity page |
| `type/sop` | Standard operating procedure |
