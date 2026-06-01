---
name: harness-engineering
description: Design runtime infrastructure around AI agents — permissions, tools, feedback loops, observability. Use when deploying agents to production or designing multi-agent systems.
version: "1.3"
updated: "2026-05-23"
assumes: "The agent workflow will use tools, permissions, logs, or production-like reliability boundaries."
conflicts_with: "Do not relax approval, sandbox, or observability constraints introduced by agentic-engineering or agent-teams-command."
---

# Harness Engineering

Design the system *around* AI agents for reliable, safe production use.

Harness Engineering protects the quality ceiling of Agentic Engineering. It turns fast agent output into controlled execution through permissions, observability, recovery, and adversarial validation.

## Agent Runtime Model

Treat the agent harness as the kernel around an LLM OS:

| Kernel concern | Agent harness responsibility |
|---|---|
| Memory management | Curate context, summarize bulky outputs, persist state to wiki/logs. |
| Syscall boundary | Expose tools with contracts, allowlists, deny rules, and retries. |
| Process isolation | Separate write scopes, sandboxes, credentials, and state per agent. |
| Scheduling | Decide sequential, parallel, or event-driven execution. |
| Interrupts | Stop, ask approval, rollback, or route to a safer action. |
| Observability | Log tool calls, decisions, outputs, costs, and verification evidence. |
| Garbage collection | Close idle agents, remove stale tasks, compact context, and record risks. |

## Productized Agent Harness

Google I/O '26 added a practical pressure test for harness design: the same runtime pattern now appears in developer tools, personal agents, search, commerce, generative media, and smart glasses.

| Product surface | Harness control that must exist |
|---|---|
| Agent-first IDE | task queue, subagent ownership, hooks, sandbox, test proof |
| Personal agent | user mandate, memory scope, tool allowlist, resumable log |
| Agentic search | source provenance, comparison criteria, action preview |
| Agentic commerce | budget, merchant/payment boundary, mandate, receipt trail |
| Generative media | prompt/edit history, watermark/disclosure, content credentials |
| Ambient eyewear/device | sensor consent, privacy mode, physical-world fallback |

If a harness cannot produce an audit trail for what the agent saw, decided, called, changed, and verified, the agent is not ready for delegated action.

## Usage Template

**Prompt**
```text
Use harness-engineering for this agent workflow. Design permissions, tools, feedback loops, observability, and failure handling.
```

**Use Case**
- Moving an agent workflow from ad hoc prompting toward a reliable runtime architecture.

**Expected Result**
- The agent produces a harness design with permission tiers, tool boundaries, logs, evals, and recovery paths.

**Output Example**
- A runtime spec with permission matrix, tool allowlist, approval gates, logs, evals, and incident response.

**Verification Case**
- The design names what the agent can do automatically, what needs approval, and what is denied.

**Verified Effect**
- An ad hoc agent workflow becomes a controlled runtime with explicit permissions, observability, and failure handling.

## Success Metrics

- Design specifies permissions, tool contracts, observability, failure handling, and recovery path.
- High-risk actions have approval or sandbox boundaries.
- Verification evidence is defined before deployment or automation.

## When to Use

- Deploying agents to production
- Setting up permissions/guardrails/approval workflows
- Designing multi-agent systems
- Agent behaved unpredictably → needs better constraints
- Configuring auto-mode or permission tiers

---

## Three Domains

| Domain | Object | Maturity |
|--------|--------|----------|
| **Physical** | Wire harnesses (automotive/aerospace) | ⭐ Mature |
| **Software** | CI/CD pipelines (Harness.io) | ⭐ Mature |
| **Cognitive** ⭐ | AI Agents | 🌱 Emerging |

---

## Six Components

### 1. Context & Knowledge Layer
- Curated access to code, docs, schemas, logs
- Use `CLAUDE.md` for project-level context
- Use `context-manager` for token budgeting
- Never inject raw 10K+ token files
- Persist reusable outputs to wiki, docs, logs, or state files; chat history is not durable memory

### 2. Tooling & API Surface
**Three-Tier Permission Model:**

| Tier | Scope | Mechanism | Examples |
|:----:|-------|-----------|----------|
| **1** | Safe tools | Always allowed | Read, search, grep, glob |
| **2** | In-project | Auto-approve (git reviewable) | Write/edit in project dir |
| **3** | High-risk | Classifier/human approval | Shell, API calls, deletes |

**Tier 3 heuristic:**
```
1. Can destroy data irreversibly? → BLOCK
2. Accesses credentials? → BLOCK
3. Affects shared infrastructure? → BLOCK
4. Target inferred (not explicit)? → BLOCK
```

**Delegated action gate:**

Before any tool call that buys, publishes, schedules, messages, edits shared state, or acts through a user's account, require:

```text
Mandate: what the user explicitly authorized
Scope: allowed accounts, surfaces, vendors, files, or domains
Limit: budget, time, rate, data, or blast radius cap
Preview: what the user can inspect before execution
Receipt: durable audit record after execution
Rollback: how to undo or compensate if wrong
```

### 3. Architectural Constraints
- Linters, structural tests
- File/directory access boundaries
- Token budget: never exceed 80% context window

### 4. Feedback & Validation Loops
- Write-Test-Fix cycle
- **Generator + Evaluator pattern** (GAN-inspired)
- Deny-and-continue: try safer alternative on block
- Escalate to human after 3 consecutive blocks
- For high-risk work: Builder -> Evaluator -> Red Team -> Fixer -> final proof

### 5. Observability & Governance
- Log every tool call + result
- Metrics: success rate, revert rate, token usage
- Cost tracking per session
- Evidence ledger: verification command, source link, screenshot, test result, or diff for each completion claim
- Provenance ledger for generated media, search summaries, and commerce decisions: source, prompt/edit trail, model/tool used, and user confirmation point

### 6. Maintenance
- Periodic agents: dead code, outdated docs, architectural drift
- Wiki lint for broken links/missing frontmatter
- Context garbage collection: summarize completed work, close idle processes, and record residual risk

---

## GAN-Inspired Multi-Agent Pattern

> "Tuning a standalone evaluator to be skeptical is far more tractable than making a generator critical of its own work."

```
Generator ←──sprint contract──→ Evaluator
    │                              │
    ▼                              ▼
 Produces output              Playwright/Test
```

**Implementation:**
1. **Planner** → 1-sentence prompt → full spec
2. **Generator** → builds in sprints
3. **Evaluator** → tests, files bugs
4. Feedback loop → 5-15 iterations

---

## Physical → Cognitive Analogies

| Physical | AI Agent | Implementation |
|----------|----------|----------------|
| Zonal Architecture | Permission scopes | `AGENTS.md` domain restrictions |
| IP68 Protection | Security isolation | Sandbox, token in vault |
| HiPot Test | Stress testing | Edge-case test suite |
| Continuity Test | Tool verification | `describe-tools` pre-flight |
| EMC/Interference | Multi-agent isolation | Separate sandbox per agent |

---

## Multi-Agent Patterns

| Pattern | Description | When to Use |
|---------|-------------|-------------|
| **Supervisor** | Orchestrator delegates to sub-agents | Complex tasks with sub-steps |
| **Peer Review** | Agents review each other | High-risk changes |
| **Competitive** | Multiple agents try same task | Creative work, optimization |
| **Pipeline** | Sequential chain | Document processing |
| **Zonal** | Domain-based routing | Enterprise systems |
| **Closed-Loop** | Output feedback shapes input | Continuous improvement |

---

## Permissioned Tool Design

Define every tool like a system call:

| Field | Required question |
|---|---|
| Purpose | What state can this tool read or change? |
| Inputs | Which arguments must be explicit, not inferred? |
| Bounds | Which paths, domains, records, or resources are allowed? |
| Failure mode | What is the safe fallback when it fails or is denied? |
| Evidence | What output proves it succeeded? |
| Audit | Where is the call logged? |

Prefer narrow tools with explicit inputs over broad shell/API access. If broad access is unavoidable, wrap it with approval gates and post-action verification.

---

## Security-Aware Integration

Before shipping high-risk agent output, run an adversarial review:

| Risk area | Minimum adversarial check |
|---|---|
| Auth, permissions, secrets | Attempt privilege escalation and secret exposure paths. |
| Data mutation or deletion | Verify backups, rollback, idempotency, and explicit target bounds. |
| Public claims or launch copy | Check evidence, source quality, and unsupported promises. |
| External API actions | Confirm rate limits, credentials, audit logs, and retry safety. |
| Commerce or delegated account actions | Verify mandate, budget, merchant/payment boundary, receipt trail, and rollback path. |
| Generated media or public content | Verify provenance, disclosure/watermark path, and unsupported claim risk. |
| Multi-agent integration | Check ownership conflicts, stale assumptions, and unverified joins. |

Use simulated hostile agents, security tests, or a skeptical evaluator before release. Do not let the same builder be the only judge of safety.

---

## Closed-Loop System (Aladdin)

```
Data Lake → Risk Engine → Optimizer → Stress Test → OMS → Compliance → Feedback Loop
     ↑                                                              ↓
     └──────────────────── 反馈闭环 ────────────────────────────────┘
```

| Aladdin Module | Agent Harness |
|----------------|---------------|
| Data Lake | Session log, knowledge base |
| Risk Engine | Risk assessment, threat detection |
| Optimizer | Task decomposition, resource allocation |
| Stress Test | Edge-case testing, failure simulation |
| OMS | Order execution, tool calls |
| Compliance | Guardrails, policy enforcement |
| Feedback Loop | Results → learning → improvement |

**Key:** Closed loop is the moat — not any single component. MECE principle applies.

---

## Quality Gates

- [ ] Each agent has defined permission scope
- [ ] Three-tier permission model documented
- [ ] Write-Test-Fix feedback loop in place
- [ ] Tool calls logged and observable
- [ ] Token costs tracked per session
- [ ] Delegated actions have mandate, scope, limit, preview, receipt, and rollback
- [ ] Generated media and public claims have provenance or disclosure path
- [ ] High-risk actions require approval
- [ ] Multi-agent isolation prevents interference
- [ ] Generator and Evaluator separate for complex tasks
- [ ] High-risk outputs receive adversarial or red-team review
- [ ] Reusable outputs have durable write-back outside chat history
- [ ] Tool contracts include bounds, failure path, evidence, and audit trail
