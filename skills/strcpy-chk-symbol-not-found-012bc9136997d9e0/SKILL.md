---
name: "strcpy-chk-symbol-not-found-012bc9136997d9e0"
description: "Libsql Client Ts: strcpy_chk: symbol not found. The verified fix is Fixed via tursodatabase/libsql#1724, released in libsql v0.4.3 - `npm update` picks it up. Use this when you hit the symptoms above in libsql-client-ts; not for unrelated libsql-client-ts errors or general setup questions."
metadata:
  skill_id: "skl_pg88gIN3sikojyBOOVz-EQ"
  title: "strcpy_chk: symbol not found"
  version: "skv_RG7cSVUc1zOXtSBD5yOKJw"
  updated: "2026-10-03T05:00:43.658366+00:00"
  canonical_url: "https://vectle.com/skills/skl_pg88gIN3sikojyBOOVz-EQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/tursodatabase/libsql-client-ts/issues/180\"]"
---

## TL;DR

Fixed via tursodatabase/libsql#1724, released in libsql v0.4.3 - `npm update` picks it up. If still stuck: override `@libsql/linux-x64-musl` to 0.2.0 (npm overrides / pnpm overrides / yarn resolutions), or use a glibc-based image (bookworm/slim) instead of Alpine.

## The error

```text
2024-02-17T11:15:12.739 app[080e513b19e298] ams [info] Error: Error relocating /app/node_modules/@libsql/linux-x64-musl/index.node: __strcpy_chk: symbol not found
```

## Fix

1. Fixed via tursodatabase/libsql#1724, released in libsql v0.4.3 - `npm update` picks it up.
2. If still stuck: override `@libsql/linux-x64-musl` to 0.2.0 (npm overrides / pnpm overrides / yarn resolutions), or use a glibc-based image (bookworm/slim) instead of Alpine.

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

- How to fix "strcpy_chk: symbol not found" in libsql-client-ts
- libsql-client-ts: strcpy_chk: symbol not found

## Source

- https://github.com/tursodatabase/libsql-client-ts/issues/180

---

Source: [Vectle](https://vectle.com/skills/skl_pg88gIN3sikojyBOOVz-EQ). Version: `skv_RG7cSVUc1zOXtSBD5yOKJw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
