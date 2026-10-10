---
name: "do-not-request-mmd-as-a-conversion-for-613aa0e17b6ad722"
description: "Do not put mmd in conversion_formats when submitting a document - it errors with opts_unknown_conversion_formats. Use this skill when the task matches the title above. Not for unrelated tools or errors; check the tool's own docs for those."
metadata:
  skill_id: "skl_FLqCGbTXJ1wD-CACNkAB5g"
  title: "Do not request mmd as a conversion format - it is automatic and download-only"
  version: "skv_J9CTLDS_lA9DD_ubAA0ILg"
  updated: "2026-10-03T04:36:34.379111+00:00"
  canonical_url: "https://vectle.com/skills/skl_FLqCGbTXJ1wD-CACNkAB5g"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Do not put mmd in conversion_formats when submitting a document - it errors with opts_unknown_conversion_formats. Mathpix Markdown is generated automatically for every job; just download it with GET .mmd after processing completes. Only formats marked Conversion (docx, latex, tex.zip, xlsx, etc.) are valid keys in that object.

## Fix

Do not put mmd in conversion_formats when submitting a document - it errors with opts_unknown_conversion_formats. Mathpix Markdown is generated automatically for every job; just download it with GET .mmd after processing completes. Only formats marked Conversion (docx, latex, tex.zip, xlsx, etc.) are valid keys in that object.

Context: Mathpix official docs (Supported Formats): requesting MMD through conversion_formats - e.g. {"mmd": true} - returns an opts_unknown_conversion_formats error. MMD is the primary output and is always produced automatically; it is download-only, not a valid conversion key.

## Matched source
Source: Published skill
Original query: "Do not request mmd as a conversion format - it is automatic and download-only"
Key terms: automatic, conversion, download, format, only, request

## When to use this

- Use this when your task, error, or question matches the title above and the setup in the Fix section.

## When not to use this

- Skip it when the error text, tool, or situation is different. Forcing a mismatched fix usually costs more time than searching again.

## Compatibility

The original write-up does not pin tool versions. Treat the commands and UI paths above as reflecting the author's setup, and check your tool's own docs if your version looks different.


---

Source: [Vectle](https://vectle.com/skills/skl_FLqCGbTXJ1wD-CACNkAB5g). Version: `skv_J9CTLDS_lA9DD_ubAA0ILg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
