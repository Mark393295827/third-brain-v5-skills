---
title: "ChatGPT Deep Research vs STOW Comparison"
type: research-output
created: "2026-06-01"
evidence_level: official-docs
related_skill: deep-research
---

# ChatGPT Deep Research vs STOW Comparison

## Question

How should Third Brain `deep-research` improve after testing it against ChatGPT Deep Research behavior and the local STOW pipeline?

## Sources Checked

| Source | Type | Checked | Use |
|---|---|---:|---|
| https://help.openai.com/en/articles/10500283-deep-research-in-chatgpt | OpenAI Help Center | 2026-06-01 | ChatGPT UI behavior: plan review, source selection, progress, citations, report view |
| https://developers.openai.com/api/docs/guides/deep-research | OpenAI API docs | 2026-06-01 | Developer behavior: data-source requirements, tool-call trace, background mode, safety controls |
| `CLAUDE.md` | Local repo rule | 2026-06-01 | STOW definition: Source -> Think -> Organize -> Write |
| `skills/wiki-ingest/SKILL.md` | Local repo skill | 2026-06-01 | Immutable sources, block refs, understanding gate, post-ingest lint |
| `skills/deep-research/SKILL.md` | Local repo skill | 2026-06-01 | Baseline research workflow under test |

## Test Matrix

| Capability | ChatGPT Deep Research | STOW requirement | Previous `deep-research` | Improvement needed |
|---|---|---|---|---|
| Plan review | Proposed plan can be reviewed/modified before start | Think before writing | Partial scope definition | Add explicit plan-review checkpoint |
| Source control | Public web, files, apps, specific sites | Source boundary and provenance | Source types listed | Add source-access boundary and excluded sources |
| Progress trace | Activity history and progress | Verify how output was made | Missing | Add activity trace |
| Citation review | Citations/source links and sources used | Source refs and confidence | Present but generic | Add source-used section and date checked |
| Long run control | Background mode, timeouts, max tool calls | Budgeted agent loop | Depth budget only | Add time/tool-call budget fields |
| Private data safety | Read-only apps, staged workflows, logging, prompt-injection controls | Governance risk and provenance | Missing | Add private-data safety gate |
| Durable write-back | Downloadable reports | Write to wiki outputs or ingest queue | Optional output | Add STOW handoff packet |

## Findings

1. The local skill already has better epistemic structure than a generic research prompt: modes, ledgers, claim confidence, and Heavy mode.
2. It was weaker than ChatGPT Deep Research on execution observability: no required activity history, source-access plan, or progress trace.
3. It was weaker than STOW on durable handoff: it could produce a report, but did not define the Source -> Think -> Organize -> Write packet that `wiki-ingest` can preserve.
4. The highest-risk gap was private-data handling. Deep research over connected apps, MCP, file search, and public web needs staged execution and exfiltration checks.

## Decision

Upgrade `deep-research` into a STOW-compatible research harness:

- Source: define source access, date windows, source ledger, and read-only/private data constraints.
- Think: require clarification, prompt rewriting, research plan review, and claim ledger.
- Organize: require outline, table of contents, sources used, and activity trace.
- Write: produce cited report plus a STOW handoff packet when the result should enter the wiki.

## Verification

The skill update should pass `python tools/lint-agent-skills.py` and preserve `deep-research` vs `wiki-ingest` boundaries.
