# Skill Template Standard

Use this standard when adding or revising a skill.

````markdown
---
name: skill-name
description: One sentence that explains what the skill does and when to use it.
version: "1.1"
updated: "YYYY-MM-DD"
assumes: "What must be true for this skill to run safely."
conflicts_with: "Which skills, assumptions, or workflows this skill must not silently override."
---

# Skill Name

One short paragraph explaining the outcome.

## Usage Template

**Prompt**
```text
Use skill-name to ...
```

**Use Case**
- When the user needs ...

**Expected Result**
- The agent produces ...

**Output Example**
- A concrete example of files, sections, or artifacts produced by the skill.

**Verification Case**
- The result is valid when ...

**Verified Effect**
- Successful use changes the user's workflow by ...

## Success Metrics

- Minimum observable result for one successful run.
- Evidence or file output that proves the skill did the job.
- Clear fail condition or escalation trigger.

## When to Use

- Trigger phrase or situation.

## Workflow

1. Step one.
2. Step two.
3. Step three.

## Quality Gates

- [ ] Gate one.
- [ ] Gate two.

## Anti-patterns

- Common failure mode to avoid.
````
