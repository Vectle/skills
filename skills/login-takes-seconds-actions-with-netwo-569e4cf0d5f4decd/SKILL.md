---
name: "login-takes-seconds-actions-with-netwo-569e4cf0d5f4decd"
description: "Symptom: login completes but takes 5+ seconds. Cause: extensibility code doing network I/O per login, often sequentially. Confirmation: Actions real-time logs with timings; tenant log timestamps. Not for different error messages."
metadata:
  skill_id: "skl_4Sc-Rd5hs1qudfVzZ8TyvQ"
  title: "Login takes seconds: Actions with network calls, Rules ordering, timeouts"
  version: "skv_cycYRPuASdthoforISvFtQ"
  updated: "2026-10-03T13:51:38.078717+00:00"
  canonical_url: "https://vectle.com/skills/skl_4Sc-Rd5hs1qudfVzZ8TyvQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** Symptom: login completes but takes 5+ seconds. Cause: extensibility code doing network I/O per login, often sequentially. Verify Time three consecutive logins; p95 under ~1.5s for database connections. Keep the timing check in your release checklist whenever an Action changes.

## The error

```text
login completes but takes 5+ seconds. Cause: extensibility code doing network I/O per login, often sequentially. Verify Time three consecutive logins; p95 under ~1.5s for database connections. Keep the timing check in your release checklist whenever an Action changes.
```

## The fix

**TL;DR:** Symptom: login completes but takes 5+ seconds. Cause: extensibility code doing network I/O per login, often sequentially. Verify Time three consecutive logins; p95 under ~1.5s for database connections. Keep the timing check in your release checklist whenever an Action changes.

## The fix

1. Actions making HTTP calls per login (enrichment APIs, CRM lookups) with no timeout or cache. Two Actions each calling out serially doubles it.

2. Legacy Rules with the same pattern, plus Rules run before Actions in mixed pipelines.

3. Custom database scripts with slow bcrypt rounds or external calls.

4. Social/enterprise IdP latency (out of your control, but measurable).

5. Actions > your Action > Real-time Logs: run a test login and watch execution time per Action.

6. Tenant logs: compare the login event's `date` with the authorize start; the gap is pipeline time.

7. Disable Actions one by one (or run the flow with the Action removed) and re-time. Binary search the slow one.

8. Cache enrichment data (per user, TTL hours) instead of fetching per login.

9. Set aggressive timeouts on outbound calls (2-3s) and fail open or closed deliberately, not by hanging.

10. Move non-critical work (analytics, CRM sync) to a post-login async path or a log-stream-triggered job, not the login pipeline.

11. Migrate remaining Rules to Actions; the mixed pipeline adds overhead.

## When to use this

- You are seeing this exact error message; match the block above, not just part of it.
- The failing call matches the scenario in the title: Login takes seconds.
- You want the fastest verified fix before digging through logs.

## When not to use this

- Your error text differs from the block above; close cousins often have different causes.
- The stack trace points at a different component than the one in the title.
- You already applied this fix and the error persists; look for a second cause instead of reapplying.

## Compatibility

- Not pinned to a specific version; follows current Login behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_4Sc-Rd5hs1qudfVzZ8TyvQ). Version: `skv_cycYRPuASdthoforISvFtQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
