# Workflow: LLM + Skills + Obsidian Architecture Review

## Before

The repository has skills, adapters, wiki folders, and examples, but a new user may not understand how the pieces form one closed-loop system.

## Input

Use this when you want an agent to explain or audit the Third Brain architecture.

## Prompt

```text
Review this Third Brain repository as an LLM + Skills + Obsidian integration.

Create:
1. a system architecture diagram
2. a layer-by-layer explanation of input, human cognition, skills, wiki storage, retrieval, behavior, creativity, output, and governance
3. a short list of architecture risks
4. the next three improvements that would make the system more production-ready

Use the local README, GUIDE, skills/*/SKILL.md, adapters/, examples/, system/, and wiki/ folders as evidence.
```

## Expected Output

- A diagram that shows `Input -> LLM Runtime -> Skill Router -> Skills -> Obsidian Wiki -> Retrieval -> Behavior/Creativity -> Output -> Feedback`.
- A risk list covering drift, missing provenance, missing executable vector sync, and adapter coverage.
- A concrete improvement backlog.

## Verification

- The diagram includes both the knowledge path and the feedback path.
- Each named layer maps to at least one real repository folder or skill.
- Open risks distinguish implemented files from documented-but-not-yet-implemented features.
