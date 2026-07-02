---
tags: [domain/agent-systems, type/concept]
type: concept
status: seed
created: 2026-06-25
updated: 2026-06-28
knowledge_stage: stored
evidence_level: single-source
---

# Closed-Loop Agent Control

> Closed-loop agent control treats an agent loop as a measured control system: define the setpoint, observe telemetry, compute the error, act inside bounds, verify independently, and write back state.
> (Source: [[src-20260625-loop-engineering-overview#^ki-closed-loop-control]]) WARNING: Single source

Primary-source check on 2026-06-28 supports the component practices behind this page, not the full control-theory analogy as a proven research claim. Keep `evidence_level: single-source` until separate control-system sources are ingested.

## Core Mechanism

```text
Setpoint / success metric
        |
        v
Observe current state -> compute error signal -> choose bounded actuator
        ^                                                |
        |                                                v
Write back state <- independent verifier <- changed system/output
```

The useful shift is from "keep trying" to "reduce a declared error signal." In `skills/loop-engineering`, the contract's objective and success metric define the setpoint; tests, logs, diffs, screenshots, or telemetry define observations; the next edit/tool call is the actuator; and the state file preserves the controller's memory. This is a local operating analogy, not evidence that agent loops have the guarantees of engineered control systems. (Source: [[src-20260625-loop-engineering-overview#^ki-closed-loop-control]]) WARNING: Single source

## Classifications / Comparisons

| Control-system term | Agent-loop equivalent | Failure if missing |
|---|---|---|
| Setpoint | Objective and success metric | Loop drifts into "keep improving" |
| Telemetry | Test output, lint output, fixture result, screenshot, metric, or log | Agent cannot see whether the action helped |
| Error signal | Measured gap between current state and success metric | Iterations become activity, not control |
| Actuator | Edit, command, tool call, queue update, rollback, or escalation | No controlled way to affect the metric |
| Verifier | Deterministic check or independent reviewer backed by evidence | Maker-checker agreement becomes false proof |
| Write-back | State file, task log, SOP, test, or wiki update | The loop relearns the same lesson each run |

## Verification Ladder

| Tier | Agent-loop translation | Use when |
|---|---|---|
| Model-in-the-loop | Mock, fixture, synthetic input, dry-run, or rubric-only review | Low-risk design, prompt, or contract work |
| Software-in-the-loop | Real code in an isolated branch/worktree with local tests | Implementation work before shared-state mutation |
| Hardware-in-the-loop | Staging, production-like integration, external telemetry, or real connector dry-run | External systems, scheduled loops, or safety-sensitive workflows |

This ladder does not prove safety by analogy. It gives the loop designer a practical question: what is the cheapest verifier that still exercises the failure mode the loop could create? (Source: [[src-20260625-loop-engineering-overview#^ki-validation-ladder]], [[src-20260625-loop-engineering-overview#^ki-deterministic-verifier-tier]]) WARNING: Single source

## Primary-Source Check

| Claim family | Status | Evidence boundary |
|---|---|---|
| Loop-engineering primitives | Supported as practitioner/vendor claims | Addy Osmani describes loops built from scheduled automations, worktrees, skills, connectors, sub-agents, and external state; TrueFoundry repeats that anatomy for governed runtimes. This supports using those primitives, not treating every product-specific capability as stable across tools. |
| Deterministic verifier tier | Supported for code-loop governance | Sonar argues that LLM verifier sub-agents are probabilistic/advisory and deterministic checks should be the hard stop for code correctness, security, maintainability, and conformance. This supports the skill's deterministic-evidence guardrail. |
| MIL/SIL/HIL verifier ladder | Supported only as an analogy | MathWorks defines MIL, SIL, PIL, and HIL as embedded-system verification techniques with different fidelities; Ansys defines HIL as real control software/hardware connected to simulated sensors, actuators, or plant behavior. This supports borrowing the ladder vocabulary, not claiming AI-agent safety certification. |
| Closed-loop control-system mapping | Partially supported, still local synthesis | The cited HIL pages describe closed-loop simulation, but none of the checked sources independently prove the wiki's full setpoint/telemetry/error/actuator/write-back mapping for AI agents. |

## Implications / Applications

- Use [[ooda-friction-minimization-loop|OODA friction minimization]] to keep each iteration small, but use closed-loop control to decide whether the observed error actually shrank.
- Use [[agent-understanding-framework|Agent Understanding Framework]] for write-back: if the loop only changes files without preserving evidence or a reusable rule, it has no compounding memory.
- Add a human-review threshold when changed surface area, architectural impact, permission scope, or external effects exceed what the operator can inspect. Passing tests can coexist with comprehension debt. (Source: [[src-20260625-loop-engineering-overview#^ki-comprehension-debt]]) WARNING: Single source

## Source Boundary

This page imports only the agent-loop operating insight from the Google Doc. It does not validate the Doc's thermodynamic, biochemical, corporate, broad historical, or formal control-theory claims. The MIL/SIL/HIL mapping is an analogy for verifier maturity, not a certification model for AI-agent safety.

## Connections

- [[ooda-friction-minimization-loop|OODA friction minimization loop]]: a neighboring iteration model focused on reducing observation, orientation, decision, and action friction.
- [[agent-understanding-framework|Agent Understanding Framework]]: explains why loop evidence should be written back into durable memory.
- [[src-20260625-loop-engineering-overview|Loop Engineering Overview source note]]: imported source and block references.

---

## 演化时间线

- **2026-06-25**: Created from the imported Google Doc `Loop Engineering Overview`, focusing only on concepts that sharpen `skills/loop-engineering`.
- **2026-06-28**: Checked the cited Addy Osmani, Sonar, TrueFoundry, Ansys, and MathWorks pages against primary sources; kept evidence level as `single-source` and tightened unsupported analogy boundaries.

