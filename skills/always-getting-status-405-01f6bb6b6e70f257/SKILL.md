---
name: "always-getting-status-405-01f6bb6b6e70f257"
description: "Libsql Client Ts: always getting status 405. The verified fix is Fixed by running `bun run dev` instead of `bun --bun run dev` (which makes bun execute scripts with node), or by passing a custom fetch to the client: `createClient({ url: DB_URL, fetch: (req: Request) => fetch(req.url, req) })` (bun doesn't accept raw Request objects, oven-sh/bun#11381). Use this when you hit the symptoms above in libsql-client-ts; not for unrelated libsql-client-ts errors or general setup questions."
metadata:
  skill_id: "skl_wL6lDhfVfDbYyEv-_gZQeA"
  title: "Always getting status 405"
  version: "skv_VgKIKKHQbXJbSi5eEWUoeA"
  updated: "2026-10-03T04:48:57.275123+00:00"
  canonical_url: "https://vectle.com/skills/skl_wL6lDhfVfDbYyEv-_gZQeA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Fixed by running `bun run dev` instead of `bun --bun run dev` (which makes bun execute scripts with node), or by passing a custom fetch to the client: `createClient({ url: DB_URL, fetch: (req: Request) => fetch(req.url, req) })` (bun doesn't accept raw Request objects, oven-sh/bun#(11381).

## The error

```text
Since today morning, i have only been getting this error. Even the simplest inserts fail. However drizzle migrations are working for some reason, so the credentials are correct. Yesterday my setup was working, so i believe this error isn't on my end
```

## Fix

1. Fixed by running `bun run dev` instead of `bun --bun run dev` (which makes bun execute scripts with node), or by passing a custom fetch to the client: `createClient({ url: DB_URL, fetch: (req: Request) => fetch(req.url, req) })` (bun doesn't accept raw Request objects, oven-sh/bun#(11381).

Success check: the symptom above is gone and the original operation completes.

## When to use

- You hit this exact symptom in libsql-client-ts.
- You want the verified fix without digging through the thread.

## When not to use

- A different error in libsql-client-ts, even a similar-looking one.
- General libsql-client-ts setup or credential questions.

## Compatibility

- Libsql Client Ts (tursodatabase/libsql-client-ts)

## Variant phrasings

- How to fix "always getting status 405" in libsql-client-ts
- libsql-client-ts: always getting status 405

## Source

- https://github.com/tursodatabase/libsql-client-ts/issues/223

---

Source: [Vectle](https://vectle.com/skills/skl_wL6lDhfVfDbYyEv-_gZQeA). Version: `skv_VgKIKKHQbXJbSi5eEWUoeA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
