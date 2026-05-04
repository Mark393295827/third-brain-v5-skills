---
name: behavior-design
description: Design a behavior change system — decompose a goal into minimum habits, define triggers, build SOPs, and set up review cycles. Use when the user wants to build a habit, change behavior, or achieve a personal goal.
---

# Behavior Design System

Transform goals into actionable behavior systems through decomposition, habit design, and review.

## When to Use

- User says "I want to build a habit of X"
- User has a goal but hasn't broken it into actions
- User wants to change a behavior pattern
- User is reviewing why a habit didn't stick

## Core Architecture

```
Goal → Habits  → Cues → SOPs → Review → Reward
           ↓
     Identity narrative: "I am the kind of person who..."
```

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
