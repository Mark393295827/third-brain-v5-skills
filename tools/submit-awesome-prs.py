#!/usr/bin/env python3
"""
Prepare or submit value-first Awesome-list pull requests.

Dry-run by default:
  python tools/submit-awesome-prs.py --limit 3

Apply with a token that can fork repositories and open pull requests:
  $env:GITHUB_TOKEN="ghp_your_token_here"
  python tools/submit-awesome-prs.py --limit 3 --apply

The script only targets repositories already discovered by
tools/find-awesome-pr-targets.py. It skips repositories whose README already
mentions Third Brain V5 Skills.
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


GITHUB_API = "https://api.github.com"
DEFAULT_CANDIDATES = Path("outreach") / "awesome-lists" / "awesome-candidates.json"
DEFAULT_TEMPLATE = Path("outreach") / "awesome-lists" / "awesome-pr-template.md"
DEFAULT_REPORT = Path("outreach") / "awesome-lists" / "awesome-pr-runbook.md"
DEFAULT_STATE = Path("outreach") / "awesome-lists" / "awesome-pr-runbook.json"
PROJECT_URL = "https://github.com/Mark393295827/third-brain-v5-skills"
PROJECT_ENTRY = (
    "- [Third Brain V5 Skills](https://github.com/Mark393295827/third-brain-v5-skills) "
    "- Production-ready Agent Skills for Claude Code, Codex, Gemini, Cursor, and "
    "Windsurf. Adds Obsidian-backed persistent memory, verification-first workflows "
    "to reduce hallucinated completion claims, context/cost control, and multi-agent "
    "orchestration."
)
BRANCH_NAME = "add-third-brain-v5-skills"
PR_TITLE = "Add Third Brain V5 Skills"


class GitHubApiError(RuntimeError):
    """Raised when GitHub API access fails."""


def headers(token: str | None) -> dict[str, str]:
    result = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "third-brain-awesome-pr-submitter",
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


def load_json(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        raise FileNotFoundError(f"Missing candidate file: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def load_cached_results(path: Path) -> dict[str, dict[str, Any]]:
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}
    return {item.get("repo", ""): item for item in data.get("results", []) if item.get("repo")}


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


def prioritized(candidates: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(
        candidates,
        key=lambda item: (candidate_priority(item), int(item.get("stars", 0))),
        reverse=True,
    )


def fetch_readme(full_name: str, token: str | None) -> dict[str, Any]:
    return github_request(f"/repos/{full_name}/readme", token)


def decode_content(encoded: str) -> str:
    return base64.b64decode(encoded).decode("utf-8", errors="replace")


def encode_content(content: str) -> str:
    return base64.b64encode(content.encode("utf-8")).decode("ascii")


def heading_level(line: str) -> int:
    match = re.match(r"^(#+)\s+", line)
    return len(match.group(1)) if match else 0


def normalize_heading(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()


def find_heading(lines: list[str], suggested_section: str) -> int | None:
    wanted = normalize_heading(suggested_section)
    wanted_tokens = [token for token in wanted.split() if len(token) > 2]
    fallback: int | None = None

    for index, line in enumerate(lines):
        if not heading_level(line):
            continue
        normalized = normalize_heading(line.lstrip("#").strip())
        if normalized == wanted:
            return index
        if wanted_tokens and all(token in normalized for token in wanted_tokens[:3]):
            fallback = index

    return fallback


def insert_entry(readme: str, suggested_section: str) -> tuple[str, str]:
    if PROJECT_URL.lower() in readme.lower() or "third brain v5 skills" in readme.lower():
        return readme, "already-present"

    lines = readme.splitlines()
    heading_index = find_heading(lines, suggested_section)
    if heading_index is None:
        new_lines = lines + ["", "## AI Agent Tools", "", PROJECT_ENTRY]
        return "\n".join(new_lines).rstrip() + "\n", "appended-new-section"

    level = heading_level(lines[heading_index])
    section_end = len(lines)
    for index in range(heading_index + 1, len(lines)):
        current_level = heading_level(lines[index])
        if current_level and current_level <= level:
            section_end = index
            break

    insert_at = section_end
    while insert_at > heading_index + 1 and lines[insert_at - 1].strip() == "":
        insert_at -= 1

    new_lines = lines[:insert_at] + [PROJECT_ENTRY] + lines[insert_at:]
    return "\n".join(new_lines).rstrip() + "\n", f"inserted-under:{lines[heading_index].strip()}"


def wait_for_fork(full_name: str, token: str, attempts: int = 10) -> None:
    for attempt in range(attempts):
        try:
            github_request(f"/repos/{full_name}", token, retries=0)
            return
        except GitHubApiError:
            time.sleep(min(2 + attempt, 10))
    raise GitHubApiError(f"Fork was not available after waiting: {full_name}")


def ensure_branch(fork: str, upstream: str, base_branch: str, token: str) -> None:
    upstream_ref = github_request(
        f"/repos/{upstream}/git/ref/heads/{urllib.parse.quote(base_branch)}", token
    )
    sha = upstream_ref["object"]["sha"]
    try:
        github_request(
            f"/repos/{fork}/git/refs",
            token,
            method="POST",
            payload={"ref": f"refs/heads/{BRANCH_NAME}", "sha": sha},
        )
    except GitHubApiError as exc:
        if "Reference already exists" not in str(exc):
            raise


def submit_pr(
    candidate: dict[str, Any],
    token: str,
    pr_body: str,
    allow_new_section: bool,
) -> dict[str, Any]:
    upstream = candidate["full_name"]
    owner, repo_name = upstream.split("/", 1)
    user = github_request("/user", token)["login"]
    fork = f"{user}/{repo_name}"
    default_branch = candidate.get("default_branch") or "main"

    github_request(f"/repos/{upstream}/forks", token, method="POST", payload={})
    wait_for_fork(fork, token)
    ensure_branch(fork, upstream, default_branch, token)

    readme = fetch_readme(upstream, token)
    readme_path = readme["path"]
    updated, mode = insert_entry(
        decode_content(readme["content"]),
        candidate.get("suggested_section") or "AI Agent Tools",
    )
    if mode == "already-present":
        return {"repo": upstream, "status": "skipped", "reason": mode}
    if mode == "appended-new-section" and not allow_new_section:
        return {
            "repo": upstream,
            "status": "needs-review",
            "reason": "No matching section found; rerun with --allow-new-section if appropriate.",
        }

    fork_readme = github_request(
        f"/repos/{fork}/contents/{urllib.parse.quote(readme_path)}"
        f"?ref={urllib.parse.quote(BRANCH_NAME)}",
        token,
    )
    github_request(
        f"/repos/{fork}/contents/{urllib.parse.quote(readme_path)}",
        token,
        method="PUT",
        payload={
            "message": "Add Third Brain V5 Skills",
            "content": encode_content(updated),
            "sha": fork_readme["sha"],
            "branch": BRANCH_NAME,
        },
    )
    pr = github_request(
        f"/repos/{upstream}/pulls",
        token,
        method="POST",
        payload={
            "title": PR_TITLE,
            "head": f"{user}:{BRANCH_NAME}",
            "base": default_branch,
            "body": pr_body,
            "maintainer_can_modify": True,
        },
    )
    return {"repo": upstream, "status": "opened", "url": pr.get("html_url"), "mode": mode}


def make_runbook(results: list[dict[str, Any]], apply: bool, limit: int) -> str:
    lines = [
        "# Awesome PR Runbook",
        "",
        f"Mode: {'apply' if apply else 'dry-run'}",
        "",
        "Suggested entry:",
        "",
        "```md",
        PROJECT_ENTRY,
        "```",
        "",
        "## Results",
        "",
    ]
    for result in results:
        lines.extend(
            [
                f"### {result['repo']}",
                "",
                f"- Status: {result['status']}",
                f"- Action: {result.get('mode') or result.get('reason') or 'n/a'}",
            ]
        )
        if result.get("note"):
            lines.append(f"- Note: {result['note']}")
        if result.get("url"):
            lines.append(f"- PR: {result['url']}")
        if result.get("preview_path"):
            lines.append(f"- Preview: {result['preview_path']}")
        lines.append("")
    if not apply:
        lines.extend(
            [
                "## Apply",
                "",
                "```powershell",
                '$env:GITHUB_TOKEN="ghp_your_token_here"',
                f"python tools\\submit-awesome-prs.py --limit {limit} --apply",
                "```",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Prepare or submit Awesome-list PRs for Third Brain V5 Skills."
    )
    parser.add_argument("--candidates", type=Path, default=DEFAULT_CANDIDATES)
    parser.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--state", type=Path, default=DEFAULT_STATE)
    parser.add_argument("--token-env", default="GITHUB_TOKEN")
    parser.add_argument("--limit", type=int, default=3)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument(
        "--allow-new-section",
        action="store_true",
        help="Allow PRs that append a new section when no relevant heading is found.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    token = os.getenv(args.token_env)
    if args.apply and not token:
        print(f"Error: --apply requires {args.token_env}.", file=sys.stderr)
        return 2

    try:
        candidates = prioritized(load_json(args.candidates))[: args.limit]
    except (FileNotFoundError, json.JSONDecodeError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    pr_body = args.template.read_text(encoding="utf-8") if args.template.exists() else ""
    cached_results = load_cached_results(args.state)
    preview_dir = args.report.parent / "previews"
    preview_dir.mkdir(parents=True, exist_ok=True)
    results: list[dict[str, Any]] = []

    for candidate in candidates:
        try:
            if args.apply:
                results.append(
                    submit_pr(candidate, token or "", pr_body, args.allow_new_section)
                )
                continue

            readme = fetch_readme(candidate["full_name"], token)
            updated, mode = insert_entry(
                decode_content(readme["content"]),
                candidate.get("suggested_section") or "AI Agent Tools",
            )
            preview_path = preview_dir / (
                candidate["full_name"].replace("/", "__") + "__README.preview.md"
            )
            preview_path.write_text(updated, encoding="utf-8")
            status = "needs-review" if mode == "appended-new-section" else "prepared"
            results.append(
                {
                    "repo": candidate["full_name"],
                    "status": status,
                    "mode": mode,
                    "preview_path": str(preview_path),
                }
            )
        except GitHubApiError as exc:
            preview_path = preview_dir / (
                candidate.get("full_name", "(unknown)").replace("/", "__")
                + "__README.preview.md"
            )
            if not args.apply and preview_path.exists():
                cached = cached_results.get(candidate.get("full_name", ""), {})
                results.append(
                    {
                        "repo": candidate.get("full_name", "(unknown)"),
                        "status": cached.get("status", "cached-preview"),
                        "mode": cached.get("mode", "cached-preview"),
                        "note": "GitHub API was rate-limited; reused the existing preview.",
                        "preview_path": str(preview_path),
                    }
                )
            else:
                results.append(
                    {
                        "repo": candidate.get("full_name", "(unknown)"),
                        "status": "error",
                        "reason": str(exc),
                    }
                )

    args.report.write_text(make_runbook(results, args.apply, args.limit), encoding="utf-8")
    args.state.write_text(
        json.dumps({"mode": "apply" if args.apply else "dry-run", "results": results}, indent=2),
        encoding="utf-8",
    )
    print(f"Wrote Awesome PR runbook to: {args.report}")
    return 0 if all(item["status"] != "error" for item in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
