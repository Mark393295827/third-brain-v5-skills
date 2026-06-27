# Ender-Palantir Command Patterns

Use this reference when a multi-agent project needs durable state, messy workflow discovery, long-running coordination, or feedback-driven improvement.

## Source Boundary

This pattern is promoted from durable Obsidian pages, not from a single clipping:

- `wiki/concepts/Claude Code Agent Teams 操作指南.md`
- `wiki/outputs/enders-game-commander-training-framework.md`
- `sources/2026-05-09-enders-game-trilogy.md`
- `wiki/entities/Palantir.md`
- `wiki/concepts/数据本体论 Data Ontology.md`
- `wiki/concepts/智能体前线部署工程师.md`
- `wiki/concepts/智能体协调器 Agentic Orchestrator.md`
- `wiki/concepts/评估驱动开发.md`

Do not promote source-specific military, investment, or vendor claims into a project rule unless independently verified.

## Ender Safety Translation

Reusable:

- Give the commander strategic choices, not every tactical instruction.
- Empower team leads and squad owners with clear territories.
- Train through bounded scenarios, immediate feedback, and after-action review.
- Use asymmetric tactics: maker-checker, red-team review, and parallel reconnaissance.
- Understand the opponent, user, bug, or market before trying to overpower it.

Forbidden:

- Hidden real-world consequences.
- Manipulative isolation or no-rest pressure.
- "Win at any cost" goals.
- Psychological stress as a management tool.
- Treating victory as correctness without moral or operational review.

## Ontology Command Board

Represent the team as objects and actions, not chat only.

```markdown
# Command Board

Mission:
  id:
  objective:
  non_goals:
  commander:
  review_budget:
  permission_boundary:

Workstreams:
  - id:
    owner:
    territory:
    inputs:
    allowed_actions:
    denied_actions:
    dependencies:
    verifier:
    stop_condition:

Evidence:
  - id:
    workstream:
    path_or_command:
    result:
    timestamp:

Feedback:
  - id:
    source: operator | reviewer | user | test | telemetry
    correction:
    specificity: high | medium | low
    becomes: eval_case | review_item | contract_update | backlog

Decisions:
  - id:
    decision:
    basis:
    owner:
    rollback:
```

Minimum verbs:

- `claim territory`
- `request input`
- `handoff`
- `verify`
- `reject`
- `integrate`
- `rollback`
- `close`

## Data-Logic-Action Mapping

Before launch, map the team plan:

| Palantir layer | Agent team equivalent |
|---|---|
| Data | Mission, files, source notes, user workflow, artifacts, logs, evidence. |
| Logic | Ownership rules, dependency graph, evaluator, eval suite, decision policy. |
| Action | Tool calls, file edits, messages, PRs, deployments, wiki writes. |
| Feedback | Operator corrections, review comments, test failures, telemetry, user rejects. |

No teammate should act on a domain object it cannot name, verify, and write back.

## FDE Reconnaissance

Use before building in messy enterprise, workflow, ops, customer, compliance, or domain-specific systems.

```text
FDE RECON:
Real workflow observed:
Operator roles:
Systems touched:
Permissions and audit boundary:
Exceptions and edge cases:
Current friction:
Hidden manual step:
Existing artifact/log/source of truth:
Gravel-road artifact to ship first:
Paved-path abstraction candidate:
```

Rule: do not abstract a platform rule from one customer, one workflow, or one demo. First ship a narrow artifact, collect feedback, then decide what generalizes.

## EDD Integration Gate

For each workstream:

```text
Baseline:
Eval suite or fixture:
Grader:
Pass threshold:
Failure triage:
Allowed repair action:
Regression check:
Feedback-to-eval path:
```

Eyeballing a demo is not enough for integration. If feedback is vague, assign a feedback-quality agent to ask for concrete examples and convert them into eval cases or review items.

## Long-Running Orchestrator State

Use when the team may run across hours, days, external approvals, or multiple sessions:

```text
Checkpoint path:
Await condition:
Resume trigger:
Trace/log path:
Human task object:
Timeout:
Retry scope:
Abort condition:
```

Retry the failed step, not the whole mission. Preserve prompt, tool output, artifact path, and decision basis so the team can resume without replaying chat.
