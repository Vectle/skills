---
name: "sentry-next-js-edge-runtime-its-own-co-1680a899fc237c60"
description: "Edge runtime code needs its own Sentry config with edge-safe integrations. What goes in sentry.edge.config.ts, what breaks there, and how tunnelRoute fixes adblocker losses. Not the full reference manual."
metadata:
  skill_id: "skl_ovfxYIHu_z_QMr0aPSvSDQ"
  title: "Sentry Next.js edge runtime: its own config, its own limits"
  version: "skv_1-c1n4ZSy8-p-rjVBYUqEg"
  updated: "2026-10-03T04:48:33.194121+00:00"
  canonical_url: "https://vectle.com/skills/skl_ovfxYIHu_z_QMr0aPSvSDQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** Edge runtime code needs its own Sentry config with edge-safe integrations. What goes in sentry.edge.config.ts, what breaks there, and how tunnelRoute fixes adblocker losses. Keep it minimal: instrumentation.ts loads it only when NEXT_RUNTIME === "edge". Integrations that depend on them (like the Node profiling integration) must stay in sentry.server.config.ts only.

## The file

`Sentry.edge.config.ts` initializes Sentry for middleware and edge-route code. Keep it minimal:

```ts
import * as Sentry from "@sentry/nextjs";

Sentry.init({
  dsn: "___PUBLIC_DSN___",
  tracesSampleRate: 0.1,
  // no Node-only integrations here
});
```

`instrumentation.ts` loads it only when `NEXT_RUNTIME === "edge"`. If edge errors are missing while Node.js server errors arrive, the edge config is usually absent or throwing on import.

## What breaks at the edge

The edge runtime has no Node.js APIs: no `fs`, no `process.nextTick` tricks, no native modules. Integrations that depend on them (like the Node profiling integration) must stay in `sentry.server.config.ts` only. An edge config that imports a Node-only integration fails at the worst time: inside middleware, on every request.

Also keep `beforeSend` lean here. Edge functions bill by duration; a heavy scrub function on every event adds latency to the request path.

## Adblockers eat client events

Browser extensions block requests to ingest endpoints. `tunnelRoute: "/sentry-tunnel"` in `withSentryConfig` routes client events through your own server so they look first-party. If client-side issues are undercounted relative to server-side, and the gap appeared without a code change, check whether tunnelRoute is actually set and the route is not behind auth middleware that rejects POSTs.

## Debugging edge init

Edge console output is harder to reach. Temporarily set `debug: true` in the edge config and watch the edge logs during a deploy preview, then remove it. Confirm with one intentional error from middleware before calling it done.

## When to use this

- This covers exactly what the title says: Sentry Next.js edge runtime.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Sentry; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Mentions 0.1 in the original; behavior may differ on much older or newer releases.

---

Source: [Vectle](https://vectle.com/skills/skl_ovfxYIHu_z_QMr0aPSvSDQ). Version: `skv_1-c1n4ZSy8-p-rjVBYUqEg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
