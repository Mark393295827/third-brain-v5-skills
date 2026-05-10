# Third Brain V5 Skills — Installation & Usage Guide

> **16 skills** transforming AI coding agents into a persistent knowledge compounding system. Compatible with Claude Code, Codex CLI, and Gemini CLI.

---

## Table of Contents

1. [Installation](#1-installation)
2. [Platform Setup](#2-platform-setup)
3. [Quick Start Wizard](#3-quick-start-wizard)
4. [Skill Reference](#4-skill-reference)
5. [Workflow Scenarios](#5-workflow-scenarios)
6. [Daily Routine](#6-daily-routine)
7. [Advanced Configurations](#7-advanced-configurations)
8. [Troubleshooting](#8-troubleshooting)

---

## 1. Installation

### Prerequisites

- **Claude Code** ≥ v2.1.32 (`claude --version`)
- **Git** (`git --version`)
- **Python 3.8+** (for token-cost-tracker and vector features)
- **Obsidian** (recommended for wiki knowledge base)

### One-Line Install

```bash
# Clone the repository
git clone https://github.com/Mark393295827/third-brain-v5-skills.git
cd third-brain-v5-skills
```

### Install for Your Platform

#### Claude Code (Recommended)

```bash
# Personal skills (available across all projects)
cp -r skills/* ~/.claude/skills/

# Verify installation
ls ~/.claude/skills/ | wc -l
# Expected output: 16
```

#### Codex CLI

```bash
mkdir -p ~/.agents/skills
cp -r skills/* ~/.agents/skills/
```

#### Gemini CLI

```bash
mkdir -p ~/.gemini/skills/
cp -r skills/* ~/.gemini/skills/
```

#### Commands (Optional)

```bash
# Copy command files for token tracking
cp commands/* ~/.claude/commands/
```

---

## 2. Platform Setup

### 2.1 Agent Teams (Optional, Experimental)

Enable multi-agent orchestration in `.claude/settings.local.json`:

```json
{
  "experimental.agentTeams": true,
  "teammateMode": "auto"
}
```

Requires Claude Code v2.1.32+.

### 2.2 Wiki Structure

Create the vault layout that skills expect:

```bash
mkdir -p {sources,wiki/{concepts,entities,atomic-notes,outputs,decisions,sops},maps,system/templates}
```

### 2.3 Token Tracking (Optional)

```bash
# Create token log
touch .token-log.csv
echo "date,task,model,input_tokens,output_tokens,cost,notes" > .token-log.csv
```

### 2.4 Vector Search (Optional, for knowledge-ops)

```bash
pip install chromadb sentence-transformers watchdog
```

---

## 3. Quick Start Wizard

Run this sequence to verify everything works:

```bash
# Step 1: Verify skills are installed
claude "What skills do I have?"

# Step 2: Ingest a piece of knowledge
claude "I just read that Curiosity Rover found organic molecules on Mars. Ingest this into my wiki."

# Step 3: Run daily OKR
claude "Run my daily OKR."

# Step 4: Check wiki health
claude "Lint my wiki."

# Step 5: Create an agent team (if enabled)
claude "Create a team of 3 agents to research this topic."
```

---

## 4. Skill Reference

### 📥 Ingestion & Knowledge Pipeline

| Skill | What It Does | Trigger Phrase |
|-------|-------------|----------------|
| **wiki-ingest** | Ingests articles, PDFs, videos into wiki | "ingest this into my wiki" |
| **knowledge-ops** | Manages multi-layer knowledge; dedup, classify, vectorize | "save this to my knowledge base" |
| **wiki-lint** | Health-check: orphans, broken links, missing frontmatter | "lint my wiki" |

### 🔄 Daily Workflow

| Skill | What It Does | Trigger Phrase |
|-------|-------------|----------------|
| **daily-okr** | 7-KR cycle: Input→Cognition→Wiki→Behavior→Creativity→Output→Feedback | "run my daily OKR" |
| **cognitive-compile** | 7-step deep learning: Question→Facts→Concepts→Patterns→Conflicts→Judgment→Action | "do a cognitive compile on X" |

### 🎨 Behavior & Creativity

| Skill | What It Does | Trigger Phrase |
|-------|-------------|----------------|
| **behavior-design** | Decompose goals into habits, triggers, SOPs, reviews. Includes HAS scale | "design a habit for X" |
| **creativity-engine** | Combinatorial ideation via Lego Building Blocks method | "generate ideas about X" |

### 🔬 Research & Quality

| Skill | What It Does | Trigger Phrase |
|-------|-------------|----------------|
| **deep-research** | Multi-source research with confidence-based evidence | "research X for me" |
| **verify-before-claim** | No completion claims without fresh verification evidence | "verify before I ship" |

### 🔄 Learning & Flow

| Skill | What It Does | Trigger Phrase |
|-------|-------------|----------------|
| **session-learn** | Extract 7 knowledge signals from sessions. Closure Protocol | "extract what we learned" |
| **project-flow-ops** | Triage, plan, track, review across projects | "triage my tasks" |

### 📊 Context & Cost

| Skill | What It Does | Trigger Phrase |
|-------|-------------|----------------|
| **context-manager** | Token budget, prompt assembly, truncation strategies | "I'm hitting context limits" |
| **token-cost-tracker** | Estimate, log, report token usage | "how many tokens will this cost?" |

### 🏗️ Engineering

| Skill | What It Does | Trigger Phrase |
|-------|-------------|----------------|
| **harness-engineering** | Agent runtime: permissions, tools, feedback loops, observability | "how do I make this agent safe?" |
| **agent-teams-command** | Multi-agent orchestration via Agent Teams (Ender's Game approach) | "create an agent team to build X" |

### 💼 Strategy

| Skill | What It Does | Trigger Phrase |
|-------|-------------|----------------|
| **startup-evaluation** | MIT 24-step startup evaluation framework | "evaluate this startup" |
| **anthropic-os** | Self-evolving work method engine. CASH, 70/30, hive mind, 3B algorithms | "launch Anthropic OS" |

---

## 5. Workflow Scenarios

### Scenario 1: Knowledge Capture & Compounding

**Goal**: Capture an article, understand it deeply, and make the knowledge compound.

```
Step 1 — Ingest:
  "I just read a fascinating article about AlphaFold 3.
   Ingest it into my wiki."

Step 2 — Deep Understanding:
  "Run a cognitive compile on AlphaFold 3's impact on drug discovery."

Step 3 — Behavioral Action:
  "Design a habit to follow AI-in-biology news weekly."

Step 4 — Generate Ideas:
  "Use the creativity engine to generate 5 startup ideas at the
   intersection of AI and protein folding."

Step 5 — Extract Learning:
  "Extract what we learned from this session."
```

### Scenario 2: Full-Stack Development Sprint

**Goal**: Build a feature with an agent team.

```
Step 1 — Plan with Context:
  "I'm building a CLI tool for tracking TODO comments.
   Run a cognitive compile on the best architecture."

Step 2 — Create Agent Team:
  "Create a team of 3 teammates using Sonnet.
   Teammate 1: Frontend (React).
   Teammate 2: Backend (FastAPI).
   Teammate 3: QA (Playwright tests).
   Build me a working prototype."

Step 3 — Quality Check:
  "Verify before I ship: run tests and check for edge cases."

Step 4 — Document:
  "Save the architecture decisions to my wiki."
```

### Scenario 3: Startup Evaluation

**Goal**: Evaluate a startup idea systematically.

```
Step 1 — Market Analysis:
  "Run a cognitive compile on the AI-powered legal tech market."

Step 2 — Startup Evaluation:
  "Evaluate this startup idea:
   An AI that automates contract review for small businesses.
   Use the startup-evaluation framework."

Step 3 — Research:
  "Research existing competitors in AI legal tech."

Step 4 — Strategy:
  "Launch anthropic-os. Evaluate this idea using 70/30 allocation.
   What's the Big Bet vs BAU growth strategy?"
```

### Scenario 4: Marketing Campaign Design

**Goal**: Design and execute a marketing campaign.

```
Step 1 — Research:
  "Research latest trends in AI marketing automation."

Step 2 — Creativity:
  "Generate 10 campaign ideas combining AI and emotional storytelling."

Step 3 — Behavior Design:
  "Design a daily content creation habit."

Step 4 — Knowledge Capture:
  "Extract what we learned. Save the winning ideas to my wiki."
```

---

## 6. Daily Routine

### Morning Session (15 min)

```
1.  "Run my daily OKR."
    └── KR1: Input → Scan 3 high-quality sources
    └── KR2: Cognition → Extract 1 key insight
    └── KR3: Wiki → Save insight to wiki
    └── KR4: Behavior → Plan 1 action ≤15 min
    └── KR5: Creativity → 1 new idea
    └── KR6: Output → 1 reusable artifact
    └── KR7: Feedback + Stop Doing List (Buffett/Munger)
```

### Deep Work Session (2-4 hours)

```
1. "Run a cognitive compile on [topic]."
2. "Research [topic] with deep-research."
3. "Ingest findings into wiki."

For complex build tasks:
4. "Create an agent team to build [feature]."
5. "Verify before I ship."

For strategic decisions:
6. "Launch anthropic-os for this decision."
```

### Evening Review (10 min)

```
1. "Extract what we learned from today."
2. "Update project status with project-flow-ops."
3. "Estimate token cost for tomorrow's planned tasks."
```

---

## 7. Advanced Configurations

### 7.1 Model Selection by Task

| Task | Recommended Model | Rationale |
|------|------------------|-----------|
| Daily OKR | Sonnet | Fast, cheap for routine tasks |
| Cognitive Compile | Opus | Deep reasoning needed |
| Wiki Ingest | Sonnet | Structured output |
| Agent Teams | Sonnet (default) / Opus (complex) | Balance speed vs quality |
| Deep Research | Opus | Synthesis and analysis |
| Creativity Engine | Sonnet | Creative fluency |
| Token Estimation | Haiku | Fast, cheap classification |

### 7.2 Custom Settings

```json
{
  // .claude/settings.json additions
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  },
  "teammateMode": "auto"
}
```

### 7.3 Git Hooks Integration

```bash
# Post-commit hook: auto-lint wiki
cat > .git/hooks/post-commit << 'EOF'
claude "Lint my wiki after this change."
EOF
chmod +x .git/hooks/post-commit
```

### 7.4 Token Budget Management

```bash
# Estimate before expensive tasks
claude "Estimate token cost for a cognitive compile on this 50-page PDF."

# Log after tasks
claude "Log this task: cognitive-compile, opus-4.6, 150K input, 35K output."

# Weekly report
claude "Generate my weekly token report."
```

---

## 8. Troubleshooting

| Issue | Likely Cause | Solution |
|-------|-------------|----------|
| Skill not found | Skills not copied to correct directory | Run `cp -r skills/* ~/.claude/skills/` |
| Agent Teams not working | Experimental flag not set | Add `"experimental.agentTeams": true` to settings |
| Token cost too high | Using Opus for simple tasks | Switch to Sonnet; use context-manager budget rules |
| Wiki links broken | Wiki structure not set up | Create folders: wiki/concepts/, wiki/entities/ etc. |
| Vector search failing | ChromaDB not installed | `pip install chromadb sentence-transformers` |
| Session-learn empty | Session too short (<5 tool calls) | Work longer or trigger manually |
| Cognitive compile too long | Topic too broad | Narrow the question; use concrete ideas |
| LLM context full | No truncation strategy | Use context-manager to budget and trim |

### Quick Diagnostics

```bash
# Check skills installed
ls ~/.claude/skills/

# Verify Claude Code version
claude --version

# Check settings
cat ~/.claude/settings.json | grep agentTeams

# Check token log
cat .token-log.csv | tail -5
```

---

## Appendix: Skill Interaction Map

```
                    ┌──────────────────┐
                    │   External       │
                    │   Sources        │
                    └────────┬─────────┘
                             ▼
              ┌──────────────────────────┐
              │    wiki-ingest            │◄── daily-okr (KR1)
              │    knowledge-ops          │
              └──────┬──────────┬────────┘
                     │          │
              ┌──────▼          └──────────┐
              │  Knowledge Layers           │
              │  ├ wiki-lint (health check) │
              │  └ session-learn (extract)  │
              └─────────────────────────────┘
                     │
        ┌────────────┼────────────┬──────────────┐
        ▼            ▼            ▼              ▼
┌─────────────┐ ┌──────────┐ ┌──────────┐ ┌──────────────┐
│ daily-okr   │ │cognitive │ │ behavior │ │ creativity   │
│ (7 KR loop) │ │-compile  │ │ -design  │ │ -engine      │
│ + Stop List │ │          │ │ + HAS    │ │ + Lego Block │
└─────────────┘ └──────────┘ └──────────┘ └──────────────┘
        │            │            │              │
        └────────────┼────────────┼──────────────┘
                     ▼
    ┌───────────────────────────────────────────────┐
    │ verify-before-claim   ← quality gate          │
    │ deep-research         ← synthesis             │
    │ project-flow-ops      ← execution             │
    │ token-cost-tracker    ← cost control          │
    │ context-manager       ← context optimization  │
    │ harness-engineering   ← agent infrastructure  │
    └───────────────────────────────────────────────┘
                     │
        ┌────────────┴────────────┐
        ▼                         ▼
┌──────────────┐         ┌─────────────────┐
│ agent-teams  │         │ anthropic-os    │
│ -command     │         │ + CASH + 3B     │
│ (fleet ops)  │         │ + Predictive    │
└──────────────┘         │   Coding        │
                         └─────────────────┘
```

---

> **Next**: Open Claude Code and say: "Run my daily OKR."
