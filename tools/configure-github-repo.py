#!/usr/bin/env python3
"""
Configure GitHub repository metadata for discovery.

Dry-run by default:
  python tools/configure-github-repo.py

Apply with a token that can administer the repository:
  $env:GITHUB_TOKEN="ghp_your_token_here"
  python tools/configure-github-repo.py --apply
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any


GITHUB_API = "https://api.github.com"
DEFAULT_REPO = "Mark393295827/third-brain-v5-skills"
DEFAULT_DESCRIPTION = (
    "Third Brain V5 - 17 Agent Skills for Claude/Codex/Cursor | "
    "Persistent Knowledge OS + verification-first AI workflows"
)
DEFAULT_TOPICS = [
    "agent-skills",
    "ai-agents",
    "codex-cli",
    "claude-code",
    "gemini-cli",
    "cursor",
    "windsurf",
    "llm-wiki",
    "cognitive-os",
    "knowledge-management",
    "personal-knowledge-base",
    "prompt-engineering",
    "context-engineering",
    "obsidian",
    "multi-agent",
    "behavior-design",
    "verification",
    "startup-evaluation",
]


class GitHubApiError(RuntimeError):
    """Raised when a GitHub API call fails."""


def headers(token: str | None) -> dict[str, str]:
    result = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "third-brain-repo-configurator",
    }
    if token:
        result["Authorization"] = f"Bearer {token}"
    return result


def github_request(
    path: str,
    token: str | None,
    method: str = "GET",
    payload: dict[str, Any] | None = None,
    retries: int = 2,
) -> Any:
    body = None
    request_headers = headers(token)
    if payload is not None:
        body = json.dumps(payload).encode("utf-8")
        request_headers["Content-Type"] = "application/json"

    for attempt in range(retries + 1):
        try:
            request = urllib.request.Request(
                f"{GITHUB_API}{path}",
                data=body,
                headers=request_headers,
                method=method,
            )
            with urllib.request.urlopen(request, timeout=30) as response:
                remaining = response.headers.get("x-ratelimit-remaining")
                if remaining == "0":
                    reset = int(response.headers.get("x-ratelimit-reset", "0"))
                    wait = max(0, reset - int(time.time()))
                    raise GitHubApiError(
                        f"GitHub API rate limit exhausted. Retry after {wait}s."
                    )
                raw = response.read().decode("utf-8")
                return json.loads(raw) if raw else {}
        except urllib.error.HTTPError as exc:
            body_text = exc.read().decode("utf-8", errors="replace")
            if exc.code in {403, 429, 500, 502, 503, 504} and attempt < retries:
                time.sleep(2**attempt)
                continue
            raise GitHubApiError(f"GitHub API HTTP {exc.code}: {body_text}") from exc
        except (urllib.error.URLError, TimeoutError) as exc:
            if attempt < retries:
                time.sleep(2**attempt)
                continue
            raise GitHubApiError(f"GitHub API network error: {exc}") from exc


def parse_topics(raw_topics: list[str]) -> list[str]:
    topics: list[str] = []
    for item in raw_topics:
        for topic in item.split(","):
            cleaned = topic.strip().lower()
            if cleaned and cleaned not in topics:
                topics.append(cleaned)
    return topics


def write_report(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Dry-run or apply GitHub description/topics for discovery."
    )
    parser.add_argument("--repo", default=DEFAULT_REPO)
    parser.add_argument("--description", default=DEFAULT_DESCRIPTION)
    parser.add_argument("--topics", nargs="*", default=DEFAULT_TOPICS)
    parser.add_argument("--token-env", default="GITHUB_TOKEN")
    parser.add_argument("--apply", action="store_true")
    parser.add_argument(
        "--replace-topics",
        action="store_true",
        help="Replace existing topics instead of preserving them and adding recommendations.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("outreach") / "github-repo-setup.json",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    token = os.getenv(args.token_env)
    recommended_topics = parse_topics(args.topics)

    if args.apply and not token:
        print(f"Error: --apply requires {args.token_env}.", file=sys.stderr)
        return 2

    try:
        repo_data = github_request(f"/repos/{args.repo}", token)
        topic_data = github_request(f"/repos/{args.repo}/topics", token)
    except GitHubApiError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    current_description = repo_data.get("description") or ""
    current_topics = topic_data.get("names", [])
    target_topics = (
        recommended_topics
        if args.replace_topics
        else parse_topics([*current_topics, *recommended_topics])
    )
    plan = {
        "repo": args.repo,
        "mode": "apply" if args.apply else "dry-run",
        "description": {
            "current": current_description,
            "target": args.description,
            "changed": current_description != args.description,
        },
        "topics": {
            "current": current_topics,
            "recommended": recommended_topics,
            "target": target_topics,
            "added": [topic for topic in target_topics if topic not in current_topics],
            "removed": [topic for topic in current_topics if topic not in target_topics],
            "changed": sorted(current_topics) != sorted(target_topics),
            "replace": args.replace_topics,
        },
    }

    if args.apply:
        if plan["description"]["changed"]:
            github_request(
                f"/repos/{args.repo}",
                token,
                method="PATCH",
                payload={"description": args.description},
            )
        if plan["topics"]["changed"]:
            github_request(
                f"/repos/{args.repo}/topics",
                token,
                method="PUT",
                payload={"names": target_topics},
            )
        plan["applied"] = True
    else:
        plan["applied"] = False
        plan["next_command"] = (
            f"$env:{args.token_env}=\"ghp_your_token_here\"; "
            "python tools\\configure-github-repo.py --apply"
        )

    write_report(args.output, plan)
    print(f"Wrote repo setup report to: {args.output}")
    if not args.apply:
        print("Dry-run only. Re-run with --apply and a token to update GitHub.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
