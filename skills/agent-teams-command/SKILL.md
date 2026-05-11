---
name: agent-teams-command
description: Ender's Game approach to commanding Claude Code Agent Teams. Strategic multi-agent orchestration with Karpathy Agentic Engineering principles — plan, act, observe, iterate. L1-L5 commander progression.
---

# Ender's Game: Agent Teams Command System

> This is not a "feature" — this is a **command system**. Based on Karpathy's Agentic Engineering framework for systematic problem-solving, transforming Claude Code Agent Teams from ad-hoc tools into a complete operational architecture.

## Usage Template

**Prompt**
```text
Use agent-teams-command for this project. Split work into roles, define ownership, coordinate progress, and verify the integrated result.
```

**Use Case**
- Coordinating multi-agent work when a task is too large for one linear agent pass.

**Expected Result**
- The agent produces a team plan with roles, responsibilities, communication cadence, integration points, and verification gates.

**Verification Case**
- Each delegated task has a bounded scope, clear owner, expected output, and integration check.

**Verified Effect**
- Parallel agent work becomes coordinated delivery instead of overlapping, unreviewed outputs.

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
```

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

QUALITY GATES:
- [ ] All tests passing
- [ ] No critical QA issues
- [ ] No file ownership conflicts
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

### Campaign 1: Full-Stack System Development

```text
GOAL: Build a full-stack app (REST API + React) running on localhost.

ORDERS: Create a team of 3 teammates using Sonnet.

─── TEAMMATE 1 (Codename: GEPARD/BACKEND) ───
  TASK: FastAPI + SQLite + REST endpoints
  OWNERSHIP: backend/
  DEPENDENCY: Notify FALCON when done

─── TEAMMATE 2 (Codename: FALCON/FRONTEND) ───
  TASK: React frontend + API integration
  OWNERSHIP: frontend/
  DEPENDENCY: Wait for GEPARD's API spec

─── TEAMMATE 3 (Codename: SENTINEL/QA) ───
  TASK: E2E tests + API tests
  OWNERSHIP: tests/
  DEPENDENCY: Wait for all teammates

QUALITY GATES:
- [ ] All tests passing
- [ ] API response time <200ms
- [ ] No frontend console errors
```

### Campaign 2: Technical Decision Research

```text
GOAL: Evaluate PostgreSQL → MongoDB migration feasibility.

ORDERS: Create a team of 3 teammates using Opus.

─── TEAMMATE 1 (Codename: OWL/DATABASE) ───
  TASK: Query pattern analysis + performance benchmarks
  OWNERSHIP: research/performance/

─── TEAMMATE 2 (Codename: BEAVER/MIGRATION) ───
  TASK: Migration tool evaluation + downtime analysis
  OWNERSHIP: research/migration/

─── TEAMMATE 3 (Codename: FOX/CRITIC) ───
  TASK: Challenge first two teammates' conclusions
  OWNERSHIP: research/risks/
  DEPENDENCY: Wait for OWL + BEAVER to complete
```

### Campaign 3: Security Audit & Fix

```text
GOAL: Find and fix all security vulnerabilities in the auth module.

ORDERS: Create a team of 2 teammates using Sonnet.

─── TEAMMATE 1 (Codename: EAGLE/AUDITOR) ───
  TASK: OWASP Top 10 scan + code audit
  OWNERSHIP: security/audit/
  DEPENDENCY: Submit issues to BADGER when done

─── TEAMMATE 2 (Codename: BADGER/FIXER) ───
  TASK: Fix all discovered security issues
  OWNERSHIP: src/auth/
  DEPENDENCY: Wait for EAGLE's issue list
```

---

## Karpathy Agentic Engineering Quality Gates

### Systems Engineering Checklist

```
[Phase 0: Plan]
□ Tasks decomposed into parallelizable sub-tasks
□ Each sub-task has clear owner and boundary
□ Dependencies modeled

[Phase 1: Act]
□ Agents launched in parallel per plan
□ No file ownership conflicts
□ Inter-process communication normal

[Phase 2: Observe]
□ QA loop executed
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
```

### Diagnostic Matrix

| Symptom | Root Cause | System-Level Solution |
|---------|-----------|---------------------|
| Agent file overwrites | No ownership protocol | Enforce Own Territory |
| Task deadlock | Dependency cycle | Simplify dependency graph, avoid cycles |
| Token explosion | Agent count >10 | Limit to 3-5 agents |
| Insufficient context | Missing initial instructions | Full context in GOAL (like system prompt) |
| Resource leak | Lead didn't run cleanup | Enforce cleanup protocol |

---

## Evolution Timeline

- **2026-05-10**: Created. Agent Teams command system based on Karpathy Agentic Engineering framework. L1-L5 commander progression path. 3 classic engineering campaigns.
