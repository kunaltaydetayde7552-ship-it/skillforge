---
name: ship-web-app
trigger: "When the user wants to deploy or ship a web application to production"
tags: [deploy, web, ci, release]
---

# Ship a Web App

## Goal
Get a web app to production safely, with no skipped safety checks.

## Checklist
1. Confirm the target environment out loud (staging vs production). Never assume production.
2. Verify the working tree is clean and on the intended branch/commit.
3. Run the full test suite. If anything fails, STOP and report — do not deploy.
4. Run the build. Treat build warnings as signals, not noise.
5. Check environment variables / secrets exist for the target env (presence only, never print values).
6. Deploy. Capture the deploy command output.
7. Run a post-deploy smoke check (health endpoint or homepage load).
8. Report: what was deployed, where, and the smoke-check result.

## Anti-patterns
- Never deploy with failing or skipped tests.
- Never print, log, or echo secret values.
- Never deploy directly to production without confirming the environment first.
- Never declare success without a post-deploy check.
