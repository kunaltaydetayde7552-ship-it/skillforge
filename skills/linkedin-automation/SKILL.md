---
name: linkedin-automation
trigger: "When the user wants to interact with LinkedIn programmatically — profiles, search, messaging, connections, or posts — via Linked API"
tags: [linkedin, automation, api, integration]
---

# LinkedIn Automation (Linked API)

## Goal
Drive LinkedIn actions (fetch profiles/companies, search, message, manage connections, post/react/comment) through the `linkedin` CLI, which runs a real cloud browser via Linked API — never by scraping directly.

## Setup
1. Check the CLI is available: `linkedin --version`. If missing, install it with `npm install -g @linkedapi/linkedin-cli`.
2. If a command fails with exit code 2 (auth error), the account isn't set up yet: have the user sign up at Linked API's dashboard, connect their LinkedIn account, and copy the Linked API Token and Identification Token.
3. Register the tokens once: `linkedin setup --linked-api-token=TOKEN --identification-token=TOKEN`.

## Checklist
1. Append `--json -q` to every call for machine-readable, quiet output.
2. Check the `success` field in the JSON body, not just the process exit code — exit 0 can still wrap a failed action (e.g. `personNotFound`).
3. Expect latency: each call drives a real browser session, from ~30 seconds to several minutes. Don't retry impatiently or assume a hang.
4. Wrap message, post, and comment text in single quotes to avoid shell interpretation of special characters.
5. Respect account-level rate/action limits; a `limitExceeded` (or similar) error means stop and report, not retry.
6. Confirm explicitly with the user before any write action (connection request, message, post, react, comment) — these are visible and largely irreversible on LinkedIn.
7. For anything beyond a single ad-hoc action — bulk outreach, scheduled/recurring campaigns, mass connection requests — stop and get explicit, informed confirmation first; this crosses into automated mass-messaging territory that can violate LinkedIn's terms.

## Anti-patterns
- Never send connection requests, messages, or posts in bulk without the user's explicit, per-batch confirmation.
- Never print, log, or echo the Linked API token or Identification token.
- Never treat a non-error exit code as success — always check the `success` field in the response.
- Never scrape LinkedIn pages directly; always route actions through the `linkedin` CLI.
