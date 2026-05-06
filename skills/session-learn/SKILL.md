---
name: session-learn
description: Extract reusable knowledge patterns from the current agent session. Scans for new concepts, entities, corrections, patterns, ideas, decisions, and knowledge gaps — then saves them to the wiki. Use at session end or when the user says "extract knowledge from this session".
---

# Session Learn — Continuous Knowledge Extraction

Automatically extract knowledge signals from the current session and persist them to the wiki. Inspired by ECC continuous-learning but outputs structured wiki pages instead of atomic instincts.

## When to Use

- User says "extract this session" or "save what we learned"
- After completing substantive work (≥5 tool calls)
- As part of a session-end review routine
- User corrects the agent's understanding of a topic
- **Auto-trigger** after completing a cognitive-compile, wiki-ingest, or deep-research task

---

## The 7 Knowledge Signals

### 1. New Concept
**Signal:** Session discussed a concept/framework/methodology not in the wiki.

**Action:** Create `wiki/concepts/[name].md` with `status: seed`.

### 2. New Entity
**Signal:** Session mentioned a person, company, or product not in the wiki.

**Action:** Create `wiki/entities/[name].md` with `type: entity`.

### 3. Knowledge Correction
**Signal:** User corrected the agent's understanding of existing wiki content.

**Action:**
1. Update the relevant wiki page
2. Annotate with the correction note
3. Log the correction

### 4. Reusable Pattern
**Signal:** Session executed a repeatable workflow.

**Action:** Create/update an SOP page.

### 5. New Idea
**Signal:** Session produced a creative insight worth saving.

**Action:** Save to creativity/ideas/ or wiki/outputs/.

### 6. Major Decision
**Signal:** Session made an architecture, strategy, or direction decision.

**Action:** Record to decisions/ with rationale.

### 7. Knowledge Gap
**Signal:** Discovered that an existing concept lacks sources or has contradictions.

**Action:** Append to the review queue.

---

## Closure Protocol ⭐

> **Problem:** Actions produce outputs (code, research, decisions) but the feedback path back to knowledge is absent — value leakage.
>
> **Solution:** Every significant output must trigger a closure cycle.

### The 3-Step Closure Cycle

```
            ┌────────────────────────────────────┐
            │  Step 1: FORMAT                    │
            │  Convert action output to wiki form │
            └──────────────┬─────────────────────┘
                           ▼
            ┌────────────────────────────────────┐
            │  Step 2: LINK                      │
            │  Cross-reference with existing      │
            │  concepts + entities + decisions    │
            └──────────────┬─────────────────────┘
                           ▼
            ┌────────────────────────────────────┐
            │  Step 3: LOG                       │
            │  Record the closure to log.md      │
            │  with [closure] tag + source        │
            └────────────────────────────────────┘
```

### Trigger Conditions

| Source | Trigger | Closure Action |
|--------|---------|----------------|
| **Cognitive compile** | Compile complete | Extract 3 key judgments → save to wiki/outputs/ + update entity pages |
| **Wiki ingest** | Source ingested | Auto-create entity pages + update overview + central index |
| **Deep research** | Report delivered | Save key findings to relevant concept pages + update sources |
| **Behavior design** | SOP created | Link SOP to relevant goals + habits in behaviors/ |
| **Code project** | Feature complete | Save architecture decisions + lessons to decisions/ |
| **User correction** | Knowledge corrected | Log correction + propagate to all related pages |

### Conflict Resolution Strategy

When closure detects a conflict between new knowledge and existing wiki:

| Conflict Type | Resolution |
|---------------|------------|
| **Direct contradiction** | Keep both, mark with `> [!conflict] YYYY-MM-DD` banner. Do not delete old content. |
| **Outdated information** | Add `> [!updated] YYYY-MM-DD` note. Move old content to timeline section. |
| **Different perspective** | Add as alternative view, link to the source that holds the alternative. |
| **Low confidence new info** | Add with `status: seed` and `evidence_level: single-source`. Never overwrite `growing`+ pages. |

---

## Knowledge Gap Detection

After extraction, check for actionable gaps:

| Gap | Action |
|-----|--------|
| Concept has no sources | Add to review queue: "needs sources" |
| Entity has only 1 source | Mark as `knowledge_stage: single-source` |
| Contradictory claims exist | Add conflict banner |
| Key concept mentioned but not defined | Create stub page with `status: seed` |

---

## Quality Rules

- **Don't over-extract**: trivial sessions (<5 tool calls) skip learning
- **Deduplicate first**: search wiki before creating
- **Closure always**: every output → format → link → log
- **Confidence markers**: new pages get `status: seed`, `knowledge_stage: captured`
- **Conflict honesty**: never overwrite without annotation
- **Log everything**: append to system/log.md with `[session-learn]` or `[closure]` tag

## Execution

```
1. Check session depth (≥5 tool calls?)
2. Scan conversation + tool calls for 7 signal types
3. For each signal: search wiki → update or create
4. Check for closure triggers → execute closure cycle
5. Check for knowledge gaps → append to review queue
6. Batch write (parallel)
7. Update wiki overview + central index if new pages created
8. Append to system/log.md with [session-learn][closure] tags
```

## Quality Gates

- [ ] Session qualified (≥5 tool calls or user-initiated)
- [ ] No duplicate pages created
- [ ] New pages have `status: seed` and ≥2 wikilinks
- [ ] Corrections annotated with `> [!note]` date stamp
- [ ] **Closure cycle executed** for all outputs (format → link → log)
- [ ] Conflicts detected and annotated (not silently overwritten)
- [ ] Knowledge gaps recorded in review queue
- [ ] Log updated with [session-learn] tag
