#!/usr/bin/env python3
"""
Run a repeatable growth test/verify/evaluate/improve loop.

Usage:
  $env:GITHUB_TOKEN="ghp_your_token_here"
  python tools/growth-loop.py

The script measures repository health, validates launch assets, evaluates
growth readiness, and writes a dated report under outreach/growth-reports/.
It does not create spam, fake stars, comments, forks, or pull requests.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


GITHUB_API = "https://api.github.com"
DEFAULT_REPO = "Mark393295827/third-brain-v5-skills"
DEFAULT_REQUIRED_FILES = [
    "README.md",
    "GUIDE.md",
    "docs/community-discovery.md",
    "docs/github-star-growth-sprint.md",
    "tools/find-awesome-pr-targets.py",
    "outreach/awesome-lists/awesome-pr-targets.md",
    "outreach/awesome-lists/awesome-pr-template.md",
    "outreach/launch/show-hn.md",
    "outreach/launch/product-hunt.md",
    "outreach/launch/x-thread.md",
    "outreach/launch/reddit-post.md",
    "outreach/launch/devto-article-outline.md",
]


class GrowthLoopError(RuntimeError):
    """Raised when growth-loop execution cannot continue."""


@dataclass
class RepoMetrics:
    full_name: str
    stars: int
    forks: int
    watchers: int
    open_issues: int
    default_branch: str
    pushed_at: str
    html_url: str


def headers(token: str | None) -> dict[str, str]:
    result = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "third-brain-growth-loop",
    }
    if token:
        result["Authorization"] = f"Bearer {token}"
    return result


def github_get(path: str, token: str | None, retries: int = 2) -> Any:
    url = f"{GITHUB_API}{path}"
    for attempt in range(retries + 1):
        try:
            request = urllib.request.Request(url, headers=headers(token))
            with urllib.request.urlopen(request, timeout=30) as response:
                remaining = response.headers.get("x-ratelimit-remaining")
                if remaining == "0":
                    reset = int(response.headers.get("x-ratelimit-reset", "0"))
                    wait = max(0, reset - int(time.time()))
                    raise GrowthLoopError(
                        f"GitHub API rate limit exhausted. Retry after {wait}s."
                    )
                return json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", errors="replace")
            if exc.code in {403, 429, 500, 502, 503, 504} and attempt < retries:
                time.sleep(2**attempt)
                continue
            raise GrowthLoopError(f"GitHub API HTTP {exc.code}: {body}") from exc
        except (urllib.error.URLError, TimeoutError) as exc:
            if attempt < retries:
                time.sleep(2**attempt)
                continue
            raise GrowthLoopError(f"GitHub API network error: {exc}") from exc


def get_repo_metrics(repo: str, token: str | None) -> RepoMetrics:
    data = github_get(f"/repos/{repo}", token)
    return RepoMetrics(
        full_name=data["full_name"],
        stars=data.get("stargazers_count", 0),
        forks=data.get("forks_count", 0),
        watchers=data.get("subscribers_count", 0),
        open_issues=data.get("open_issues_count", 0),
        default_branch=data.get("default_branch", "main"),
        pushed_at=data.get("pushed_at", ""),
        html_url=data.get("html_url", ""),
    )


def get_open_pull_requests(repo: str, token: str | None) -> list[dict[str, Any]]:
    return github_get(f"/repos/{repo}/pulls?state=open&per_page=20", token)


def read_previous_report(report_dir: Path) -> dict[str, Any] | None:
    json_reports = sorted(report_dir.glob("*.json"))
    if not json_reports:
        return None
    try:
        return json.loads(json_reports[-1].read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None


def validate_assets(root: Path) -> tuple[list[str], list[str]]:
    present: list[str] = []
    missing: list[str] = []
    for rel in DEFAULT_REQUIRED_FILES:
        path = root / rel
        if path.exists() and path.stat().st_size > 0:
            present.append(rel)
        else:
            missing.append(rel)
    return present, missing


def load_candidates(root: Path) -> list[dict[str, Any]]:
    path = root / "outreach" / "awesome-lists" / "awesome-candidates.json"
    if not path.exists():
        return []
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []


def candidate_priority(candidate: dict[str, Any]) -> int:
    text = " ".join(
        [
            candidate.get("full_name", ""),
            candidate.get("description", ""),
            candidate.get("keyword", ""),
            candidate.get("suggested_section", ""),
        ]
    ).lower()
    score = min(30, int(candidate.get("stars", 0)) // 1500)
    if "llm-skills" in text or "agent skills" in text:
        score += 60
    if "cursor" in text and ("rules" in text or "mdc" in text):
        score += 45
    if "llm" in text and "agent" in text:
        score += 45
    if "memory" in text or "knowledge" in text:
        score += 35
    if "claude" in text or "codex" in text:
        score += 25
    if "prompt" in text:
        score += 10
    return score


def prioritized_candidates(candidates: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(
        candidates,
        key=lambda item: (candidate_priority(item), int(item.get("stars", 0))),
        reverse=True,
    )


def score_growth_readiness(
    present: list[str],
    missing: list[str],
    candidates: list[dict[str, Any]],
    open_prs: list[dict[str, Any]],
) -> tuple[int, list[str]]:
    score = 0
    notes: list[str] = []

    asset_score = round((len(present) / len(DEFAULT_REQUIRED_FILES)) * 40)
    score += asset_score
    notes.append(f"Launch asset readiness: {asset_score}/40")

    candidate_score = min(25, len(candidates) * 3)
    score += candidate_score
    notes.append(f"Awesome-list candidate coverage: {candidate_score}/25")

    pr_score = min(20, len(open_prs) * 10)
    score += pr_score
    notes.append(f"Open PR momentum: {pr_score}/20")

    if not missing:
        score += 15
        notes.append("All required launch assets exist: 15/15")
    else:
        notes.append(f"Missing required launch assets: {', '.join(missing)}")

    return min(score, 100), notes


def next_actions(
    missing: list[str],
    candidates: list[dict[str, Any]],
    open_prs: list[dict[str, Any]],
) -> list[str]:
    actions: list[str] = []
    if missing:
        actions.append(f"Fix missing launch assets: {', '.join(missing)}.")
    if candidates:
        top = prioritized_candidates(candidates)[:5]
        actions.append(
            "Open or update 3-5 high-fit Awesome-list PRs: "
            + ", ".join(item["full_name"] for item in top)
            + "."
        )
    else:
        actions.append("Run tools/find-awesome-pr-targets.py to refresh Awesome-list targets.")
    if not open_prs:
        actions.append("Open a draft PR or release PR that packages the launch kit.")
    actions.append("Publish one native launch post, then convert repeated feedback into docs.")
    actions.append("Track star delta and issue quality after each distribution action.")
    return actions


def make_report(
    root: Path,
    repo: str,
    metrics: RepoMetrics,
    open_prs: list[dict[str, Any]],
    present: list[str],
    missing: list[str],
    candidates: list[dict[str, Any]],
    previous: dict[str, Any] | None,
) -> tuple[str, dict[str, Any]]:
    readiness, notes = score_growth_readiness(present, missing, candidates, open_prs)
    star_delta = None
    if previous and "metrics" in previous:
        star_delta = metrics.stars - int(previous["metrics"].get("stars", metrics.stars))

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")
    actions = next_actions(missing, candidates, open_prs)
    data = {
        "generated_at": now,
        "repo": repo,
        "metrics": {
            "stars": metrics.stars,
            "forks": metrics.forks,
            "watchers": metrics.watchers,
            "open_issues": metrics.open_issues,
            "pushed_at": metrics.pushed_at,
        },
        "star_delta_since_previous_report": star_delta,
        "open_pull_requests": [
            {
                "number": pr.get("number"),
                "title": pr.get("title"),
                "draft": pr.get("draft"),
                "html_url": pr.get("html_url"),
            }
            for pr in open_prs
        ],
        "growth_readiness_score": readiness,
        "score_notes": notes,
        "awesome_candidate_count": len(candidates),
        "top_awesome_candidates": prioritized_candidates(candidates)[:5],
        "missing_assets": missing,
        "next_actions": actions,
    }

    md = [
        f"# Growth Loop Report — {now}",
        "",
        f"Repository: [{metrics.full_name}]({metrics.html_url})",
        "",
        "## Test",
        "",
        "- Checked GitHub repository metrics via API.",
        "- Checked launch assets and Awesome-list outreach files.",
        "- Checked open pull requests for current execution momentum.",
        "",
        "## Verify",
        "",
        f"- Stars: {metrics.stars}",
        f"- Forks: {metrics.forks}",
        f"- Watchers: {metrics.watchers}",
        f"- Open issues/PR count from repo API: {metrics.open_issues}",
        f"- Star delta since previous report: {star_delta if star_delta is not None else 'n/a'}",
        f"- Required launch assets present: {len(present)}/{len(DEFAULT_REQUIRED_FILES)}",
        f"- Awesome-list candidates: {len(candidates)}",
        f"- Open PRs: {len(open_prs)}",
        "",
        "## Evaluate",
        "",
        f"Growth readiness score: **{readiness}/100**",
        "",
    ]
    md.extend(f"- {note}" for note in notes)
    md.extend(["", "## Improve / Execute", ""])
    md.extend(f"- [ ] {action}" for action in actions)
    md.extend(["", "## Top Awesome-list Targets", ""])
    for item in prioritized_candidates(candidates)[:5]:
        md.append(
            f"- [{item['full_name']}]({item['html_url']}) — priority {candidate_priority(item)}, {item['stars']} stars; suggested section: `{item['suggested_section']}`"
        )
    md.extend(["", "## Open PRs", ""])
    if open_prs:
        for pr in open_prs:
            md.append(f"- #{pr.get('number')} {pr.get('title')} — {pr.get('html_url')}")
    else:
        md.append("- None found.")
    md.append("")
    return "\n".join(md), data


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the Third Brain growth loop.")
    parser.add_argument("--repo", default=DEFAULT_REPO)
    parser.add_argument("--token-env", default="GITHUB_TOKEN")
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument(
        "--report-dir",
        type=Path,
        default=Path("outreach") / "growth-reports",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    report_dir = (root / args.report_dir).resolve()
    report_dir.mkdir(parents=True, exist_ok=True)

    token = os.getenv(args.token_env)
    if not token:
        print(
            f"Warning: {args.token_env} is not set. Unauthenticated GitHub API calls "
            "are rate-limited.",
            file=sys.stderr,
        )

    try:
        metrics = get_repo_metrics(args.repo, token)
        open_prs = get_open_pull_requests(args.repo, token)
        present, missing = validate_assets(root)
        candidates = load_candidates(root)
        previous = read_previous_report(report_dir)
        markdown, data = make_report(
            root, args.repo, metrics, open_prs, present, missing, candidates, previous
        )
    except GrowthLoopError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    (report_dir / f"{stamp}.md").write_text(markdown, encoding="utf-8")
    (report_dir / f"{stamp}.json").write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"Wrote growth report: {report_dir / f'{stamp}.md'}")
    print(f"Growth readiness score: {data['growth_readiness_score']}/100")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
