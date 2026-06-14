---
name: api-error-triage
trigger: "When an API call is failing and the user needs a systematic diagnosis"
tags: [debug, api, networking]
---

# API Error Triage

## Goal
Locate the layer where an API call breaks, methodically.

## Checklist
1. Capture the exact failure: status code, error body, and timestamp.
2. Classify by status: 4xx → likely request/auth/client; 5xx → likely server/upstream.
3. Verify the request: URL, method, headers, auth token presence (never print the token).
4. Reproduce with a minimal call (curl or one isolated request).
5. Check the obvious culprits in order: auth → payload shape → endpoint/version → rate limit → upstream status.
6. Confirm the root cause with evidence before proposing a fix.

## Anti-patterns
- Never retry blindly hoping it works.
- Never print or paste secrets/tokens into logs or output.
- Never guess the cause without reproducing the failure.
