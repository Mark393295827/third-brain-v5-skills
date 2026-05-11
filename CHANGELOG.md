# Changelog

All notable changes to Third Brain V5 Skills are documented here.

This project follows a small-release rhythm: ship one focused release every 1-2 weeks when there are meaningful fixes, docs improvements, or skill updates.

## Unreleased

### Added
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

### Changed
- README first screen now emphasizes value proposition, quick install, try-it prompts, and local demos.
- Each skill now includes a verified-effect statement in its usage template.
- Each skill now includes version, update date, and output example metadata.
- Dashboard now includes visual navigation shortcuts and skill search.
- `install.sh` now supports explicit `codex`, `claude`, `gemini`, `cursor`, `windsurf`, and `all` targets.

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
