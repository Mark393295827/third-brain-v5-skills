---
name: deep-research
description: Multi-source deep research — search, synthesize, and deliver cited reports. Use when the user wants thorough research on any topic with evidence and citations.
---

# Deep Research

Conduct multi-source research — search across sources, synthesize findings, and produce structured, cited reports.

## When to Use

- User says "research X for me" or "deep dive into X"
- User needs a comprehensive overview of a topic
- Comparing multiple viewpoints or sources
- Before making a significant decision that requires evidence

## Workflow

### Phase 1: Scope Definition

```
BEFORE searching, define:

1. Core question: What exactly are we researching?
2. Confidence target: Casual overview vs. authoritative reference?
3. Depth: 3 sources (quick) | 10 sources (standard) | 20+ sources (deep)
4. Constraints: Recent only? Specific domains? Specific languages?
```

### Phase 2: Multi-Source Collection

Collect sources across different types for balanced coverage:

| Type | Purpose |
|------|---------|
| Primary sources | Original research, official docs |
| Expert commentary | Analysis and interpretation |
| Contrarian views | Challenge assumptions |
| Data/evidence | Quantitative support |

For each source captured:
- Extract key claims with source attribution
- Note confidence level and potential bias
- Flag contradictions between sources

### Phase 3: Synthesis

Organize findings into a structured synthesis:

```
1. Executive Summary — 3 bullet points max
2. Key Findings — what the evidence says
3. Points of Agreement — where sources converge
4. Points of Disagreement — where sources diverge
5. Gaps — what isn't known or is uncertain
6. Sources — full list with citations
```

### Phase 4: Output

Write the research output with:
- Clear attribution for each claim `(Source: [[source]])`
- Confidence markers (high/medium/low) for each finding
- Recommendation or next steps

## Research Quality Standards

| Confidence | Evidence Required |
|-----------|------------------|
| High | ≥3 independent sources, or 1 authoritative primary source |
| Medium | 2 sources, or 1 source with reasonable authority |
| Low | 1 source, unverified claim |
| Speculative | No source — clearly marked as inference |

## Quality Gates

- [ ] Research scope defined before collection
- [ ] ≥3 sources collected (or specified depth)
- [ ] Contradictions flagged
- [ ] Each finding has confidence marker
- [ ] Output saved to wiki outputs/
- [ ] Sources list complete with citations
