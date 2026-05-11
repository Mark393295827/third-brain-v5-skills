---
name: behavior-design
description: Design a behavior change system — decompose a goal into minimum habits, define triggers, build SOPs, and set up review cycles. Use when the user wants to build a habit, change behavior, or achieve a personal goal.
version: "1.1"
updated: "2026-05-12"
---

# Behavior Design System

Transform goals into actionable behavior systems through decomposition, habit design, and review.

## Usage Template

**Prompt**
```text
Use behavior-design for this goal. Decompose it into minimum habits, triggers, SOPs, review cadence, and failure handling.
```

**Use Case**
- Converting a goal or intention into a behavior system the user can actually repeat.

**Expected Result**
- The agent creates a habit plan with trigger, minimum action, environment design, review metric, and fallback.

**Output Example**
- A behavior card with goal, trigger, 15-minute action, cue, reward, review metric, and fallback.

**Verification Case**
- The first action takes 15 minutes or less and has a concrete time, place, trigger, and success criterion.

**Verified Effect**
- A vague goal becomes a repeatable behavior loop with a trigger, minimum action, review metric, and fallback.

## When to Use

- User says "I want to build a habit of X"
- User has a goal but hasn't broken it into actions
- User wants to change a behavior pattern
- User is reviewing why a habit didn't stick
- User wants to understand their relationship with AI tools

## Core Architecture

```
Goal → Habits  → Cues → SOPs → Review → Reward
           ↓
     Identity narrative: "I am the kind of person who..."
```

## Human Agency Scale (HAS) — Stanford Framework

When designing behavior systems involving AI tools, use the HAS framework to determine the right level of human involvement:

| Level | Description | When to Use | Example |
|:-----:|-------------|-------------|---------|
| **H1** | AI handles entirely, no human | Routine, low-stakes tasks | Auto-lint, auto-format |
| **H2** | AI needs minimal input | Tasks with clear success criteria | Code review, data entry |
| **H3** | Equal partnership | Creative/analytical work | Research synthesis, design |
| **H4** | Human drives, AI assists | High-stakes decisions | Investment analysis, strategy |
| **H5** | Human essential, AI supports | Relationship/empathy tasks | Coaching, conflict resolution |

**Key insight from Stanford research:**
- 45.2% of occupations prefer H3 (equal partnership) as the dominant level
- Workers generally prefer higher human agency than experts deem necessary
- Skills shift: from information processing → interpersonal competence

**Apply to behavior design:**
- For habits involving AI: Choose the appropriate HAS level
- For skill development: Focus on H4/H5 skills (interpersonal, strategic)
- For automation: Start with H1/H2 tasks, gradually expand

## Workflow

### B1: Define the Goal

Answer:
- Why is this important?
- What identity does it build? ("I want to be someone who...")
- What does success look like in 3 months?

### B2: Decompose into Minimum Habits

Break the goal into 3 minimum habits — actions so small they can't fail:

| Habit | Minimum Viable Action | Trigger | Frequency |
|-------|----------------------|---------|-----------|
| 1 | ≤2 minutes | After existing habit X | Daily |
| 2 | ≤5 minutes | When situation Y occurs | 3x/week |
| 3 | ≤15 minutes | At time Z | Weekly |

### B3: Define SOPs

For each habit, write the execution SOP:

```
WHEN [trigger]
THEN:
1. [step 1 — what to do]
2. [step 2 — what to do]
3. [step 3 — what to do]
AFTER: [immediate reward]

Barrier removal: [what prevents doing this?]
```

### B4: Set Up Review

- Daily: check off habit completion (≤30 sec)
- Weekly: review completion rate + resistance patterns
- Monthly: adjust habits + upgrade minimum bar

### B5: Reframe Identity

Instead of "I want to read more" → "I am a reader."
Instead of "I want to exercise" → "I am someone who moves daily."

## Behavior Design Principles

1. **Minimum start** (< 5 min) — if it takes willpower to start, the habit won't stick
2. **Trigger binding** — attach new habit to an existing routine
3. **Friction removal** — prepare the environment to make it easy
4. **Immediate reward** — the brain needs dopamine within seconds, not months
5. **Identity narrative** — lasting change comes from identity shift, not goal completion

## Quality Gates

- [ ] Goal framed as identity, not outcome
- [ ] 3 minimum habits defined (≤2/5/15 min)
- [ ] Each habit has a clear trigger
- [ ] Friction removal identified for each
- [ ] Review schedule set
