# Agent Teams Classic Campaigns

Use these as copy-ready templates when `agent-teams-command` needs concrete multi-agent orders.

## Full-Stack System Development

```text
GOAL: Build a full-stack app (REST API + React) running on localhost.

ORDERS: Create a team of 3 teammates using Sonnet.

TEAMMATE 1 (BACKEND)
  TASK: FastAPI + SQLite + REST endpoints
  OWNERSHIP: backend/
  DEPENDENCY: Notify FRONTEND when done

TEAMMATE 2 (FRONTEND)
  TASK: React frontend + API integration
  OWNERSHIP: frontend/
  DEPENDENCY: Wait for BACKEND's API spec

TEAMMATE 3 (QA)
  TASK: E2E tests + API tests
  OWNERSHIP: tests/
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

TEAMMATE 1 (DATABASE)
  TASK: Query pattern analysis + performance benchmarks
  OWNERSHIP: research/performance/

TEAMMATE 2 (MIGRATION)
  TASK: Migration tool evaluation + downtime analysis
  OWNERSHIP: research/migration/

TEAMMATE 3 (CRITIC)
  TASK: Challenge the first two teammates' conclusions
  OWNERSHIP: research/risks/
  DEPENDENCY: Wait for DATABASE + MIGRATION to complete
```

## Security Audit And Fix

```text
GOAL: Find and fix all security vulnerabilities in the auth module.

ORDERS: Create a team of 2 teammates using Sonnet.

TEAMMATE 1 (AUDITOR)
  TASK: OWASP Top 10 scan + code audit
  OWNERSHIP: security/audit/
  DEPENDENCY: Submit issues to FIXER when done

TEAMMATE 2 (FIXER)
  TASK: Fix all discovered security issues
  OWNERSHIP: src/auth/
  DEPENDENCY: Wait for AUDITOR's issue list
```
