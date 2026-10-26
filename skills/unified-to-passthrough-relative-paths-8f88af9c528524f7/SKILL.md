---
name: "unified-to-passthrough-relative-paths-8f88af9c528524f7"
description: "Guide Unified.to passthrough: relative paths, __domain, and raw responses: The path must be relative to the platform base API URL, so for a full endpoint of YOUR_HOST.vendor.com/v2/users you pass v2/users. Context: Official docs (docs.unified. Use this when you hit exactly this in Unified.to passthrough. Not for different errors or different tools."
metadata:
  skill_id: "skl_MGxIMd2kvqfGMIcNNgo2HA"
  title: "Unified.to passthrough: relative paths, __domain, and raw responses"
  version: "skv_S9Up5H1n2zQQKiGZOuZADw"
  updated: "2026-10-03T13:59:37.913056+00:00"
  canonical_url: "https://vectle.com/skills/skl_MGxIMd2kvqfGMIcNNgo2HA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.unified.to/passthrough/overview\"]"
---

TL;DR: The path must be relative to the platform base API URL, so for a full endpoint of YOUR_HOST.vendor.com/v2/users you pass v2/users. Context: Official docs (docs.unified.to, Passthrough API): teaches the rules that make passthrough calls succeed. Find each integration's base URL under Feature Support then Passthrough on app.unified.to/integrations (click through to the integration).

Context: Official docs (docs.unified.to, Passthrough API): teaches the rules that make passthrough calls succeed. The path must be relative to the platform base API URL, so for a full endpoint of YOUR_HOST.vendor.com/v2/users you pass v2/users. Find each integration's base URL under Feature Support then Passthrough on app.unified.to/integrations (click through to the integration). There is exactly one reserved URL parameter: __domain, which overrides the default API URL for that integration. Passthrough responses are raw and unmodified, so formats, data structures, and error shapes vary per platform and your code must handle that. If you only need vendor fields missing from the unified model, the docs say to try raw fields or the Metadata API first, and if you reach for passthrough the record's original vendor ID is available in raw.__id. Most implementations should not need passthrough at all; for a real gap the docs suggest contacting them so the capability can be added to the unified API instead.

Checklist from the docs: 1. Pass the path relative to the platform base URL, never the full URL. 2. Look up the base URL per integration under Feature Support then Passthrough. 3. Use __domain only to override the default API URL. 4. Expect raw, platform-specific responses and error formats, no normalization. 5. Grab the original vendor ID from raw.__id when you need it for passthrough calls. 6. Try raw fields or the Metadata API before building on passthrough, and report genuine gaps so they can be added to the unified API.

## When to use
You hit exactly this: Unified.to passthrough: relative paths, __domain, and raw responses in Unified.to passthrough.

## When not to use
A different error, or the same symptom in a different tool. This page only covers the failure above.

## Compatibility
Unified.to passthrough (versions mentioned here: v2).

---

Source: [Vectle](https://vectle.com/skills/skl_MGxIMd2kvqfGMIcNNgo2HA). Version: `skv_S9Up5H1n2zQQKiGZOuZADw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
