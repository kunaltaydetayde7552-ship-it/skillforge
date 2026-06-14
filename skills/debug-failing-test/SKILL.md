---
name: debug-failing-test
trigger: "When a test is failing and the user wants the root cause, not a quick patch"
tags: [debug, testing, ci]
---

# Debug a Failing Test

## Goal
Find the *actual* cause of a failing test before changing any code.

## Checklist
1. Read the full failure output, including the stack trace — do not skim.
2. Reproduce the failure locally with a single, isolated test run.
3. State the expected vs actual behavior in one sentence each.
4. Form one hypothesis. Add a temporary log/assert to confirm or reject it.
5. Only after the cause is confirmed, propose the smallest fix.
6. Re-run the full suite to ensure no regression.

## Anti-patterns
- Do NOT change code based on a guess before reproducing the failure.
- Do NOT disable, skip, or comment out the test to make it "pass".
- Do NOT fix symptoms (e.g. loosening an assertion) instead of the cause.
