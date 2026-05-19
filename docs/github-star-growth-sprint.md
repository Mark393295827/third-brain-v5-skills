# GitHub Star Growth Sprint

Goal: grow `third-brain-v5-skills` stars through legitimate distribution: better first-screen conversion, Awesome-list PRs, launch posts, and high-signal community sharing.

This avoids fake stars, paid star farms, spam comments, and irrelevant pull requests. Those create short-term vanity metrics and long-term trust damage.

## Why This Path

Fast open-source star growth usually comes from four compounding channels:

1. A README that explains the value in seconds.
2. Discovery surfaces where developers already search: Awesome lists, GitHub topics, and related repos.
3. Launch platforms with technical audiences: Hacker News, Product Hunt, X, Reddit, Dev.to, Hashnode.
4. Release cadence that gives people a reason to revisit and share.

## 48-Hour Sprint

### Continuous Loop

Run this at least daily during launch week:

```powershell
$env:GITHUB_TOKEN="ghp_your_token_here"
python tools\find-awesome-pr-targets.py
python tools\growth-loop.py
```

Outputs:

- `outreach/growth-reports/YYYY-MM-DD.md`
- `outreach/growth-reports/YYYY-MM-DD.json`

The loop follows: test repository metrics and launch assets -> verify current stars/PRs/candidates -> evaluate readiness score -> improve with next actions.

### Hour 0-2: Repository Conversion

- [ ] Set GitHub description:
  `Third Brain V5 — 17 Agent Skills for Claude/Codex/Cursor | Persistent Knowledge OS + verification-first AI workflows`
- [ ] Set GitHub topics from [community-discovery.md](community-discovery.md).
- [ ] Confirm README first screen shows: value prop, install command, compatibility, demo, star CTA.
- [ ] Pin current draft PR or release if it explains the agent framework update.
- [ ] Create a GitHub Release titled `v5.2 Agent Understanding Framework` after merging the current PR.

### Hour 2-8: Awesome-List PRs

Run:

```powershell
$env:GITHUB_TOKEN="ghp_your_token_here"
python tools\find-awesome-pr-targets.py
```

Open 3-5 high-fit PRs first:

| Priority | Repo | Why |
|---:|---|---|
| 1 | `Prat011/awesome-llm-skills` | Directly about LLM/AI Agent Skills; best semantic fit. |
| 2 | `PatrickJS/awesome-cursorrules` | Very high stars; Cursor audience benefits from adapter rules. |
| 3 | `sanjeed5/awesome-cursor-rules-mdc` | Cursor rules audience; lower friction PR. |
| 4 | `hyp1231/awesome-llm-powered-agent` | Agent ecosystem discovery. |
| 5 | `IAAR-Shanghai/Awesome-AI-Memory` | Persistent memory and LLM Wiki angle. |

Use generated assets:

- `outreach/awesome-lists/awesome-pr-targets.md`
- `outreach/awesome-lists/awesome-pr-template.md`
- `outreach/awesome-lists/awesome-candidates.json`

### Hour 8-24: Launch Posts

Post in this order:

1. X thread from `outreach/launch/x-thread.md`.
2. Show HN from `outreach/launch/show-hn.md`.
3. Product Hunt launch draft from `outreach/launch/product-hunt.md`.
4. Reddit adaptation from `outreach/launch/reddit-post.md` only in communities that allow project sharing.
5. Dev.to/Hashnode article from `outreach/launch/devto-article-outline.md`.

Do not post identical copy everywhere. Keep each post native to the community.

### Hour 24-48: Response Loop

- [ ] Reply to every useful comment with a concrete answer, not a sales pitch.
- [ ] Convert repeated questions into README/GUIDE improvements.
- [ ] Open `good-first-issue` issues for small adapter/example requests.
- [ ] Ship one small release note or example update from launch feedback.
- [ ] Repost only one concrete lesson, not “please star.”

## PR Description Template

Use the generated file:

```text
outreach/awesome-lists/awesome-pr-template.md
```

Keep PRs narrow: one README list entry, one category, no unrelated edits.

## Success Metrics

| Metric | Target |
|---|---:|
| Awesome-list PRs opened | 3-5 |
| Relevant community posts | 3-4 |
| README conversion blockers fixed | 2+ |
| GitHub stars | Track daily for 7 days |
| New issues/discussions | More important than raw stars |
| Growth report cadence | Daily during launch week |

## Anti-Spam Rules

- Submit only to lists where the project clearly fits.
- Read contribution rules before opening each PR.
- Do not mass-tag maintainers.
- Do not ask for stars in PRs.
- Lead with user value: persistent memory, verification gates, and lower hallucination risk.
