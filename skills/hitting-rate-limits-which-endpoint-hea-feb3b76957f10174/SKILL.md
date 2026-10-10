---
name: "hitting-rate-limits-which-endpoint-hea-feb3b76957f10174"
description: "Symptom: intermittent 429s. Cause: one hot endpoint or one misbehaving client. Confirmation: rate-limit response headers plus the tenant's rate-limit log events identify the endpoint and the caller. Not the full reference manual."
metadata:
  skill_id: "skl_gKDtQi3qO17p5ad5ItgrHQ"
  title: "Hitting rate limits: which endpoint, headers, and log events to read"
  version: "skv_z_S0moBchOsBQHfrOqkcbw"
  updated: "2026-10-03T13:57:17.48055+00:00"
  canonical_url: "https://vectle.com/skills/skl_gKDtQi3qO17p5ad5ItgrHQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** Symptom: intermittent 429s. Cause: one hot endpoint or one misbehaving client. Confirm - Response headers on the 429: Retry-After and Auth0's rate-limit headers name the limit and reset. - Monitoring > Logs: filter for rate-limit event types. Verify Re-run the offending workload and watch the rate-limit events go quiet.

## The fix

1. /oauth/token hammered by M2M code minting per request.

2. /dbconnections/signup or passwordless endpoints hit by a retry loop or a bot.

3. Management API paginated listing without backoff.

4. Load test or bulk import against the wrong tenant.

5. Response headers on the 429: `Retry-After` and Auth0's rate-limit headers name the limit and reset.

6. Monitoring > Logs: filter for rate-limit event types. The events name the endpoint and the client. One client dominating = fix the client, not the tenant.

7. Correlate timestamps with deploys or cron jobs; a new 429 that starts at 02:00 is a batch job.

8. Token caching with single-flight for /oauth/token.

9. Exponential backoff with jitter on 429; honor Retry-After.

10. Self-throttle UI resends (passwordless, reset) with countdowns.

11. Management API: page slowly, cache, and use the `include_totals=false` where supported.

## When to use this

- This covers exactly what the title says: Hitting rate limits.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Hitting; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current Hitting behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_gKDtQi3qO17p5ad5ItgrHQ). Version: `skv_z_S0moBchOsBQHfrOqkcbw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
