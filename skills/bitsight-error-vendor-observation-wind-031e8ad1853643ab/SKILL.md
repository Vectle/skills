---
name: "bitsight-error-vendor-observation-wind-031e8ad1853643ab"
description: "BitSight error vendor observation window shows findings after remediation"
metadata:
  skill_id: "skl_NVjaKwJFjgVAFQzC7wFvJw"
  title: "BitSight error vendor observation window shows findings after remediation"
  version: "skv_vFLfjtLrr4m03kc_5Y1fhw"
  updated: "2026-10-31T01:55:23.231537+00:00"
  canonical_url: "https://vectle.com/skills/skl_NVjaKwJFjgVAFQzC7wFvJw"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

**Open the finding and read its dates.** Note the first-seen date, the last-seen date, and the observation window the rating uses. Expected: you can place the vendor claimed fix date against the last-seen date.

**Compare the fix date with the last-seen date.** If the last observation is older than the fix, the record is stale, not wrong. Expected: a clear stale versus still-present call before anyone escalates.

**For a stale finding, trigger or await a rescan.** Use the available refresh or rescan path for the vendor, or note the next scheduled observation. Expected: a new observation date appears and the finding either closes or updates its last-seen date.

**If the finding was observed after the fix, inspect what is externally visible.** Check the affected asset address and service from outside the vendor network and compare it with the finding detail. Expected: either the old configuration is still exposed (the fix was internal only) or the finding detail no longer matches reality.

**Record the outcome on the vendor review.** Attach the rescan result or the external check to the vendor record. Success check: the finding status matches an observation dated after the remediation, and the review notes state which case it was.

---

Source: [Vectle](https://vectle.com/skills/skl_NVjaKwJFjgVAFQzC7wFvJw). Version: `skv_vFLfjtLrr4m03kc_5Y1fhw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
