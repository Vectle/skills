---
name: "allow-configuring-http-56b33680bbc8a03b"
description: "Libsql Client Ts: allow configuring http. The verified fix is Fix: For plaintext local dev, pass an explicit `http:` or `ws:` URL (e.g. the service URL for that host and port), or use the `?tls=0` query parameter added in 0.2.0. Use this when you hit the symptoms above in libsql-client-ts; not for unrelated libsql-client-ts errors or general setup questions."
metadata:
  skill_id: "skl_EZoJKbq3lrU5XUDzwBBoPA"
  title: "Allow configuring http"
  version: "skv_By5UxcR8C_z-gkSir1fJDw"
  updated: "2026-10-03T04:42:49.205736+00:00"
  canonical_url: "https://vectle.com/skills/skl_EZoJKbq3lrU5XUDzwBBoPA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/tursodatabase/libsql-client-ts/issues/39\"]"
---

## TL;DR

Fix: For plaintext local dev, pass an explicit `http:` or `ws:` URL (e.g. the service URL for that host and port), or use the `?tls=0` query parameter added in 0.2.0. Also note: `turso dev` only speaks a very old HTTP API the client can't talk to - run `sqld` directly for a compatible local server.

## The error

```text
Issue tursodatabase/libsql-client-ts#39 (closed, 11 comments): When using a local database, e.g. `libsql://YOUR_HOST:3030`, this library would use `https`. This fails because I can't access YOUR_HOST over https. Please allow me to disable https, so that I can connect to a local client over HTTP. I'm using Cloudflare Workers so it seems like I cannot use the file directly.
```

## Fix

1. For plaintext local dev, pass an explicit `http:` or `ws:` URL (e.g. the service URL for that host and port), or use the `?tls=0` query parameter added in 0.2.0.
2. Also note: `turso dev` only speaks a very old HTTP API the client can't talk to - run `sqld` directly for a compatible local server.

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

- How to fix "allow configuring http" in libsql-client-ts
- libsql-client-ts: allow configuring http

## Source

- https://github.com/tursodatabase/libsql-client-ts/issues/39

---

Source: [Vectle](https://vectle.com/skills/skl_EZoJKbq3lrU5XUDzwBBoPA). Version: `skv_By5UxcR8C_z-gkSir1fJDw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
