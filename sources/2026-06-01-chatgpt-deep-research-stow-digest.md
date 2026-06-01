---
source_title: "ChatGPT Deep Research STOW Comparison Digest"
source_date: 2026-06-01
source_type: official-docs-comparison
input_class: external-fact
evidence_level: official-docs
related_skill: deep-research
repo_scope:
  - skills/deep-research/SKILL.md
official_sources:
  - https://help.openai.com/en/articles/10500283-deep-research-in-chatgpt
  - https://developers.openai.com/api/docs/guides/deep-research
---

# ChatGPT Deep Research STOW Comparison Digest

## Inputs

- OpenAI Help Center: `Deep research in ChatGPT`, checked 2026-06-01.
- OpenAI API docs: `Deep research`, checked 2026-06-01.
- Local STOW contract: `Source -> Think -> Organize -> Write` from `CLAUDE.md` and `wiki-ingest`.
- Local skill under test: `skills/deep-research/SKILL.md`.

## Verified OpenAI Patterns

OpenAI's ChatGPT deep research flow includes these product-level behaviors:

- User describes the outcome, then chooses source access across public web, uploaded files, specific sites, and connected apps.
- ChatGPT proposes a research plan that the user can review or modify before execution.
- Users can follow progress, interrupt the run, adjust focus, and change source access while it is running.
- Final reports include citations or source links, a table of contents, sources used, and activity history.
- Connected apps are read-only for deep research.

OpenAI's API docs add these developer-facing patterns:

- Deep research models require at least one data source: web search, file search/vector store, or remote MCP.
- Output arrays expose intermediate actions such as web search calls, code interpreter calls, MCP calls, file search calls, and final cited messages.
- Long-running tasks should use background mode or higher timeouts; `max_tool_calls` can constrain cost and latency.
- ChatGPT UI performs clarification and prompt rewriting before research; the API does not, so developers must implement that step.
- Supported tools are search/browse sources and code interpreter; arbitrary function calling is not supported for deep research models.
- Private-data workflows need prompt-injection and exfiltration controls, trusted MCP/file sources, tool-call logging, staged public/private phases, and link screening.

## STOW Delta

| STOW stage | ChatGPT deep research behavior | Local skill gap before update |
|---|---|---|
| Source | User-controlled sources, specific sites, uploads, connected apps, source links | Source ledger existed, but source access boundary and read-only/private-data rules were weak |
| Think | Clarification, prompt rewriting, research plan review | Scope definition existed, but no explicit plan-review checkpoint |
| Organize | Table of contents, sources used, activity history | Outline-first existed, but no required activity trace |
| Write | Structured report with citations and exports | Report shape existed, but STOW handoff to wiki-ingest was not explicit |

## Repo Translation

- Add a ChatGPT-style preflight: outcome, source boundary, source access, privacy risk, plan review, budget/timebox.
- Add STOW mapping to `deep-research`: Source ledger, Think tree, Organize outline/activity trace, Write report/handoff.
- Add activity trace as required evidence for standard and deep work.
- Add private-data safety: read-only sources, public/private phase separation, prompt-injection and exfiltration checks.
- Add verification tests that compare outputs against STOW and ChatGPT deep research behaviors.

## Verification Expectations

- `python tools/lint-agent-skills.py` passes.
- `deep-research` retains its conflict boundary with `wiki-ingest`: it can create research outputs and handoff packets, but immutable source-note creation remains `wiki-ingest` territory.
