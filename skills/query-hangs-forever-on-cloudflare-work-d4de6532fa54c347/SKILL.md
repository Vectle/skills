---
name: "query-hangs-forever-on-cloudflare-work-d4de6532fa54c347"
description: "Libsql Client Ts: query hangs forever on Cloudflare Worker local dev. The verified fix is Fix: [honzasp (maintainer)]: Fixed in @libsql/hrana-client 0.3.8 (a dependency of @libsql/client) - run `npm update`. Use this when you hit the symptoms above in libsql-client-ts; not for unrelated libsql-client-ts errors or general setup questions."
metadata:
  skill_id: "skl_2dIVQ9xVz8NDa_LCc-YjYA"
  title: "Query hangs forever on Cloudflare Worker local dev"
  version: "skv_iF60nlWiCWnyXs-9Yjc-FA"
  updated: "2026-10-03T04:43:28.785831+00:00"
  canonical_url: "https://vectle.com/skills/skl_2dIVQ9xVz8NDa_LCc-YjYA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/tursodatabase/libsql-client-ts/issues/29\"]"
---

## TL;DR

Fix: [honzasp (maintainer)]: Fixed in @libsql/hrana-client 0.3.8 (a dependency of @libsql/client) - run `npm update`. Reporter confirmed the repro works after the update.

## The error

```text
Debugging shows its stuck on this line but can't debug further because it just hangs, doesn't throw an error https://github.com/libsql/libsql-client-ts/blob/358767835750c69df3073d0f43bb7f9e2d8cc34f/src/hrana.ts#L64
```

## Fix

1. [honzasp (maintainer)]: Fixed in @libsql/hrana-client 0.3.8 (a dependency of @libsql/client) - run `npm update`.
2. Reporter confirmed the repro works after the update.

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

- How to fix "query hangs forever on Cloudflare Worker local dev" in libsql-client-ts
- libsql-client-ts: query hangs forever on Cloudflare Worker local dev

## Root cause

Root cause was in the hrana WebSocket client used by `@libsql/client/web`, which hung instead of connecting on Cloudflare Workers local dev (wrangler).

## Source

- https://github.com/tursodatabase/libsql-client-ts/issues/29

---

Source: [Vectle](https://vectle.com/skills/skl_2dIVQ9xVz8NDa_LCc-YjYA). Version: `skv_iF60nlWiCWnyXs-9Yjc-FA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
