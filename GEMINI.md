# Third Brain V5 Skills — Agent Guidelines

This repository contains Agent Skills for knowledge compounding, behavior design, and creativity. Compatible with Gemini CLI.

## Skill Format

All skills follow the [Agent Skills specification](https://agentskills.io):

```
skill-name/
├── SKILL.md       # Required: YAML frontmatter + Markdown instructions
```

## Available Skills

| Skill | Description |
|-------|-------------|
| [wiki-ingest](skills/wiki-ingest/SKILL.md) | Ingest sources into a persistent interlinked wiki |
| [daily-okr](skills/daily-okr/SKILL.md) | Daily 7 KR knowledge compound closed loop |
| [cognitive-compile](skills/cognitive-compile/SKILL.md) | 7-step deep learning framework |
| [behavior-design](skills/behavior-design/SKILL.md) | Goals → Habits → SOPs → Review |
| [creativity-engine](skills/creativity-engine/SKILL.md) | Combinatorial ideation + experiments |
| [session-learn](skills/session-learn/SKILL.md) | Extract knowledge patterns from sessions |
| [verify-before-claim](skills/verify-before-claim/SKILL.md) | Evidence before completion claims |
| [wiki-lint](skills/wiki-lint/SKILL.md) | 8-dimension wiki health check |

## Key Principles

1. Knowledge compounds — every operation should make the wiki richer
2. Evidence before claims — never assert completion without verification
3. TDD for SOPs — define failure mode before writing the SOP
