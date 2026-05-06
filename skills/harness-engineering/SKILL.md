---
name: harness-engineering
description: Design the runtime infrastructure around AI agents — permissions, tools, feedback loops, observability, and architectural constraints. Use when deploying agents to production, setting up agent guardrails, or designing multi-agent systems.
---

# Harness Engineering for AI Agents

Design the system *around* AI agents so they behave reliably, safely, and usefully in production. Not tweaking the model — designing everything around it.

## When to Use

- Deploying an AI agent to production
- Setting up permissions, guardrails, or approval workflows for agents
- Designing multi-agent systems with different roles and access levels
- An agent behaved unpredictably and needs better constraints
- User asks "how do I make this agent safe/reliable?"
- Configuring auto-mode or permission tiers for Claude Code

---

## The Three Domains of Harness Engineering

| Domain | Object | Maturity |
|--------|--------|----------|
| **Physical** | Wire harnesses (automotive/aerospace) | ⭐ Mature (IPC/WHMA-A-620) |
| **Software** | CI/CD pipelines (Harness.io) | ⭐ Mature (DORA metrics) |
| **Cognitive** ⭐ | AI Agents | 🌱 Emerging (2025-2026) |

---

## Six Components of an AI Agent Harness

### 1. Context & Knowledge Layer
Curated access to code, docs, schemas, logs, and runtime data.

**Design questions:**
- What knowledge does the agent need to start?
- What should it be able to retrieve on demand?
- What should it NOT have access to?

**Implementation patterns:**
- Use `CLAUDE.md` for project-level context that loads at session start
- Use `context-manager` skill to budget tokens when loading large context
- Pre-compute summaries of large documents; never inject raw 10K+ token files

### 2. Tooling & API Surface
Well-designed tools with clear contracts.

**Anti-pattern:** Giving the agent a `bash` tool with no restrictions = giving a hammer to a toddler.

**Implementation: Three-Tier Permission Model** (inspired by Claude Code Auto Mode)

| Tier | Scope | Mechanism | Example Rules |
|:----:|-------|-----------|---------------|
| **1** | Safe built-in tools | Always allowed (no approval) | Read file, search, grep, glob, plan mode |
| **2** | In-project changes | Auto-approve (reviewable via git) | Write/edit within project dir, create files |
| **3** | High-risk actions | Classifier gate / human approval | Shell commands, external API calls, delete ops |

**Tier 3 classifier heuristic (implement as prompt rule):**
```
Before executing any Tier-3 action, check:
1. Can this destroy data irreversibly? → BLOCK unless user explicitly named the target
2. Does this access credentials or secrets? → BLOCK, ask user for the specific credential
3. Does this affect infrastructure others depend on? → BLOCK, require user confirmation
4. Was the target inferred (not explicitly named by user)? → BLOCK, ask user to confirm
```

### 3. Architectural Constraints & Policy
Deterministic checks that enforce what an agent may change:
- Linters and structural tests
- File/directory access boundaries
- Module dependency rules
- Read-only vs. writable paths
- **Token budget:** never exceed 80% of context window without explicit approval

### 4. Feedback & Validation Loops
Automatic verification of agent output:
- Write-Test-Fix cycle (agent must run tests after changes)
- Spec-checkers and reviewers (including other agents)
- **Generator + Evaluator pattern** (GAN-inspired): separate the agent doing work from the agent judging it
- Deny-and-continue: on block, agent tries safer alternative path (not abort)
- Escalation to human after 3 consecutive blocks

### 5. Observability & Governance
- Logging every tool call and its result
- Metrics: success rate per task type, revert rate, token usage
- Human-in-the-loop approval for high-risk actions
- Traces for multi-step agent workflows
- **Cost tracking:** log token usage per session, estimate weekly burn

### 6. Maintenance / Garbage Collection
Periodic agents that find:
- Dead code and outdated docs
- Violations of architectural constraints
- Entropy over time
- Wiki pages with broken links or missing frontmatter (see `wiki-lint`)

---

## GAN-Inspired Multi-Agent Pattern

> Source: Anthropic's Harness Design for Long-Running Apps (2026)

The most effective pattern for complex tasks: **separate the generator from the evaluator**.

```
┌─────────────────┐     sprint contract     ┌─────────────────┐
│   Generator     │ ◄────── negotiate ──────► │   Evaluator     │
│  (does the work)│                           │  (judges output) │
└────────┬────────┘                           └────────┬────────┘
         │                                              │
         ▼                                              ▼
┌─────────────────┐                           ┌─────────────────┐
│ Produces output │                           │ Playwright/Test │
│ (code/design)   │                           │ Clicks through  │
└─────────────────┘                           └─────────────────┘
```

**Key insight:** "Tuning a standalone evaluator to be skeptical is far more tractable than making a generator critical of its own work."

**Implement as:**
1. **Planner** agent expands 1-sentence prompt → full spec
2. **Generator** agent builds in sprints, one feature at a time
3. **Evaluator** agent tests with Playwright (or similar), files bugs
4. Feedback loops back to Generator for N iterations (5-15 typical)

---

## Physical → Cognitive Analogies

| Physical Harness | AI Agent Harness | Implementation |
|-----------------|------------------|----------------|
| **Zonal Architecture** | Agent permission scopes | Each agent restricted to its domain via `AGENTS.md` |
| **IP68 Ingress Protection** | Security isolation | Sandbox execution, token in vault not in container |
| **HiPot Dielectric Test** | Stress testing | Edge-case test suite for agent behavior |
| **Continuity Test** | Tool chain verification | `describe-tools` pre-flight check |
| **EMC / Interference** | Multi-agent isolation | Separate sandbox per agent, no shared state |

---

## Multi-Agent Orchestration Patterns

| Pattern | Description | When to Use |
|---------|-------------|-------------|
| **Supervisor** | One orchestrator delegates to specialized sub-agents | Complex tasks with clear sub-steps |
| **Peer Review** | Agents review each other's output before production | High-risk changes (code, config, data) |
| **Competitive** | Multiple agents try the same task, best result wins | Creative work, optimization problems |
| **Pipeline** | Agents pass work sequentially in a chain | Document processing, data pipelines |
| **Zonal** | Each agent owns a domain/zone, orchestrator routes | Enterprise systems with clear boundaries |
| **Generator+Evaluator** | Separate builder from critic (GAN-inspired) | Long-running builds, design, full-stack apps |

---

## Quality Gates

- [ ] Each agent has a defined permission scope (what it CAN and CANNOT do)
- [ ] Three-tier permission model documented
- [ ] Write-Test-Fix feedback loop in place
- [ ] Tool calls are logged and observable
- [ ] Token costs tracked per session
- [ ] High-risk actions require human approval OR classifier gate
- [ ] Multi-agent isolation prevents cross-agent interference
- [ ] Periodic maintenance agents check for architectural drift
- [ ] Generator and Evaluator are separate agents for complex tasks
