#!/usr/bin/env python3
"""Validate the minimum control fields required before an agent loop starts."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


REQUIRED = {
    "objective",
    "scope",
    "non-goals",
    "owner",
    "inputs",
    "state path",
    "success metric",
    "evidence",
    "verifier",
    "topology",
    "max iterations",
    "time limit",
    "budget",
    "stop condition",
    "write-back",
    "permission boundary",
    "recovery",
}
VALID_TOPOLOGIES = {"single-agent", "maker-checker", "manager-workers"}
EMPTY_MARKERS = {"", "-", "n/a", "na", "none", "tbd", "todo", "unknown"}
FIELD_RE = re.compile(r"^\s*(?:[-*+]\s+)?(?:\*\*)?([^:*]+?)(?:\*\*)?\s*:\s*(.+?)\s*$")


def normalize(field: str) -> str:
    return re.sub(r"\s+", " ", field.strip().lower())


def parse_contract(path: Path) -> dict[str, str]:
    fields: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        match = FIELD_RE.match(line)
        if match:
            fields[normalize(match.group(1))] = match.group(2).strip()
    return fields


def validate(fields: dict[str, str], strict: bool) -> list[str]:
    errors: list[str] = []
    for field in sorted(REQUIRED):
        value = fields.get(field, "")
        if normalize(value) in EMPTY_MARKERS:
            errors.append(f"missing or empty field: {field}")

    topology = normalize(fields.get("topology", "")).rstrip(".")
    if topology and topology not in VALID_TOPOLOGIES:
        errors.append("topology must be single-agent, maker-checker, or manager-workers")

    for field in ("max iterations", "time limit", "budget"):
        value = normalize(fields.get(field, ""))
        if value and not re.search(r"\d", value):
            errors.append(f"{field} must contain a finite numeric cap")

    stop = normalize(fields.get("stop condition", ""))
    if any(phrase in stop for phrase in ("until satisfied", "keep improving", "run forever", "infinite")):
        errors.append("stop condition must be an evidence-based result or finite cap")

    verifier = normalize(fields.get("verifier", ""))
    if "self" in verifier or "same builder" in verifier:
        errors.append("verifier cannot be the builder alone")

    boundary = normalize(fields.get("permission boundary", ""))
    high_risk_boundary = re.search(r"\b(production|deploy|publish|external|shared)\b", boundary)
    explicitly_denied = re.search(
        r"\b(no|not|without|deny|denied)\b.{0,32}\b(production|deploy|publish|external|shared)\b",
        boundary,
    )
    if high_risk_boundary and not explicitly_denied:
        if "approval" not in boundary or "rollback" not in boundary:
            errors.append("external or production boundary requires approval and rollback")

    if strict and topology == "manager-workers":
        if "integration" not in normalize(fields.get("recovery", "")) and "integration" not in boundary:
            errors.append("manager-workers requires an integration rule in recovery or permission boundary")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("contract", type=Path)
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    if not args.contract.is_file():
        parser.error(f"contract does not exist: {args.contract}")

    fields = parse_contract(args.contract)
    errors = validate(fields, args.strict)
    result = {"contract": str(args.contract), "valid": not errors, "errors": errors}

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    elif errors:
        print("FAIL loop contract")
        for error in errors:
            print(f"- {error}")
    else:
        print("PASS loop contract")
        print(f"- fields: {len(fields)}")
        print(f"- topology: {normalize(fields['topology']).rstrip('.')}")
        print(f"- stop condition: {fields['stop condition']}")

    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
