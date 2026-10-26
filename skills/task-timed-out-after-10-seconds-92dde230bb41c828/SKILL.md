---
name: "task-timed-out-after-10-seconds-92dde230bb41c828"
description: "Your Vercel serverless function gets killed mid-request with \"Task timed out after 10 seconds\". This covers the real fixes: raise maxDuration in vercel.json on a paid plan, or stay on Hobby by caching the slow upstream call, splitting the work, or moving the heavy path off serverless. Use when Vercel function logs show the timeout line. Not for build timeouts, local dev hangs, or other platforms."
metadata:
  skill_id: "skl_Md22l3_6_7jpc8iNn0sJFg"
  title: "Task timed out after 10 seconds"
  version: "skv_IPGsGyIpvLks0Pz-kuxRDg"
  updated: "2026-10-03T05:31:35.573203+00:00"
  canonical_url: "https://vectle.com/skills/skl_Md22l3_6_7jpc8iNn0sJFg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/transitive-bullshit/nextjs-notion-starter-kit/issues/276\"]"
---

# Task timed out after 10 seconds (Vercel)

TL;DR: Vercel killed your serverless function because it ran past the plan limit, 10 seconds on Hobby. If you can pay: set `maxDuration` for that function in vercel.json (Pro allows up to 60s). Staying on Hobby: the limit is fixed, so cache the slow upstream call, split the work, or move the heavy path off serverless. The timeout is a platform kill, not a bug in your code.

```text
2022-04-23T09:14:28.394Z 5cc63739-5b89-4e3f-8ebb-6d467db86fa0 Task timed out after 10.03 seconds
```

## 1. Confirm it is the platform limit

Open your Vercel project dashboard, go to Logs, and filter by the failing route. If you see `Task timed out after 10.xx seconds` about ten seconds after the request starts, the platform killed it. No stack trace means your code did not throw, it just ran too long.

Expected: the timeout line appears at a consistent ~10s mark across requests.

## 2. Raise maxDuration (paid plans only)

In `vercel.json`, target the slow function:

```json
{
  "functions": {
    "app/api/heavy/route.ts": { "maxDuration": 60 }
  }
}
```

Deploy and check the function entry in the dashboard shows the new duration. Hobby ignores any value above 10. Pro allows up to 60s, Enterprise higher.

Expected: requests that took 11 to 50 seconds now complete instead of dying at 10s.

## 3. On Hobby: cache the slow upstream call

Almost every one of these is a slow upstream: an LLM API, a cold database connection, image generation. Cache it so the slow path only runs once:

- Upstash Redis (or any KV) for API/DB results, keyed by the request input
- `stale-while-revalidate` cache headers for pages that can tolerate it

Expected: the first request may still be slow, repeat requests return in milliseconds.

## 4. Split the work or move it off serverless

If the work fundamentally takes longer than 10s, stop doing it inside the request:

- Return a fast 202 and finish the job in a background worker, queue consumer, or cron
- Break one big function into smaller chained functions
- Move the heavy endpoint to a long-running host

Expected: the user-facing request returns in under 2s; the heavy work completes async.

## When this applies

- Vercel function logs show `Task timed out after 10.xx seconds`
- The function calls something slow: LLM APIs, databases, image/PDF processing
- Next.js or Python serverless functions on Vercel

## When it does not apply

- `Build exceeded maximum duration`: that is the build limit, different knob
- Timeouts when running locally with `next dev` or `vercel dev`
- Function timeouts on Netlify, Cloudflare Workers, or Railway: different limits, different fixes

## Compatibility

Vercel Hobby (10s fixed), Pro (maxDuration up to 60s), Enterprise (higher). Applies to `vercel.json` `functions.maxDuration` for Node.js and Python serverless functions. Does not apply to Edge Middleware, which has separate limits.

## Why it happens

Vercel runs your function inside a hard execution budget. On Hobby that budget is 10 seconds and no setting overrides it. Anything that routinely takes longer, usually a slow third-party API or an uncached database round trip, gets killed mid-flight and the client sees a 500 or 504.

## Edge cases

- You set maxDuration but still die at 10s: you are on Hobby, or the glob in `functions` does not match the route file. Check the function list in the dashboard to confirm the value applied.
- The decimal varies (`10.01`, `10.03` seconds): same error.
- Cold starts eat into the budget: a function that takes 9s warm can time out cold. Caching and smaller bundles help.
- Python functions use the same knob and the same limits.

---

Source: [Vectle](https://vectle.com/skills/skl_Md22l3_6_7jpc8iNn0sJFg). Version: `skv_IPGsGyIpvLks0Pz-kuxRDg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
