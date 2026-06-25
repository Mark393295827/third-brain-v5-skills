# Worked Example: CI Repair Loop

Use this as a copyable companion when a repository has a repeatable CI failure and the agent needs bounded autonomy. It demonstrates the minimum contract, state ledger, verifier tier, and final receipt expected by `loop-engineering`.

## Admission Decision

| Question | Answer |
|---|---|
| Repeatable task? | Yes. CI fails on the same package and can be rerun locally. |
| Inspectable output? | Yes. Test output, lint output, and diff are available. |
| Independent verifier? | Yes. The local test command and lint command are deterministic evidence. A checker may interpret results but cannot replace them. |
| External mutation? | No push, merge, deploy, issue update, or production action without explicit approval. |
| Topology | Maker-checker only if diagnosis is ambiguous; otherwise single-agent with external tests. |

## Loop Contract

```markdown
# Loop Contract

- Objective: Make `packages/billing` CI pass for the failing checkout.
- Scope: `packages/billing/**`, `packages/billing/package.json`, and directly related tests only.
- Non-goals: No dependency upgrades, API redesign, formatting churn, or production deployment.
- Owner: Primary agent; checker may review evidence but cannot edit before reporting.
- Inputs: CI failure log, repository guidance files, and current failing test output.
- State path: `.agent-state/billing-ci-loop.md`.
- Success metric: `pnpm --filter billing test` and `pnpm --filter billing lint` both exit 0.
- Evidence: Fresh command output plus changed-file diff after each iteration.
- Verifier: Deterministic local commands; checker agent may inspect the output and diff.
- Topology: single-agent.
- Max iterations: 4.
- Time limit: 35 minutes.
- Budget: 18 tool calls.
- Stop condition: Both verifier commands pass, or an iteration/time/tool cap fires, or the same failure appears twice without a new diagnosis.
- Write-back: Update `.agent-state/billing-ci-loop.md` with diagnosis, action, metric delta, and next decision.
- Permission boundary: Local branch writes only; no push, merge, deploy, external issue update, or shared-state mutation.
- Recovery: Revert the last edit if either verifier regresses; escalate with logs after two repeated failures.
```

Validate before acting:

```powershell
python skills/loop-engineering/scripts/validate_loop_contract.py .agent-state/loop-contract.md --strict
```

## Verification Tier

| Tier | Concrete verifier |
|---|---|
| Fixture/model tier | Reproduce the failing test with the smallest local command. |
| Software tier | Run the real package test and lint command in the current branch/worktree. |
| Integration tier | Only request staging, CI rerun, push, or PR after local evidence passes and the user approves the external action. |

## State Ledger Shape

```markdown
# Billing CI Loop State

## Iteration 1

- Hypothesis: Validation helper accepts `undefined` but the test now expects an explicit null check.
- Action: Add a guard in `packages/billing/src/validate.ts` and one regression test.
- Evidence:
  - Before: `pnpm --filter billing test` failed 1 test in `validate.test.ts`.
  - After: `pnpm --filter billing test` passed; lint not yet run.
- Changed files:
  - `packages/billing/src/validate.ts`
  - `packages/billing/src/validate.test.ts`
- Decision: Continue to lint because the success metric has two commands.
- Budget used: 5 / 18 tool calls, 1 / 4 iterations.
```

## Final Receipt Example

```markdown
Result: success
Metric: test failed 1 -> test passed 42; lint passed 0 errors
Evidence: `pnpm --filter billing test`; `pnpm --filter billing lint`; final diff
Iterations: 2 / 4
Changes: validation guard plus regression test in `packages/billing`
Residual risk: only package-local checks ran; full monorepo CI not rerun
Next action: request approval before pushing or opening a PR
```

## Common Stops

| Signal | Receipt wording |
|---|---|
| Same failure twice | `Result: stalled`; include both logs and the abandoned hypothesis. |
| Local pass but full CI unknown | `Result: locally verified`; do not claim CI is fixed until CI evidence exists. |
| Diff grows beyond review budget | `Result: stopped for review`; include the changed-file count and risky areas. |
| Need to push or rerun hosted CI | Stop and ask for explicit approval with the local evidence attached. |

