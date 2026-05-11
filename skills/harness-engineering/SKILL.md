---
name: harness-engineering
description: Design runtime infrastructure around AI agents — permissions, tools, feedback loops, observability. Use when deploying agents to production or designing multi-agent systems.
version: "1.1"
updated: "2026-05-12"
---

# Harness Engineering

Design the system *around* AI agents for reliable, safe production use.

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

### 3. Architectural Constraints
- Linters, structural tests
- File/directory access boundaries
- Token budget: never exceed 80% context window

### 4. Feedback & Validation Loops
- Write-Test-Fix cycle
- **Generator + Evaluator pattern** (GAN-inspired)
- Deny-and-continue: try safer alternative on block
- Escalate to human after 3 consecutive blocks

### 5. Observability & Governance
- Log every tool call + result
- Metrics: success rate, revert rate, token usage
- Cost tracking per session

### 6. Maintenance
- Periodic agents: dead code, outdated docs, architectural drift
- Wiki lint for broken links/missing frontmatter

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
- [ ] High-risk actions require approval
- [ ] Multi-agent isolation prevents interference
- [ ] Generator and Evaluator separate for complex tasks
