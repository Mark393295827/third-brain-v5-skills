---
name: agentic-engineering
description: Design or refactor agent skills, workflows, and operating loops for model-native Agentic Engineering. Use when making skills more autonomous, concise, verifiable, long-horizon capable, token-efficient, and lower-friction for human-LLM collaboration.
version: "1.2"
updated: "2026-05-18"
---

# Agentic Engineering

Refactor a skill or workflow so the model can execute more work with less human steering, while preserving verification, provenance, and control of high-risk actions.

## Agent Understanding Model

Use the Karpathy-style LLM OS mapping as the design baseline:

| OS concept | Agent workflow meaning |
|---|---|
| LLM = CPU | The model runs the next reasoning/action loop. |
| Context = RAM | Load only the state needed for the next step. |
| Wiki/logs = Disk | Durable knowledge lives outside chat memory. |
| Tools = System calls | Actions must have contracts, permissions, and evidence. |
| Loop = Scheduler | Plan -> Act -> Observe -> Iterate controls work. |

The agent is a process with state, tools, permissions, and write-back duties. Do not design skills as advice pages; design them as executable control loops.

## Usage Template

**Prompt**
```text
Use agentic-engineering to revise this skill/workflow. Make it model-native, concise, autonomous, verifiable, and long-horizon capable.
```

**Use Case**
- Improving an existing skill, SOP, command, agent workflow, or multi-agent plan.

**Expected Result**
- A compact agentic workflow with clear defaults, state checkpoints, verification gates, and escalation rules.

**Output Example**
- A revised `SKILL.md` with model assumptions, autonomous execution loop, quality gates, and anti-patterns.

**Verification Case**
- A fresh agent can run the workflow without repeated clarification and can prove completion with evidence.

**Verified Effect**
- Human coordination load drops; the LLM spends fewer tokens asking for obvious decisions and more tokens executing, checking, and learning.

## Model Meta-Properties

Design around the model as it is, not as a human assistant metaphor.

| Meta-property | Skill design response |
|---|---|
| Context is scarce working memory | Keep `SKILL.md` short; move examples/details to references; load only what is needed. |
| Output is probabilistic | Require tests, citations, diffs, screenshots, or link checks before claims. |
| Tool use is the action layer | Name allowed tools, denied actions, and idempotent retries. |
| Long-horizon drift is normal | Add checkpoints, state files, stop criteria, and recovery paths. |
| Durable knowledge is external | Persist reusable results into wiki, docs, logs, or state files. |
| The model is strong at synthesis | Do not over-explain generic concepts; specify local constraints and unusual rules. |
| The model can over-ask | Provide safe defaults and ask only for irreversible, high-risk, or genuinely ambiguous decisions. |
| Cost and latency matter | Route simple work to thin loops; reserve deep context for high-uncertainty decisions. |

## Workflow

### 1. Compress the Contract

State the workflow in one sentence:

```text
Input -> transformation -> durable output -> verification evidence
```

If this sentence is vague, fix it before adding steps.

### 2. Set Autonomy Defaults

Use this escalation policy:

| Situation | Default |
|---|---|
| Reversible local edit | Proceed, then verify. |
| Missing low-risk detail | Make a conservative assumption and record it. |
| Conflicting existing files | Preserve user changes and adapt. |
| Destructive, irreversible, credential, payment, legal, or production action | Stop and ask. |
| User explicitly requested a choice | Ask once, briefly. |

### 3. Externalize State

For long tasks, create or update one durable state artifact:

```markdown
Goal:
Current step:
Assumptions:
Files touched:
Evidence:
Open risks:
Next action:
```

Avoid relying on chat memory for multi-hour or multi-session continuity.

### 4. Use the Thin Loop

```text
Boot minimal context.
Plan the next smallest useful step.
Act with tools as system calls.
Observe environmental evidence.
Update durable state.
Verify or iterate.
Write back reusable learning.
Stop when definition of done is proven.
```

Keep the loop short. Do not produce broad plans unless the task is broad.

### 5. Convert Human Collaboration into Interfaces

Replace repeated human check-ins with artifacts:

| Human need | Agentic interface |
|---|---|
| "What are you doing?" | Task state + changed files + next action |
| "Is it done?" | Verification command/output + residual risk |
| "Why this choice?" | Assumption ledger + tradeoff table |
| "Can this be reused?" | SOP, skill update, or wiki output |

### 6. Verify Before Claiming

Every completion claim needs fresh evidence:

- files exist or diffs show expected edits
- tests, lint, link checks, or schema checks pass
- source references resolve
- known residual risks are named

### 7. Close the Memory Loop

After significant output, decide where the result belongs:

| Output | Durable home |
|---|---|
| Source-derived claim | `sources/` reference + `wiki/` synthesis |
| Reusable workflow | skill, SOP, or command file |
| Project decision | `wiki/decisions/` or project log |
| Correction | related wiki page + change log |
| Open risk | review queue or issue tracker |

## Quality Gates

- [ ] Trigger description says exactly when to use the skill.
- [ ] `SKILL.md` removes generic teaching and keeps only non-obvious procedure.
- [ ] Workflow has safe defaults and a narrow ask-user policy.
- [ ] Long-horizon tasks have checkpoints or state artifacts.
- [ ] Quality gates include executable or inspectable evidence.
- [ ] Significant outputs have a write-back destination.
- [ ] Anti-patterns name the most likely model failure modes.
- [ ] Output format is concrete enough for another agent to follow.

## Anti-patterns

- Asking the user to decide routine reversible details.
- Writing long philosophy where a table or checklist would guide better.
- Claiming completion from confidence instead of verification.
- Keeping state only in conversation.
- Treating tools as magic actions instead of permissioned system calls.
- Optimizing for one impressive answer instead of a reusable loop.
