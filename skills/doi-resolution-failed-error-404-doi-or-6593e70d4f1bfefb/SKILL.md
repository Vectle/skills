---
name: "doi-resolution-failed-error-404-doi-or-6593e70d4f1bfefb"
description: "DOI resolution failed error 404 doi.org link not found"
metadata:
  skill_id: "skl_T0s5fuXZ04iewGQi-XWd0g"
  title: "DOI resolution failed error 404 doi.org link not found"
  version: "skv_z07katMwwlslJ6NS93mfBg"
  updated: "2026-11-04T13:54:13.470333+00:00"
  canonical_url: "https://vectle.com/skills/skl_T0s5fuXZ04iewGQi-XWd0g"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Extract the DOI exactly as stored and strip surrounding punctuation, trailing periods, and URL prefixes. Keep only the part starting with 10.

Resolve the cleaned DOI directly in a browser or with curl -I against the doi.org resolver.

Query the Crossref API for the same DOI to check registration.

If Crossref returns 404, search Crossref by the exact paper title from the reference.

Fix the reference: replace the DOI with the verified DOI from step 4, or flag the entry for human review if no match exists. Never invent a DOI.

Re-run the citation verifier on the full reference list.

---

Source: [Vectle](https://vectle.com/skills/skl_T0s5fuXZ04iewGQi-XWd0g). Version: `skv_z07katMwwlslJ6NS93mfBg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
