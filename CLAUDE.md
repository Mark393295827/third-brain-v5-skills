# Third Brain V5 Skills — Claude Code

For detailed installation, usage, and workflow scenarios, see **[GUIDE.md](GUIDE.md)**.

You have access to the following Agent Skills. Each skill is a markdown file in `~/.claude/skills/` that defines a specific capability.

## Skill Categories

### 📥 Knowledge Pipeline
- **wiki-ingest** — Ingest sources (articles, PDFs, videos) into an interlinked wiki. STOW pipeline: Source → Think → Organize → Write.
- **knowledge-ops** — Multi-layer knowledge management with ChromaDB vector storage.
- **wiki-lint** — Health-check the wiki across 8 dimensions.

### 🔄 Daily Loop
- **daily-okr** — 7 Key Results daily cycle: Input → Cognition → Wiki → Behavior → Creativity → Output → Feedback. Includes Stop Doing List.
- **cognitive-compile** — 8-section deep learning compile: Question → Facts → Concepts → Patterns → Conflicts → Hypotheses → Decision → Action.

### 🎨 Behavior & Creativity
- **behavior-design** — Behavior change system: goals → habits → triggers → SOPs → review. Includes HAS (Human Agency Scale).
- **creativity-engine** — Combinatorial ideation with Lego Building Blocks method. Cross-domain analogies + minimum experiments.

### 🔬 Research & Quality
- **deep-research** — Multi-source research with confidence-based evidence standards.
- **verify-before-claim** — No completion claims without fresh verification evidence. Includes expected value thinking.

### 🔄 Learning
- **session-learn** — Extract 7 knowledge signal types from sessions. Closure Protocol for feedback loops.
- **project-flow-ops** — Triage, plan, track, review across projects.

### 📊 Cost
- **context-manager** — Token budgeting, prompt assembly, truncation strategies. Tokenmaxxing vs Efficiency.
- **token-cost-tracker** — Command: estimate, log, report token usage.

### 🏗️ Engineering
- **agentic-engineering** — Refactor skills and workflows as agent processes with autonomy defaults, delegated-action boundaries, state checkpoints, write-back, and verification gates.
- **harness-engineering** — Agent runtime kernel: three-tier permissions, tools as system calls, provenance ledgers, delegated-action gates, observability, recovery, and closed-loop design.
- **agent-teams-command** — Multi-agent process orchestration with ownership, IPC, async budget envelopes, integration, cleanup, and evidence gates.

### 💼 Strategy
- **startup-evaluation** — MIT 24-step startup evaluation framework.
- **anthropic-os** — Cognitive Symbiont Engine. Livewired + 3B creativity algorithms (Bending/Breaking/Blending). Predictive coding, time-arrow diagnostics.

## Usage

Invoke any skill naturally:
- "Ingest this article into my wiki"
- "Run a cognitive compile on X"
- "Create an agent team to build Y"
- "Launch Anthropic OS for my team" — includes 3B creativity algorithms
- "Apply 3B to our growth strategy" — Bending/Breaking/Blending
- "Bias to yes on this decision" — Costolo operator mode
- "Estimate token cost for this task"

## Skill Contract

Before executing a selected skill, read the skill frontmatter and enforce:

- `assumes`: required operating assumptions for safe use.
- `conflicts_with`: workflows or assumptions that must not be silently overridden.
- `## Success Metrics`: minimum measurable result for one successful run.
- `## Quality Gates`: checks required before completion claims.

For wiki-writing skills, resolve `SOURCES_DIR`, `CONCEPTS_DIR`, `ENTITIES_DIR`, `OUTPUTS_DIR`, and `LOG_FILE` from `system/config.md` when available. If no config exists, use the default STOW layout.

## Recommended Adoption Ladder

1. Week 1: `wiki-ingest` + `verify-before-claim`.
2. Weeks 2-4: add `daily-okr` + `session-learn`.
3. Month 2+: add `cognitive-compile`, `behavior-design`, and `creativity-engine`.
4. Month 3+: add `knowledge-ops`, `harness-engineering`, and `agentic-engineering`.
5. Multi-agent scale: add `agent-teams-command` and `project-flow-ops`.

## Grounding Principles

### Karpathy LLM OS
LLM=CPU · Context=RAM · Storage=Disk · Tools=System Calls · Skills=Programs · Harness=Kernel · Agent Teams=Processes

### 3B Creativity Algorithms
- **Bending**: Mutate existing success patterns into new contexts
- **Breaking**: Eliminate worst-performing patterns; break path dependency
- **Blending**: Fuse elements from different domains for novel patterns

### Operator Mode (Costolo)
- **Bias to Yes**: Only direct manager can say no
- **DRI**: Directly Responsible Individual over group consensus
- **Speed**: "If this takes 6 weeks, what would make it 2 weeks?"

### Agent Teams

Agent Teams are experimental. Enable via `settings.local.json`:
```json
{
  "experimental.agentTeams": true,
  "teammateMode": "auto"
}
```
Requires Claude Code v2.1.32+.
Use `agent-teams-command` skill for multi-agent orchestration (Ender's Game approach).
