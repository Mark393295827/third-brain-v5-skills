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

## The Three Domains of Harness Engineering

Harness Engineering is a unified discipline across three domains. This skill focuses on the **cognitive/AI layer**, but draws analogies from the other two:

| Domain | Object | Maturity |
|--------|--------|----------|
| **Physical** | Wire harnesses (automotive/aerospace) | ⭐ Mature (IPC/WHMA-A-620) |
| **Software** | CI/CD pipelines (Harness.io) | ⭐ Mature (DORA metrics) |
| **Cognitive** ⭐ | AI Agents | 🌱 Emerging (2025-2026) |

## Six Components of an AI Agent Harness

### 1. Context & Knowledge Layer
Curated access to code, docs, schemas, logs, and runtime data. The agent should see the right information at the right time — no more, no less.

**Design questions:**
- What knowledge does the agent need to start?
- What should it be able to retrieve on demand?
- What should it NOT have access to?

### 2. Tooling & API Surface
Well-designed tools with clear contracts so agents can call them predictably. Each tool is a capability with defined inputs, outputs, and side effects.

**Anti-pattern:** Giving the agent a `bash` tool with no restrictions = giving a hammer to a toddler.

### 3. Architectural Constraints & Policy
Deterministic checks that enforce what an agent may change:
- Linters and structural tests
- File/directory access boundaries
- Module dependency rules
- Read-only vs. writable paths

### 4. Feedback & Validation Loops
Automatic verification of agent output:
- Write-Test-Fix cycle (agent must run tests after changes)
- Spec-checkers and reviewers (including other agents)
- Rollback on failure
- Escalation to human when confidence is low

### 5. Observability & Governance
- Logging every tool call and its result
- Metrics: success rate per task type, revert rate, token usage
- Human-in-the-loop approval for high-risk actions
- Traces for multi-step agent workflows

### 6. Maintenance / Garbage Collection
Periodic agents that find:
- Dead code and outdated docs
- Violations of architectural constraints
- Entropy over time

## Physical → Cognitive Analogies

| Physical Harness | AI Agent Harness |
|-----------------|------------------|
| **Zonal Architecture** (car divided into physical zones, each with a local controller) | Agent permission scopes — each agent restricted to its domain |
| **IP68 Ingress Protection** | Security isolation — prevent prompt injection, privilege escalation |
| **HiPot Dielectric Test** | Stress testing — verify behavior doesn't break under edge cases |
| **Continuity Test** | Tool chain verification — ensure all tool paths are complete |
| **EMC / Interference Shielding** | Multi-agent isolation — prevent agents from interfering with each other |

## Multi-Agent Orchestration Patterns

| Pattern | Description | When to Use |
|---------|-------------|-------------|
| **Supervisor** | One orchestrator delegates to specialized sub-agents | Complex tasks with clear sub-steps |
| **Peer Review** | Agents review each other's output before production | High-risk changes (code, config, data) |
| **Competitive** | Multiple agents try the same task, best result wins | Creative work, optimization problems |
| **Pipeline** | Agents pass work sequentially in a chain | Document processing, data pipelines |
| **Zonal** | Each agent owns a domain/zone, orchestrator routes | Enterprise systems with clear boundaries |

## Quality Gates

- [ ] Each agent has a defined permission scope (what it CAN and CANNOT do)
- [ ] Write-Test-Fix feedback loop is in place
- [ ] Tool calls are logged and observable
- [ ] High-risk actions require human approval
- [ ] Multi-agent isolation prevents cross-agent interference
- [ ] Periodic maintenance agents check for architectural drift
