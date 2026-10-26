---
name: "kysely-neon-neondialect-for-http-and-n-50abcb84416ddb5c"
description: "Shows how to fix kysely + Neon: NeonDialect for HTTP, and no interactive transactions on it. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl__FKBRoqCDPosNXVE8ERYaw"
  title: "Kysely + Neon: NeonDialect for HTTP, and no interactive transactions on it"
  version: "skv_L7JlvS2VCmV_OiaAqKUQaA"
  updated: "2026-10-03T13:50:33.269145+00:00"
  canonical_url: "https://vectle.com/skills/skl__FKBRoqCDPosNXVE8ERYaw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://neon.com/docs/guides/kysely\",\"https://neon.com/docs/serverless/serverless-driver\"]"
---

## TL;DR

Kysely tutorials for Neon use NeonDialect from kysely-neon backed by the neon() HTTP client. It works great for queries, then fails the moment someone writes an interactive transaction, because the HTTP driver is stateless with no persistent connections.

## Steps

1. - HTTP driver (`NeonDialect` + `neon()`): serverless-friendly, one-shot queries only.
- Need transactions: use the Neon WebSocket driver or node-postgres dialect instead.

```ts
import { Kysely } from 'kysely';
import { NeonDialect } from 'kysely-neon';
import { neon } from '@neondatabase/serverless';

export const db = new Kysely[Database]({
 dialect: new NeonDialect({ neon: neon(process.env.DATABASE_URL) }),
});
```

2. - Audit for `.transaction()` usage before choosing the HTTP dialect.
- Migrations run against the direct connection string.
- Unlike many ORMs, Kysely does not sync types from the schema; tables must exist before you query, so run migrations before first use.
- On Node with the WebSocket path, supply the `ws` constructor via `neonConfig.webSocketConstructor`.

## When to use

Use this skill when you run into "Kysely + Neon: NeonDialect for HTTP, and no interactive transactions on it".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl__FKBRoqCDPosNXVE8ERYaw). Version: `skv_L7JlvS2VCmV_OiaAqKUQaA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
