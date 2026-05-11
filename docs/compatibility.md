# Compatibility

Third Brain V5 Skills use the open Agent Skills-style `SKILL.md` format. Compatibility has two levels:

1. Native skills: the tool can discover `SKILL.md` files directly.
2. Rules/context adapter: the tool can read these skills through project rules, `AGENTS.md`, or manual prompt context.

## Support Matrix

| Tool | Support Level | Recommended Setup |
|------|---------------|-------------------|
| Codex CLI | Native | Copy `skills/*` to `~/.agents/skills/`. |
| Claude Code | Native | Copy `skills/*` to `~/.claude/skills/`. |
| Gemini CLI | Native-compatible | Copy `skills/*` to `~/.gemini/skills/`. |
| Windsurf / Cascade | Native + rules | Copy `skills/*` to `.windsurf/skills/` or `~/.codeium/windsurf/skills/`; optional rule in `.windsurf/rules/`. |
| Cursor | Rules/context adapter | Add `.cursor/rules/third-brain-skills.mdc` and keep `skills/` in the repo. |
| Other AI IDEs | Prompt/context adapter | Keep `AGENTS.md`, `skills/`, and `examples/`; ask the agent to read the relevant `SKILL.md`. |

## Cursor Setup

Cursor supports project rules under `.cursor/rules/` and can also use `AGENTS.md` as a simple project instruction file. Use the adapter template in [adapters/cursor/third-brain-skills.mdc](../adapters/cursor/third-brain-skills.mdc).

```bash
mkdir -p .cursor/rules
cp adapters/cursor/third-brain-skills.mdc .cursor/rules/third-brain-skills.mdc
```

Recommended prompt:

```text
Use the Third Brain V5 skill router. For this task, select the relevant skill from skills/*/SKILL.md and follow its Usage Template, Workflow, Quality Gates, and Verified Effect.
```

## Windsurf Setup

Windsurf Cascade supports workspace skills in `.windsurf/skills/<skill-name>/SKILL.md`, global skills in `~/.codeium/windsurf/skills/<skill-name>/SKILL.md`, and workspace rules in `.windsurf/rules/*.md`.

Workspace skills:

```bash
mkdir -p .windsurf/skills
cp -r skills/* .windsurf/skills/
```

Optional rule adapter:

```bash
mkdir -p .windsurf/rules
cp adapters/windsurf/third-brain-skills.md .windsurf/rules/third-brain-skills.md
```

Recommended prompt:

```text
Use @wiki-ingest on this source, then verify the created files and list the single-source claims.
```

## Other Tools

For tools without native skill discovery:

1. Keep `AGENTS.md` at the repo root.
2. Keep `skills/` and `examples/` in the repo.
3. Start with one explicit prompt:

```text
Read AGENTS.md and the relevant file under skills/*/SKILL.md before acting. Follow the skill's Prompt, Use Case, Expected Result, Verification Case, and Verified Effect.
```

## Notes

- Prefer native skills when the tool supports `SKILL.md`.
- Prefer rules for lightweight routing instructions.
- Prefer examples when the user wants a copyable workflow rather than an always-on behavior rule.

## References

- Cursor Rules documentation: https://docs.cursor.com/en/context/rules
- Windsurf Memories & Rules: https://docs.windsurf.com/windsurf/cascade/memories
- Windsurf Cascade Skills: https://docs.windsurf.com/windsurf/cascade/skills
