---
name: "edge-neondatabase-serverless-pool-crea-a7bf842649de344a"
description: "Shows how to fix edge + @neondatabase/serverless Pool: create, use, close per request. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_ayExvJb9XRKNBXcFD5oqKg"
  title: "Edge + @neondatabase/serverless Pool: create, use, close per request"
  version: "skv_T2ICNk6SzXxeMzit4Bph3A"
  updated: "2026-10-03T13:57:32.033112+00:00"
  canonical_url: "https://vectle.com/skills/skl_ayExvJb9XRKNBXcFD5oqKg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://neon.com/docs/serverless/serverless-driver\"]"
---

## TL;DR

Do not create them outside a request handler; do not create them in one handler and reuse them in another. Pool or Client objects must be connected, used, and closed within a single request handler.

## Steps

1. - Factory function per handler, `pool.end()` in a finally block.
- For single queries, prefer the `neon()` HTTP client: no lifecycle to manage at all.
- If you need connection reuse on the Edge, that is what Cloudflare Hyperdrive is for, not a shared Pool.
- Load-test with sequential requests, not just one: the bug only shows on request two and later.

## When to use

You are seeing this: On a normal Node server you create one Pool at startup and share it. Use this skill when you run into "Edge + @neondatabase/serverless Pool: create, use, close per request".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_ayExvJb9XRKNBXcFD5oqKg). Version: `skv_T2ICNk6SzXxeMzit4Bph3A`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
