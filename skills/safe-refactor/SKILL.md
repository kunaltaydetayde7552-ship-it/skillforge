---
name: safe-refactor
trigger: "When the user wants to refactor code without changing its external behavior"
tags: [refactor, quality, testing]
---

# Safe Refactor

## Goal
Improve internal structure while keeping observable behavior identical.

## Checklist
1. Identify the exact scope. List the files/functions in, and explicitly state what is out.
2. Ensure tests cover the behavior. If coverage is thin, add characterization tests FIRST.
3. Make one small, mechanical change at a time. Re-run tests after each.
4. Keep public interfaces stable unless the user explicitly approved a breaking change.
5. Do not mix refactor with feature changes in the same step.
6. Summarize what structurally changed and confirm behavior is unchanged.

## Anti-patterns
- Never refactor without a passing test net.
- Never sneak in behavior or feature changes during a refactor.
- Never do a large rewrite when small steps are possible.
