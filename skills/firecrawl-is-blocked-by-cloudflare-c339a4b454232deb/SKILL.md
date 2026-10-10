---
name: "firecrawl-is-blocked-by-cloudflare-c339a4b454232deb"
description: "Firecrawl: firecrawl is blocked by Cloudflare. The verified fix is Fix: Lesson: treat Cloudflare-blocked targets as a known limitation - retry once, then route around (different engine or source) rather than assuming a bug. Use this when you hit the symptoms above in firecrawl; not for unrelated firecrawl errors or general setup questions."
metadata:
  skill_id: "skl_3Hbh7dnW6McZRkdZgj8gbQ"
  title: "Firecrawl is blocked by Cloudflare"
  version: "skv_B3VtGO-sniUV9f9P2jrXYg"
  updated: "2026-10-03T05:00:08.96979+00:00"
  canonical_url: "https://vectle.com/skills/skl_3Hbh7dnW6McZRkdZgj8gbQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Fix: Lesson: treat Cloudflare-blocked targets as a known limitation - retry once, then route around (different engine or source) rather than assuming a bug.

## The error

```text
Firecrawl is blocked by Cloudflare's free bot protection, both self-hosted and cloud, when scraping protected sites.
```

## Fix

1. Lesson: treat Cloudflare-blocked targets as a known limitation - retry once, then route around (different engine or source) rather than assuming a bug.

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

- How to fix "firecrawl is blocked by Cloudflare" in firecrawl

## Source

- https://github.com/firecrawl/firecrawl/issues/495

---

Source: [Vectle](https://vectle.com/skills/skl_3Hbh7dnW6McZRkdZgj8gbQ). Version: `skv_B3VtGO-sniUV9f9P2jrXYg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
