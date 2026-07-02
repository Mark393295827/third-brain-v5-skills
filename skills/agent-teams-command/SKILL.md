---
name: agent-teams-command
description: Command V6 multi-agent work with bounded roles, ownership, worktree isolation, IPC, integration gates, cleanup, attention budgets, and verification loops. Use when the user needs Claude Code Agent Teams, parallel agents, delegation strategy, Ender-style commander training, von Neumann-style command architecture, Palantir-style ontology command boards, FDE field discovery, EDD integration gates, dynamic workflow tradeoffs, or multi-agent orchestration grounded in Obsidian wiki operating rules.
version: "6.2"
updated: "2026-07-02"
assumes: "Multi-agent work has separable ownership, clear integration points, risk budgets, and a configured agent runtime."
conflicts_with: "Do not use for tasks with a single obvious next step or no separable write scopes; prefer agentic-engineering or project-flow-ops."
---

# Agent Teams Command System

Command agent teams as bounded processes with ownership, IPC, integration gates, and proof. Use parallelism only when it reduces wall-clock time or improves review quality after accounting for coordination cost.

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
- V6 plan states human review bandwidth, kill/downweight signals, and durable write-back target before scaling agent count.
- Team state is represented as durable objects, actions, evidence, feedback, and decisions, not chat-only coordination.
- Human operators keep visibility into real stakes, permissions, and review burden; hidden-real-world consequences are forbidden.
- Team plan maps command program, control path, memory, IPC bus, tools, disk, verifier, and self-improvement boundary before launch.

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

## V6 Attention and Ownership Gate

Execution can become cheap while review stays scarce. Before adding agents, define:

| Gate | Required answer |
|---|---|
| Review bandwidth | How many outputs, PRs, diffs, or reports can the human/lead actually inspect? |
| Worktree / state isolation | Which branch, worktree, folder, database, or sandbox belongs to each agent? |
| Join gate | What evidence must exist before integration? |
| Quiet-success risk | How will the lead keep understanding if agents make many correct-but-large changes? |
| Cleanup | Who closes agents, archives state, and writes lessons back? |

If the answer is unclear, reduce agent count or use a single thin loop.

## Ender-Palantir Command Gate

Use Ender as a command metaphor, not a stress-design recipe. Reuse empowered squad leaders, own territory, direct messaging, asymmetric problem solving, and after-action learning. Do not copy manipulation, hidden real-world stakes, no-rest pressure, or isolation without support.

Use Palantir's ontology pattern when team outputs must become a durable operating system:

| Layer | Team artifact |
|---|---|
| Data | Mission, workstream, territory, dependency, risk, evidence, feedback, and decision objects. |
| Logic | Ownership rules, dependency graph, verifier, eval/grader, and integration policy. |
| Action | Allowed tools plus handoff, verify, reject, integrate, rollback, and close verbs. |
| Feedback | Operator correction becomes a review item, eval case, or contract update. |

When the domain is messy or user workflows are implicit, run FDE reconnaissance before building: observe real workflow, permissions, exceptions, and current friction; ship a narrow gravel-road artifact; only then abstract a paved path. Long-running teams need orchestrator state: checkpoint, await condition, resume trigger, and trace path.

For concrete templates, read `references/ender-palantir-command-patterns.md`.

## Von Neumann Command Frame

Use this frame when agent-team work needs architecture, not more teammates. Convert the commander's intent into a stored program: explicit order, serial control path, small per-agent RAM, durable disk, typed IPC bus, permissioned tools, independent verifier, and V6 promotion boundary.

Parallelize only after intent, ownership, and join gate are fixed. Each workstream needs a local automata rule: `state + evidence -> next action -> verifier -> next state | stop | escalate`. For the fuller template, read `references/ender-palantir-command-patterns.md`.

## Antifragile Swarm Gate

Before spawning agents, assume the environment has fog and friction: incomplete context, stale assumptions, noisy outputs, tool failures, and permission risk. Command the team as a risk-budgeted swarm, not a pile of helpers.

| Gate | Command rule |
|---|---|
| Survival first | Define the maximum acceptable blast radius per teammate. |
| No hero node | No single teammate owns planning, execution, verification, and write-back for a high-risk path. |
| Replaceability | Each teammate has a narrow role, bounded tools, and a handoff format another agent can continue. |
| Mechanical rebalancing | Define when to downweight, kill, replace, or add a reviewer based on cost, error rate, risk, or blocked state. |
| OODA low friction | Observe few signals, orient with the shared plan, decide from finite actions, act in reversible steps, and write back evidence. |

If you cannot name blast radius, kill condition, and verification evidence for a teammate, do not spawn that teammate.

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
Risk budget / blast radius:
Allowed tools / denied actions:
Expected output:
Verification evidence:
Ontology object / action:
Feedback capture:
Eval or grader:
Risk review:
Handoff target:
Stop condition:
```

If two teammates need the same files, split by phase instead of parallel ownership. If proof is unclear, assign a researcher or evaluator before assigning a builder.

---

## Command Architecture

Run phases as `Plan -> Act -> Observe -> Iterate -> Learn`: decompose, launch bounded workers, cross-validate, repair until the threshold or cap fires, then close and write lessons.

## Chain of Command

Chain: `You / strategic scheduler -> Team Lead / tactical loop -> Teammates / worker processes`.

### Three-Layer Decision Model

| Layer | Role | Responsibility | Karpathy Equivalent |
|:----:|------|--------------|-------------------|
| **Strategic** | You (Ender) | Set goals, allocate resources, key decisions | Process Scheduler |
| **Tactical** | Team Lead | Task decomposition, agent coordination, quality monitoring | Main Agent Loop |
| **Execution** | Teammates | Execute, call tools, return results | Worker Processes |

---

## L1: Recruit — System Activation

Verify the runtime before launch: Agent Teams enabled, current CLI supports teammates, a simple 2-3 agent smoke task runs, and the lead can view or interrupt each teammate. If activation fails, fix config and version before assigning real work.

First deployment order:

```text
Create a team of 3 teammates using Sonnet:
1. Front-end developer
2. Back-end developer
3. QA agent
Build a small localhost app and return changed files plus QA evidence.
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

RISK BUDGET:
  Max blast radius per teammate: [files/actions/data/accounts]
  Kill/downweight signals: [cost spike | repeated error | blocked | unsafe action]
  Rebalance options: [replace | add critic | narrow scope | switch sequential]
  Write-back target: [wiki/log/state file]
  Command board: [mission/workstream/evidence/feedback/decision object path]
  EDD gate: [eval suite, grader, review fixture, or deterministic command]
  Von Neumann frame: [program | control | memory | IPC bus | tools | disk | verifier | promotion boundary]

─── TEAMMATE 1 ─── Codename: [NAME] — Role: [ROLE]
  TASK: [Specific task description]
  OWNERSHIP: [file/module ownership]
  PERMISSIONS: [allowed tools/actions; denied actions]
  BLAST RADIUS: [maximum change or effect]
  DEPENDENCY: Message [TEAMMATE] when done
  
─── TEAMMATE 2 ─── Codename: [NAME] — Role: [ROLE]
  TASK: [Specific task description]
  OWNERSHIP: [file/module ownership]
  PERMISSIONS: [allowed tools/actions; denied actions]
  BLAST RADIUS: [maximum change or effect]
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
- [ ] Blast radius and permission limits held
- [ ] Each teammate reports changed files, evidence, and open risks
- [ ] High-risk outputs reviewed by a separate critic or red team
- [ ] Lessons, decisions, and risk adjustments written back
- [ ] Human review bandwidth and quiet-success risk stayed inside the declared cap
```

### Three Engineering Laws

| # | Principle | Engineering Meaning | Violation Consequence |
|:-|----------|-------------------|---------------------|
| 1 | **Own Territory** | Each module has a clear owner | File overwrites, logic conflicts |
| 2 | **Direct Messaging** | Inter-process IPC communication | Dependency blocking, serialization |
| 3 | **Wait-for-Dependencies** | Synchronization point management | Data inconsistency, race conditions |

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

Mechanical rebalancing rules:

| Signal | Action |
|---|---|
| Same blocker twice | Narrow scope or switch to sequential execution. |
| Rising cost without evidence | Pause or downweight the teammate. |
| Unsafe or out-of-scope tool request | Kill or sandbox the process; add reviewer. |
| High-value uncertainty | Add a critic/researcher before adding a builder. |
| Integration conflict | Stop parallel writes and join through the lead. |

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
□ Each sub-task has risk budget, blast radius, and kill/downweight condition
□ Each macro action has non-goals, proof, and stop condition
□ Dependencies modeled
□ Team vs dynamic workflow vs long-running goal choice is justified
□ Ender safety boundary stated: no hidden real stakes, manipulation, or unsupported pressure
□ Command board defines Data, Logic, Action, and Feedback objects
□ Von Neumann command frame defines program, control path, memory, IPC bus, tools, disk, verifier, and promotion boundary

[Phase 1: Act]
□ Agents launched in parallel per plan
□ No file ownership conflicts
□ Inter-process communication normal
□ Permission and blast-radius limits held
□ Agent count, wall-clock, request count, and token budget inside cap
□ Generated workflow scripts reviewed before execution when used
□ Messy workflow tasks run FDE reconnaissance before abstraction

[Phase 2: Observe]
□ QA loop executed
□ High-risk outputs passed adversarial review
□ EDD gate uses an eval suite, grader, fixture, or deterministic command; eyeballing is not enough
□ Operator feedback is codified into review items, eval cases, or contract updates
□ Rebalancing decisions applied when agents drifted, stalled, or exceeded budget
□ Issues fed back to corresponding agent
□ Re-verified after fixes

[Phase 3: Iterate]
□ Quality met → exit loop
□ Not met → continue iteration
□ OODA loop stayed low-friction: few signals, finite decisions, reversible actions
□ Max iterations exceeded → escalate to commander

[Phase 4: Learn]
□ Post-mission report generated
□ Lessons captured in knowledge base
□ Risk budget and rebalancing lessons written back
□ Applicable to future campaigns
□ Teammates closed or explicitly handed off
□ Human review bandwidth and quiet-success risk recorded
□ Reusable skill/SOP/hook candidates were queued through the V6 promotion gate, not self-promoted from a single run
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
| Swarm gets noisy | No shared OODA frame | Reduce signals, freeze plan, route updates through lead |
| One agent becomes hero node | Too much authority in one process | Split planner/builder/evaluator/write-back roles |
| Agent spends without proof | No mechanical rebalancing | Downweight, narrow scope, or kill based on predeclared signal |
| Human cannot review the output queue | Attention bottleneck ignored | Lower parallelism, batch by risk, or add evaluator summaries with proof links |
| Agents converge on the same hidden assumption | Cognitive monoculture | Add diverse reviewer prompts, perturb assumptions, or require external evidence |
| Team talks but state is unrecoverable | No ontology command board | Convert mission, workstreams, evidence, feedback, and decisions into durable objects |
| Polished demo fails in real workflow | No FDE reconnaissance | Observe operators, permissions, exceptions, and friction before abstracting product rules |
| User feedback stays vague | No feedback quality gate | Add an interceptor/reviewer that asks for concrete correction and turns it into eval cases |

---

## Evolution Timeline

- **2026-05-10**: Created. Agent Teams command system based on Karpathy Agentic Engineering framework. L1-L5 commander progression path. 3 classic engineering campaigns.
- **2026-06-08**: Added antifragile swarm gate from same-day Obsidian ingest: risk budgets, blast radius, no-hero-node decomposition, mechanical rebalancing, and low-friction OODA write-back.
- **2026-06-27**: V6 update: added attention/ownership gate, quiet-success risk, review bandwidth caps, worktree/state isolation, and cognitive-monoculture mitigation.
- **2026-06-27**: V6.1 update: added Ender safety boundary, Palantir ontology command board, FDE reconnaissance, EDD gates, feedback codification, and orchestrator checkpoints.
- **2026-07-02**: V6.2 update: added von Neumann command frame from Obsidian wiki to structure agent teams as stored-program systems with explicit control, memory, IPC, tools, verifiers, and promotion boundaries.
