---
name: daily-okr
description: Execute a daily knowledge compound closed loop — 7 Key Results from input to feedback with scoring. Use when the user wants to do a daily review, plan their day, or run a knowledge workflow.
version: "1.1"
updated: "2026-05-12"
---

# Daily OKR — Knowledge Compound Closed Loop

Run a complete 7-KR cycle: Input → Cognition → Wiki → Behavior → Creativity → Output → Feedback.

## Usage Template

**Prompt**
```text
Run daily-okr in compact mode. Produce one insight, one wiki update, one action under 15 minutes, one reusable output, and a final score.
```

**Use Case**
- Starting or closing a knowledge-work day with a repeatable compounding loop.

**Expected Result**
- The agent addresses all 7 KRs and leaves a concise daily artifact.

**Output Example**
- A 7-KR scorecard with one captured input, one insight, one wiki update, one action, one idea, one output, and one review.

**Verification Case**
- KR3 has a wiki update, KR4 has a concrete action, KR7 includes evidence for completed claims, and the score is calculated.

**Verified Effect**
- A scattered workday becomes one captured insight, one action, one reusable output, and one feedback score.

## When to Use

- User says "start my daily OKR", "daily review", "today's workflow"
- Beginning of a work session focused on knowledge work
- User wants to capture, think, act, and reflect

## The 7 KR Cycle

```
KR1 输入    → 记录 1-3 条高质量信息          [5 min]
KR2 认知    → 提炼 1 句话摘要 + 1 个洞察      [5 min]
KR3 Wiki   → 新增/更新 1 个 Wiki 页面         [5 min]
KR4 行为    → 设计并执行 1 个 15 分钟行动       [5 min]
KR5 创意    → 写下 1 个新想法                 [1 min]
KR6 输出    → 留下 1 个可复用成果              [2 min]
KR7 反馈    → 3 行复盘 + 验证证据              [3 min]
```

> Minimum bar: **1 input + 1 insight + 1 action + 1 review.**

### The Stop Doing List (Warren Buffett & Charlie Munger)

> "The difference between successful people and very successful people is that very successful people say 'no' to almost everything." — Warren Buffett

> "It is remarkable how much long-term advantage people have gotten by trying to be consistently not stupid, instead of trying to be very intelligent." — Charlie Munger

During KR7, in addition to reviewing what was done, ask:

| Question | Purpose | Master Who Used It |
|----------|---------|-------------------|
| What should I NOT have done today? | Identify time-wasting activities | Buffett: "Avoiding stupidity is easier than seeking brilliance" |
| What habit should I stop? | Break bad patterns | Munger: "Invert, always invert" |
| What commitment should I decline? | Protect time and energy | Peter Drucker: "The most important decision is what not to do" |
| What investment should I cut losses on? | Avoid sunk cost fallacy | Graham: "The intelligent investor sells when a stock reaches its intrinsic value" |

**The Wisdom of Not Doing:**
- Saying no is harder than saying yes, but far more effective
- Knowing what to ignore lets you focus on what matters
- "The stock market is a device for transferring money from the impatient to the patient." — Buffett

### KR1 — Input
- Record 1-3 high-quality information items
- At least 1 from external world (article/report/video/data)
- At least 1 from personal experience (observation/conversation/project)
- Note the source and why it matters

### KR2 — Cognition
- Select 1 item for deep understanding
- Extract: 1-sentence summary + 1 insight/judgment

### KR3 — Wiki
- Create or update 1 wiki page
- Add tags and ≥2 wikilinks
- Set status (seed/growing/evergreen)

### KR4 — Behavior
- Derive 1 actionable item from today's knowledge
- Break it down to ≤15 minutes
- Execute or schedule it

### KR5 — Creativity
- Generate 1-3 ideas based on today's knowledge
- At least 1 from cross-domain analogy
- Select 1 worth pursuing

### KR6 — Output
- Produce 1 small reusable artifact
- State which long-term goal it serves
- Judge reusability

### KR7 — Feedback + Verification
- Write 3 lines of retrospective
- ⭐ **Verification**: For every "completed" claim, show evidence (command output, diff, screenshot)
- Anti-pattern: "should be fine" without proof
- Update the daily log

## Daily Scoring Card

```
输入 +1 | 认知 +1 | Wiki +2 | 行为 +2 | 创意 +1 | 输出 +2 | 反馈 +1 = /10
3=still going  5=minimal loop  7=quality loop  10=compounding flywheel
```

## Quality Gates

- [ ] All 7 KRs addressed (even briefly)
- [ ] KR3: page has ≥2 `[[wikilinks]]`
- [ ] KR4: action is ≤15 minutes
- [ ] KR6: output is reusable
- [ ] KR7: every done-claim has evidence
- [ ] Score calculated
