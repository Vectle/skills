---
name: "vespa-proton-taking-20gb-upon-start-up-49d7a3289e20eb5a"
description: "Fixes Vespa proton using 20GB of memory on startup with zero documents by upgrading to 8.140.13+ (improved memory accounting) or 8.181.15 (cuts multivalue attribute static memory up to 40 percent). Use when proton memory is high at startup with empty document types. Not for memory growth during feeding or querying."
metadata:
  skill_id: "skl_FLAx0g-1DO5V6f-8MxO4gg"
  title: "Vespa proton taking 20GB upon start-up"
  version: "skv_9AsF_JDHOlvcPPYu_PxFuA"
  updated: "2026-10-03T04:15:16.018401+00:00"
  canonical_url: "https://vectle.com/skills/skl_FLAx0g-1DO5V6f-8MxO4gg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Upgrade: memory accounting and usage were improved in 8.140.13, and 8.181.15 cut static memory of multivalue attributes by up to 40 percent. There is a fixed memory cost per document type and per field (the reporter had 39 schemas), so high startup memory with zero documents is expected on older 8.x versions.

## The problem

Vespa proton takes 20GB upon startup with zero documents deployed across many schemas (the reporter had 39).

## Fix it

1. Check your Vespa version.
   Success check: you are on an 8.x older than 8.140.13, confirming the fix applies.

2. Upgrade to 8.140.13 or newer (8.181.15+ preferred for the multivalue attribute savings).
   Success check: startup memory drops noticeably with the same schemas.

3. Inspect per-document-type usage via the searchnode metrics or the proton state API to confirm which types cost the most.
   Success check: metrics show the fixed per-type cost.

## When this applies

- Proton uses a lot of memory at startup with zero or few documents.
- Many schemas/document types deployed (dozens).
- You are on Vespa 8.x older than 8.140.13.

## When it does not apply

- Memory grows during feeding or querying; that is a different tuning problem.
- You are already on 8.181.15+ and memory is still high; profile with the state API.
- Vespa 7.x; the fixes are 8.x-specific.

## Compatibility

- Vespa 8.140.13+: improved memory accounting. 8.181.15+: multivalue attribute static memory cut up to 40 percent.

## Variant phrasings

- Vespa proton high memory startup zero documents
- proton 20GB memory startup
- Vespa memory per document type field fixed cost

## Why it happens

Proton allocates a fixed memory footprint per document type and per field at startup, before any documents arrive. With many schemas this adds up. Older 8.x versions also over-accounted multivalue attribute memory, fixed in the versions above.

## Edge cases

- Reducing schema count or consolidating fields lowers the fixed cost directly.
- Source: https://github.com/vespa-engine/vespa/issues/26350


---

Source: [Vectle](https://vectle.com/skills/skl_FLAx0g-1DO5V6f-8MxO4gg). Version: `skv_9AsF_JDHOlvcPPYu_PxFuA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
