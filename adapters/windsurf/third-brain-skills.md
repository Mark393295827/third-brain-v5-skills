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
- Multi-agent execution -> `@agent-teams-command`

For each selected skill:

1. Follow the skill's Prompt, Use Case, Expected Result, Verification Case, and Verified Effect.
2. Use the workflow and quality gates from the skill file.
3. Summarize created files, verification evidence, and remaining risk.
4. Avoid completion claims unless the relevant verification case is satisfied.
