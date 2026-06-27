---
name: loop-engineering
description: Turn a repeatable task into a bounded, evidence-driven agent loop. Use when Codex needs to decide whether a task merits looping, define a loop contract, choose single-agent versus maker-checker versus manager-workers topology, prevent runaway iteration, or repair a loop that stalls, self-grades, exceeds budget, or writes without verified evidence.
metadata:
  version: "6.0"
  updated: "2026-06-27"
  assumes: "The proposed task has a reachable local state, an inspectable output, and a feasible evidence source."
  conflicts_with: "Do not bypass explicit approval, sandbox, permission, or production controls imposed by harness-engineering, agentic-engineering, or agent-teams-command."
---

# Loop Engineering

Design a loop as a control system, not a repeated prompt. Its only valid form is:

```text
goal + state + tools + budget
            |
            v
plan -> act -> observe -> independently verify -> decide
  ^                                               |
  |---------------- continue / stop / escalate ---|
```

V6 shorthand: every loop must state `Trigger -> Execute -> Verify -> State`. If any field is vague, do a one-shot task or write a review item instead of starting a loop.

Use `scripts/validate_loop_contract.py` before starting a loop. Do not bypass a failed contract.

For a concrete pattern, see `references/ci-repair-loop-example.md`.

## Usage Template

```text
Use loop-engineering for this task.

Objective: [measurable outcome]
Scope: [owned files, systems, or outputs]
Evidence: [test, metric, fixture, review, or inspection]
Limits: [iterations, time, tool/token/request budget]
Permission boundary: [allowed writes and approval gates]
```

## Success Metrics

- A valid contract names the metric, independent verifier, finite caps, recovery path, and durable write-back.
- The selected topology is the lowest-complexity topology that can produce independent evidence.
- The final receipt distinguishes verified success, budget stop, stall, and blocked state.
- Scheduled knowledge loops distinguish unattended objective scans from supervised semantic writes.

## 1. Admit Or Reject The Loop

Use a loop only when the work is repeatable, the output can be checked, and each iteration can leave inspectable evidence.

| Situation | Default |
|---|---|
| One reversible edit or answer | Do the task once; do not create a loop. |
| Objective metric and cheap verification | Use a single-agent loop. |
| Builder cannot objectively verify its own output | Use maker-checker. |
| Independent workstreams with explicit file/output ownership | Use manager-workers with an integration gate. |
| Taste-only, ambiguous, irreversible, or production-changing task | Keep a human approval gate; do not run unattended. |

Reject a loop when its only stopping rule is “until satisfied,” “keep improving,” or “run forever.” Convert those requests into a metric, an acceptance fixture, a review queue, or a one-shot draft.

## 2. Create The Loop Contract

Create `.agent-state/loop-contract.md` or an equivalent durable state file before the first action. Use this exact shape:

```markdown
# Loop Contract

- Objective: Reduce the selected test suite's failures to zero.
- Scope: `packages/payments/**` and its tests only.
- Non-goals: No API redesign, dependency upgrades, or production deployment.
- Owner: Primary agent; checker owns verification only.
- Inputs: Failing test output and repository guidance files.
- State path: `.agent-state/payments-loop.md`.
- Success metric: Selected test command exits 0 with no skipped failures.
- Evidence: `pnpm test --filter payments` output and changed-file diff.
- Verifier: Independent test command plus a checker agent or reviewer.
- Topology: maker-checker.
- Max iterations: 5.
- Time limit: 45 minutes.
- Budget: 20 tool calls; stop before context or cost cap.
- Stop condition: Success metric passes, or any cap/stall condition fires.
- Write-back: Update `.agent-state/payments-loop.md` and the task log.
- Permission boundary: Local branch writes only; no push, merge, or production action.
- Recovery: Revert the last iteration if tests regress; escalate with evidence after two repeated failures.
```

For scheduled knowledge-management loops, add:

```markdown
- Trigger: Cron, automation, webhook, or daily note refresh.
- Execute: Objective scans, queue generation, dashboard refresh, or one supervised KR.
- Verify: Script receipt, lint report, link check, diff, or review receipt.
- State: Daily note, governance dashboard, backlog, log, or skill/SOP candidate.
- Automation boundary: No source-body mutation, concept merge/delete/rename, provenance invention, or semantic rule promotion without review.
```

Run:

```powershell
python scripts/validate_loop_contract.py .agent-state/loop-contract.md --strict
```

Treat a budget cap or stall condition as a controlled stop, not success.

## 2A. Calibrate The Verification Tier

Choose the cheapest verifier that still exercises the failure mode the loop could create. An LLM checker may interpret evidence, but for code, infrastructure, external systems, or durable wiki changes it cannot replace deterministic evidence.

| Loop risk | Minimum verifier |
|---|---|
| Draft, plan, rubric, or contract work | Fixture, checklist, schema, or reviewer inspection. |
| Local code or document transformation | Real local command, parser, linter, render, diff, or targeted test. |
| Concurrent repository writes | Isolated branch/worktree plus integration diff and tests. |
| External connector, scheduled, staging, or production-like loop | Explicit approval, rollback path, audit log, and telemetry or dry-run evidence. |

If no telemetry can reveal whether the loop helped, reject the loop or convert it into a one-shot draft with human review.

## 3. Run The Thin Loop

For each iteration:

1. Read only the contract, current state, last evidence, and minimum task context.
2. Plan one smallest reversible action that can affect the metric.
3. Act inside the contract's file, tool, and permission boundary.
4. Observe tool output, diffs, logs, tests, screenshots, or telemetry.
5. Have the declared verifier evaluate the evidence. The builder cannot be the sole verifier.
6. Record metric delta, changed files, evidence path, budget used, and next decision in state.
7. Stop, continue, or escalate according to the contract.

Keep context lean. Persist state and evidence in files rather than replaying a long chat transcript.

## 4. Select Topology Conservatively

| Topology | Use when | Required controls |
|---|---|---|
| Single-agent | One owner and an objective check exist. | External test/linter/fixture; finite budget. |
| Maker-checker | Generation and evaluation need separate judgment. | Checker has a separate prompt or tool evidence and cannot edit before reporting. |
| Manager-workers | Work decomposes into independent territories. | Per-worker ownership, branch/worktree isolation for concurrent repo writes, integration order, shared-state rule, and final evaluator. |

Do not use manager-workers merely to make a task feel more autonomous. Escalate to `agent-teams-command` when real multi-agent ownership, IPC, or integration work is required. Escalate to `harness-engineering` when permissions, credentials, scheduling, or production observability are the primary problem.

## 5. Stop, Recover, Or Escalate

Stop successfully only when the declared verifier accepts the declared evidence. Stop without success when a hard cap fires.

| Signal | Action |
|---|---|
| Success metric passes | Record proof, write back learning, stop. |
| Same failure twice | Stop editing that hypothesis; choose a different diagnosis or escalate. |
| No measurable progress for three iterations | Stop and request a human decision or redefine the metric. |
| Time, tool, token, or request cap reached | Preserve evidence and state; report budget stop. |
| Regression, permission denial, or shared-state conflict | Revert or isolate the last action; escalate with the receipt. |
| Change volume outpaces human comprehension | Stop for review, shrink scope, or add an architecture summary before continuing. |
| Need to push, merge, deploy, publish, pay, message, or mutate shared production state | Stop for explicit approval. |
| Scheduled loop wants to rewrite meaning from signal heat alone | Write a candidate to review queue; do not promote. |

## 6. Close The Memory Loop

At termination, write one compact receipt:

```markdown
Result: success | budget-stop | stalled | blocked
Metric: before -> after
Evidence: command, output path, screenshot, or diff
Iterations: N / cap
Changes: files or external actions
Residual risk: what remains unverified
Next action: only if not successful
```

Promote reusable constraints to a project `AGENTS.md`, SOP, or related skill. Do not promote an unverified heuristic as a rule.

## Quality Gates

- [ ] Contract passes `validate_loop_contract.py --strict` before execution.
- [ ] Success metric and stop condition are separately stated.
- [ ] Verifier is independent from the builder or backed by external evidence.
- [ ] Iteration, time, and tool/token/request budgets are finite.
- [ ] State, evidence, and write-back paths are durable and explicit.
- [ ] Production or external mutations have approval, rollback, and audit boundaries.
- [ ] Multi-agent use has independent ownership and an integration gate.
- [ ] Completion claim cites fresh verifier evidence; budget stop never masquerades as success.
- [ ] V6 loop form states Trigger, Execute, Verify, and State, with unattended vs supervised actions separated.

## Anti-Patterns

- Letting the builder score itself and treating that score as proof.
- Treating maker-checker agreement as proof when no deterministic evidence was run.
- Adding more agents before the task, metric, or ownership is clear.
- Treating “no errors observed” as success without a declared check.
- Carrying state only in chat memory.
- Running a scheduled or production loop without caps, rollback, and anomaly escalation.
- Repeating the same failed hypothesis without changing evidence or diagnosis.
