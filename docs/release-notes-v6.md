# Third Brain V6 Release Notes

Third Brain V6 turns the V5 knowledge pipeline into a knowledge operating system for agents. The upgrade is grounded in the Obsidian vault's recent Agent/Wiki flywheel, daily knowledge loop, Loop Programming, AI Agent Harness, Claude Code extensibility, and multi-agent orchestration notes.

## What Changed

- `input-skills-obsidian` is promoted from a fast STOW importer to the front door of the V6 knowledge OS: every ingest now has trigger, context, steering, verification, and write-back boundaries.
- `wiki-ingest`, `knowledge-ops`, and `wiki-lint` now share the same provenance contract: Markdown first, immutable sources, block refs, clipping lifecycle, review queues, and objective health checks.
- `agentic-engineering`, `loop-engineering`, `harness-engineering`, and `agent-teams-command` now use the V6 loop contract: Trigger -> Execute -> Verify -> State, with hard budgets, independent evidence, recovery, and durable write-back.
- Scheduled knowledge management is a first-class consumer of the system: daily loops can run health scans, Agent/Wiki flywheel scans, queue reports, and daily notes, but semantic writes stay supervised.
- Context management is now a zero-overhead default: hot paths load only task-local rules; cold paths live in reports, backlogs, maps, and wiki pages until needed.

## V6 Operating Model

```text
Input
  -> Source note
  -> Concept/entity compile
  -> Maps and dashboards
  -> Daily loop
  -> Agent/Wiki flywheel
  -> Skill/SOP/schema upgrade
  -> Verification and review queue
```

## Promotion Gates

Promote a wiki insight into a skill, SOP, schema rule, or automation only when all are true:

- It is supported by at least two durable wiki/source pages, or one high-quality source plus local verification.
- It can be expressed as a bounded macro action with input, output, verifier, budget, stop condition, and write-back target.
- It does not relax source immutability, provenance, permissions, or human review boundaries.
- It has a cheap check: lint, script output, link check, test, dashboard metric, or review receipt.

## Upgrade Notes

- Existing V5 vault pages remain valid. V6 adds stricter promotion and automation boundaries rather than changing historical source notes.
- Historical structure debt should stay in lint reports or review queues. Do not rewrite the whole vault only to satisfy V6 metadata.
- For active use, install or copy updated skills from `skills/` into the target agent's native skill directory after review.
