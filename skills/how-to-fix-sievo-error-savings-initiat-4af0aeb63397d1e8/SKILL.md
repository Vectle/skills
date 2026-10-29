---
name: "how-to-fix-sievo-error-savings-initiat-4af0aeb63397d1e8"
description: "how to fix Sievo error savings initiative double counted across two categories fails error"
metadata:
  skill_id: "skl_Q2dHqZ2wkiE7tqT9AZ_Y7w"
  title: "how to fix Sievo error savings initiative double counted across two categories fails error"
  version: "skv_kF7R5J-FlCm-WYwoYTpFDQ"
  updated: "2026-10-29T01:57:05.758064+00:00"
  canonical_url: "https://vectle.com/skills/skl_Q2dHqZ2wkiE7tqT9AZ_Y7w"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Open the initiative in Sievo and note its total validated savings figure. Expected: one initiative total exists; use it as the reference number for every check below.

Open the category allocation on the initiative. Expected: either two categories each at 100 percent (the double count), or an intended split such as 60 and 40 that sums to 100.

Check the initiative history or change log for a category edit. Expected: if the category was changed mid-project, both the original and replacement category rows may still be active, which is the second common cause.

Correct the allocation: set the intended percentage per category so the percentages sum to exactly 100, and deactivate or delete the stale category row rather than leaving it at zero with savings attached. Expected: the allocation panel shows one active row per real category and a total of 100 percent.

Check any sub-initiatives or child actions under the initiative. Expected: children inherit the corrected allocation and do not carry their own separate full-value category assignment.

Refresh or re-run the reporting for the affected period and compare the category dashboards against the initiative total. Expected: the two category figures now sum to the initiative total instead of doubling it.

Spot-check the programme rollup for the same period. Expected: total programme savings drop by exactly the duplicated amount and no other initiative changes.

---

Source: [Vectle](https://vectle.com/skills/skl_Q2dHqZ2wkiE7tqT9AZ_Y7w). Version: `skv_kF7R5J-FlCm-WYwoYTpFDQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
