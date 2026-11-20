---
name: "google-custom-search-weighting-results-f557969367bcfb0c"
description: "google custom search weighting results not applied error sites ranking wrong"
metadata:
  skill_id: "skl_M_9nz2aRSoWlXVvuhcQ3_A"
  title: "google custom search weighting results not applied error sites ranking wrong"
  version: "skv_9BTrU_aNllloSsFV-xbRow"
  updated: "2026-11-20T01:52:48.207632+00:00"
  canonical_url: "https://vectle.com/skills/skl_M_9nz2aRSoWlXVvuhcQ3_A"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Log the exact engine identifier your application sends on a failing search and compare it with the engine you edited in the control panel.

In the control panel, confirm each boosted or weighted site is actually included in the sites to search list.

Pick a query where the target page is already returned somewhere in the results without weighting changes.

Apply a strong boost to that site, wait a few minutes for the configuration to propagate, and rerun the same query.

If results are unchanged, check for cached responses in your app and for refinement or annotation files overriding the control panel settings.

---

Source: [Vectle](https://vectle.com/skills/skl_M_9nz2aRSoWlXVvuhcQ3_A). Version: `skv_9BTrU_aNllloSsFV-xbRow`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
