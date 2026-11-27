---
name: "amadeus-api-error-flight-search-fails-ce8daf7de80041c4"
description: "amadeus api error flight search fails with 400 invalid origin"
metadata:
  skill_id: "skl_MmgPlsGHqkvK_fpZFnQyoA"
  title: "amadeus api error flight search fails with 400 invalid origin"
  version: "skv_QD3sEqtTZ5eIjV5wGl4sKA"
  updated: "2026-11-27T01:53:00.216042+00:00"
  canonical_url: "https://vectle.com/skills/skl_MmgPlsGHqkvK_fpZFnQyoA"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Print the exact request body your code sends and read the originLocationCode value literally.

Replace it with the uppercase 3 letter IATA code for the departure airport or city.

Verify the code with the Amadeus reference data locations call in the same environment, test or production.

Re-run the flight search with a simple one way request, a near departure date, and one adult traveler.

Re-add your real parameters one at a time: return date, travelers, cabin, and filters.

---

Source: [Vectle](https://vectle.com/skills/skl_MmgPlsGHqkvK_fpZFnQyoA). Version: `skv_QD3sEqtTZ5eIjV5wGl4sKA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
