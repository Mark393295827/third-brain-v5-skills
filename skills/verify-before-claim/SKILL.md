---
name: verify-before-claim
description: Iron rule — no completion claims without fresh verification evidence. Use whenever about to claim work is done, fixed, working, or passing. Run verification commands and show output before making any success statement.
---

# Verify Before Claim

**NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE.**

## When to Use

- Before saying "done", "fixed", "complete", "passing", "working"
- Before committing or creating a PR
- Before expressing satisfaction with results
- When the user asks "is it working?"
- Any time the agent feels the urge to say "it should work"

## The Gate Function

```
BEFORE claiming any status:

1. IDENTIFY: What command proves this claim?
2. RUN: Execute the FULL command (fresh, complete)
3. READ: Full output, check exit code, count failures
4. VERIFY: Does output confirm the claim?
   - If NO: State actual status with evidence
   - If YES: State claim WITH evidence
5. ONLY THEN: Make the claim
```

**Skip any step = lying, not verifying.**

## Common Failures

| Claim | Requires | Not Sufficient |
|-------|----------|----------------|
| Tests pass | Test output: 0 failures | Previous run, "should pass" |
| Linter clean | Linter output: 0 errors | Partial check |
| Build succeeds | Build exit code 0 | "Looks good" |
| Bug fixed | Reproduce original symptom: passes | "I changed the code" |
| Tests added | New tests exist + old tests still pass | "Tests should work" |

## Red Flags — STOP

- Using "should", "probably", "seems to" about completion
- Expressing satisfaction before verification ("Great!", "Perfect!", "Done!")
- About to commit/push/PR without verification
- Trusting agent success reports without independent check
- Relying on partial verification
- **ANY wording implying success without having run verification**

## Rationalization Prevention

| Excuse | Reality |
|--------|---------|
| "Should work now" | RUN the verification |
| "I'm confident" | Confidence ≠ evidence |
| "Just this once" | No exceptions |
| "Different context so rule doesn't apply" | Spirit over letter |

## SOP TDD Context

This skill is the verification component of the TDD-for-SOPs approach. Before writing a new SOP:

1. **Define failure**: What will the agent do wrong without the SOP?
2. **Watch it fail**: Verify the baseline error exists (RED)
3. **Write the SOP**: Address those specific failure modes
4. **Watch it pass**: Verify the agent now complies (GREEN)
5. **Refactor**: Close loopholes while maintaining compliance

## Quality Gates

- [ ] Verification command identified and run
- [ ] Full output shown (exit code, failure count)
- [ ] Claim only made WITH evidence
- [ ] No "should", "probably", "I think" on completion status
