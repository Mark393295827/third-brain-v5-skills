---
title: "Lint Report"
type: system
updated: "2026-06-28"
---

# Lint Report - 2026-06-28

## Targeted Check: Loop Engineering Overview Primary-Source Verification

| Check | Result | Evidence |
|---|---|---|
| Addy Osmani source checked | Pass | Primary page supports loop anatomy, external state, maker/checker split, and human verification/comprehension warnings |
| Sonar source checked | Pass | Primary page supports two-tier verification and deterministic checks as the hard stop for code loops |
| TrueFoundry source checked | Pass | Primary page supports governed runtime concerns: scoped identity, human gates, budgets, guardrails, durable state, and traces |
| Ansys source checked | Pass | Primary page supports HIL as real control software/hardware connected to simulated sensors, actuators, or plant behavior |
| MathWorks source checked | Pass | Primary page supports MIL/SIL/PIL/HIL as distinct embedded-system verification techniques with different fidelity |
| Source boundary preserved | Pass | Source body remains an immutable capture; governance notes record verification scope and remaining unsupported boundaries |
| Concept evidence level | Pass | `wiki/concepts/closed-loop-agent-control.md` remains `single-source`; unsupported control-theory and safety inheritance claims are explicit |
| Skill wording | Pass | `skills/loop-engineering/SKILL.md` now states the control-system and MIL/SIL/HIL vocabulary is an analogy, not a safety proof |

## Targeted Check: Loop Engineering Overview Import

| Check | Result | Evidence |
|---|---|---|
| Source artifact exists | Pass | `sources/src-20260625-loop-engineering-overview.md` |
| Source frontmatter present | Pass | Includes `source_id`, `source_date`, `source_title`, `source_url`, `hash`, `trust_level`, and `status` |
| Block refs resolve | Pass | `^ki-closed-loop-control`, `^ki-deterministic-verifier-tier`, `^ki-validation-ladder`, `^ki-isolated-state`, `^ki-comprehension-debt` |
| Concept frontmatter present | Pass | `wiki/concepts/closed-loop-agent-control.md` |
| Concept outbound links | Pass | Links to source note, `ooda-friction-minimization-loop`, and `agent-understanding-framework` |
| Navigation inlink | Pass | `wiki/index.md` links to `closed-loop-agent-control` and the source note |
| Skill format lint | Pass | `python tools/lint-agent-skills.py` passed for 19 skills |
| Loop contract validation | Pass | `python skills/loop-engineering/scripts/validate_loop_contract.py skills/loop-engineering/references/ci-repair-loop-example.md --strict` |

## Issues Found

| Type | Count | Severity |
|---|---:|---|
| P0 broken source refs in touched files | 0 | P0 |
| P0 missing frontmatter in touched wiki pages | 0 | P0 |
| P1 missing navigation for new concept | 0 | P1 |
| P1 skill contract failure | 0 | P1 |

## Requires Human Review

| Page | Issue | Suggested Action |
|---|---|---|
| `sources/src-20260625-loop-engineering-overview.md` | Imported Google Doc remains single-source synthesis despite cited primary-source spot check | Ingest separate control-system sources before promoting the closed-loop-control analogy as anything stronger than a practical agent-loop frame |
| `sources/src-20260625-loop-engineering-overview.md` | Broad thermodynamic, biochemical, corporate, and historical claims remain outside the verified subset | Do not reuse those claims operationally without a separate source/claim ledger |

Historical wiki health outside this ingest was not re-audited in this targeted pass.
