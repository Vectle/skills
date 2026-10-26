---
name: "rate-limit-is-exceeded-try-again-in-10-ac914389e90d9022"
description: "Diagnoses Azure OpenAI HTTP 429 'Rate limit is exceeded' errors, which mean the deployment's tokens-per-minute quota is exhausted. Use when an agent sees this on Azure OpenAI chat or embedding calls. Covers reading the retry hint, backing off, and requesting a quota increase in the Azure portal. Not for context-length 400s or authentication failures."
metadata:
  skill_id: "skl_tCh4Gfdg_dYwn0sj1fCjPg"
  title: "Rate limit is exceeded. Try again in 10 seconds. (Azure OpenAI 429)"
  version: "skv_3DCwiX-eRJ9W2IrSGn3ukA"
  updated: "2026-10-03T04:45:52.726179+00:00"
  canonical_url: "https://vectle.com/skills/skl_tCh4Gfdg_dYwn0sj1fCjPg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://learn.microsoft.com/en-us/answers/questions/1867144/an-error-occurred-when-calling-azure-openai-server\"]"
---

# Rate limit is exceeded. Try again in 10 seconds. (Azure OpenAI 429)

## TL;DR
Your deployment blew through its tokens-per-minute quota. Honor the retry hint, back off, and if it keeps happening, request a quota increase for the model in the Azure portal. Retrying faster just extends the pain.

## The error
```
Rate limit is exceeded. Try again in 10 seconds.
```
(HTTP 429 from the Azure OpenAI endpoint.)

## Fix it
1. Read the number in the message and wait at least that long before retrying. Expected: the next attempt has a chance instead of a guaranteed 429.
2. Add exponential backoff with jitter to the calling code. Expected: bursts smooth out and the error rate drops.
3. Check current usage: Azure portal, your OpenAI resource, Quotas. Expected: you see the TPM limit and how close you are.
4. If you consistently hit the ceiling, request a quota increase: portal, Quotas, select the model and region, request more TPM. Expected: the increase is approved and the errors stop.
5. Split load across regions or deployments if one quota pool is too small. Expected: per-deployment TPM stays under the limit.

## When to use this
- An agent sees "Rate limit is exceeded. Try again in N seconds." from Azure OpenAI.
- Embedding or chat workloads that run fine at low volume and 429 under load.

## When NOT to use this
- 400 context-length errors. Those never succeed on retry; this one does.
- 401 or 403 errors. Those are keys and access, not quota.

## Compatibility
- Azure OpenAI Service, all models. Quotas are per model, per region, per subscription.

### Variant phrasings
- "Rate limit is exceeded. Try again in 20 seconds."
- "429 Too Many Requests" on the Azure OpenAI endpoint
- "You exceeded your current quota"

## Root cause
Azure OpenAI throttles per deployment on tokens per minute and requests per minute. The message names the wait because the throttle is time-based: the bucket refills and the next attempt succeeds. Chronic 429s mean the quota is simply too small for the workload, which is why the Microsoft Q&A thread's accepted resolution was a quota increase.

## Edge cases
- Batch embedding jobs can 429 one minute and pass the next. That is normal; backoff handles it.
- Different models have separate quotas. Raising GPT-4o quota does nothing for your embedding model's 429s.


---

Source: [Vectle](https://vectle.com/skills/skl_tCh4Gfdg_dYwn0sj1fCjPg). Version: `skv_3DCwiX-eRJ9W2IrSGn3ukA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
