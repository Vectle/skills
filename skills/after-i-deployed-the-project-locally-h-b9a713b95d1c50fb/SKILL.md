---
name: "after-i-deployed-the-project-locally-h-b9a713b95d1c50fb"
description: "Firecrawl: after I deployed the project locally, he couldn't crawl the webpage and kept waiting. The verified fix is Fix: Collaborator rafaelsideguide merged PR #396 adding command: ['pnpm', 'run', 'worker:production'] to the worker service. Use this when you hit the symptoms above in firecrawl; not for unrelated firecrawl errors or general setup questions."
metadata:
  skill_id: "skl_F9-60NVcSVQYAVcZihaAoA"
  title: "After I deployed the project locally, he couldn't crawl the webpage and kept waiting"
  version: "skv_L9dpJ-Q-OOOVhAh6H2I58Q"
  updated: "2026-10-03T05:01:51.793293+00:00"
  canonical_url: "https://vectle.com/skills/skl_F9-60NVcSVQYAVcZihaAoA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/firecrawl/firecrawl/issues/340\"]"
---

## TL;DR

Fix: Collaborator rafaelsideguide merged PR #396 adding command: ['pnpm', 'run', 'worker:production'] to the worker service.

## The error

```text
[Self-Host] After docker-deploying Firecrawl, crawl jobs sit in 'waiting' forever in the UI while /scrape works.
```

## Fix

1. Collaborator rafaelsideguide merged PR #396 adding command: ['pnpm', 'run', 'worker:production'] to the worker service.

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

- How to fix "after I deployed the project locally, he couldn't crawl the webpage and kept waiting" in firecrawl
- firecrawl: after I deployed the project locally, he couldn't crawl the webpage and kept waiting

## Root cause

Root cause found by contributor kun432: the docker-compose worker service was not running the worker production command, so no worker consumed crawl jobs.

## Source

- https://github.com/firecrawl/firecrawl/issues/340

---

Source: [Vectle](https://vectle.com/skills/skl_F9-60NVcSVQYAVcZihaAoA). Version: `skv_L9dpJ-Q-OOOVhAh6H2I58Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
