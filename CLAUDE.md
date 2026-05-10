# Third Brain V5 Skills — Claude Code

You have access to the following Agent Skills. Each skill is a markdown file in `~/.claude/skills/` that defines a specific capability.

## Skill Categories

### 📥 Knowledge Pipeline
- **wiki-ingest** — Ingest sources (articles, PDFs, videos) into an interlinked wiki. STOW pipeline: Source → Think → Organize → Write.
- **knowledge-ops** — Multi-layer knowledge management with ChromaDB vector storage.
- **wiki-lint** — Health-check the wiki across 8 dimensions.

### 🔄 Daily Loop
- **daily-okr** — 7 Key Results daily cycle: Input → Cognition → Wiki → Behavior → Creativity → Output → Feedback. Includes Stop Doing List.
- **cognitive-compile** — 7-step deep learning: Question → Facts → Concepts → Patterns → Conflicts → Judgment → Action.

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
- **harness-engineering** — Agent runtime infrastructure: three-tier permissions, GAN patterns, closed-loop design.
- **agent-teams-command** — Ender's Game approach to Claude Code Agent Teams. Karpathy Agentic Engineering.

### 💼 Strategy
- **startup-evaluation** — MIT 24-step startup evaluation framework.
- **anthropic-os** — Self-Evolving Work Method Engine. CASH, 70/30, two-week rule, hive mind, working backwards.

## Usage

Invoke any skill naturally:
- "Ingest this article into my wiki"
- "Run a cognitive compile on X"
- "Create an agent team to build Y"
- "Launch Anthropic OS for my team"
- "Estimate token cost for this task"

## Agent Teams Note

Agent Teams are experimental. Enable via `settings.local.json`:
```json
{
  "experimental.agentTeams": true,
  "teammateMode": "auto"
}
```
Requires Claude Code v2.1.32+.
