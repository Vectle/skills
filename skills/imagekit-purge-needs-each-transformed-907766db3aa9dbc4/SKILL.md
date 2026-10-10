---
name: "imagekit-purge-needs-each-transformed-907766db3aa9dbc4"
description: "For bulk changes, consider versioning filenames instead of purging dozens of variants. Use this skill when the task matches the title above. Not for unrelated tools or errors; check the tool's own docs for those."
metadata:
  skill_id: "skl_iEWij1GfbmXhhr8zp_fQMA"
  title: "ImageKit purge needs each transformed URL and completes asynchronously"
  version: "skv_X0HK2S5sIAW_4dDOO5z82Q"
  updated: "2026-10-03T05:56:44.886145+00:00"
  canonical_url: "https://vectle.com/skills/skl_iEWij1GfbmXhhr8zp_fQMA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

For bulk changes, consider versioning filenames instead of purging dozens of variants. Because each transformed variant is its own URL, purging the original does not purge the transformed copies; you must purge each variant URL. The purge is also asynchronous: the API returns a request ID and you check completion with the purge status endpoint.

## Fix

Purge every transformed variant URL explicitly, not just the source file. Treat the purge call as a job: capture the request ID and poll the status endpoint before declaring the cache clear. For bulk changes, consider versioning filenames instead of purging dozens of variants.

Context: Official docs (ImageKit API reference, via SDK docs): purge cache accepts the full URL of the file to clear, covering both the CDN and ImageKit's internal cache. Because each transformed variant is its own URL, purging the original does not purge the transformed copies; you must purge each variant URL. The purge is also asynchronous: the API returns a request ID and you check completion with the purge status endpoint.

## Matched source
Source: Published skill
Original query: "ImageKit purge needs each transformed URL and completes asynchronously"
Key terms: asynchronously, completes, each, imagekit, needs, purge, transformed

## When to use this

- Use this when your task, error, or question matches the title above and the setup in the Fix section.

## When not to use this

- Skip it when the error text, tool, or situation is different. Forcing a mismatched fix usually costs more time than searching again.

## Compatibility

The original write-up does not pin tool versions. Treat the commands and UI paths above as reflecting the author's setup, and check your tool's own docs if your version looks different.


---

Source: [Vectle](https://vectle.com/skills/skl_iEWij1GfbmXhhr8zp_fQMA). Version: `skv_X0HK2S5sIAW_4dDOO5z82Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
