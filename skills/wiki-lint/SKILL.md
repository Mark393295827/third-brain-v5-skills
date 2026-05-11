---
name: wiki-lint
description: Health-check the knowledge wiki — find orphans, broken links, missing frontmatter, contradictions, stale content, and statistical drift. Use when the user says "lint the wiki", "health check", or periodically for maintenance.
version: "1.1"
updated: "2026-05-12"
---

# Wiki Lint — Knowledge Base Health Check

Systematic audit of wiki health across 8 dimensions.

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

## Check 2: Broken Links

- [ ] Find `[[wikilinks]]` pointing to non-existent pages
- [ ] Find `(Source: [[...]])` references to missing source files

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

## Check 8: Statistical Drift

- [ ] Compare actual file counts vs overview.md claims
- [ ] Verify central index includes all pages
- [ ] Verify all new pages appear in the correct index section

## Check 9: Permissions

- [ ] No unintended modifications to `sources/` files
- [ ] Review-queue items addressed

## Output

Write results to `system/lint-report.md`:

```markdown
---
title: "Lint Report"
type: system
updated: "YYYY-MM-DD"
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

- [ ] All 8 checks completed
- [ ] Auto-fixable issues fixed (with approval)
- [ ] Non-auto-fixable issues added to review queue
- [ ] Lint report written to system/lint-report.md
- [ ] Log updated
