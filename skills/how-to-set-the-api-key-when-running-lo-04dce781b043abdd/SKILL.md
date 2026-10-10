---
name: "how-to-set-the-api-key-when-running-lo-04dce781b043abdd"
description: "Firecrawl: how to set the api key when running locally?. The verified fix is Fix: Collaborator rafaelsideguide: set USE_DB_AUTHENTICATION=false in .env and use any string as the API key; follow the self-host guide. Use this when you hit the symptoms above in firecrawl; not for unrelated firecrawl errors or general setup questions."
metadata:
  skill_id: "skl_3oLkZLhkZKWMhN8NLwxBEg"
  title: "How to set the api key when running locally?"
  version: "skv_Dm9QpEOOa9WJK7GAxs3YtA"
  updated: "2026-10-03T05:56:27.561136+00:00"
  canonical_url: "https://vectle.com/skills/skl_3oLkZLhkZKWMhN8NLwxBEg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Fix: Collaborator rafaelsideguide: set USE_DB_AUTHENTICATION=false in .env and use any string as the API key; follow the self-host guide.

## The error

```text
[Self-Host] Question: how to set the API key when running Firecrawl locally / what value to use in client SDKs and integrations like Dify.
```

## Fix

1. Collaborator rafaelsideguide: set USE_DB_AUTHENTICATION=false in .env and use any string as the API key; follow the self-host guide.

Success check: the symptom above is gone and the original operation completes.

## When to use

- You hit this exact symptom in firecrawl.
- You want the verified fix without digging through the thread.

## When not to use

- A different error in firecrawl, even a similar-looking one.
- General firecrawl setup or credential questions.

## Compatibility

- Firecrawl (firecrawl/firecrawl)

## Variant phrasings

- How to fix "how to set the api key when running locally?" in firecrawl
- firecrawl: how to set the api key when running locally?

## Source

- https://github.com/firecrawl/firecrawl/issues/557

---

Source: [Vectle](https://vectle.com/skills/skl_3oLkZLhkZKWMhN8NLwxBEg). Version: `skv_Dm9QpEOOa9WJK7GAxs3YtA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
