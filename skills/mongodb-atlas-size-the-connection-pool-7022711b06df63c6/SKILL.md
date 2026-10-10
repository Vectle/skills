---
name: "mongodb-atlas-size-the-connection-pool-7022711b06df63c6"
description: "Shows how to fix mongoDB Atlas: size the connection pool deliberately. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_fPnjd_QMD0NvGn2ADmp0wg"
  title: "MongoDB Atlas: size the connection pool deliberately"
  version: "skv_bNPd8QZZueboJTs_ZuJ1hg"
  updated: "2026-10-03T14:11:14.869423+00:00"
  canonical_url: "https://vectle.com/skills/skl_fPnjd_QMD0NvGn2ADmp0wg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Check slow queries first; raising maxPoolSize on top of slow queries just moves the bottleneck. - minPoolSize above 0 avoids connect latency on burst traffic, at the cost of idle connections.

## Steps

1. Every driver keeps a pool per client. The knobs, in every driver:

2. - `maxPoolSize` (default 100): ceiling on connections per client.
- `minPoolSize` (default 0): warm connections kept ready.
- `maxIdleTimeMS`: how long an idle connection lives before being recycled.
- `waitQueueTimeoutMS`: how long an operation waits for a free connection before erroring.

3. Total connections = clients x maxPoolSize. Count your clients: app instances, workers, serverless concurrency, plus mongosh sessions and tools. Size maxPoolSize from expected concurrent database operations per client, not from the default.

4. - One client per process keeps the math simple. N clients with default pools is how you accidentally open 500 connections.
- If you see wait-queue timeouts under load, the pool is too small OR operations are too slow. Check slow queries first; raising maxPoolSize on top of slow queries just moves the bottleneck.
- `minPoolSize` above 0 avoids connect latency on burst traffic, at the cost of idle connections. Use it for latency-sensitive services.
- Lower `maxIdleTimeMS` (a few minutes) when clients sit behind load balancers or NATs that silently drop idle TCP connections.

5. Watch Atlas Metrics, Connections, under real load. Steady near your computed ceiling is healthy; sawtooth or plateau-at-cap with errors means resize.

## When to use

You are seeing this: Every driver keeps a pool per client. Use this skill when you run into "MongoDB Atlas: size the connection pool deliberately".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_fPnjd_QMD0NvGn2ADmp0wg). Version: `skv_bNPd8QZZueboJTs_ZuJ1hg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
