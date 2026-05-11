---
name: cognitive-compile
description: Deep learning 7-step framework — transforms raw information into actionable judgment. Use when the user wants to deeply understand a topic, not just capture it.
---

# Cognitive Compile — Deep Learning Framework

Transform raw information into structured understanding and actionable judgment through 7 steps.

## Usage Template

**Prompt**
```text
Use cognitive-compile on this topic. Move from question to facts, concepts, patterns, conflicts, judgment, and action.
```

**Use Case**
- Understanding a complex topic deeply enough to make a decision or produce a reusable explanation.

**Expected Result**
- The agent produces a structured reasoning artifact with conflicts, judgment, and next actions.

**Verification Case**
- The output separates facts from interpretation and names unresolved assumptions or evidence gaps.

## When to Use

- User wants to "understand X deeply"
- User asks for analysis, synthesis, or judgment
- After ingesting an important source, before filing it away
- User says "help me think through this"

## The 7 Steps

### 1. What is the original question?

Define the core question that makes this exploration worthwhile.

```
Why does this matter?
What am I trying to understand?
What decision will this inform?
```

### 2. What are the key facts?

Extract verifiable claims from the source. Separate observation from interpretation.

- List factual claims with source references
- Note confidence level for each
- Distinguish: firsthand observation vs secondhand report vs inference

### 3. What concepts/entities are involved?

Map the intellectual terrain.

- Link to existing wiki concepts and entities
- Identify relationships between them
- Note: is this connecting previously unconnected ideas?

### 4. What patterns does this resemble?

Connect new knowledge to existing mental models.

- What known pattern does this fit?
- What analogy from a different domain applies?
- Does this confirm or challenge existing models in the wiki?

### 5. What conflicts or uncertainties exist?

Surface tensions, contradictions, and gaps.

- Does this source contradict existing wiki pages? → Flag with `> [!warning] Contradiction`
- What is the key uncertainty?
- What information is missing?

### 6. What judgment can I form?

Form a tentative thesis — not final truth, but best current understanding.

```
On balance, the evidence suggests that...
The key insight that changes my mental model is...
I'm most uncertain about...
```

### 7. What can I act on?

Convert understanding into action.

- One thing to do differently
- One thing to investigate further
- One thing to write to the wiki

## Output

Save the compile result to the wiki as a concept page or atomic note with these frontmatter fields:

```yaml
---
type: concept | atomic-note
knowledge_stage: captured | cross-checked
evidence_level: single-source | multi-source
---
```

## Quality Gates

- [ ] All 7 steps completed
- [ ] Step 3: linked to ≥2 existing wiki pages
- [ ] Step 5: contradictions flagged if any
- [ ] Step 7: at least 1 concrete action
- [ ] Result saved to wiki
- [ ] Log updated
