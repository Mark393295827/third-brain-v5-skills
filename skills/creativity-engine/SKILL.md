---
name: creativity-engine
description: Generate, validate, and output new ideas based on existing knowledge. Combines combinatorial creativity, cross-domain analogy, and minimum experiments. Use when the user wants fresh ideas, new product concepts, or creative solutions.
version: "1.2"
updated: "2026-05-22"
assumes: "The user wants divergent options and is willing to validate one minimum experiment."
conflicts_with: "Do not present untested ideas as validated; route evidence claims through verify-before-claim or deep-research."
---

# Creativity Engine

Generate novel ideas by combining existing knowledge across domains, then validate them through minimum experiments.

## Usage Template

**Prompt**
```text
Use creativity-engine on this challenge. Generate cross-domain combinations, rank them, and design the smallest test for the best idea.
```

**Use Case**
- Producing new product ideas, content angles, experiments, or strategic options from existing knowledge.

**Expected Result**
- The agent returns a ranked idea set plus one minimum experiment.

**Output Example**
- 10 idea candidates, 3 finalists, 1 selected experiment, and a 7-day validation plan.

**Verification Case**
- Each finalist idea states the source ingredients, target user, expected value, and a testable next step.
- Post-ingest ideas are saved as experiment notes when they have a plausible minimum test.

**Verified Effect**
- Brainstorming turns into ranked options with a smallest viable experiment for the best idea.

## Success Metrics

- Produces ranked options with source ingredients, target user, expected value, and risk for each finalist.
- Selects one minimum experiment with a success signal, cost, and review date.
- Saves the experiment when operating inside a configured wiki or creativity workspace.

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

For Obsidian workflows, save the selected experiment to `CREATIVITY_DIR/experiments/` with:
- source ingredients
- combination formula
- target user
- hypothesis
- minimum test
- success signal
- next output

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
- [ ] Selected experiment is saved to `CREATIVITY_DIR/experiments/` when working in an Obsidian vault
- [ ] Validated ideas written to durable output
