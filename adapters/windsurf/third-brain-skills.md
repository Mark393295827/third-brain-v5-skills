---
trigger: model_decision
description: Route knowledge, behavior, research, verification, and agent-team tasks to Third Brain V5 workspace skills.
---

# Third Brain V5 Skill Router

Use this rule when the user asks Cascade for knowledge ingestion, daily review, research, verification, behavior design, creativity, startup evaluation, or agent-team orchestration.

Routing:

- Source, PDF, article, or note ingestion -> `@wiki-ingest`
- Daily review or daily planning -> `@daily-okr`
- Deep understanding or synthesis -> `@cognitive-compile`
- Completion claim, bug fix, tests, shipping -> `@verify-before-claim`
- Habit or behavior change -> `@behavior-design`
- Idea generation -> `@creativity-engine`
- Research report -> `@deep-research`
- Startup idea or due diligence -> `@startup-evaluation`
- Knowledge organization, deduplication, or vector search -> `@knowledge-ops`
- Wiki health check, broken links, or stale pages -> `@wiki-lint`
- Context limits or token budget -> `@context-manager`
- Agent workflow refactor or autonomy design -> `@agentic-engineering`
- Agent permissions, tools, observability, or runtime safety -> `@harness-engineering`
- Team operating system, growth method, or self-evolving work method -> `@anthropic-os`
- Multi-agent execution -> `@agent-teams-command`

For each selected skill:

1. Follow the skill's Prompt, Use Case, Expected Result, Verification Case, and Verified Effect.
2. Check `assumes` and `conflicts_with` before acting.
3. Use the workflow, `Success Metrics`, and quality gates from the skill file.
4. Resolve wiki paths from `system/config.md` when present.
5. Summarize created files, verification evidence, and remaining risk.
6. Avoid completion claims unless the relevant verification case and success metrics are satisfied.
