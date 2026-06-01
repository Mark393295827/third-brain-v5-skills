---
name: context-manager
description: Manage the LLM's context window — token budgeting, prompt assembly, truncation strategies. Use when approaching context limits or optimizing prompt costs.
version: "1.2"
updated: "2026-06-01"
assumes: "Context is scarce; source priority and token budget matter for task success."
conflicts_with: "Do not drop source evidence required by verify-before-claim, deep-research, or wiki-ingest provenance."
---

# Context Manager

Manage the scarcest resource in the LLM OS: **context window (RAM)**.

## Usage Template

**Prompt**
```text
Use context-manager for this task. Estimate token budget, choose what to keep, what to summarize, and what to drop.
```

**Use Case**
- Preparing a long task, large document set, or multi-step agent workflow without overrunning context.

**Expected Result**
- The agent produces a context budget, priority order, truncation plan, and cost-aware prompt assembly.

**Output Example**
- A table of keep/summarize/drop decisions with estimated tokens and retrieval priority.

**Verification Case**
- The final context plan names included sources, excluded sources, and the reason for each exclusion.

**Verified Effect**
- Long or messy context becomes a scoped prompt plan with lower token waste and clearer retrieval priorities.

## Success Metrics

- Output includes an estimated token budget and a keep/summarize/drop table.
- Each excluded source has a reason, and critical context has a retrieval path.
- Final prompt plan fits the target context window with margin.

## When to Use

- "Context is full", "too many tokens", "slow responses"
- Before complex multi-step tasks
- Designing prompt templates with variable-length content
- "Optimize my prompts" or "reduce token cost"
- Before ingesting large documents

---

## Core Principles

### 0. Concrete Ideas Buy Speed (Andrew Ng)

> "When you're vague, you're almost always right. When you're concrete, you may be right or wrong. Either way is fine — we can discover that much more fast."

| Vague | Concrete | Savings |
|-------|----------|:-------:|
| "Analyze this document" | "Extract 3 key metrics from earnings report, compare to last quarter" | ~60% |
| "Help with this code" | "Fix TypeScript error line 42: 'Property id does not exist on type User'" | ~70% |
| "Research this topic" | "Find 5 sources about Claude Code auto-mode security, focus on classifier" | ~50% |

### 1. Token Budgeting

```
Context Window = System Prompt + User Input + Retrieved Context + Tool Results + Agent Thoughts

Budget:
├─ System Prompt + Schema     10-15%
├─ User Request                 5-10%
├─ Retrieved Context (RAG)    30-40%
├─ Tool Results                20-30%
└─ Agent Reasoning             10-15%
```

**Rule:** Exceeds 80% → must truncate/compress.

### 2. Prompt Assembly

```
Layer 1: Immutable Core (always injected)
├─ System prompt (persona + constraints)
├─ Schema/ontology
└─ Safety rules

Layer 2: Task Context (per-request)
├─ User request
├─ Relevant wiki pages (top-k)
└─ Recent session log

Layer 3: Ephemeral (auto-managed)
├─ Tool call history (trim old)
├─ Large outputs (summarize)
└─ Extended thinking (compact)
```

### 3. Truncation Strategies

| Strategy | When | How | Saved |
|----------|------|-----|:-----:|
| **Summarize** | Output >500 tokens | `summarize()` | ~70% |
| **Trim oldest** | Loop >10 turns | Remove earliest | ~40% |
| **Deduplicate** | Repeated content | Keep one copy | ~20% |
| **Drop results** | Action complete | Keep calls + errors only | ~50% |
| **Compact CoT** | Thinking used | 1-sentence conclusion | ~80% |
| **Cache prefix** | Repeated prompt | Identical prefix first | ~90% latency |

---

## Token Cost (Claude)

| Model | Input/MTok | Output/MTok | Window |
|-------|:----------:|:-----------:|:------:|
| Opus 4.6 | $15.00 | $75.00 | 200K |
| Sonnet 4.6 | $3.00 | $15.00 | 200K |
| Haiku 3.5 | $0.80 | $4.00 | 200K |

**Quick estimates:**
- 1 token ≈ 0.75 word
- 1 page ≈ 300-500 tokens
- 1 source ≈ 2000-8000 tokens
- 1 hour agentic ≈ 100K-500K tokens
- Weekly active user ≈ $9-15

---

## Decision Tree

```
Simple task (1-2 steps)?
├─ YES → Haiku, ~10K tokens
└─ NO → Analytical (research/compile)?
    ├─ YES → Opus, ~50-100K
    └─ NO → Procedural (ingest/lint)?
        ├─ YES → Sonnet, ~20-50K
        └─ NO → Sonnet default
```

---

## Long-Horizon Compaction Contract

For long tasks, compaction is not just shorter text. The summary must preserve the state needed to continue without drift:

```markdown
Goal:
Current definition of done:
User constraints and denied actions:
Key files, sources, or artifacts:
Completed steps:
Failed paths and why:
Verification evidence:
Open risks:
Next action:
```

Use compaction before context pressure becomes an emergency. After resuming from a compacted state, run one quick continuity check: confirm the goal, constraints, current step, and evidence before taking the next action.

---

## Tokenmaxxing vs Efficiency

> "Token maxing is actually the coolest thing you can do now." — Gary Tan

| Strategy | When | Approach |
|----------|------|----------|
| **Tokenmaxxing** | Research, deep analysis | 20 sources, cross-reference everything |
| **Efficiency** | Production, cost-sensitive | Concrete prompts, caching, truncation |

**Thin Harness, Fat Skills:**
- Simple tasks → thin prompt
- Complex tasks → fat prompt with examples

### When to Tokenmax

| Scenario | Approach | Quality Gain |
|----------|----------|:------------:|
| Research synthesis | 20 sources, cross-reference | 3-5x |
| Code review | Full repo analysis | 2-3x fewer bugs |
| Creative writing | Multiple drafts, self-critique | Significantly better |

### When to Be Efficient

| Scenario | Approach | Savings |
|----------|----------|:-------:|
| Routine linting | Haiku, minimal context | ~80% |
| Simple edits | Concrete prompt, no CoT | ~60% |
| Status checks | One-liner | ~90% |

---

## Quality Gates

- [ ] Token budget <80% before first call
- [ ] 3-layer prompt assembly
- [ ] Large outputs (>500 tokens) summarized
- [ ] Long-horizon compactions preserve goal, constraints, evidence, risks, and next action
- [ ] Cost estimated for >100K token tasks
- [ ] Cache-friendly ordering
- [ ] Context utilization logged
