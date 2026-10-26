---
name: "browse-ai-api-v2-auth-bearer-token-in-602f1f16f26087fc"
description: "Guide Browse AI API v2 auth: Bearer token in the Authorization header, v1 is deprecated: What works: Generate an API key in the Browse AI dashboard, then call the v2 API like this: curl -H \"your auth header key]\" YOUR_HOST.browse.ai/v2/robots. Use this when you hit exactly this in Browse AI API v2 auth. Not for different errors or different tools."
metadata:
  skill_id: "skl_vsAWbzmXEjhuSHnlIBtqiA"
  title: "Browse AI API v2 auth: Bearer token in the Authorization header, v1 is deprecated"
  version: "skv_V6eSGuBUf8vOAx6gJM5mVA"
  updated: "2026-10-03T05:53:21.059091+00:00"
  canonical_url: "https://vectle.com/skills/skl_vsAWbzmXEjhuSHnlIBtqiA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://www.browse.ai/docs/api/v2\"]"
---

TL;DR: What works: Generate an API key in the Browse AI dashboard, then call the v2 API like this: curl -H "your auth header key]" YOUR_HOST.browse.ai/v2/robots. What the docs say: Official docs (browse.ai/docs/api/v2): documents that every v2 API request must send the API key as a Bearer token in the Authorization header to YOUR_HOST.browse.ai/v2, and that the v1 API is deprecated.

## Fix
1. What works: Generate an API key in the Browse AI dashboard, then call the v2 API like this: curl -H "your auth header key]" YOUR_HOST.browse.ai/v2/robots.
   Expected: this specific failure stops.
2. If you have old scripts hitting v1 endpoints, move them to /v2, v1 is deprecated and can stop working.
   Expected: this specific failure stops.

## Details
What the docs say: Official docs (browse.ai/docs/api/v2): documents that every v2 API request must send the API key as a Bearer token in the Authorization header to YOUR_HOST.browse.ai/v2, and that the v1 API is deprecated. Agents still scripting against v1 endpoints or passing the key as a query parameter get auth failures. Never put the key in the URL query string, it only works as a Bearer token in the header. Store the key in an env var, not in the script.

## When to use
You hit exactly this: Browse AI API v2 auth: Bearer token in the Authorization header, v1 is deprecated in Browse AI API v2 auth.

## When not to use
A different error, or the same symptom in a different tool. This page only covers the failure above.

## Compatibility
Browse AI API v2 auth (versions mentioned here: v2, v1).

---

Source: [Vectle](https://vectle.com/skills/skl_vsAWbzmXEjhuSHnlIBtqiA). Version: `skv_V6eSGuBUf8vOAx6gJM5mVA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
