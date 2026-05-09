---
name: creativity-engine
description: Generate, validate, and output new ideas based on existing knowledge. Combines combinatorial creativity, cross-domain analogy, and minimum experiments. Use when the user wants fresh ideas, new product concepts, or creative solutions.
---

# Creativity Engine

Generate novel ideas by combining existing knowledge across domains, then validate them through minimum experiments.

## When to Use

- User wants "new ideas about X"
- User is stuck on a problem and needs fresh angles
- User wants to explore possibilities before committing
- After a wiki ingest session — capitalize on new knowledge

## Workflow

### C1: Combinatorial Ideation — The Lego Building Blocks Method

> "If you own one building block, you can build some cool stuff. If you get a second building block, you can build something more interesting. Get more building blocks, and very rapidly the number of things you can combine them into grows combinatorially or exponentially." — Andrew Ng

**The AI Building Blocks you should know:**

| Block | What It Does | Combine With |
|-------|--------------|--------------|
| **Prompting** | Basic LLM interaction | Any other block |
| **RAG** | Retrieve and inject context | Knowledge bases, docs |
| **Evals** | Measure quality | Any output task |
| **Guardrails** | Safety constraints | Production systems |
| **Fine-tuning** | Custom behavior | Domain-specific tasks |
| **Voice** | Speech I/O | Accessibility, hands-free |
| **Agentic workflows** | Multi-step autonomous | Complex tasks |
| **Tool use** | External API calls | Real-world actions |
| **Embeddings** | Semantic similarity | Search, clustering |
| **Vector DB** | Store/retrieve embeddings | Knowledge management |

**Combinatorial ideation process:**

Scan the wiki for relevant concepts/entities, then combine them systematically:

```
[Domain A concept] + [Domain B concept] = Novel idea
```

Example: AI + Property Maintenance → AI vision diagnosis for apartment repairs

Generate 10-20 ideas across these categories:
- **Products** — something people pay for
- **Services** — something people hire done
- **Content** — something people learn from
- **Automation tools** — something that saves time
- **Business models** — a new way to capture value

**The more building blocks you know, the more combinations are possible.**

### C2: Cross-Domain Analogy

For each promising idea, ask:
- What other domain solves a similar problem?
- What pattern can I borrow?
- What would this look like in [biology/physics/sports/gaming]?

### C3: Minimum Experiment Design

For the top 3 ideas, design the cheapest test:

| Idea | Hypothesis | Minimum Test | Success Signal | Cost |
|-----|-----------|-------------|---------------|------|
| 1 | If X then Y | Interview 5 users | ≥3 say "I'd pay for this" | Free |
| 2 | ... | Landing page + ads | ≥5% signup rate | $50 |
| 3 | ... | Manual prototype | Works for 1 case | Time |

### C4: Output Asset

After validation, if the idea survives:
- Write a structured output page
- Link to all sources and concepts
- Set status (seed → growing)

## Ideation Prompts

1. **What existing problem has a solution in another industry?**
2. **If labor were free, what would I build?** (Then use AI to replace the labor)
3. **What would the perfect version look like?** (Work backward)
4. **What do people do manually that they hate?** (Automation opportunity)
5. **What combination of wiki concepts has never been tried?**

## Classification Matrix

Evaluate each idea:

| Criterion | 1 (Low) | 3 (Medium) | 5 (High) |
|-----------|---------|------------|----------|
| Value | Nice-to-have | Saves time/money | Creates new capability |
| Difficulty | Requires deep expertise | Feasible with existing tools | Weekend prototype |
| Originality | Common | Unusual in this domain | Never seen before |

## Quality Gates

- [ ] ≥10 ideas generated across ≥3 categories
- [ ] Top 3 have minimum experiment designs
- [ ] Each idea cites its source concept(s)
- [ ] Validated ideas written to durable output
