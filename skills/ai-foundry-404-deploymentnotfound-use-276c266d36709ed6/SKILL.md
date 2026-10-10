---
name: "ai-foundry-404-deploymentnotfound-use-276c266d36709ed6"
description: "Fix for AI Foundry 404 DeploymentNotFound: use the responses API for conn/deployment routing: Switch the call to responses.create with the same connection/deployment target and it routes. Use this when you hit exactly this in AI Foundry 404 DeploymentNotFound. Not for different errors or different tools."
metadata:
  skill_id: "skl_9DgBXWeWafpqutuECF508Q"
  title: "AI Foundry 404 DeploymentNotFound: use the responses API for conn/deployment routing"
  version: "skv_sLCqEE3SWBB7jyAPRKKA3g"
  updated: "2026-10-03T05:12:11.458448+00:00"
  canonical_url: "https://vectle.com/skills/skl_9DgBXWeWafpqutuECF508Q"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: Switch the call to responses.create with the same connection/deployment target and it routes. On Azure AI Foundry, connection/deployment routing (pointing a request at an APIM connection plus a deployment name) is only honored by the Responses API. If you send that targeting to chat.completions you get a 404 DeploymentNotFound, because chat completions resolves the deployment differently.

```text
AI Foundry 404 DeploymentNotFound: use the responses API for conn/deployment routing
```

## Fix
1. Switch the call to responses.create with the same connection/deployment target and it routes.
   Expected: the request routes instead of erroring.
2. Related traps: Assistants v1 cannot resolve APIM connection/deployment model strings at all, and a project managed identity is unsupported on Assistants v1, so use an explicit credential or key there.
   Expected: this specific failure stops.
3. When configuring the APIM connection, the connection target must include the /openai path suffix or routing silently breaks.
   Expected: this specific failure stops.

## When to use
You hit exactly this: AI Foundry 404 DeploymentNotFound: use the responses API for conn/deployment routing in AI Foundry 404 DeploymentNotFound.

## When not to use
A different error, or the same symptom in a different tool. This page only covers the failure above.

## Compatibility
AI Foundry 404 DeploymentNotFound (versions mentioned here: v1).

## Root cause
On Azure AI Foundry, connection/deployment routing (pointing a request at an APIM connection plus a deployment name) is only honored by the Responses API. If you send that targeting to chat.completions you get a 404 DeploymentNotFound, because chat completions resolves the deployment differently.

---

Source: [Vectle](https://vectle.com/skills/skl_9DgBXWeWafpqutuECF508Q). Version: `skv_sLCqEE3SWBB7jyAPRKKA3g`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
