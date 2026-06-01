# Workflow: Deep Research to STOW Handoff

## Before

A broad question needs evidence from multiple sources, but the result should not become an untraceable chat summary.

## Input

```text
Question: a market, technical, policy, competitor, or fast-changing research question.
Goal: produce a cited research report plus a STOW handoff packet for durable wiki ingest.
```

## Prompt

```text
Use deep-research on this question:
[paste question]

Run the ChatGPT-style preflight first:
- desired outcome
- source access and excluded sources
- privacy risk
- budget / depth
- plan-review status

Then produce:
1. source ledger with dates checked
2. claim ledger with evidence, counterevidence, confidence, and implication
3. activity trace of searches/source groups/tools/skipped paths
4. cited synthesis with disagreements and gaps
5. STOW handoff packet for wiki-ingest
```

## After

The research result becomes:

- one cited report in `OUTPUTS_DIR` when durable
- a source-access boundary and privacy note
- a source ledger and claim ledger
- an activity trace that makes the report auditable
- a STOW handoff packet for follow-up `wiki-ingest`

## Output Example

```text
OUTPUTS_DIR/2026-06-01-ai-agent-market-brief.md

STOW handoff:
Source candidates:
Concept pages to create/update:
Entity pages to create/update:
Key claims needing block refs:
Single-source warnings:
Contradictions:
Governance risks:
Recommended wiki-ingest next action:
```

## Verification

The workflow is complete only after the agent satisfies the `deep-research` quality gates: preflight, source boundary, source ledger, claim ledger, STOW mapping, activity trace, citations, confidence markers, and privacy checks when relevant.
