---
source_id: "src-20260625-loop-engineering-overview"
source_date: "2026-06-17"
source_title: "Loop Engineering Overview"
source_author: ""
source_type: "local-synthesis"
source_url: "https://docs.google.com/document/d/1jY5vTvjDbJF9Q0OIXnKIOs8yucDMIAdL07vGnClYfTg"
input_class: "external-fact"
created: "2026-06-25"
knowledge_stage: captured
evidence_level: "single-source"
trust_level: "1-unverified"
hash: "sha256-92c1ebc1adcbe3a2"
status: "ingested"
repo_scope:
  - skills/loop-engineering/SKILL.md
  - skills/loop-engineering/references/ci-repair-loop-example.md
  - wiki/concepts/closed-loop-agent-control.md
---

# Loop Engineering Overview

## Source Boundary

Imported from the user's Google Doc `Loop Engineering Overview`, exported as Markdown on 2026-06-25 and hashed as `92c1ebc1adcbe3a21fef0972af828220cd23cd435d1afba90e07852a96ae1253`.

This is a useful local synthesis, not an independently verified research bundle. Treat product, vendor, historical, thermodynamic, biochemical, and company-specific claims as single-source until checked with primary sources. Only the agent-loop operating lessons below were promoted into `skills/loop-engineering`.

## Key Insights

### Closed-loop control is the sharper mental model for agent loops

A loop should be designed like a control system: a goal/setpoint, observable telemetry, an error signal, a bounded actuator, verification, and write-back. This sharpens `loop-engineering` by making each iteration answer one question: what measured gap still remains between the current state and the desired state? ^ki-closed-loop-control

> [!warning] Single source
> The control-theory translation comes from the imported Google Doc and should be treated as a local synthesis until source 19 and related control-system references are independently checked.

### Verifier maturity matters more than another LLM opinion

The Doc's strongest practical warning is the premature-completion loop: a maker and checker can agree that work is complete while subtle defects remain. For code and infrastructure loops, an LLM checker can interpret evidence, but it should not replace a deterministic verifier such as a targeted test, typecheck, lint run, fixture replay, staging check, or monitored telemetry threshold. ^ki-deterministic-verifier-tier

> [!warning] Single source
> The imported Doc cites Sonar and managed-runtime sources for this claim, but this note has not independently verified those sources.

### Simulation ladders map cleanly onto agent-loop risk

The Model-in-the-Loop / Software-in-the-Loop / Hardware-in-the-Loop ladder suggests an agent-loop verifier ladder: use cheap mocked or fixture checks for low-risk design work, real code in an isolated worktree for implementation loops, and staging or production-like telemetry only when external systems are involved and explicit approval/rollback exists. ^ki-validation-ladder

> [!warning] Single source
> The HIL analogy is useful as a design pattern, not proof that AI-agent loops inherit safety properties from cyber-physical testing.

### Isolation plus external state is the minimum for concurrent loops

Parallel or scheduled loops need isolated workspaces and durable state. Worktrees/branches prevent file collisions, while state files record attempted hypotheses, failed checks, remaining tasks, and restart context. This extends the existing `loop-engineering` state requirement to concurrent repo writes. ^ki-isolated-state

> [!warning] Single source
> The repo already had durable state guidance; only the worktree/isolation emphasis was imported.

### Human comprehension is a safety budget

Passing tests can outpace human understanding. A loop that changes many files, architecture, permissions, or external behavior can create comprehension debt even when the verifier passes. The loop contract should have a review trigger when changed surface area exceeds the operator's ability to inspect the result. ^ki-comprehension-debt

> [!warning] Single source
> This is a governance heuristic extracted from the Doc, not a measured threshold.

## Skill Translation

- Add a compact verifier-tier rule to `skills/loop-engineering`: LLM checker agreement is not enough for code/infrastructure loops unless backed by deterministic evidence.
- Add a worked CI repair example that shows the contract, state ledger, verification ladder, and receipt in one usable companion doc.
- Add a comprehension-debt stop signal so success is not reduced to "tests passed" when the loop changes too much for human review.
- Do not import the Doc's broad thermodynamic, biochemical, or corporate-company material into the skill; those analogies do not directly improve the agent-loop operating contract.

## Imported Works-Cited Subset

- Addy Osmani, "Loop Engineering": `https://addyosmani.com/blog/loop-engineering/`
- Sonar, "Loop engineering without verification is just automation": `https://www.sonarsource.com/blog/loop-engineering-without-verification-is-just-automation/`
- TrueFoundry, "Loop Engineering at Enterprise Grade": `https://www.truefoundry.com/blog/loop-engineering-enterprise-agent-runtime`
- Ansys, "What is Hardware-in-the-Loop Testing?": `https://www.ansys.com/simulation-topics/what-is-hardware-in-the-loop-testing`
- MathWorks, "What Is Hardware-in-the-Loop (HIL)?": `https://www.mathworks.com/discovery/hardware-in-the-loop-hil.html`

## Governance Notes

- Evidence level remains `single-source` for the imported Google Doc and the promoted local synthesis. The cited primary-source subset was checked on 2026-06-28, but the source note itself is still an immutable capture rather than a reauthored research brief.
- No source-file mutation should happen after this ingest unless the user requests a source correction.
- Primary-source check: Addy Osmani supports the loop-engineering anatomy of automations, worktrees, skills, connectors, sub-agents, and external state, plus the warnings that verification and comprehension remain human responsibilities. Sonar supports the two-tier verification claim: LLM review is advisory/probabilistic, while deterministic checks are the hard gate for code loops. TrueFoundry supports the governed-runtime translation: scoped identities, human approval gates, budgets, guardrails, durable state, and run traces. Ansys and MathWorks support HIL and MIL/SIL/PIL/HIL definitions for embedded-system validation.
- Remaining boundary: these sources do not prove that AI-agent loops inherit safety properties from HIL, and they do not independently validate the Google Doc's broader thermodynamic, biochemical, corporate, or formal control-theory claims. Treat the closed-loop-control mapping as a practical agent-loop analogy until separate control-system sources are ingested.

