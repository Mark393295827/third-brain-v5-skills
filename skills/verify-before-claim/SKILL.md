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

## Expected Value Thinking (From Poker Psychology)

> "The biggest bluff is convincing yourself you have control when you don't." — Maria Konnikova

**Apply to verification:**

| Poker Concept | Verification Application |
|---------------|-------------------------|
| **Expected Value (EV)** | Don't just check if it works now; check if it will work reliably |
| **Controllable vs Uncontrollable** | Focus on what you can verify; acknowledge what you can't |
| **Tilt Control** | Don't let excitement about "it works!" skip verification |
| **Process over Results** | Good verification process > lucky outcome |

**The verification mindset:**

```
1. Separate what you CAN verify from what you CAN'T
   - CAN: Code compiles, tests pass, output matches expected
   - CAN'T: Edge cases, production behavior, user experience

2. Focus on EXPECTED VALUE, not single results
   - "Tests pass once" ≠ "Tests will pass reliably"
   - "Works in my environment" ≠ "Works in all environments"

3. Be skeptical of success
   - Good decisions can have bad outcomes
   - Bad decisions can have good outcomes
   - KEY: Evaluate the PROCESS, not just the result
```

**The Biggest Lesson from Poker:**
> "Knowing when to fold is more important than knowing when to play."

In verification: Knowing when to say "I'm not sure" is better than claiming "it works" without evidence.
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
