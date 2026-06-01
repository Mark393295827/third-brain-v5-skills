---
source_title: "GitHub Deep Research Top-5 Repository Digest"
source_date: 2026-06-01
source_type: github-topic-digest
input_class: external-repo-analysis
evidence_level: github-topic-plus-repo-readme
related_skill: deep-research
repo_scope:
  - skills/deep-research/SKILL.md
observed_query: "https://github.com/topics/deep-research"
---

# GitHub Deep Research Top-5 Repository Digest

## Inputs

Observed from GitHub topic `deep-research` on 2026-06-01, sorted by displayed stars:

| Rank | Repository | Observed stars | Relevant pattern |
|---:|---|---:|---|
| 1 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | 31.5k | Long-horizon deep-research harness with skills, tools, sandboxing, subagents, context engineering, and long-term memory. |
| 2 | [666ghj/BettaFish](https://github.com/666ghj/BettaFish) | 27.3k | Multi-agent intelligence-analysis pipeline with query, media, insight, forum/collaboration, and report agents. |
| 3 | [stanford-oval/storm](https://github.com/stanford-oval/storm) | 26.9k | Knowledge-curation pipeline: source discovery, outline construction, article generation, citation, and polishing. |
| 4 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | 17.1k | Recency-first research skill across Reddit, X, YouTube transcripts, HN, Polymarket, and arXiv with social-signal weighting. |
| 5 | [Alibaba-NLP/DeepResearch](https://github.com/Alibaba-NLP/DeepResearch) | 8.2k | Long-horizon information-seeking agent and benchmark with ReAct and Heavy iterative modes. |

## Synthesis

The top repositories converge on five upgrades beyond a simple "collect sources and summarize" workflow:

1. **Harness, not prompt**: deep research is a managed loop with tools, memory, sandboxing, observability, and explicit quality checks.
2. **Mode selection**: standard web synthesis, recency pulse, knowledge curation, domain intelligence, and long-horizon heavy research need different source mixes and budgets.
3. **Agent decomposition**: strong systems split search, media/source parsing, insight extraction, adversarial discussion, and report writing into separable stages or agents.
4. **Outline-first synthesis**: high-quality reports build an intermediate outline or information-requirement tree before final prose.
5. **Signal-aware source ranking**: fresh topics need date windows, social engagement, primary evidence, and contradiction tracking, not generic search results alone.

## Repo Translation

- `deep-research` should start by selecting a research mode and budget.
- Collection should use a source ledger with source type, date, reliability, bias, and claim contribution.
- Synthesis should use a claim ledger and outline-first report plan for standard/deep work.
- Heavy mode should run multiple passes: first map, gap fill, contradiction/adversarial review, then final synthesis.
- Recency work should support social/conversational sources, but down-rank them unless backed by primary evidence.
- Final outputs should separate evidence, interpretation, confidence, and next research gaps.

## Verification Expectations

- Skill metadata and required sections still pass `python tools/lint-agent-skills.py`.
- Claims about repository behavior should be treated as pattern extraction from public GitHub repository pages, not as benchmarked performance guarantees.
