---
name: "bigquery-group-concat-function-not-fou-ffd55e6b38e860a7"
description: "bigquery group_concat function not found error use string_agg fails"
metadata:
  skill_id: "skl_RqydWTCBDRioXgvTiy_3ew"
  title: "bigquery group_concat function not found error use string_agg fails"
  version: "skv_cijY2_9UjSWKzOc9EengtA"
  updated: "2026-11-09T01:54:25.774862+00:00"
  canonical_url: "https://vectle.com/skills/skl_RqydWTCBDRioXgvTiy_3ew"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Confirm the query uses Standard SQL and find every GROUP_CONCAT call in it.

Replace GROUP_CONCAT with STRING_AGG and pass the separator as the second argument, for example STRING_AGG with a value and a comma separator.

If STRING_AGG now fails on types, wrap the value in CAST AS STRING inside the aggregate. Numbers, dates, and booleans must be cast before aggregation.

Move any ordering into the aggregate call using ORDER BY inside STRING_AGG, and remove an outer ORDER BY that was only ordering the concatenated list.

Run the query on one group first and check the combined value, its separator, and how missing values are handled. Add a filter to skip nulls before aggregation if empty entries appear.

---

Source: [Vectle](https://vectle.com/skills/skl_RqydWTCBDRioXgvTiy_3ew). Version: `skv_cijY2_9UjSWKzOc9EengtA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
