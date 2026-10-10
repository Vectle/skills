---
name: "upstash-redis-choose-rest-or-the-nativ-4b2dc9d9aa97ad52"
description: "Shows how to fix upstash Redis: choose REST or the native Redis protocol before you write any code. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_KeWt94ibSoa618VDioiw2Q"
  title: "Upstash Redis: choose REST or the native Redis protocol before you write any code"
  version: "skv_GQFB2FOe1A6xaVL5VXbLsA"
  updated: "2026-10-03T14:12:41.50113+00:00"
  canonical_url: "https://vectle.com/skills/skl_KeWt94ibSoa618VDioiw2Q"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

The Redis protocol is TCP based and simply cannot connect there. - You run serverless functions (Lambda, Vercel) and do not want to manage connection pools across cold starts. Point it at Upstash with TLS on and it works with no code changes. - You need the wider Redis ecosystem: BullMQ, Celery, Sidekiq, session stores for Express, and similar tooling that speaks RESP. - You need blocking commands (BLPOP, BRPOP, blocking XREAD).

## When to use

You are seeing this: Upstash serves the same database two ways. Use this skill when you run into "Upstash Redis: choose REST or the native Redis protocol before you write any code".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Upstash Redis: pick REST or the native protocol before you write code

Upstash serves the same database two ways. Picking wrong costs you a rewrite later.

## Choose the REST API when

- You run on Cloudflare Workers, Fastly Compute@Edge, WASM, or any runtime
 where TCP sockets are unavailable. The Redis protocol is TCP based and
 simply cannot connect there.
- You run serverless functions (Lambda, Vercel) and do not want to manage
 connection pools across cold starts. REST is request based, no connections
 to babysit.
- You want to call Redis from any HTTP client, curl included, with no
 client library.

## Choose the native Redis protocol when

- You have legacy code built on ioredis, redis-py, jedis, or similar. Point
 it at Upstash with TLS on and it works with no code changes.
- You need the wider Redis ecosystem: BullMQ, Celery, Sidekiq, session
 stores for Express, and similar tooling that speaks RESP.
- You need blocking commands (BLPOP, BRPOP, blocking XREAD). These are not
 supported over REST.

## Rules that apply to both

- Pricing is per command/request on both paths. A chatty REST loop costs
 exactly as much as a chatty RESP loop.
- TLS is always on. There is no plaintext mode.
- Commands you cannot use over REST: blocking list/zset/stream pops,
 CLUSTER commands, and WATCH/UNWATCH/DISCARD inside transactions.

## Quick check

If your runtime can open a TCP socket and you already have Redis client
code, use the protocol. If your runtime is edge/serverless-first or you
are writing fresh agent code, use REST with the official SDK for your
language.


---

Source: [Vectle](https://vectle.com/skills/skl_KeWt94ibSoa618VDioiw2Q). Version: `skv_GQFB2FOe1A6xaVL5VXbLsA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
