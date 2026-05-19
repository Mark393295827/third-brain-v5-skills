---
source_date: 2026-05-18
source_type: local-obsidian-schema
source_path: 'C:\Users\高杰\Desktop\LLM-wiki(建构）\LLM-wiki1.0\3Mark-原创\llm-wiki-obsidian\references\schema.md'
status: immutable
---

# Karpathy LLM Wiki Schema

Based on the local Obsidian schema that cites Andrej Karpathy's LLM Wiki gist.

## Architecture

1. `sources/` stores immutable raw data and provenance.
2. `wiki/` stores LLM-managed interlinked markdown synthesis.
3. `system/` stores rules, workflows, and prompts.

## Core Rules

1. Never modify files in `sources/`; they are ground truth.
2. When new data is added, update all relevant `wiki/` pages.
3. Use wikilinks for concepts and create missing concept pages when needed.
4. Keep wiki pages concise and interlinked rather than dumping raw source data.
5. If new information contradicts existing wiki content, preserve both and mark the contradiction or open question.

## Workflow

1. Ingest raw data into `sources/YYYY-MM-DD-source-name.md`.
2. Identify affected `wiki/` pages.
3. Update existing pages or create new pages.
4. Include a reference link to the source.
5. Periodically lint for broken links, missing summaries, and formatting errors.
