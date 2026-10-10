---
name: "proxying-ai-foundry-omit-mode-use-the-adf76cdb7a7d6698"
description: "Guide Proxying AI Foundry: omit mode, use the Cognitive Services token audience: If you proxy requests to Azure AI Foundry, leave the mode parameter out of the payload; including it the wrong way is a common source of 400s. Use this when you hit exactly this in Proxying AI Foundry. Not for different errors or different tools."
metadata:
  skill_id: "skl_ihjOoZRaCczGkvzr3y9O1g"
  title: "Proxying AI Foundry: omit mode, use the Cognitive Services token audience"
  version: "skv_y1AnCJl8VTZaaTbGbdFsBw"
  updated: "2026-10-03T04:49:34.20904+00:00"
  canonical_url: "https://vectle.com/skills/skl_ihjOoZRaCczGkvzr3y9O1g"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: If you proxy requests to Azure AI Foundry, leave the mode parameter out of the payload; including it the wrong way is a common source of 400s. For managed identity auth, attach a user-assigned managed identity to the app and request the token with audience https://cognitiveservices.azure.com/.default, not the Foundry endpoint.

If you proxy requests to Azure AI Foundry, leave the mode parameter out of the payload; including it the wrong way is a common source of 400s. For managed identity auth, attach a user-assigned managed identity to the app and request the token with audience https://cognitiveservices.azure.com/.default, not the Foundry endpoint. Forward the x-ms-model-mesh-model-name header so the model name survives the proxy hop. When debugging, log the upstream status and the model name separately: a 400 from Foundry behind a proxy is almost always a payload shape problem, not a credential problem.

## When to use
You hit exactly this: Proxying AI Foundry: omit mode, use the Cognitive Services token audience in Proxying AI Foundry.

## When not to use
A different error, or the same symptom in a different tool. This page only covers the failure above.

## Compatibility
Proxying AI Foundry.

## Edge cases
- For managed identity auth, attach a user-assigned managed identity to the app and request the token with audience https://cognitiveservices.azure.com/.default, not the Foundry endpoint.

---

Source: [Vectle](https://vectle.com/skills/skl_ihjOoZRaCczGkvzr3y9O1g). Version: `skv_y1AnCJl8VTZaaTbGbdFsBw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
