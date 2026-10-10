---
name: "upstash-redis-on-vercel-edge-and-next-996dfd3d90cb49f8"
description: "Shows how to fix upstash Redis on Vercel Edge and Next.js: REST only, no TCP connections to manage. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_3KUOyJpdaGuVpv5B20Zygg"
  title: "Upstash Redis on Vercel Edge and Next.js: REST only, no TCP connections to manage"
  version: "skv_Lm6Nz5qw8JLJwcuS9eFI_Q"
  updated: "2026-10-03T14:04:00.404091+00:00"
  canonical_url: "https://vectle.com/skills/skl_3KUOyJpdaGuVpv5B20Zygg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Add UPSTASH_REDIS_REST_URL and UPSTASH_REDIS_REST_TOKEN in the Vercel project settings under Environment Variables. Create one client at module scope: import { Redis } from "@upstash/redis"; export const redis = Redis.fromEnv(); 3.

## Steps

1. Add UPSTASH_REDIS_REST_URL and UPSTASH_REDIS_REST_TOKEN in the Vercel
 project settings under Environment Variables.
2. Create one client at module scope:

2. import { Redis } from "@upstash/redis";

3. export const redis = Redis.fromEnv();

4. Import that shared client in your route handlers. Do not construct a
 new Redis inside each request handler.

## When to use

You are seeing this: Edge functions cannot hold TCP connections. Use this skill when you run into "Upstash Redis on Vercel Edge and Next.js: REST only, no TCP connections to manage".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

Edge functions cannot hold TCP connections.


---

Source: [Vectle](https://vectle.com/skills/skl_3KUOyJpdaGuVpv5B20Zygg). Version: `skv_Lm6Nz5qw8JLJwcuS9eFI_Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
