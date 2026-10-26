---
name: "libsql-client-0-6-1-next-js-b8058b733e719460"
description: "Libsql Client Ts: libsql/client@0.6.1 + Next.js. The verified fix is Fixed in 0.6.2 (reporter confirmed, thanks to giovannibenussi). Use this when you hit the symptoms above in libsql-client-ts; not for unrelated libsql-client-ts errors or general setup questions."
metadata:
  skill_id: "skl_xu29_WDafvU9YX6GvPOWGg"
  title: "libsql/client@0.6.1 + Next.js"
  version: "skv_6fF-B5spdcxE7DHzyPVOmw"
  updated: "2026-10-03T05:57:36.073275+00:00"
  canonical_url: "https://vectle.com/skills/skl_xu29_WDafvU9YX6GvPOWGg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/tursodatabase/libsql-client-ts/issues/216\"]"
---

## TL;DR

Fixed in 0.6.2 (reporter confirmed, thanks to giovannibenussi). If you hit this, upgrade past 0.6.1.

## The error

```text
After updating to version [0.6.1](https://www.npmjs.com/package/@libsql/client/v/0.6.1), I'm getting `Error: Unexpected end of JSON input`
Uncaught SyntaxError: Unexpected end of JSON input
```

## Fix

1. Fixed in 0.6.2 (reporter confirmed, thanks to giovannibenussi).
2. If you hit this, upgrade past 0.6.1.

Success check: the symptom above is gone and the original operation completes.

## When to use

- You hit this exact symptom in libsql-client-ts.
- You want the verified fix without digging through the thread.

## When not to use

- A different error in libsql-client-ts, even a similar-looking one.
- General libsql-client-ts setup or credential questions.

## Compatibility

- Libsql Client Ts (tursodatabase/libsql-client-ts) Reported against version 0.6.0.

## Variant phrasings

- How to fix "libsql/client@0.6.1 + Next.js" in libsql-client-ts
- libsql-client-ts: libsql/client@0.6.1 + Next.js

## Root cause

[tomek-f (reporter)]: Regression in @libsql/client 0.6.1 - `Error: Unexpected end of JSON input` (SyntaxError at JSON.parse) in a Next.js 14 app that worked on 0.6.0.

## Source

- https://github.com/tursodatabase/libsql-client-ts/issues/216

---

Source: [Vectle](https://vectle.com/skills/skl_xu29_WDafvU9YX6GvPOWGg). Version: `skv_6fF-B5spdcxE7DHzyPVOmw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
