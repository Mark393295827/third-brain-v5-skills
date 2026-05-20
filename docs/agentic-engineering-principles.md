# Agentic Engineering Principles

This standard translates the Obsidian note `wiki/concepts/Agentic Engineering`
into operating rules for Third Brain V5 Skills.

## Doctrine

Agentic Engineering is not faster prompting. It is the discipline of coordinating
fallible but powerful AI agents so delivery speed rises while the quality ceiling
does not fall.

Use this distinction:

| Mode | Optimizes for | Failure mode |
|---|---|---|
| Vibe coding | Accessibility and speed | Fast output without durable quality gates |
| Agentic engineering | Speed plus professional quality | Over-orchestration if specs and evals are weak |

## Five Practices

1. **Spec-driven development**: convert intent into a concrete spec before broad execution.
2. **Verification-first work**: define proof before claiming success.
3. **Macro action orchestration**: delegate features, research, plans, and verification as bounded agent jobs.
4. **Security-aware integration**: red-team high-risk outputs before release.
5. **Closed-loop optimization**: use cheap objective metrics when the task can be evaluated repeatedly.

## Macro Action Contract

Use this contract before assigning an agent or skill a large unit of work:

```text
Objective:
Scope:
Non-goals:
Inputs:
Owned files or territory:
Expected output:
Verification evidence:
Security/risk review:
Write-back destination:
Stop condition:
```

If any field is missing, shrink the macro action until it can be verified.

## Quality Ceiling Gates

Every agentic workflow should answer:

- What professional standard must not drop?
- What evidence proves the standard was met?
- Which failures require a critic, evaluator, or adversarial agent?
- Which outputs need human judgment for taste, architecture, or risk?
- Where is reusable learning written back?

## AutoResearch Boundary

Use autonomous iteration only when all three are true:

- The task has an objective metric.
- The metric is cheap enough to run many times.
- The search space is bounded by safety, cost, and time limits.

When any condition is false, use a supervised loop with explicit review gates.

## Skill Mapping

| Skill | Agentic role |
|---|---|
| `agentic-engineering` | Convert workflows into specs, macro actions, loops, and gates. |
| `harness-engineering` | Provide runtime permissions, observability, security, and recovery. |
| `agent-teams-command` | Coordinate parallel agents with ownership, IPC, joins, and cleanup. |
| `verify-before-claim` | Enforce proof before completion claims. |
| `session-learn` | Capture reusable learning after each loop. |
