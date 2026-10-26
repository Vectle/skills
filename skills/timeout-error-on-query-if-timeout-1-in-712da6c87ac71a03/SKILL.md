---
name: "timeout-error-on-query-if-timeout-1-in-712da6c87ac71a03"
description: "Qdrant: timeout error on query if timeout=1 in a distributed deployment. The verified fix is Fix: Maintainer generall: fixed in PR #5495; maintainer timvisee confirmed the fix shipped in Qdrant 1.12.5. Use this when you hit the symptoms above in qdrant; not for unrelated qdrant errors or general setup questions."
metadata:
  skill_id: "skl_aq_gRY5fHqWSEoXGXJq2rg"
  title: "Timeout error on query if timeout=1 in a distributed deployment"
  version: "skv_8b2GOWteZrfXEiMEOPOzDg"
  updated: "2026-10-03T04:38:36.239556+00:00"
  canonical_url: "https://vectle.com/skills/skl_aq_gRY5fHqWSEoXGXJq2rg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/qdrant/qdrant/issues/5463\"]"
---

## TL;DR

Fix: Maintainer generall: fixed in PR #5495; maintainer timvisee confirmed the fix shipped in Qdrant 1.12.5. Lesson for agents: if tiny timeouts fail on sharded collections while untimed queries succeed, upgrade to >= 1.12.5 instead of tuning the query.

## The error

```text
On a sharded (multi-node) collection, recommend/query requests fail with a timeout error when timeout=1 is passed, even though the actual execution takes less than a second. Without timeout, or with timeout=2, the same request succeeds.
```

## Fix

1. Maintainer generall: fixed in PR #5495; maintainer timvisee confirmed the fix shipped in Qdrant 1.12.5.
2. Lesson for agents: if tiny timeouts fail on sharded collections while untimed queries succeed, upgrade to >= 1.12.5 instead of tuning the query.

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

- How to fix "timeout error on query if timeout=1 in a distributed deployment" in qdrant
- qdrant: timeout error on query if timeout=1 in a distributed deployment
- timeout problem on query if timeout=1 in a distributed deployment

## Source

- https://github.com/qdrant/qdrant/issues/5463

---

Source: [Vectle](https://vectle.com/skills/skl_aq_gRY5fHqWSEoXGXJq2rg). Version: `skv_8b2GOWteZrfXEiMEOPOzDg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
