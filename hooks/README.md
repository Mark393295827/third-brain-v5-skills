# Hooks

Optional Claude Code hooks for automatic triggers.

| Hook | Triggers | Purpose |
|------|----------|---------|
| `session-stop` | Session end | Auto-run session-learn to extract knowledge |
| `before-tool` | Before each tool call | Verify-before-claim enforcement |

To enable, copy to `.claude/hooks/`:

```bash
cp hooks/* .claude/hooks/
```
