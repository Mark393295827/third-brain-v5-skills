# Community Discovery Checklist

Use this checklist when publishing or refreshing the GitHub repository page.

## Repository Description

Recommended description:

```text
Third Brain V5 — 17 Production-Ready Agent Skills for Claude / Codex / Cursor | Persistent Knowledge OS + Behavior Design + Creativity Engine
```

Recommended Chinese description:

```text
第三大脑 V5 — 17 个生产就绪的 Claude/Codex/Cursor 技能 | 持久知识操作系统 + 行为设计 + 创意引擎
```

## Topics

Recommended GitHub topics:

```text
agent-skills
ai-agents
codex-cli
claude-code
gemini-cli
cursor
windsurf
llm-wiki
cognitive-os
knowledge-management
personal-knowledge-base
prompt-engineering
context-engineering
obsidian
multi-agent
behavior-design
verification
startup-evaluation
```

## Awesome List Targets

Submit only after the README, examples, and install path are stable.

Run the target finder:

```powershell
$env:GITHUB_TOKEN="ghp_your_token_here"
python tools\find-awesome-pr-targets.py
```

Current high-priority targets:

| Priority | Repository | Fit |
|---:|---|---|
| 1 | `Prat011/awesome-llm-skills` | Direct fit: LLM and AI Agent Skills. |
| 2 | `PatrickJS/awesome-cursorrules` | Very high-star Cursor audience; adapter-rule angle. |
| 3 | `sanjeed5/awesome-cursor-rules-mdc` | Cursor `.mdc` rules audience. |
| 4 | `hyp1231/awesome-llm-powered-agent` | Broad LLM agent ecosystem. |
| 5 | `IAAR-Shanghai/Awesome-AI-Memory` | Memory / persistent knowledge angle. |
| 6 | `kaushikb11/awesome-llm-agents` | Agent frameworks and resources. |

Use generated files:

- `outreach/awesome-lists/awesome-pr-targets.md`
- `outreach/awesome-lists/awesome-pr-template.md`
- `outreach/awesome-lists/awesome-candidates.json`

## Submission Blurb

```text
Third Brain V5 Skills is a collection of 17 Agent Skills that turn AI coding agents into a persistent knowledge compounding system. It supports Codex CLI, Claude Code, Gemini CLI, Cursor, and Windsurf, with workflows for LLM Wiki ingestion, cognitive compile, behavior redesign, verification, agentic workflow design, multi-agent orchestration, and startup evaluation.
```

## Maintenance Cadence

- Weekly: review Issues/PRs and update `CHANGELOG.md`.
- Every 1-2 weeks: ship one focused release.
- Monthly: refresh screenshots, examples, topics, and compatibility notes.

## Launch Channels

Use the launch pack in `outreach/launch/`:

- `show-hn.md`
- `product-hunt.md`
- `x-thread.md`
- `reddit-post.md`
- `devto-article-outline.md`

Do not post identical copy everywhere. Adapt the language to each community and ask for workflow feedback instead of asking for stars.
