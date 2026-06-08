---
title: "Lint Report"
type: system
updated: "2026-06-08"
---

# Lint Report — 2026-06-08

## Scope

Targeted post-ingest lint for the 2026-06-08 batch importing:

- [[src-20260608-agent-era-antifragile-system-design-playbook]]
- [[src-20260608-bernstein-military-antifragile-synthesis]]
- [[src-20260608-minimal-investing-military-theory-research]]

## Issues Found

| Type | Count | Severity |
|---|---:|---|
| Missing touched files | 0 | P0 |
| Empty touched files | 0 | P0 |
| Broken wikilinks in touched files | 0 | P1 |
| Missing source block refs | 0 | P1 |
| Missing V5 frontmatter on new wiki/map pages | 0 | P1 |
| New wiki/map pages with fewer than two outbound wikilinks | 0 | P1 |

## Verification Evidence

```text
PASS targeted wiki lint
Checked files: 17
Broken links: 0
Missing block refs: 0
Frontmatter failures: 0
Outbound-link failures: 0
```

## Requires Human Review

| Page | Issue | Suggested Action |
|---|---|---|
| [[antifragile-system-decision-framework]] | Cross-domain theory mapping is single-source local synthesis. | Verify against Bernstein primary/near-primary investment sources and military theory references before treating as research-grade. |
| [[agent-era-antifragile-system-design-playbook]] | Agent swarm, prompt injection, and microservice resilience claims are current-practice sensitive. | Re-check current official docs, security research, and production architecture constraints before operational use. |
| [[mechanical-rebalancing-discipline]] | Investment analogies can be mistaken for financial advice. | Keep as system-design metaphor unless independently reviewed for investment context. |

## Auto-Fixed

| Issue | Fix |
|---|---|
| Obsidian broken-link risk for skill name | Converted `verify-before-claim` references from wikilinks to code identifiers. |

