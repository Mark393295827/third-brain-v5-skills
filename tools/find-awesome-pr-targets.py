#!/usr/bin/env python3
"""
Find high-signal Awesome-list repositories and prepare PR outreach material.

Usage:
  $env:GITHUB_TOKEN="ghp_your_token_here"
  python tools/find-awesome-pr-targets.py

The script does not create forks, branches, commits, or pull requests. It finds
candidate repositories and writes review-ready outreach files that you can use
before submitting PRs manually or with a separate GitHub automation flow.
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


GITHUB_API = "https://api.github.com"
DEFAULT_KEYWORDS = [
    "Awesome-Cursor",
    "Awesome-Claude-Prompt",
    "Awesome-LLM-Agents",
]
PROJECT = {
    "name": "Third Brain V5 Skills",
    "repo": "https://github.com/Mark393295827/third-brain-v5-skills",
    "description": (
        "17 production-ready Agent Skills for Claude Code, Codex, Gemini, "
        "Cursor, and Windsurf. It turns AI coding agents into a persistent "
        "Knowledge OS with Obsidian ingestion, verification-first workflows, "
        "context management, and multi-agent orchestration."
    ),
}


class GitHubApiError(RuntimeError):
    """Raised when GitHub API access fails."""


@dataclass
class Candidate:
    full_name: str
    html_url: str
    description: str
    stars: int
    forks: int
    default_branch: str
    keyword: str
    suggested_section: str
    suggested_markdown: str


def build_headers(token: str | None) -> dict[str, str]:
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "third-brain-awesome-pr-target-finder",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def github_get(url: str, headers: dict[str, str], retries: int = 2) -> Any:
    for attempt in range(retries + 1):
        try:
            request = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(request, timeout=30) as response:
                remaining = response.headers.get("x-ratelimit-remaining")
                if remaining == "0":
                    reset = int(response.headers.get("x-ratelimit-reset", "0"))
                    wait = max(0, reset - int(time.time()))
                    raise GitHubApiError(
                        f"GitHub API rate limit exhausted. Retry after {wait}s."
                    )
                return json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", errors="replace")
            if exc.code in {403, 429, 500, 502, 503, 504} and attempt < retries:
                time.sleep(2**attempt)
                continue
            raise GitHubApiError(f"GitHub API HTTP {exc.code}: {body}") from exc
        except (urllib.error.URLError, TimeoutError) as exc:
            if attempt < retries:
                time.sleep(2**attempt)
                continue
            raise GitHubApiError(f"GitHub API network error: {exc}") from exc


def search_repositories(
    keyword: str,
    min_stars: int,
    per_page: int,
    headers: dict[str, str],
) -> list[dict[str, Any]]:
    query = f'{keyword} stars:>{min_stars}'
    params = urllib.parse.urlencode(
        {
            "q": query,
            "sort": "stars",
            "order": "desc",
            "per_page": per_page,
        }
    )
    url = f"{GITHUB_API}/search/repositories?{params}"
    data = github_get(url, headers)
    return data.get("items", [])


def is_awesome_list_repo(item: dict[str, Any]) -> bool:
    name = (item.get("name") or "").lower()
    full_name = (item.get("full_name") or "").lower()
    return "awesome" in name or "/awesome-" in full_name


def fetch_readme(owner: str, repo: str, headers: dict[str, str]) -> str:
    url = f"{GITHUB_API}/repos/{owner}/{repo}/readme"
    try:
        data = github_get(url, headers, retries=1)
    except GitHubApiError:
        return ""
    encoded = data.get("content", "")
    if not encoded:
        return ""
    try:
        return base64.b64decode(encoded).decode("utf-8", errors="replace")
    except (ValueError, UnicodeDecodeError):
        return ""


def suggest_section(readme: str) -> str:
    preferred = [
        "Agent",
        "AI Agent",
        "Claude",
        "Cursor",
        "Prompt",
        "Tools",
        "Developer Tools",
        "Knowledge Management",
        "Resources",
    ]
    headings: list[str] = []
    for line in readme.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            heading = stripped.lstrip("#").strip()
            if heading:
                headings.append(heading)

    for label in preferred:
        for heading in headings:
            if label.lower() in heading.lower():
                return heading
    return "AI Agent Tools"


def project_markdown() -> str:
    return (
        f"- [{PROJECT['name']}]({PROJECT['repo']}) - "
        "Production-ready Agent Skills for Claude Code, Codex, Gemini, Cursor, "
        "and Windsurf. Adds Obsidian-backed persistent memory, verification-first "
        "workflows to reduce hallucinated completion claims, context/cost control, "
        "and multi-agent orchestration."
    )


def make_candidate(item: dict[str, Any], keyword: str, headers: dict[str, str]) -> Candidate:
    owner, repo = item["full_name"].split("/", 1)
    readme = fetch_readme(owner, repo, headers)
    section = suggest_section(readme)
    return Candidate(
        full_name=item["full_name"],
        html_url=item["html_url"],
        description=item.get("description") or "",
        stars=item.get("stargazers_count", 0),
        forks=item.get("forks_count", 0),
        default_branch=item.get("default_branch", "main"),
        keyword=keyword,
        suggested_section=section,
        suggested_markdown=project_markdown(),
    )


def pr_template() -> str:
    return f"""## Summary

Add **{PROJECT['name']}** to this Awesome list.

{PROJECT['description']}

## Why it fits

- Works with popular AI coding environments: Claude Code, Codex CLI, Gemini CLI, Cursor, and Windsurf.
- Provides drop-in skill files and adapter rules, so users can integrate it without building a custom agent framework first.
- Reduces hallucinated "done" claims through verification-first workflows, evidence gates, and source-linked Obsidian notes.
- Helps long-running AI work retain context through a persistent knowledge base instead of relying only on chat history.

## Suggested entry

```md
{project_markdown()}
```

## Checklist

- [ ] I added the entry to the most relevant section.
- [ ] The description is concise and neutral.
- [ ] The repository is open source and directly useful to this list's audience.
"""


def write_outputs(candidates: list[Candidate], output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    (output_dir / "awesome-pr-template.md").write_text(pr_template(), encoding="utf-8")
    (output_dir / "awesome-candidates.json").write_text(
        json.dumps([asdict(c) for c in candidates], ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    lines = [
        "# Awesome List PR Targets",
        "",
        "Use this file to review candidate repositories before opening PRs.",
        "",
        f"Suggested entry:",
        "",
        "```md",
        project_markdown(),
        "```",
        "",
        "## Candidates",
        "",
    ]
    for candidate in candidates:
        lines.extend(
            [
                f"### {candidate.full_name}",
                "",
                f"- URL: {candidate.html_url}",
                f"- Stars: {candidate.stars}",
                f"- Matched keyword: `{candidate.keyword}`",
                f"- Suggested section: `{candidate.suggested_section}`",
                f"- Default branch: `{candidate.default_branch}`",
                f"- Description: {candidate.description or '(none)'}",
                "",
            ]
        )
    (output_dir / "awesome-pr-targets.md").write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Search GitHub for high-star Awesome lists and prepare PR copy."
    )
    parser.add_argument(
        "--keywords",
        nargs="+",
        default=DEFAULT_KEYWORDS,
        help="Search keywords. Defaults to Awesome-Cursor, Awesome-Claude-Prompt, Awesome-LLM-Agents.",
    )
    parser.add_argument("--min-stars", type=int, default=500)
    parser.add_argument("--per-page", type=int, default=10)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("outreach") / "awesome-lists",
    )
    parser.add_argument(
        "--token-env",
        default="GITHUB_TOKEN",
        help="Environment variable containing a GitHub API token.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    token = os.getenv(args.token_env)
    if not token:
        print(
            f"Warning: {args.token_env} is not set. Unauthenticated GitHub API calls "
            "are heavily rate-limited.",
            file=sys.stderr,
        )

    headers = build_headers(token)
    seen: set[str] = set()
    candidates: list[Candidate] = []

    try:
        for keyword in args.keywords:
            items = search_repositories(keyword, args.min_stars, args.per_page, headers)
            for item in items:
                full_name = item.get("full_name")
                if not full_name or full_name in seen:
                    continue
                if not is_awesome_list_repo(item):
                    continue
                seen.add(full_name)
                candidates.append(make_candidate(item, keyword, headers))
    except GitHubApiError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    candidates.sort(key=lambda c: c.stars, reverse=True)
    write_outputs(candidates, args.output_dir)
    print(f"Found {len(candidates)} candidate repositories.")
    print(f"Wrote outputs to: {args.output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
