---
name: "connection-resilience-what-langchain-r-5a10bc580ba9a9cc"
description: "Chat models retry failed requests with exponential backoff automatically: up to 6 times for network errors, 429 rate limits, and 5xx server errors. 401 and 404 are never retried. Tune with max_retries and timeout."
metadata:
  skill_id: "skl_-AYmf4TdlGoXzVA1In0-Fg"
  title: "Connection resilience: what LangChain retries automatically and what it does not"
  version: "skv_5ZEMjO6pcDMsrIt5kMmZxw"
  updated: "2026-10-03T15:16:06.856545+00:00"
  canonical_url: "https://vectle.com/skills/skl_-AYmf4TdlGoXzVA1In0-Fg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** Chat models retry failed requests with exponential backoff automatically: up to 6 times for network errors, 429 rate limits, and 5xx server errors. 401 and 404 are never retried.

## The fix

1. Network errors, rate limits (429), server errors (5xx): yes, with exponential backoff.

2. Client errors like 401 unauthorized or 404: no. Retrying those is pointless; fix the credentials or the request.

3. For long-running agent graphs on flaky networks, raise max_retries (10 to 15) AND use a checkpointer, so progress survives a failure that retries cannot paper over.

4. The exceptions carry an `is_retryable` attribute. Model retry middleware respects it by default, so custom retry code should check the attribute instead of maintaining its own list.

5. In create_agent, prefer ModelRetryMiddleware (max_retries, backoff_factor, initial_delay, on_failure) over wrapping the whole agent in your own loop.

## When to use this

- This covers exactly what the title says: Connection resilience.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Connection; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Mentions 3.6 in the original; behavior may differ on much older or newer releases.

---

Source: [Vectle](https://vectle.com/skills/skl_-AYmf4TdlGoXzVA1In0-Fg). Version: `skv_5ZEMjO6pcDMsrIt5kMmZxw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
