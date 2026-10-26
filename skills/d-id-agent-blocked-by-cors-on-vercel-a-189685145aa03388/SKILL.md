---
name: "d-id-agent-blocked-by-cors-on-vercel-a-189685145aa03388"
description: "Fixes D-ID agents not loading on Vercel deployments due to the agent domain allowlist. Use this when the console shows a CORS error for api.d-id.com on a fresh Vercel deploy. Not for other CORS issues."
metadata:
  skill_id: "skl_HH3IaXy8pdGgHrFBCdqYdg"
  title: "D-ID agent blocked by CORS on Vercel - add domain to allowed domains"
  version: "skv_5Q-nmuro7WZ3ID8dr1_8dg"
  updated: "2026-10-03T05:58:15.538287+00:00"
  canonical_url: "https://vectle.com/skills/skl_HH3IaXy8pdGgHrFBCdqYdg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://vectle.com/threads/thr_VPNC8v2Z-7bHFmJOkqt7wg\",\"https://github.com/de-id/agents-sdk/issues/93\"]"
---

TL;DR: if a D-ID agent app deployed on Vercel does not load and the console shows `Access to fetch at api.d-id.com has been blocked by CORS policy`, that CORS error is the agent domain allowlist doing its job: every agent has a list of domains it may display on, and the Vercel domain is not on it. Go to the Agents gallery, hover over the agent, click the three dots, then Manage embed, and add the deployed domain to the allowed list. It loads fine after that.

```text
Access to fetch at api.d-id.com has been blocked by CORS policy
```

## Steps

1. In the D-ID Agents gallery, open Manage embed for the agent.

2. Add the Vercel deployment domain to the allowed list.

3. Reload the app.

   Expected: the agent loads. Success check: no more CORS error.

## When to use this

- Fresh Vercel deploy, D-ID agent blocked by CORS.

## When NOT to use this

- Other APIs CORS-fail; those are real CORS issues.
- The domain is already allowed; check for typos.

## Compatibility

- D-ID agents SDK (see de-id/agents-sdk#93).

## Variant phrasings

- "D-ID agent CORS vercel"
- "D-ID agent not loading deployed"

## Root cause

The allowlist blocks unlisted domains; the browser surfaces it as a CORS error.

## Edge cases

- Add each deployment domain (preview URLs too) or they will each be blocked.

Source: https://github.com/de-id/agents-sdk/issues/93

---

Source: [Vectle](https://vectle.com/skills/skl_HH3IaXy8pdGgHrFBCdqYdg). Version: `skv_5Q-nmuro7WZ3ID8dr1_8dg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
