---
name: "invalidargumenterror-invalid-upgrade-h-de7786f48d23439c"
description: "Serverless: invalidArgumentError: invalid upgrade header. The verified fix is Fix: [jawj (maintainer)]: In Node there is no global WebSocket, so the driver falls back to the Cloudflare-style fetch-with-upgrade-header method, which fails with 'invalid upgrade header'. Use this when you hit the symptoms above in serverless; not for unrelated serverless errors or general setup questions."
metadata:
  skill_id: "skl_6wwgZPLtYn64YiIlUZVs7Q"
  title: "InvalidArgumentError: invalid upgrade header"
  version: "skv_c82ZU6FE9pmM7N140PNQnw"
  updated: "2026-10-03T05:05:38.019153+00:00"
  canonical_url: "https://vectle.com/skills/skl_6wwgZPLtYn64YiIlUZVs7Q"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/neondatabase/serverless/issues/7\"]"
---

## TL;DR

Fix: [jawj (maintainer)]: In Node there is no global WebSocket, so the driver falls back to the Cloudflare-style fetch-with-upgrade-header method, which fails with 'invalid upgrade header'.

## The error

```text
Is the connection string the right URL? `invalid upgrade header` sounds like a websocket error, so I'm wondering if I was supposed to use the connection string or maybe a URL for the proxy.
```

## Fix

1. [jawj (maintainer)]: In Node there is no global WebSocket, so the driver falls back to the Cloudflare-style fetch-with-upgrade-header method, which fails with 'invalid upgrade header'.

Success check: the symptom above is gone and the original operation completes.

## When to use

- You hit this exact symptom in serverless.
- You want the verified fix without digging through the thread.

## When not to use

- A different error in serverless, even a similar-looking one.
- General serverless setup or credential questions.

## Compatibility

- Serverless (neondatabase/serverless)

## Variant phrasings

- How to fix "invalidArgumentError: invalid upgrade header" in serverless
- serverless: invalidArgumentError: invalid upgrade header

## Source

- https://github.com/neondatabase/serverless/issues/7

---

Source: [Vectle](https://vectle.com/skills/skl_6wwgZPLtYn64YiIlUZVs7Q). Version: `skv_c82ZU6FE9pmM7N140PNQnw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
