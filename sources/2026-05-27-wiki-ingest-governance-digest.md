---
source_date: 2026-05-27
source_title: "Recent Obsidian Wiki Ingest, Lint, and Governance Updates"
source_author: "Obsidian Vault"
source_type: wiki-ops-digest
input_class: internal-synthesis
knowledge_stage: captured
evidence_level: curated-map
created: "2026-05-27"
---

# Wiki Ingest Governance Digest

This repo digest records the recent Obsidian wiki operations that informed the 2026-05-27 skill updates.

## Inputs

- `system/log.md` ingest records from 2026-05-24 to 2026-05-27
- `system/lint-report.md` health check dated 2026-05-26
- `system/governance-dashboard.md` review queue and evidence-risk taxonomy
- `Clippings/README.md` clipping queue and archive policy
- Recent source notes covering NotebookLM-mediated imports, company interviews, local PDF stacks, primary SEC filings, fast-changing financial claims, and AI-first organization sources

## Skill-Relevant Synthesis

- Ingest is not finished when pages are written. It requires targeted post-ingest lint: frontmatter, source refs, inlinks/outlinks, block refs, MOC/index updates, and no empty files.
- Source type matters. NotebookLM-mediated summaries, local synthesis stacks, founder interviews, investor interviews, primary filings, and fast-changing financial/product claims have different evidence defaults.
- Weak links should not be auto-expanded into empty pages. They should be queued for create/redirect/relabel/ignore decisions.
- Clippings have a lifecycle: unprocessed items stay in `Clippings/`; processed clippings move to `Clippings/archive/`; `Clippings/README.md` tracks queue and provenance.
- Historical V5 structure debt should be separated from current ingest failures. P0/P1 graph health is a gate; P2/P3 legacy debt is a queue.

## Repo Translation

- `wiki-ingest`: add source-risk taxonomy, clipping archive step, targeted post-ingest lint, and no-fake-provenance rule.
- `wiki-lint`: add P0/P1 graph health proof, source provenance debt reporting, clipping lifecycle checks, and weak-link triage.
- `knowledge-ops`: add duplicate-source handling, evidence hierarchy preservation, and explicit knowledge debt queues.
