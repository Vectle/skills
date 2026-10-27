---
name: "coupa-spend-error-tail-supplier-count-be81de1ae1487910"
description: "Coupa spend error tail supplier count changes after hierarchy update"
metadata:
  skill_id: "skl_x2xk_6hEpF18HV8obCHe_w"
  title: "Coupa spend error tail supplier count changes after hierarchy update"
  version: "skv_ZPc_yEFhvHkDQCajlb57qA"
  updated: "2026-10-26T21:19:08.166403+00:00"
  canonical_url: "https://vectle.com/skills/skl_x2xk_6hEpF18HV8obCHe_w"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Freeze the comparison. Run the tail supplier report for the same period and the same spend threshold twice, noting the count before and after the hierarchy update. Expected: only the count and grouping changed, total spend for the period is unchanged.

Export the supplier lists from both runs and diff them. Expected: the difference is a named set of suppliers that moved, not a broad unexplained change.

Check each moved supplier in the supplier hierarchy. Expected: its parent or rollup node changed during the update, which explains why it entered or left the tail count.

Decide how the tail report should treat parent rollups: count suppliers at leaf level or at parent level, and confirm that choice with the spend analytics owner. Expected: one stated counting rule.

Rebuild or refresh the hierarchy mapping used by the report, then re-run the report for the original period. Expected: the tail count is stable across a second run with no hierarchy changes in between.

Annotate the report for the update date so readers do not read the count jump as procurement behaviour. Expected: the published report carries a note naming the hierarchy update as the cause.

---

Source: [Vectle](https://vectle.com/skills/skl_x2xk_6hEpF18HV8obCHe_w). Version: `skv_ZPc_yEFhvHkDQCajlb57qA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
