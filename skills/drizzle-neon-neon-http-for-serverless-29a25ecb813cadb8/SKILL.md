---
name: "drizzle-neon-neon-http-for-serverless-29a25ecb813cadb8"
description: "Shows how to fix drizzle + Neon: neon-http for serverless one-shots, neon-ws for transactions. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_72-DPvmpokHCOLV2eKPk1Q"
  title: "Drizzle + Neon: neon-http for serverless one-shots, neon-ws for transactions"
  version: "skv_NynKEyWJIbNq2N5p3YTl5w"
  updated: "2026-10-03T14:06:30.375812+00:00"
  canonical_url: "https://vectle.com/skills/skl_72-DPvmpokHCOLV2eKPk1Q"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://neon.com/docs/guides/drizzle\",\"https://neon.com/docs/serverless/serverless-driver\"]"
---

## TL;DR

drizzle-orm/neon-http (backed by the neon() fetch client) is the default in every serverless tutorial, and it is right for Vercel/Netlify one-shot queries. But it is stateless HTTP: no persistent connections, no interactive transactions.

## Steps

1. - Serverless one-shot queries -> `drizzle-orm/neon-http` with `neon(process.env.DATABASE_URL)`.
- Interactive transactions or node-postgres compatibility -> `drizzle-orm/neon-serverless` (WebSocket) or `drizzle-orm/node-postgres`.
- Migrations via Drizzle Kit -> run against the direct connection string, not pooled.

```ts
// HTTP: serverless one-shots
import { drizzle } from 'drizzle-orm/neon-http';
import { neon } from '@neondatabase/serverless';
const db = drizzle(neon(process.env.DATABASE_URL));

// WebSocket: interactive transactions
import { drizzle } from 'drizzle-orm/neon-serverless';
import { Pool, neonConfig } from '@neondatabase/serverless';
import ws from 'ws';
neonConfig.webSocketConstructor = ws; // Node.js only; not needed on Edge
const db = drizzle(new Pool({ connectionString: process.env.DATABASE_URL }));
```

## When to use

You are seeing this: drizzle-orm/neon-http (backed by the neon() fetch client) is the default in every serverless tutorial, and it is right for Vercel/Netlify one-shot queries. Use this skill when you run into "Drizzle + Neon: neon-http for serverless one-shots, neon-ws for transactions".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_72-DPvmpokHCOLV2eKPk1Q). Version: `skv_NynKEyWJIbNq2N5p3YTl5w`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
