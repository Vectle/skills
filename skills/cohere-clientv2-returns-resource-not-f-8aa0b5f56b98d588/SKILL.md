---
name: "cohere-clientv2-returns-resource-not-f-8aa0b5f56b98d588"
description: "Fixes cohere.ClientV2 returning 'Resource not found error' against an Azure-deployed Cohere model while cohere.Client works. Use this when embeddings work on v1 but fail on v2 against Azure. Not for non-Azure deployments or for auth errors."
metadata:
  skill_id: "skl_7ySe0dm6OV_XJ5Qy9JZI8A"
  title: "cohere.ClientV2 returns Resource not found error against an Azure-deployed Cohere model"
  version: "skv_BLcOQwiCGlH3ZebGNsN5Hw"
  updated: "2026-10-03T04:42:21.658459+00:00"
  canonical_url: "https://vectle.com/skills/skl_7ySe0dm6OV_XJ5Qy9JZI8A"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://vectle.com/threads/thr_ZoR7CORZURzjl2eGun3eQg\",\"https://github.com/cohere-ai/cohere-python/issues/661\"]"
---

TL;DR: if `cohere.Client` works but `cohere.ClientV2` returns `Resource not found error` against an Azure deployment of a Cohere model, the deployment itself is the problem, not your code. The model must be deployed as a serverless endpoint: the "Deploy models to Azure AI model inference service" setting under Preview Features has to be OFF when you deploy. Also do not append `/v1` to the base URL. The Cohere maintainer reproduced this on Azure and confirmed the toggle-off deployment fixes it.

```text
Resource not found error
```

## Steps

1. Redeploy the model with the "Deploy models to Azure AI model inference service" preview toggle set to OFF.

2. Point the client's base_url at the deployment URL without appending `/v1`.

3. Retry the ClientV2 call.

   Expected: embeddings return. Success check: no more resource-not-found.

## When to use this

- Azure-deployed Cohere model (e.g. Cohere-embed-v3-english), ClientV2 fails while Client works.

## When NOT to use this

- Non-Azure deployments; the toggle is Azure-specific.
- Auth errors; check the key.

## Compatibility

- cohere-python ClientV2 against Azure AI deployments.

## Variant phrasings

- "cohere ClientV2 azure resource not found"
- "cohere azure serverless endpoint ClientV2"

## Root cause

With the preview toggle on, the model deploys to the AI model inference service, whose routing the Cohere client cannot address directly; the serverless endpoint shape is what ClientV2 expects.

## Edge cases

- The maintainer confirmed deploying Embed V4 with the toggle off works; the pattern holds across embed models.

Source: https://github.com/cohere-ai/cohere-python/issues/661

---

Source: [Vectle](https://vectle.com/skills/skl_7ySe0dm6OV_XJ5Qy9JZI8A). Version: `skv_BLcOQwiCGlH3ZebGNsN5Hw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
