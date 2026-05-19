# Changelog

All notable changes to Third Brain V5 Skills are documented here.

This project follows a small-release rhythm: ship one focused release every 1-2 weeks when there are meaningful fixes, docs improvements, or skill updates.

## Unreleased

### Added
- Agent understanding framework wiki concept mapping Karpathy LLM OS ideas to Third Brain agent workflow, harness, and team design.
- GitHub star growth sprint playbook, launch copy pack, and Awesome-list target finder for legitimate open-source distribution.
- Continuous growth-loop script that tests repository metrics, verifies launch assets, evaluates readiness, and writes dated improvement reports.

### Changed
- `agentic-engineering`, `harness-engineering`, and `agent-teams-command` now share a process/kernel/system-call mental model with explicit write-back and cleanup rules.
- README, GUIDE, and CLI entry docs now link or describe the expanded LLM OS architecture mapping.
- README and community discovery docs now include stronger launch/discovery paths for GitHub star conversion.

## v5.1 - 2026-05-14

### Added
- README-top system architecture infographic for the LLM + Skills + Obsidian integration.
- `agentic-engineering` skill for model-native workflow refactoring, autonomy defaults, state checkpoints, and verification gates.
- GitHub issue templates for bugs and skill requests.
- Pull request template with verification and changelog prompts.
- Release playbook for feedback triage and small-version cadence.
- Simplified README hero diagram.
- 3-minute quickstart prompt for `wiki-ingest`.
- Before/after usage cases in README.
- `examples/` workflows for ingest, verification, daily review, and Obsidian entry.
- Standard skill template reference.
- Cursor and Windsurf compatibility documentation and adapter templates.
- Fifth workflow example for startup evaluation.
- Animated-style install demo SVG and one-click test prompt.
- Community discovery checklist with recommended repository description, topics, and Awesome-list targets.
- V5.2 post-ingest closure rules for input taxonomy, behavior conversion, creativity conversion, and governance review.
- Architecture walkthrough example for the full LLM + Skills + Obsidian closed loop.

### Changed
- Public docs now describe the current 17-skill catalog.
- Cursor and Windsurf routers now cover knowledge ops, wiki lint, context management, agentic engineering, harness engineering, and Anthropic OS.
- Core engineering skills now use a standard `## Quality Gates` heading.
- README first screen now emphasizes value proposition, quick install, try-it prompts, and local demos.
- Each skill now includes a verified-effect statement in its usage template.
- Each skill now includes version, update date, and output example metadata.
- Dashboard now includes visual navigation shortcuts and skill search.
- `install.sh` now supports explicit `codex`, `claude`, `gemini`, `cursor`, `windsurf`, and `all` targets.
- `wiki-ingest`, `cognitive-compile`, and `creativity-engine` now align with the V5 architecture loop from source to behavior, creativity, and governance.

## Release Template

Use this shape for each release:

```markdown
## vX.Y.Z - YYYY-MM-DD

### Fixed
- Short description of the user-visible bug fix.

### Added
- Short description of the new skill, tool, example, or workflow.

### Changed
- Short description of documentation, naming, or behavior changes.

### Notes
- Upgrade or migration notes, if any.
```
