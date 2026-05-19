---
title: Agent Understanding Framework
status: seed
updated: 2026-05-18
source_basis:
  - ../../sources/2026-05-18-karpathy-llm-wiki-schema.md
  - ../../skills/agentic-engineering/SKILL.md
  - ../../skills/harness-engineering/SKILL.md
  - ../../skills/agent-teams-command/SKILL.md
---

# Agent Understanding Framework

This framework translates the Karpathy-style LLM Wiki / LLM OS model into practical Agent Skills design.

## Core Mapping

| OS concept | Agent system equivalent | Third Brain skill surface |
|---|---|---|
| CPU | LLM inference loop | `agentic-engineering` |
| RAM | Context window | `context-manager` |
| Disk | Obsidian wiki, source notes, logs | `wiki-ingest`, `session-learn` |
| System calls | Tools, shell, browser, APIs | `harness-engineering` |
| Kernel | Permissions, policies, approvals, isolation | `harness-engineering` |
| Process scheduler | Plan -> Act -> Observe -> Iterate loop | `agentic-engineering`, `project-flow-ops` |
| Processes | Single agents or teammates | `agent-teams-command` |
| IPC | Task board, handoff notes, review comments | `agent-teams-command` |
| Garbage collection | Context compaction, cleanup, stale-state removal | `context-manager`, `wiki-lint` |

## Agent Lifecycle

1. **Boot**: Load task, project rules, relevant skills, and minimal working context.
2. **Plan**: Define one useful next action, not a broad speculative plan.
3. **Act**: Use tools as system calls with permission boundaries.
4. **Observe**: Read command output, tests, diffs, citations, screenshots, or logs.
5. **Iterate**: Repair based on evidence until the definition of done is met.
6. **Write back**: Persist reusable knowledge to wiki, logs, docs, or state files.
7. **Garbage collect**: Close agents, summarize bulky context, remove stale tasks, record residual risk.

## Three Design Layers

| Layer | Question | Skill |
|---|---|---|
| Agentic workflow | Can one model execute this with fewer clarifications and more evidence? | `agentic-engineering` |
| Harness runtime | What is the permission, tool, logging, and recovery boundary? | `harness-engineering` |
| Agent team | Which work should become separate processes with clear ownership and synchronization? | `agent-teams-command` |

## Design Rules

- Sources are immutable ground truth; wiki pages are living synthesis.
- Skills are executable programs for the LLM, not essays for humans.
- Context is scarce RAM; load only the state needed for the next step.
- Tools are system calls; every high-risk call needs a policy boundary.
- Completion claims require fresh evidence from the environment.
- Multi-agent work only helps when ownership, IPC, and integration gates are explicit.
- Every significant output needs closure: format, link, log, and make it retrievable.

## Anti-patterns

- Treating an agent as a chat persona instead of a process with state and permissions.
- Keeping durable knowledge only in conversation memory.
- Giving tools without allowlists, denial paths, observability, or rollback.
- Spawning multiple agents before defining ownership boundaries.
- Optimizing for a large one-shot answer instead of a loop that can observe and repair.
