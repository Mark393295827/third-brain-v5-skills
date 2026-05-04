---
name: knowledge-ops
description: Manage a multi-layered knowledge system — ingest, organize, deduplicate, sync, and retrieve across wiki files, memory, and external stores. Use when the user wants to save, organize, sync, or search their knowledge base.
---

# Knowledge Operations

Manage a multi-layered knowledge system for ingesting, organizing, syncing, and retrieving knowledge across multiple stores.

## When to Use

- User wants to "save this to my knowledge base"
- Syncing knowledge across systems (wiki, memory, git repos)
- Deduplicating or organizing existing knowledge
- User asks "what do I know about X?"
- User says "sync", "organize", "deduplicate"

## Knowledge Layers

### Layer 1: Active Execution Truth
- GitHub issues, PRs, Linear tasks — current operational state
- Rule: if it affects an active plan or release, put it here first

### Layer 2: Quick Access Memory
- Agent-specific memory files (e.g., `~/.claude/projects/*/memory/`)
- Markdown with frontmatter — user preferences, feedback, project context
- Automatically loaded at session start

### Layer 3: Durable Wiki
- Curated, interlinked wiki pages (concepts, entities, outputs)
- The canonical store for long-term knowledge
- Cross-referenced with `[[wikilinks]]`

### Layer 4: External Stores
- Vector databases, structured databases — for large-scale retrieval
- Used when wiki files become too numerous for manual navigation

## Ingestion Workflow

### 1. Classify
| Type | Primary Store | Secondary |
|------|--------------|-----------|
| Business decision | Memory (project) | Wiki decision log |
| Personal preference | Memory (user) | — |
| Reference info | Memory (reference) | Wiki concept page |
| Research output | Wiki outputs/ | Memory summary |
| Session knowledge | Session-learn extraction | Wiki concepts/entities |

### 2. Deduplicate
- Search existing knowledge before creating
- Check wiki concepts, entities, and memory for duplicates
- Update existing entries instead of creating new ones

### 3. Store
- Write to the appropriate layer
- Update summaries and indexes
- Cross-reference with `[[wikilinks]]`

### 4. Verify
- Confirm stored knowledge can be retrieved
- Check that links resolve correctly

## Quality Gates

- [ ] Knowledge classified to correct layer
- [ ] No duplicates created (searched first)
- [ ] Index/summary updated
- [ ] Cross-references added
- [ ] Verification: knowledge is retrievable
