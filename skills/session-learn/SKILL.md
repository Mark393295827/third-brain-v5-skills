---
name: session-learn
description: Extract reusable knowledge from sessions. Scans for new concepts, entities, corrections, patterns, ideas, decisions, gaps — saves to wiki. Use at session end or "extract knowledge".
---

# Session Learn

Extract knowledge signals from current session and persist to wiki.

## Usage Template

**Prompt**
```text
Use session-learn on this conversation. Extract reusable concepts, decisions, corrections, patterns, ideas, and gaps into my wiki.
```

**Use Case**
- Ending a substantive work session without losing reusable learning to chat history.

**Expected Result**
- The agent creates or updates notes for concepts, decisions, corrections, and reusable patterns.

**Verification Case**
- The output lists saved files and separates confirmed learning from open questions.

## When to Use

- "Extract this session" or "save what we learned"
- After substantive work (≥5 tool calls)
- Session-end review routine
- User corrects agent's understanding
- **Auto-trigger** after cognitive-compile, wiki-ingest, deep-research

---

## 7 Knowledge Signals

| # | Signal | Action |
|:--|--------|--------|
| 1 | **New Concept** | Create `wiki/concepts/[name].md` status:seed |
| 2 | **New Entity** | Create `wiki/entities/[name].md` type:entity |
| 3 | **Correction** | Update page + annotate + log |
| 4 | **Reusable Pattern** | Create/update SOP page |
| 5 | **New Idea** | Save to creativity/ideas/ or wiki/outputs/ |
| 6 | **Major Decision** | Record to decisions/ with rationale |
| 7 | **Knowledge Gap** | Append to review queue |

---

## Closure Protocol ⭐

> Every significant output must trigger a closure cycle to prevent value leakage.

### 3-Step Cycle

```
FORMAT → LINK → LOG
Convert to wiki form → Cross-reference → Record to log.md
```

### Triggers

| Source | Trigger | Action |
|--------|---------|--------|
| Cognitive compile | Complete | Extract 3 judgments → wiki/outputs/ + update entities |
| Wiki ingest | Source ingested | Auto-create entities + update overview + central index |
| Deep research | Report delivered | Save findings to concept pages + update sources |
| Behavior design | SOP created | Link SOP to goals + habits |
| Code project | Feature complete | Save decisions + lessons |
| User correction | Corrected | Log + propagate to related pages |

### Conflict Resolution

| Type | Resolution |
|------|------------|
| **Direct contradiction** | Keep both, mark `> [!conflict] YYYY-MM-DD` |
| **Outdated** | Add `> [!updated] YYYY-MM-DD`, move old to timeline |
| **Different perspective** | Add as alternative view with source |
| **Low confidence** | `status: seed`, `evidence_level: single-source` |

---

## Knowledge Gaps

| Gap | Action |
|-----|--------|
| No sources | Add to review queue |
| Only 1 source | Mark `knowledge_stage: single-source` |
| Contradictions | Add conflict banner |
| Undefined concept | Create stub with `status: seed` |

---

## Quality Rules

- **Don't over-extract**: <5 tool calls → skip
- **Deduplicate first**: search before creating
- **Closure always**: every output → format → link → log
- **Confidence markers**: new pages get `status: seed`
- **Conflict honesty**: never overwrite without annotation
- **Log everything**: append to system/log.md

## Execution

```
1. Check depth (≥5 tool calls?)
2. Scan for 7 signal types
3. For each: search wiki → update/create
4. Execute closure cycle
5. Check gaps → append to review queue
6. Batch write (parallel)
7. Update overview + central index
8. Append to system/log.md
```

## Quality Gates

- [ ] Session qualified (≥5 tool calls or user-initiated)
- [ ] No duplicates created
- [ ] New pages: `status: seed` + ≥2 wikilinks
- [ ] Closure cycle executed for all outputs
- [ ] Conflicts annotated (not silently overwritten)
- [ ] Gaps recorded in review queue
- [ ] Log updated
