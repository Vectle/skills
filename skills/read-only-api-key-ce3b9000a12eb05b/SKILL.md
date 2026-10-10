---
name: "read-only-api-key-ce3b9000a12eb05b"
description: "Qdrant: read-only API key. The verified fix is Implemented and closed as completed via bounty PR #2979. Use this when you hit the symptoms above in qdrant; not for unrelated qdrant errors or general setup questions."
metadata:
  skill_id: "skl_HbSvV6reNSDd0SWrXr6qKQ"
  title: "Read-only API key"
  version: "skv_NZDXEn7y7cXm49yw7yBU5Q"
  updated: "2026-10-03T04:45:22.962285+00:00"
  canonical_url: "https://vectle.com/skills/skl_HbSvV6reNSDd0SWrXr6qKQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Implemented and closed as completed via bounty PR #2979. Qdrant now supports read-only API keys (JWT-based RBAC): agents can be issued a search-only credential instead of the full API key when the instance only needs to serve queries.

## The error

```text
Feature request: an API key that only allows read operations (search, scroll, get-point, recommend, list collections) so a Qdrant instance can be safely exposed for search-only workloads without reverse-proxy hacks.
```

## Fix

1. Implemented and closed as completed via bounty PR #2979.
2. Qdrant now supports read-only API keys (JWT-based RBAC): agents can be issued a search-only credential instead of the full API key when the instance only needs to serve queries.

Success check: the symptom above is gone and the original operation completes.

## When to use

- You hit this exact symptom in qdrant.
- You want the verified fix without digging through the thread.

## When not to use

- A different error in qdrant, even a similar-looking one.
- General qdrant setup or credential questions.

## Compatibility

- Qdrant (qdrant/qdrant)

## Variant phrasings

- How to fix "read-only API key" in qdrant
- qdrant: read-only API key

## Source

- https://github.com/qdrant/qdrant/issues/1959

---

Source: [Vectle](https://vectle.com/skills/skl_HbSvV6reNSDd0SWrXr6qKQ). Version: `skv_NZDXEn7y7cXm49yw7yBU5Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
