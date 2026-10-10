---
name: "debugging-workers-with-wrangler-tail-a-5ed942479eaedb34"
description: "Shows how to fix debugging Workers with wrangler tail and real-time logs. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_PNkHVagbq1MLPWrI5H8eWA"
  title: "Debugging Workers with wrangler tail and real-time logs"
  version: "skv_IY7gzVoZFRAkhOHNcS80cA"
  updated: "2026-10-04T00:25:24.03885+00:00"
  canonical_url: "https://vectle.com/skills/skl_PNkHVagbq1MLPWrI5H8eWA"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

## TL;DR

Run it in the Worker project root, reproduce the problem, and watch the actual behavior instead of guessing. wrangler tail displays a live feed of console and exception logs for every request served by your Worker code, including Durable Object requests handled by that Worker. Log the discriminating values: request path, binding call arguments, branch taken. console.log is cheap; a second deploy to add the missing log line is expensive.

## When to use

You are seeing this: wrangler tail displays a live feed of console and exception logs for every request served by your Worker code, including Durable Object requests handled by that Worker. Use this skill when you run into "Debugging Workers with wrangler tail and real-time logs".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Debugging with tail and real-time logs

`wrangler tail` displays a live feed of console and exception logs for every request served by your Worker code, including Durable Object requests handled by that Worker. Run it in the Worker project root, reproduce the problem, and watch the actual behavior instead of guessing.

## The options

- **`wrangler tail`**: terminal live feed. Best during active debugging; filterable.
- **Real-time logs** (dashboard): near real-time log events in the Cloudflare dashboard. Best when you cannot or do not want a terminal session, or for showing someone else.
- **Tail Workers** (beta): programmatic tail with custom filtering, sampling, and transformation of telemetry. Best for persistent pipelines (forward errors to your own systems).

## The discipline

1. Reproduce under tail: the log line you need only exists while the bug happens.
2. Log the discriminating values: request path, binding call arguments, branch taken. `console.log` is cheap; a second deploy to add the missing log line is expensive.
3. For Durable Objects, tail the Worker that owns the DO binding: DO request logs flow through it.
4. Exceptions in tail include stacks: copy the full stack into the incident record, not just the message.

## Checklist

- Keep a tail running during every production deploy verification.
- Strip or redact sensitive values from logs before they become a permanent stream: logs are stored and visible to the team.
- If tail shows nothing, confirm you are tailing the right environment (production vs preview).


---

Source: [Vectle](https://vectle.com/skills/skl_PNkHVagbq1MLPWrI5H8eWA). Version: `skv_IY7gzVoZFRAkhOHNcS80cA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
