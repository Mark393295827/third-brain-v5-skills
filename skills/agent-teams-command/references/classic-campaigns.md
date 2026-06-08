# Agent Teams Classic Campaigns

Use these as copy-ready templates when `agent-teams-command` needs concrete multi-agent orders.

## Full-Stack System Development

```text
GOAL: Build a full-stack app (REST API + React) running on localhost.

ORDERS: Create a team of 3 teammates using Sonnet.

RISK BUDGET:
  Max blast radius: each teammate edits only its owned directory.
  Kill/downweight signals: repeated failing tests, API contract drift, or writes outside ownership.
  Rebalance: add QA critic or switch to sequential integration if contracts conflict.

TEAMMATE 1 (BACKEND)
  TASK: FastAPI + SQLite + REST endpoints
  OWNERSHIP: backend/
  BLAST RADIUS: backend/ only; no frontend edits
  DEPENDENCY: Notify FRONTEND when done

TEAMMATE 2 (FRONTEND)
  TASK: React frontend + API integration
  OWNERSHIP: frontend/
  BLAST RADIUS: frontend/ only; no backend edits
  DEPENDENCY: Wait for BACKEND's API spec

TEAMMATE 3 (QA)
  TASK: E2E tests + API tests
  OWNERSHIP: tests/
  BLAST RADIUS: tests/ and QA report only
  DEPENDENCY: Wait for all teammates

QUALITY GATES:
- All tests passing
- API response time <200ms
- No frontend console errors
```

## Technical Decision Research

```text
GOAL: Evaluate PostgreSQL -> MongoDB migration feasibility.

ORDERS: Create a team of 3 teammates using Opus.

RISK BUDGET:
  Max blast radius: research artifacts only; no production data or schema writes.
  Kill/downweight signals: unverifiable claims, missing benchmark method, or migration-risk blind spot.
  Rebalance: add red-team review before any recommendation that changes production architecture.

TEAMMATE 1 (DATABASE)
  TASK: Query pattern analysis + performance benchmarks
  OWNERSHIP: research/performance/
  BLAST RADIUS: benchmark notes and reproducible scripts

TEAMMATE 2 (MIGRATION)
  TASK: Migration tool evaluation + downtime analysis
  OWNERSHIP: research/migration/
  BLAST RADIUS: migration notes only

TEAMMATE 3 (CRITIC)
  TASK: Challenge the first two teammates' conclusions
  OWNERSHIP: research/risks/
  BLAST RADIUS: risk review and counterarguments
  DEPENDENCY: Wait for DATABASE + MIGRATION to complete
```

## Security Audit And Fix

```text
GOAL: Find and fix all security vulnerabilities in the auth module.

ORDERS: Create a team of 2 teammates using Sonnet.

RISK BUDGET:
  Max blast radius: AUDITOR reads broadly; FIXER edits only src/auth/ after issue handoff.
  Kill/downweight signals: unverified vulnerability, secret exposure risk, or fix without regression proof.
  Rebalance: add a separate red-team pass before final integration.

TEAMMATE 1 (AUDITOR)
  TASK: OWASP Top 10 scan + code audit
  OWNERSHIP: security/audit/
  BLAST RADIUS: read/report only
  DEPENDENCY: Submit issues to FIXER when done

TEAMMATE 2 (FIXER)
  TASK: Fix all discovered security issues
  OWNERSHIP: src/auth/
  BLAST RADIUS: src/auth/ only unless commander approves broader change
  DEPENDENCY: Wait for AUDITOR's issue list
```
