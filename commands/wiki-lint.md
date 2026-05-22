---
name: wiki-lint
description: Run a health check on the wiki. Invoke with /wiki-lint or "lint the wiki".
---
Run the `wiki-lint` skill — 8-dimension health check on the knowledge wiki.

Before scanning, resolve paths from `system/config.md` when present. The run is successful only when the skill's `## Success Metrics` and `## Quality Gates` are satisfied, including writing the report to `LINT_REPORT_FILE` and avoiding source-file modifications.
