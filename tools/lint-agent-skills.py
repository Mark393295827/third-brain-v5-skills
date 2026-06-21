#!/usr/bin/env python3
"""
Validate Third Brain V5 skills against the Agent Skills open-format standard.

Usage:
  python tools/lint-agent-skills.py
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
MAX_SKILL_LINES = 500
ALLOWED_TOP_LEVEL = {"SKILL.md", "scripts", "references", "assets", "agents"}
REQUIRED_FRONTMATTER = ["name", "description", "assumes", "conflicts_with"]
REQUIRED_SECTIONS = ["## Usage Template", "## Success Metrics", "## Quality Gates"]


@dataclass
class Issue:
    path: Path
    message: str


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    raw = text[4:end]
    body = text[end + 5 :]
    data: dict[str, str] = {}
    in_metadata = False
    for line in raw.splitlines():
        if line.strip() == "metadata:":
            in_metadata = True
            continue
        if line and not line[0].isspace():
            in_metadata = False
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        normalized_key = key.strip()
        if in_metadata and line[0].isspace():
            normalized_key = f"metadata.{normalized_key}"
        data[normalized_key] = value.strip().strip('"').strip("'")
    return data, body


def frontmatter_value(frontmatter: dict[str, str], key: str) -> str:
    return frontmatter.get(key) or frontmatter.get(f"metadata.{key}", "")


def check_skill(skill_dir: Path) -> list[Issue]:
    issues: list[Issue] = []
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.exists():
        return [Issue(skill_dir, "missing SKILL.md")]

    text = skill_file.read_text(encoding="utf-8")
    frontmatter, body = parse_frontmatter(text)
    lines = text.splitlines()

    if len(lines) > MAX_SKILL_LINES:
        issues.append(
            Issue(
                skill_file,
                f"SKILL.md has {len(lines)} lines; move details into references/ before {MAX_SKILL_LINES}",
            )
        )

    for key in REQUIRED_FRONTMATTER:
        if not frontmatter_value(frontmatter, key):
            issues.append(Issue(skill_file, f"frontmatter missing {key}"))

    name = frontmatter.get("name")
    if name and name != skill_dir.name:
        issues.append(Issue(skill_file, f"name '{name}' does not match folder '{skill_dir.name}'"))

    description = frontmatter.get("description")
    if description and "Use when" not in description:
        issues.append(Issue(skill_file, "description must include an explicit 'Use when' trigger"))

    if not re.search(r"^#\s+\S+", body, flags=re.MULTILINE):
        issues.append(Issue(skill_file, "missing top-level title"))

    for section in REQUIRED_SECTIONS:
        if section not in text:
            issues.append(Issue(skill_file, f"missing required section: {section}"))

    for child in skill_dir.iterdir():
        if child.name not in ALLOWED_TOP_LEVEL:
            issues.append(Issue(child, "unexpected file or folder inside skill directory"))

    return issues


def main() -> int:
    if not SKILLS_DIR.exists():
        print(f"Missing skills directory: {SKILLS_DIR}", file=sys.stderr)
        return 2

    issues: list[Issue] = []
    for skill_dir in sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir()):
        issues.extend(check_skill(skill_dir))

    if issues:
        print("Agent Skills lint failed:")
        for issue in issues:
            print(f"- {issue.path.relative_to(ROOT)}: {issue.message}")
        return 1

    count = len([path for path in SKILLS_DIR.iterdir() if path.is_dir()])
    print(f"Agent Skills lint passed for {count} skills.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
