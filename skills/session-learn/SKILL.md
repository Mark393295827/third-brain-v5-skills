---
name: session-learn
description: Extract reusable knowledge from a work session and save concepts, entities, corrections, patterns, ideas, decisions, and gaps to the wiki. Use when ending a session or when the user says to extract knowledge.
version: "1.1"
updated: "2026-05-22"
assumes: "The current session contains reusable learning worth writing back to durable storage."
conflicts_with: "Do not rewrite immutable source notes; use wiki-ingest for raw source capture and append logs instead."
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

**Output Example**
- A session learning note with concepts, decisions, corrections, reusable patterns, and open gaps.

**Verification Case**
- The output lists saved files and separates confirmed learning from open questions.

**Verified Effect**
- Useful session knowledge is preserved as durable notes instead of disappearing into chat history.

## Success Metrics

- Extracts signals into durable notes or explicitly states that no durable signal met the save threshold.
- Saved items are classified as concept, entity, correction, pattern, idea, decision, or gap.
- Final summary lists saved files and open questions separately.

## When to Use

- "Extract this session" or "save what we learned"
- After substantive work (≥5 tool calls)
- Session-end review routine
- User corrects agent's understanding
- **Auto-trigger** after cognitive-compile, wiki-ingest, deep-research

---

## 7 Knowledge Signals

Resolve destination paths from `system/config.md` when available. If no config exists, use the default wiki and system paths.

| # | Signal | Action |
|:--|--------|--------|
| 1 | **New Concept** | Create `CONCEPTS_DIR/[name].md` status:seed |
| 2 | **New Entity** | Create `ENTITIES_DIR/[name].md` type:entity |
| 3 | **Correction** | Update page + annotate + log |
| 4 | **Reusable Pattern** | Create/update SOP page |
| 5 | **New Idea** | Save to `CREATIVITY_DIR/ideas/` or `OUTPUTS_DIR/` |
| 6 | **Major Decision** | Record to `DECISIONS_DIR/` with rationale |
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
- **Log everything**: append to `LOG_FILE`

## Execution

```
1. Check depth (≥5 tool calls?)
2. Scan for 7 signal types
3. For each: search wiki → update/create
4. Execute closure cycle
5. Check gaps → append to review queue
6. Batch write (parallel)
7. Update overview + central index
8. Append to `LOG_FILE`
```

## Quality Gates

- [ ] Session qualified (≥5 tool calls or user-initiated)
- [ ] No duplicates created
- [ ] New pages: `status: seed` + ≥2 wikilinks
- [ ] Closure cycle executed for all outputs
- [ ] Conflicts annotated (not silently overwritten)
- [ ] Gaps recorded in review queue
- [ ] Log updated
