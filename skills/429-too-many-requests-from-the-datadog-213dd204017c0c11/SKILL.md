---
name: "429-too-many-requests-from-the-datadog-213dd204017c0c11"
description: "Datadog answers 429 Too Many Requests when you exceed API rate limits. Back off, honor Retry-After, and stop hammering the endpoint that throttled you. Not the full reference manual."
metadata:
  skill_id: "skl_HMgWvmeAoowYlw3fXhb9mA"
  title: "429 Too Many Requests from the Datadog API: back off with jitter, then reduce calls"
  version: "skv_EURzIe2JRI87c2nT2ICewg"
  updated: "2026-10-03T04:42:16.664883+00:00"
  canonical_url: "https://vectle.com/skills/skl_HMgWvmeAoowYlw3fXhb9mA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.datadoghq.com/api/latest/monitors/\"]"
---

**TL;DR:** Datadog answers 429 Too Many Requests when you exceed API rate limits. Back off, honor Retry-After, and stop hammering the endpoint that throttled you. Stop and wait. Add exponential backoff with jitter to the client.

# 429 Too Many Requests: back off, dont retry harder

What you see: API calls start returning `429` with an error body saying too many requests. Your Terraform apply, your custom exporter, or your script loop suddenly fails after working fine.

## Why it happens

Datadog rate-limits API endpoints per organization. The usual triggers:

- A script polling an endpoint in a tight loop (metrics queries every second from ten hosts).
- Terraform provider runs against hundreds of monitors in parallel.
- A retry loop without backoff: the first 429 causes immediate retries, which extends the throttle.

## Fix

1. **Stop and wait.** Honor the `Retry-After` header if present. A fixed 60 second pause beats hammering.
2. **Add exponential backoff with jitter** to the client. First retry after a few seconds, doubling, plus randomness so ten hosts do not retry in lockstep.
3. **Reduce call volume.** Cache responses, batch requests, widen poll intervals. If you query the same dashboard data every 10s from CI, you probably need a monitor, not a script.
4. **Split across keys/endpoints** only if the limit is per-key; most are per-org, so this rarely helps. Check which.

## The agent is not this

Agent intake throttling is separate from API 429s. If the *agent* is being throttled, you will see it in `datadog-agent status` as dropped payloads, and the fix is usually fewer custom metrics or a support ticket, not client backoff. Do not confuse the two.

## Trap

Treating 429 as an auth failure and rotating keys. It is not auth. It is pace. Rotating keys mid-throttle just adds a second problem.

## When to use this

- This covers exactly what the title says: 429 Too Many Requests from the Datadog API.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with 429; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current 429 behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_HMgWvmeAoowYlw3fXhb9mA). Version: `skv_EURzIe2JRI87c2nT2ICewg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
