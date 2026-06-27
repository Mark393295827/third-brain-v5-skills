---
name: wiki-lint
description: Health-check the V6 knowledge wiki — find orphans, broken links, missing frontmatter, contradictions, stale content, statistical drift, source/provenance debt, daily-loop health, and rule-promotion readiness. Use when the user says "lint the wiki", "health check", "check Obsidian system", "verify the knowledge loop", or periodically for maintenance.
version: "6.0"
updated: "2026-06-27"
assumes: "Vault paths are resolved from system/config.md when present; otherwise default STOW paths are used."
conflicts_with: "Do not silently repair high-risk or source-file issues; report them or ask before modifying durable records."
---

# Wiki Lint — Knowledge Base Health Check

Systematic audit of wiki health across 8 dimensions.

Resolve target paths from `system/config.md` when available. If no config exists, use the default STOW layout and write the report to `system/lint-report.md`.

## Usage Template

**Prompt**
```text
Use wiki-lint on my vault. Check frontmatter, broken links, orphans, stale pages, contradictions, drift, stats, and index health.
```

**Use Case**
- Maintaining a growing Obsidian or markdown wiki before it becomes hard to trust or navigate.

**Expected Result**
- The agent produces a lint report with ranked issues and concrete repair actions.

**Output Example**
- A lint report grouped by severity with file paths, issue counts, and repair checklist.

**Verification Case**
- The report includes file paths, issue counts, severity, and at least one recommended fix per high-priority issue.

**Verified Effect**
- Wiki health becomes visible through ranked issues instead of vague feelings that the vault is disorganized.

## Success Metrics

- Report includes issue counts, severity, file paths, and recommended fixes.
- Broken links, orphans, missing frontmatter, stale pages, and source-protection risks are checked or marked not applicable.
- No source files are modified during linting.
- P0/P1 checks can prove main graph health after an ingest: no empty files, missing wiki frontmatter, broken source refs, zero-inlink wiki pages, or wiki pages with fewer than two outbound links.
- Concept-page quality checks separate real understanding from raw summaries: thesis, mechanism, source boundary, uncertainty, and connections.
- V6 checks report daily-loop health, Agent/Wiki flywheel candidates, and whether proposed skill/schema promotions have enough evidence.

## When to Use

- User says "lint the wiki", "health check", "run lint"
- Periodically (weekly recommended)
- Before/after major batch operations
- When wiki feels disorganized

## Check 1: Frontmatter Integrity

Scan every wiki page for:
- [ ] Missing `type:` field
- [ ] Missing `status:` field
- [ ] Missing `created:` field
- [ ] Pages without frontmatter entirely
- [ ] Legacy status values (e.g., `seedling` → `seed`)
- [ ] Missing `knowledge_stage:` or `evidence_level:` on V5 pages
- [ ] Source files missing `source_id`, `hash`, `trust_level`, or `status` are reported as provenance debt; do not fabricate values

## Check 2: Broken Links

- [ ] Find `[[wikilinks]]` pointing to non-existent pages
- [ ] Find `(Source: [[...]])` references to missing source files
- [ ] Distinguish true missing sources from weak concept/entity links and example-text false positives

## Check 3: Orphan Pages

- [ ] Pages with zero incoming `[[wikilinks]]`
- [ ] Pages with zero outgoing `[[wikilinks]]` (violates ≥2 rule)

## Check 4: Stale Content

- [ ] Pages not updated in >90 days with `status: growing` or higher
- [ ] Pages with `status: stale` that should be archived or refreshed

## Check 5: Contradictions

- [ ] Conflicting claims across different sources on the same topic
- [ ] Missing `> [!warning] Contradiction` markers

## Check 6: Single-Source Claims

- [ ] Pages with `evidence_level: single-source` that have accumulated multiple sources

## Check 7: Page Structure Standards ⭐

- [ ] Concept pages missing leading quote block (core thesis)
- [ ] Concept pages missing `---` separator before timeline
- [ ] Concept pages missing `## 演化时间线` section
- [ ] Concept pages missing `## 关联` or `## Connections` section
- [ ] Pages with no ASCII diagram or comparison table for framework-type content
- [ ] New pages without ≥2 outgoing `[[wikilinks]]`
- [ ] Concept pages that summarize a source without a mechanism, boundary, uncertainty, or reusable insight

## Check 7A: Karpathy Understanding Integrity

Flag pages that violate LLM Wiki intent:

| Symptom | Why it matters | Action |
|---|---|---|
| Raw summary only | Future agents must re-understand the source | add thesis, mechanism, connections |
| No source boundary | Claim strength is unclear | add evidence note or single-source warning |
| No uncertainty | The page looks more certain than the source | add review queue item |
| Vector/RAG-only pointer | Knowledge is not compiled into Markdown | create or update a durable wiki page |
| Workflow buried in prose | Agent cannot reuse it | extract SOP, skill rule, or behavior experiment |

## Check 8: Statistical Drift

- [ ] Compare actual file counts vs overview.md claims
- [ ] Verify central index includes all pages
- [ ] Verify all new pages appear in the correct index section

## Check 9: Clipping Queue and Source Lifecycle

- [ ] Processed clippings are in `Clippings/archive/`
- [ ] `Clippings/README.md` queue counts and processed-source table are current when present
- [ ] Duplicate clippings point to canonical source notes instead of creating parallel facts

## Check 10: Permissions

- [ ] No unintended modifications to `sources/` files
- [ ] Review-queue items addressed

## Check 11: V6 Daily Loop and Flywheel Health

- [ ] `system/daily-knowledge-loop.md` exists when a scheduled loop is expected
- [ ] Latest `system/daily/YYYY-MM-DD-daily-knowledge-loop.md` exists or absence is reported
- [ ] `system/auto-update-report.md`, `system/agent-wiki-flywheel-report.md`, and `system/system-evolution-backlog.md` are present when referenced
- [ ] Automated report blocks do not overwrite manual KR, review, or timeline sections
- [ ] Candidate rules stay in backlog until evidence and objective checks support promotion

## Check 12: V6 Promotion Readiness

For any proposed change to a skill, SOP, schema rule, or automation, report:

| Field | Required |
|---|---|
| Evidence | at least two durable wiki/source pages, or one high-quality source plus local verification |
| Macro action | Trigger, Execute, Verify, State, budget, stop condition, recovery |
| Boundary | no provenance, permission, source, or review relaxation |
| Cheap check | lint, test, link check, script receipt, dashboard metric, or review receipt |

If any field is missing, leave the proposal in review queue.

## Output

Write results to `LINT_REPORT_FILE`:

```markdown
---
title: "Lint Report"
type: system
updated: "[date]"
---

# Lint Report — [date]

## Issues Found
| Type | Count | Severity |
|------|-------|----------|
| ... | ... | ... |

## Auto-Fixed
| Issue | Fix |
|-------|-----|

## Requires Human Review
| Page | Issue | Suggested Action |
|------|-------|-----------------|
```

## Quality Gates

- [ ] All checks completed
- [ ] P0/P1 graph health summarized
- [ ] Auto-fixable issues fixed (with approval)
- [ ] Non-auto-fixable issues added to review queue
- [ ] Lint report written to `LINT_REPORT_FILE`
- [ ] Log updated
- [ ] Historical V5 structure debt is reported separately from current ingest failures
- [ ] Understanding-integrity failures are reported separately from formatting debt
- [ ] V6 daily-loop and promotion-readiness findings are separated from ordinary graph lint
