---
name: project-flow-ops
description: Operate execution flow — triage tasks, manage priorities, keep progress structured. Use when the user needs backlog control, task planning, or workflow coordination across projects.
version: "1.1"
updated: "2026-05-22"
assumes: "There is a backlog or set of projects that can be ranked and reviewed."
conflicts_with: "Do not replace behavior-design for habit formation or agent-teams-command for active multi-agent orchestration."
---

# Project Flow Operations

Keep execution structured and progress visible — triage, plan, track, and review across projects.

## Usage Template

**Prompt**
```text
Use project-flow-ops to triage this backlog. Rank priorities, identify blockers, and produce the next execution plan.
```

**Use Case**
- Turning scattered tasks or competing projects into a clear action queue.

**Expected Result**
- The agent returns prioritized work, blockers, next actions, and review cadence.

**Output Example**
- A ranked backlog with status, owner, next action, blocker, priority reason, and review date.

**Verification Case**
- Every top-priority item has an owner, next action, status, and reason for priority.

**Verified Effect**
- A messy backlog becomes a ranked execution queue with visible blockers and review cadence.

## Success Metrics

- Top-priority items each have owner, status, blocker, next action, and review date.
- Backlog is ranked with a reason for priority instead of only grouped by theme.
- Output identifies one immediate next action and one item to defer or drop.

## When to Use

- User says "what should I work on next?"
- Starting a new task or project
- Reviewing progress or blocked items
- User feels overwhelmed or unclear on priorities

## Workflow

### P1: Triage — What's Active?

Scan current state:

```
ACTIVE:   What's in progress now? (limit: 1-2)
BACKLOG:  What's waiting? (ordered by priority)
BLOCKED:  What's stuck and why?
COMPLETED: What's done since last review?
```

For each blocked item: identify the **one thing** that unblocks it.

### P2: Plan — What's Next?

Select the next task from the backlog with clear scope:

```
Task: [one-line description]
Why now: [urgency or opportunity]
Definition of done: [what "done" looks like]
Timebox: [max time to spend]
```

Rule: **One task at a time.** Context switching is the productivity killer.

### P3: Execute — Focus & Track

During execution:
- Break the task into ≤15 minute steps
- Verify after each step (verify-before-claim)
- Check in after timebox expires — extend or pivot

### P4: Review — Close & Learn

After completion:
- What did we learn?
- What should be documented? → wiki or SOP
- What's next?

## Priority Framework

| Priority | Criteria | Action |
|----------|----------|--------|
| 🔴 Critical | Blocks others, deadline imminent | Do now |
| 🟡 Important | Moves key metric, this week | Schedule today |
| 🟢 Normal | Valuable, no deadline | Backlog |
| ⚪ Low | Nice-to-have | Someday/maybe |

## Anti-patterns

- **Doing everything** — multitasking reduces throughput for everyone
- **Perfectionism** — done beats perfect for early-stage work
- **No timebox** — unbounded tasks expand to fill all available time

## Quality Gates

- [ ] Active items limited to 1-2
- [ ] Blocked items have an unblock action identified
- [ ] Next task has definition of done and timebox
- [ ] Completed items reviewed for documentation needs
- [ ] Priority labels applied
