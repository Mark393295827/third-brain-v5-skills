---
name: agent-teams-command
description: Command multi-agent work with bounded roles, ownership, integration gates, and verification loops. Use when the user needs Claude Code Agent Teams, parallel agents, delegation strategy, or multi-agent orchestration.
version: "1.4"
updated: "2026-06-01"
assumes: "Multi-agent work has separable ownership, clear integration points, and a configured agent runtime."
conflicts_with: "Do not use for tasks with a single obvious next step or no separable write scopes; prefer agentic-engineering or project-flow-ops."
---

# Ender's Game: Agent Teams Command System

> "Ender knew, even as he gave the order, that this was the way victory would come — not through strength, but through understanding." — Orson Scott Card

> This is not a "feature" — this is a **command system**. You are not "using" Agent Teams. You are **commanding a fleet**. Based on Karpathy's Agentic Engineering framework, transforming Claude Code Agent Teams into a complete operational architecture.

## Command Philosophy: Ender's Three Principles

| Principle | Meaning | Agent Teams |
|-----------|---------|-------------|
| **Trust Your Commander** | Ender commands through squad leaders, not every soldier | Let Team Lead coordinate; you don't micromanage each agent |
| **Understanding Over Strength** | Study the enemy's thinking | Know each agent's capability; choose Opus vs Sonnet deliberately |
| **Asymmetric Tactics** | Solve problems in unexpected ways | Let agents QA each other; parallel multi-directional exploration |

## Usage Template

**Prompt**
```text
Use agent-teams-command for this project. Split work into roles, define ownership, coordinate progress, and verify the integrated result.
```

**Use Case**
- Coordinating multi-agent work when a task is too large for one linear agent pass.

**Expected Result**
- The agent produces a team plan with roles, responsibilities, communication cadence, integration points, and verification gates.

**Output Example**
- A team map with agent roles, owned files or modules, deliverables, integration plan, and verification checklist.

**Verification Case**
- Each delegated task has a bounded scope, clear owner, expected output, and integration check.

**Verified Effect**
- Parallel agent work becomes coordinated delivery instead of overlapping, unreviewed outputs.

## Success Metrics

- Team plan names each role, owner, write scope, IPC channel, integration point, and stop condition.
- Every delegated workstream has at least one verification gate before integration.
- Final report states integrated status, unresolved risks, and which agents can be closed.

---

## Karpathy Agentic Engineering Mapping

```
You (Commander) = Process Scheduler
Team Lead       = CPU Core
Teammates       = Parallel Processes
Task List       = Shared Memory / IPC
Context Window  = RAM (per agent, isolated)
Tools           = System Calls
QA Loop         = Error Correction / Interrupt Handler
Team Log        = Durable Disk / Write-back
```

---

## Agent Team Operating Model

Use agent teams only when parallel processes reduce wall-clock time or increase quality. Each process needs a bounded territory, explicit IPC, and an integration gate.

| OS concern | Team command rule |
|---|---|
| Process creation | Spawn only for independent or reviewable work. |
| Memory isolation | Give each teammate only the context needed for its scope. |
| IPC | Use task lists, handoff notes, and review reports. |
| Locks | Assign file/module ownership before work begins. |
| Interrupts | Stop or redirect agents when scope, safety, or quality drifts. |
| Join | Integrate only after each output has evidence. |
| Cleanup | Close agents and write lessons to wiki/logs. |

Avoid parallelism when the next step depends on a single blocking decision. Do that work locally, then delegate independent slices.

## Antigravity-Style Swarm Boundary

Google I/O '26 described Antigravity as an agent-first development surface with subagents, hooks, async task management, and very large token budgets. Treat this as a cautionary operating pattern: swarm execution is useful only when the harness can prove progress.

Use a swarm only when all are true:

- tasks can be split into independent owned territories
- every territory has objective verification
- an async task queue or visible task list exists
- token, time, and request budgets are capped
- integration happens through a join gate, not direct file collision

Do not scale agent count to create momentum. Scale only when isolation plus verification reduces wall-clock time or improves review quality.

## Dynamic Workflow Choice Gate

Agent teams solve communication and coordination. Dynamic workflows solve width: a reviewed script launches many independent workers, then a synthesis step merges outputs.

Use a dynamic workflow instead of an agent team only when all are true:

- the work shards into many independent files, sources, tests, or review targets
- workers do not need frequent peer communication
- synthesis can merge results from structured outputs
- the generated script can be reviewed before execution
- agent count, model choice, files/directories, wall-clock, and token budget are capped
- runtime state exposes active workers, tool calls, cost, errors, and stop controls
- the workflow is archived in the project only if it is worth reusing

Choose an agent team when roles need IPC, debate, dependency handoffs, shared judgment, or iterative repair. Choose a long-running goal when the hard part is depth: keep iterating until objective criteria pass.

## Agentic Macro Actions

Delegate macro actions, not vague wishes. Each teammate receives a bounded unit such as feature implementation, research, plan critique, test design, or adversarial review.

```text
MACRO ACTION:
Objective:
Scope:
Non-goals:
Owned territory:
Inputs:
Expected output:
Verification evidence:
Risk review:
Handoff target:
Stop condition:
```

If two teammates need the same files, split by phase instead of parallel ownership. If proof is unclear, assign a researcher or evaluator before assigning a builder.

---

## Command Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                   Fleet Command System                         │
├──────────────────────────────────────────────────────────────┤
│  Phase 0: Plan     — Task decomposition + resource allocation │
│  Phase 1: Act      — Parallel multi-directional exploration   │
│  Phase 2: Observe  — Cross-validation + QA loop               │
│  Phase 3: Iterate  — Refine until quality threshold met       │
│  Phase 4: Learn    — Post-mission review + knowledge capture  │
└──────────────────────────────────────────────────────────────┘
```

---

## Chain of Command

```
You ──→ Team Lead ──→ Teammates
  ↓         ↓            ↓
Strategic  Tactical     Execution
```

### Three-Layer Decision Model

| Layer | Role | Responsibility | Karpathy Equivalent |
|:----:|------|--------------|-------------------|
| **Strategic** | You (Ender) | Set goals, allocate resources, key decisions | Process Scheduler |
| **Tactical** | Team Lead | Task decomposition, agent coordination, quality monitoring | Main Agent Loop |
| **Execution** | Teammates | Execute, call tools, return results | Worker Processes |

---

## L1: Recruit — System Activation

### Initial Setup
```json
// .claude/settings.local.json — Activate fleet command
{
  "experimental.agentTeams": true,
  "teammateMode": "auto"
}
```

```bash
claude --version  # Require ≥ v2.1.32
```

### System Verification (Plan→Act→Observe)
```
Plan:    Verify Agent Teams are available
Act:     Create a 3-agent team for a simple task
Observe: Check multi-color panels are active
Iterate: If failed, check config and version
```

### First Deployment
```
Create a team of 3 teammates using Sonnet.
1. Front-end developer
2. Back-end developer
3. QA agent
Build me a landing page.
```

---

## L2: Squad Leader — Understanding the System

### Agentic Engineering Core Concepts

```
Agent Teams = Multi-processing parallel system
Sub-agents  = Single-threaded sub-processes
```

| Architecture | Sub-agents | Agent Teams |
|-------------|-----------|-------------|
| **Context** | Isolated process, result returns to main | Fully isolated processes |
| **IPC** | Reports to main agent only | **Direct inter-process messaging** |
| **Scheduling** | Main agent manages all | **Shared memory + self-scheduling** |
| **Token Cost** | Lower | Higher (but significantly better quality) |

### Karpathy Engineering Checklist

```
□ Each agent has clear system boundary (Own Territory)
□ Task list managed as shared memory
□ QA loop as error correction mechanism
□ Plan→Act→Observe iteration
□ Resource monitoring (Token cost)
□ Team log captures decisions, evidence, and reusable learning
```

---

## L3: Tactician — Efficient Execution

### Standard Orders Template (Karpathy Plan→Act→Observe)

```
GOAL: [Strategic objective — sets context, like loading system prompt]

ORDERS: Create a team of [N] teammates using [MODEL].

─── TEAMMATE 1 ─── Codename: [NAME] — Role: [ROLE]
  TASK: [Specific task description]
  OWNERSHIP: [file/module ownership]
  DEPENDENCY: Message [TEAMMATE] when done
  
─── TEAMMATE 2 ─── Codename: [NAME] — Role: [ROLE]
  TASK: [Specific task description]
  OWNERSHIP: [file/module ownership]
  DEPENDENCY: Wait for [TEAMMATE] to complete

─── TEAMMATE 3 ─── Codename: [NAME] — Role: QA
  TASK: Validate all outputs
  OWNERSHIP: tests/
  DEPENDENCY: Wait for all teammates

DELIVERABLES:
1. [Deliverable 1]
2. [Deliverable 2]
3. QA report
4. Integration notes + residual risks

QUALITY GATES:
- [ ] All tests passing
- [ ] No critical QA issues
- [ ] No file ownership conflicts
- [ ] Token/time/request budget stayed inside cap
- [ ] Each teammate reports changed files, evidence, and open risks
- [ ] High-risk outputs reviewed by a separate critic or red team
```

### Three Engineering Laws

| # | Principle | Engineering Meaning | Violation Consequence |
|:-|----------|-------------------|---------------------|
| 1 | **Own Territory** | Each module has a clear owner | File overwrites, logic conflicts |
| 2 | **Direct Messaging** | Inter-process IPC communication | Dependency blocking, serialization |
| 3 | **Wait-for-Dependencies** | Synchronization point management | Data inconsistency, race conditions |

### Command Interface

```
In-process mode:
  Shift+Down = Switch process context
  Escape     = Send interrupt signal (SIGINT)
  Ctrl+T     = View process table (task list)

Split-panes mode (tmux):
  Each process in its own terminal
  Color coding: Red(BE)/Green(FE)/Blue(QA)/Yellow(Research)
```

---

## L4: Commander — Advanced Systems Engineering

### Plan Approval Gate

> Engineering equivalent of "design review" phase.

```text
Spawn an architect teammate to refactor the auth module.
Require plan approval before they make any changes.
```

```
Teammate (Plan Mode) → Submit design proposal
    ↓
Lead → Design review
    ├── Approved → Enter execution phase
    └── Rejected → Revise and resubmit
```

**Review criteria (programmable quality gates):**
```
"Only approve plans that include test coverage"        → Test coverage gate
"Reject plans that modify the database schema"          → Architecture protection gate
"Every plan must have a rollback strategy"              → Rollback strategy gate
```

### Hooks: System Event Callbacks

> Similar to Karpathy's tool-call hook mechanism — triggers callbacks on key system events.

```json
{
  "hooks": {
    "TeammateIdle":   "python scripts/check-idle.py",    // Process idle → reschedule
    "TaskCreated":    "python scripts/validate-task.py",  // Task created → validate
    "TaskCompleted":  "python scripts/verify-quality.py"  // Task done → quality check
  }
}
```

### Multi-Phase Pipeline

> Classic systems engineering pattern: parallel sub-tasks within sequential phases.

```
PHASE 0 — Plan
  3 researchers exploring different directions in parallel
  ↓ Sync point: All directions complete

PHASE 1 — Observe
  Critic reviews all findings
  ↓ Sync point: Consensus reached

PHASE 2 — Act
  Builder executes validated solution
  ↓ Sync point: Execution complete

PHASE 3 — QA (Iterate)
  Full test + fix loop
  ↓ Exit when quality threshold met
```

### Fleet Resource Management

```
Optimal size: 3-5 agents (beyond → scheduling overhead > parallel gain)
Model selection: Sonnet (default) | Opus (complex reasoning) | Haiku (simple tasks)
Token budget: Each agent has independent context window
Cleanup protocol: Lead MUST execute cleanup (otherwise resource leak)
Write-back: Lead records decisions, evidence, and reusable lessons
```

For long-horizon builds, add a budget envelope before launch:

```text
Max agents:
Max wall-clock:
Max tool calls / model requests:
Max token or cost estimate:
Checkpoint cadence:
Kill condition:
```

### Resource Cleanup Protocol

```text
1. "Ask [teammate] to shut down"     → Send termination signal
2. Wait for confirmation              → Graceful shutdown
3. Repeat until all teammates down   → All processes terminated
4. "Clean up the team"                → Release shared resources
```

---

## L5: Legendary Commander — Classic Campaigns

Detailed campaign templates live in `references/classic-campaigns.md` to keep the executable skill short. Use them for full-stack builds, technical decision research, and security audit/fix work when a concrete order format is needed.

---

## Quality Gates

### Systems Engineering Checklist

```
[Phase 0: Plan]
□ Tasks decomposed into parallelizable sub-tasks
□ Each sub-task has clear owner and boundary
□ Each macro action has non-goals, proof, and stop condition
□ Dependencies modeled
□ Team vs dynamic workflow vs long-running goal choice is justified

[Phase 1: Act]
□ Agents launched in parallel per plan
□ No file ownership conflicts
□ Inter-process communication normal
□ Agent count, wall-clock, request count, and token budget inside cap
□ Generated workflow scripts reviewed before execution when used

[Phase 2: Observe]
□ QA loop executed
□ High-risk outputs passed adversarial review
□ Issues fed back to corresponding agent
□ Re-verified after fixes

[Phase 3: Iterate]
□ Quality met → exit loop
□ Not met → continue iteration
□ Max iterations exceeded → escalate to commander

[Phase 4: Learn]
□ Post-mission report generated
□ Lessons captured in knowledge base
□ Applicable to future campaigns
□ Teammates closed or explicitly handed off
```

### Diagnostic Matrix

| Symptom | Root Cause | System-Level Solution |
|---------|-----------|---------------------|
| Agent file overwrites | No ownership protocol | Enforce Own Territory |
| Task deadlock | Dependency cycle | Simplify dependency graph, avoid cycles |
| Token explosion | Agent count >10 | Limit to 3-5 agents |
| Insufficient context | Missing initial instructions | Full context in GOAL (like system prompt) |
| Resource leak | Lead didn't run cleanup | Enforce cleanup protocol |
| Fast but fragile output | Vibe coding without quality ceiling | Add spec, evaluator, and proof gate |

---

## Evolution Timeline

- **2026-05-10**: Created. Agent Teams command system based on Karpathy Agentic Engineering framework. L1-L5 commander progression path. 3 classic engineering campaigns.
