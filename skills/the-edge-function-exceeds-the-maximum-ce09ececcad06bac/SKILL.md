---
name: "the-edge-function-exceeds-the-maximum-ce09ececcad06bac"
description: "Your Vercel deploy fails because an Edge Function (usually middleware.ts) is bigger than the edge size cap: 1 MB on Hobby, 2 MB on Pro, 4 MB on Enterprise, measured after gzip. This shows how to slim it down: audit what middleware imports, move heavy libs out, narrow the matcher so it does not bundle page code. Use when the deploy errors on edge function size. Not for the 250 MB serverless limit or runtime timeouts."
metadata:
  skill_id: "skl_NaXhY2ZU__KgdchhNSSBYg"
  title: "The Edge Function exceeds the maximum size limit of 1 MB"
  version: "skv_k8KCo88p8sUZ2Q1gm7OcjA"
  updated: "2026-10-03T05:36:47.885012+00:00"
  canonical_url: "https://vectle.com/skills/skl_NaXhY2ZU__KgdchhNSSBYg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/vercel/next.js/issues/32907\"]"
---

# The Edge Function exceeds the maximum size limit of 1 MB (Vercel)

TL;DR: your middleware or edge route bundles more than the edge size cap (1 MB on Hobby after gzip, 2 MB on Pro, 4 MB on Enterprise) and the deploy is rejected. Edge code has to stay tiny: audit what `middleware.ts` imports, drop heavy libs (charting, 3D, UI kits) from the edge path, and narrow the `matcher` so the edge bundle does not drag in page code. There is no config to raise the cap on Hobby.

```text
The Edge Function "middleware" is 1.13 MB which exceeds the maximum size limit of 1 MB.
```

## 1. See what the edge bundle pulls in

The error names the function. Check its imports: `middleware.ts` (or any route with `runtime = 'edge'`) bundles everything it touches. Common bloat: UI kits, charting/3D libs, date libraries with all locales, SDKs meant for Node.

Expected: you find one or two imports responsible for most of the megabytes.

## 2. Keep heavy libs out of the edge path

Move anything heavy behind a serverless route or a client component:

- Auth/session checks in middleware: keep, but import only the tiny edge-safe helper, not the full SDK
- Charting, 3D, PDF, image libs: these do not belong in edge code, move them to API routes or the client
- `import ... from 'lib'` pulling a whole barrel file: import the single module path instead

Expected: the reported edge function size drops under the cap.

## 3. Narrow the matcher

A middleware with no `matcher` (or a `/(.*)` matcher) bundles against every route. Scope it to the paths that need it:

```ts
export const config = {
  matcher: ['/dashboard/:path*', '/account/:path*'],
};
```

Expected: the edge bundle only includes code reachable from the matched routes.

## 4. If it still does not fit, move off the edge runtime

Some logic genuinely needs Node APIs or big deps. For those routes, drop `runtime = 'edge'` and run on Node.js serverless functions (250 MB cap, much more headroom). Keep middleware itself minimal: redirect, rewrite, or header tweaks only.

Expected: the route deploys as a serverless function; middleware stays under 1 MB.

## When this applies

- Vercel deploy fails with the edge function size error
- The named function is `middleware` or a route with `runtime = 'edge'`
- Next.js on Vercel, any plan

## When it does not apply

- `A Serverless Function has exceeded the unzipped maximum size of 250 MB`: the Node.js function limit, different fixes
- Edge runtime errors at request time (those are invocation failures, not size)
- Middleware that is small but crashes: check for Node-only imports instead

## Compatibility

Vercel Edge Functions: 1 MB cap on Hobby, 2 MB on Pro, 4 MB on Enterprise, measured after gzip. Next.js middleware (`middleware.ts`) always runs on the edge runtime. Applies to Next.js 12.2+ middleware and any `runtime = 'edge'` route.

## Why it happens

Edge functions run on V8 isolates distributed worldwide, so Vercel caps their size hard. Your middleware bundles every import transitively, and one heavy library (a UI kit, three.js, a full SDK) is enough to push a 50 KB middleware past 1 MB. `next/dynamic` does not help here because the edge bundle is built at deploy time, not lazily.

## Edge cases

- The size in the error varies (`1.13mb`, `2.4 MB`): same error, the cap is what matters.
- On Pro the cap is 2 MB: if you are at 1.5 MB, upgrading buys room, but slimming is still cheaper.
- Barrel imports (`import { x } from 'huge-lib'`) defeat tree-shaking on the edge; import the deep path.
- Middleware must also avoid Node-only APIs (`fs`, `crypto.createHash`); those fail differently, at runtime.

---

Source: [Vectle](https://vectle.com/skills/skl_NaXhY2ZU__KgdchhNSSBYg). Version: `skv_k8KCo88p8sUZ2Q1gm7OcjA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
