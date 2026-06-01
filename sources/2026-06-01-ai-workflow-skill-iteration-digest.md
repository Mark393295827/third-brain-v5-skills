---
source_title: "AI Workflow Map Skill Iteration Digest"
source_date: 2026-06-01
source_type: wiki-map-digest
input_class: internal-synthesis
evidence_level: curated-map-with-single-source-notes
related_map: "[[maps/AI 知识工作流]]"
related_concepts:
  - "[[Claude Code Dynamic Workflows]]"
  - "[[Agent工作流复杂度阶梯]]"
  - "[[AI个人操作系统]]"
  - "[[AIOS四C框架]]"
  - "[[Agent权限自行车方法]]"
  - "[[Agent-Environment-Session 模型]]"
  - "[[Agent自我压缩]]"
repo_scope:
  - skills/agentic-engineering/SKILL.md
  - skills/harness-engineering/SKILL.md
  - skills/agent-teams-command/SKILL.md
  - skills/anthropic-os/SKILL.md
  - skills/context-manager/SKILL.md
---

# AI Workflow Map Skill Iteration Digest

## Inputs

- `maps/AI 知识工作流.md`
- `Claude Code Dynamic Workflows`
- `Agent工作流复杂度阶梯`
- `AI个人操作系统`
- `AIOS四C框架`
- `Agent权限自行车方法`
- `Agent-Environment-Session 模型`
- `Agent自我压缩`

## Synthesis

The latest AI workflow map shifts Third Brain skills from "better prompts" toward runtime choice, operating-system design, and long-horizon continuity.

Dynamic workflows should be treated as width-first orchestration: many independent workers run from a reviewed script, then a synthesis step merges results. They are not a default upgrade over skills, subagents, agent teams, or long-running goals. Use them only when work naturally shards, communication between workers is low, and the value justifies extra model calls, script review, and runtime observability.

The workflow complexity ladder is the governing gate: prompt -> skill -> subagent -> agent team -> long-running goal -> dynamic workflow. Each step raises coordination cost, permission risk, and audit burden.

AIOS notes add a workspace-level view: Context, Connections, Capabilities, and Cadence. Capabilities are skills and commands; cadence is proactive execution. Connections and cadence must be paired with permission gradients. The Bike Method says do not grant real write/send/delete/pay keys before the system has proven reliability at lower autonomy levels.

Managed-agent notes clarify the production runtime model: Agent defines the persona and capabilities; Environment defines the execution hands; Session binds them with mounted context, event logs, recovery, and observability.

Self-compaction notes make context management a long-horizon reliability issue. Summaries must preserve goal, constraints, completed work, failed paths, evidence, open risks, and next action, or the agent will drift after compaction.

## Repo Translation

- `agentic-engineering` should include a workflow complexity gate before escalating from prompt/skill to teams, goals, or dynamic workflows.
- `harness-engineering` should include the Agent/Environment/Session model, event-log expectations, and permission escalation from read-only through monitored autonomy.
- `agent-teams-command` should distinguish communicative teams from script-first dynamic workflows and require script review, cost envelopes, runtime observability, and archive/reuse decisions.
- `anthropic-os` should add AIOS 4C and Bike Method audits so a personal/team OS is judged by context, connections, capabilities, cadence, and permission maturity.
- `context-manager` should add a long-horizon compaction contract for safe continuation after context compression.

## Verification Expectations

- Updated skills still pass `python tools/lint-agent-skills.py`.
- New guidance preserves existing safety boundaries around delegated action, source verification, and durable write-back.
- Product-specific workflow claims remain treated as single-source operating patterns unless independently verified.
