---
name: context-manager
description: Manage the LLM's context window — token budgeting, prompt assembly, truncation strategies, and cache optimization. Use when approaching context limits, optimizing prompt costs, or designing multi-step agent workflows.
---

# Context Manager — Token Budget & Prompt Assembly

Manage the scarcest resource in the LLM OS: the **context window (RAM)**. Every token you don't need is latency and cost you don't have to pay.

## When to Use

- User says "context is full", "too many tokens", "slow responses"
- Before running a complex multi-step task that will generate large context
- When designing prompt templates that include variable-length content
- User asks "optimize my prompts" or "reduce token cost"
- Before ingesting large documents into a session

---

## Core Principles

### 1. Token Budgeting

Every LLM call has a fixed context window. Allocate it deliberately:

```
Total Context Window = System Prompt + User Input + Retrieved Context + Tool Results + Agent Thoughts

Budget allocation (recommended):
├─ System Prompt + Schema     10-15%  (fixed, always needed)
├─ User Request                 5-10%  (the actual task)
├─ Retrieved Context (RAG)    30-40%  (knowledge, search results)
├─ Tool Results                20-30%  (file reads, shell output, API responses)
└─ Agent Reasoning             10-15%  (CoT, planning, reflections)
```

**Rule:** If total exceeds 80% of context window → must truncate or compress before sending.

### 2. Prompt Assembly Strategy

```
┌─────────────────────────────────────────────┐
│  Layer 1: Immutable Core (always injected)   │
│  ├─ System prompt (persona + constraints)    │
│  ├─ Schema / ontology (knowledge structure)  │
│  └─ Safety rules (never override)            │
├─────────────────────────────────────────────┤
│  Layer 2: Task Context (per-request)         │
│  ├─ User's current request                   │
│  ├─ Relevant wiki pages (top-k by relevance) │
│  └─ Recent session log (last N events)       │
├─────────────────────────────────────────────┤
│  Layer 3: Ephemeral (auto-managed)           │
│  ├─ Tool call history (trim old)             │
│  ├─ Large file outputs (summarize not paste) │
│  └─ Extended thinking (compact when done)    │
└─────────────────────────────────────────────┘
```

### 3. Truncation & Compression Strategies

| Strategy | When | How | Token Saved |
|----------|------|-----|:-----------:|
| **Summarize** | Tool output >500 tokens | `summarize()` before injecting | ~70% |
| **Trim oldest** | Agent loop >10 turns | Remove earliest exchanges, keep latest | ~40% |
| **Deduplicate** | Repeated content detected | Keep one copy, reference others | ~20% |
| **Drop tool results** | After action complete | Keep only tool calls + errors, remove outputs | ~50% |
| **Compact reasoning** | Extended thinking used | Replace CoT with 1-sentence conclusion | ~80% |
| **Cache prompt prefix** | Repeated system prompt | Ensure identical prefix → prompt cache hit | ~90% latency |

---

## Token Cost Estimation

### Per-Model Pricing (Claude)

| Model | Input (per MTok) | Output (per MTok) | Context Window |
|-------|:----------------:|:-----------------:|:--------------:|
| Opus 4.6 | $15.00 | $75.00 | 200K |
| Sonnet 4.6 | $3.00 | $15.00 | 200K |
| Haiku 3.5 | $0.80 | $4.00 | 200K |

### Quick Estimation

```
1 token  ≈ 0.75 English word
1 page   ≈ 300-500 tokens (English)
1 source ≈ 2000-8000 tokens (typical article)
1 hour session ≈ 100K-500K tokens (agentic)
1 full compile ≈ 200K-1M tokens (research + output)

Weekly estimate (active user):
  wiki-ingest:   ~300K tokens × $3   = $0.90 (Sonnet)
  session-learn:~100K tokens × $3   = $0.30 (Sonnet)
  cognitive-compile: ~500K tokens × $15 = $7.50 (Opus)
  lint/daily:    ~50K tokens × $0.80 = $0.04 (Haiku)
  ─────────────────────────────────────
  Weekly total:                 ≈ $9-15
```

---

## Context Window Decision Tree

```
Is the task simple (1-2 steps)?
├─ YES → Use Haiku. Context: minimal (~10K tokens)
└─ NO → Is it analytical (research/compile)?
    ├─ YES → Use Opus. Context: strategic (~50-100K)
    └─ NO → Is it procedural (ingest/lint)?
        ├─ YES → Use Sonnet. Context: moderate (~20-50K)
        └─ NO → Use Sonnet default
```

## Quality Gates

- [ ] Token budget allocated before first LLM call (<80% context window)
- [ ] Prompt assembly follows 3-layer strategy (Core → Task → Ephemeral)
- [ ] Large outputs (>500 tokens) summarized before injection
- [ ] Cost estimated before running expensive tasks (>100K tokens)
- [ ] Cache-friendly prompt ordering (identical prefix first)
- [ ] Context window utilization logged after each major call
