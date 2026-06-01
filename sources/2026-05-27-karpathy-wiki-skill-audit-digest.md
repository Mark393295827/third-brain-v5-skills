---
source_title: "Andrej Karpathy LLM Wiki / Agentic Engineering Skill Audit"
source_date: 2026-05-27
source_type: wiki-entity-digest
input_class: internal-synthesis
evidence_level: curated-map
related_entity: "[[Andrej Karpathy]]"
related_concepts:
  - "[[LLM Wiki]]"
  - "[[Agentic Engineering]]"
  - "[[Agentic Macro Actions]]"
  - "[[AutoResearch]]"
  - "[[Agentic Education]]"
repo_scope:
  - skills/wiki-ingest/SKILL.md
  - skills/wiki-lint/SKILL.md
  - skills/knowledge-ops/SKILL.md
---

# Andrej Karpathy Wiki Skill Audit Digest

## Inputs

- `wiki/entities/Andrej Karpathy.md`
- `sources/2026-04-07-karpathy-llm-wiki-gist.md`
- `sources/2026-04-07-karpathy-obsidian-rag.md`
- `sources/2026-05-14-karpathy-skill-issue-autoresearch.md`

## Synthesis

Karpathy's LLM Wiki pattern treats durable Markdown as the primary knowledge product. Search, vectors, and tools can help retrieve pages, but they should not replace compiled source notes, concept pages, provenance, and human-readable links.

Agentic Engineering raises the quality ceiling by moving the unit of work from line-by-line edits to macro actions: feature, research, ingest, lint, plan, verify, and write-back. A macro action needs an objective, boundary, owned files, verification evidence, non-goals, and a stop condition.

AutoResearch is useful only when the task has objective metrics and cheap repeated checks. Broken links, orphan counts, missing frontmatter, source references, and retrieval hit rate are good candidates. Interpretation, taste, strategy, and claim confidence need supervised review queues.

The human role remains understanding, taste, judgment, goal setting, and deciding what matters. Skill output should therefore help future humans and agents understand mechanisms and boundaries, not merely store summaries.

## Repo Translation

- `wiki-ingest` should require an ingest macro-action contract before broad write-heavy work.
- `wiki-ingest` should add a Karpathy understanding gate for concept pages: thesis, mechanism, source boundary, counterpoint, and reusable bit.
- `wiki-ingest` should detect when a source contains a repeatable agent workflow and either update an existing skill/SOP or queue the extraction.
- `wiki-lint` should report understanding-integrity failures separately from formatting and link debt.
- `wiki-lint` should flag raw-summary pages, missing uncertainty, missing source boundaries, vector-only pointers, and buried workflows.
- `knowledge-ops` should make Markdown-first retrieval the default and treat vectors as optional retrieval support.
- `knowledge-ops` should separate objective AutoResearch loops from supervised judgment queues.

## Verification Expectations

- Skill metadata still passes the repository skill linter.
- Entry docs describe the new understanding gate and Markdown-first retrieval behavior.
- The three updated skills keep source capture, linting, and retrieval responsibilities separate.
