# Release Playbook

This playbook turns the repository's iteration strategy into a repeatable weekly loop.

## Weekly Feedback Loop

Run this once per week:

1. Review open Issues and PRs.
2. Label each item as `bug`, `skill-request`, `docs`, `good-first-issue`, `needs-info`, or `high-frequency-pain`.
3. Reply to every new issue, even if the answer is only a triage note.
4. Pick 1-2 user-visible fixes or improvements for the next small release.
5. Update `CHANGELOG.md` before tagging a release.

## Priority Order

1. Broken install or skill loading.
2. Data loss, misleading verification, or incorrect claim behavior.
3. High-frequency user confusion from README, GUIDE, or templates.
4. Small "wow" improvements that make the first successful run faster.
5. Larger new skills or architecture changes.

## Small Release Checklist

- [ ] Fix or improve 1-2 focused things.
- [ ] Add or update a usage example.
- [ ] Update `CHANGELOG.md`.
- [ ] Verify install commands still work.
- [ ] Create a GitHub Release with a short changelog.
- [ ] Reply to the issues or PRs that the release addresses.

## README Discovery Checklist

- [ ] First screen has a clear value proposition.
- [ ] Install commands are copyable.
- [ ] At least one quick prompt shows the expected workflow.
- [ ] Demo or screenshot links are easy to find.
- [ ] Troubleshooting covers the most common failure mode.
- [ ] The README has one honest star CTA tied to user value.
- [ ] The release has a short launch post ready for X / HN / Product Hunt.

## Launch Checklist

- [ ] Run `python tools/find-awesome-pr-targets.py`.
- [ ] Run `python tools/growth-loop.py`.
- [ ] Open 3-5 relevant Awesome-list PRs.
- [ ] Publish one X thread from `outreach/launch/x-thread.md`.
- [ ] Submit Show HN only when README and demo links are stable.
- [ ] Convert repeated launch feedback into docs or examples within 48 hours.

## Suggested GitHub Topics

Use concise topics so the repo is discoverable:

`agent-skills`, `codex-cli`, `claude-code`, `gemini-cli`, `llm-wiki`, `knowledge-management`, `personal-knowledge-base`, `ai-agents`, `obsidian`, `agentic-workflow`, `context-engineering`
