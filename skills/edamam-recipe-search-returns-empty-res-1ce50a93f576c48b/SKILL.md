---
name: "edamam-recipe-search-returns-empty-res-1ce50a93f576c48b"
description: "Edamam recipe search returns empty results for common ingredient: query error fix"
metadata:
  skill_id: "skl_YD6JkcQlJYLIbqPS_8v1YA"
  title: "Edamam recipe search returns empty results for common ingredient: query error fix"
  version: "skv_IC0WWQoe_A7g7lXQ87AR2g"
  updated: "2026-11-13T13:54:53.884026+00:00"
  canonical_url: "https://vectle.com/skills/skl_YD6JkcQlJYLIbqPS_8v1YA"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Reproduce with the simplest possible call: one common ingredient as the query, no diet, health, cuisine, or meal filters, and a small result window.

Check how the ingredient text is sent: spaces and multi word ingredients must be URL encoded as a single query value, and the query must not carry surrounding quotes or a trailing operator word.

Add the filters from the failing call back one at a time, running the call after each addition.

Check the result window parameters on the failing call: a from offset beyond the total count returns an empty page even when matches exist.

Compare the app id and key environment: a development credential against the production endpoint, or the recipe search plan without a filter the call relies on, can silently narrow results.

Fix the identified filter or parameter in the app, then rerun the original failing search.

---

Source: [Vectle](https://vectle.com/skills/skl_YD6JkcQlJYLIbqPS_8v1YA). Version: `skv_IC0WWQoe_A7g7lXQ87AR2g`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
