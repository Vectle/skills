---
name: "imgix-changing-params-after-signing-br-0ad846ac3aa91e53"
description: "Keep the secure token server-side and generate signed URLs at render time rather than storing them. Use this skill when the task matches the title above. Not for unrelated tools or errors; check the tool's own docs for those."
metadata:
  skill_id: "skl_kE_AxBJOoS8P0TyHtsZF7w"
  title: "imgix: changing params after signing breaks the URL with a 403"
  version: "skv_3yrW2eCRtEqKac33K7AtyA"
  updated: "2026-10-03T05:55:22.964361+00:00"
  canonical_url: "https://vectle.com/skills/skl_kE_AxBJOoS8P0TyHtsZF7w"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Keep the secure token server-side and generate signed URLs at render time rather than storing them. If the path or parameters are altered after signing, the URL returns 403 Forbidden instead of the asset. That means any code that tweaks width or height on an already-signed URL breaks it; you must re-sign after every parameter change.

## Fix

Sign URLs as the last step of URL construction, after all parameters are final. If a signed URL 403s, check whether anything appended, reordered, or re-encoded a parameter after signing. Keep the secure token server-side and generate signed URLs at render time rather than storing them.

Context: Official docs (imgix, securing assets): signed URLs use an MD5 of the URL plus the source's secure token, appended as the s parameter. If the path or parameters are altered after signing, the URL returns 403 Forbidden instead of the asset. That means any code that tweaks width or height on an already-signed URL breaks it; you must re-sign after every parameter change.

## Matched source
Source: Published skill
Original query: "imgix: changing params after signing breaks the URL with a 403"
Key terms: after, breaks, changing, imgix, params, signing

## When to use this

- Use this when your task, error, or question matches the title above and the setup in the Fix section.

## When not to use this

- Skip it when the error text, tool, or situation is different. Forcing a mismatched fix usually costs more time than searching again.

## Compatibility

The original write-up does not pin tool versions. Treat the commands and UI paths above as reflecting the author's setup, and check your tool's own docs if your version looks different.


---

Source: [Vectle](https://vectle.com/skills/skl_kE_AxBJOoS8P0TyHtsZF7w). Version: `skv_3yrW2eCRtEqKac33K7AtyA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
