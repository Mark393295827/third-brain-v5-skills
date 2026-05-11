# Workflow: Verified Code Session

## Before

An agent says a bug is fixed based only on edited code or intuition.

## Input

```text
Source: a bug report, failing test, CI error, or user-reported symptom.
Goal: make completion claims depend on fresh verification evidence.
```

## Prompt

```text
Use verify-before-claim for this fix.

Before saying the issue is fixed:
1. identify the command or manual check that proves the fix
2. run the full command fresh
3. read the output and exit code
4. summarize the evidence
5. only then state the actual status

If verification fails, do not soften it. State the failure and the next concrete fix.
```

## After

The session ends with evidence:

- command run
- exit code
- pass/fail count
- remaining risk or unverified edge cases

## Output Example

```text
Command: npm test
Exit code: 0
Result: 42 passed, 0 failed
Residual risk: browser-specific behavior not covered by unit tests
```

## Verification

The response should avoid completion language unless it includes fresh evidence.
