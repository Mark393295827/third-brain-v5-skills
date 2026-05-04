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

## Quality Rules

- **Don't over-extract**: trivial sessions (<5 tool calls) skip learning
- **Deduplicate first**: search wiki before creating
- **Confidence markers**: new pages get `status: seed`, `knowledge_stage: captured`
- **Log everything**: append to system/log.md with `[session-learn]` tag

## Execution

```
1. Check session depth (≥5 tool calls?)
2. Scan conversation + tool calls for 7 signal types
3. For each signal: search wiki → update or create
4. Batch write (parallel)
5. Update wiki overview + central index if new pages created
6. Append to system/log.md
```

## Quality Gates

- [ ] Session qualified (≥5 tool calls or user-initiated)
- [ ] No duplicate pages created
- [ ] New pages have `status: seed` and ≥2 wikilinks
- [ ] Corrections annotated with `> [!note]` date stamp
- [ ] Log updated with [session-learn] tag
