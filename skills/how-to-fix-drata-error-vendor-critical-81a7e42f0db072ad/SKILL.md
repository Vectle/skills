---
name: "how-to-fix-drata-error-vendor-critical-81a7e42f0db072ad"
description: "how to fix Drata error vendor criticality not synced from asset inventory fails error"
metadata:
  skill_id: "skl_S8LTYpqu_q6etID_0O8RYw"
  title: "how to fix Drata error vendor criticality not synced from asset inventory fails error"
  version: "skv_j1Q4Hk30IfIoM27MDbOejQ"
  updated: "2026-10-30T13:55:11.962379+00:00"
  canonical_url: "https://vectle.com/skills/skl_S8LTYpqu_q6etID_0O8RYw"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

**Compare the two values directly.** Open the vendor in Drata and the matching asset in the inventory and note both criticality values and their last-updated dates. Expected: the inventory value is newer and different; if both match, there is no sync problem to fix.

**Check the vendor-to-asset mapping.** Confirm the Drata vendor is linked to the correct inventory asset, not a similarly named asset or a parent company record. Expected: the linked asset is the one the vendor actually provides.

**Review the latest sync result.** Open the integration sync history and look for a warning or skipped record for this vendor. Expected: either a clean run that predates the inventory change, or a skipped record with a reason such as a missing owner or domain.

**Fix the source-side blocker, then re-run the sync.** Correct the missing or invalid field in the inventory, then run the integration sync again. Expected: the sync completes and lists the vendor record as updated.

**Verify in Drata.** Reload the vendor record. Success check: criticality now matches the inventory value, and the vendor list filter by that criticality includes the vendor.

---

Source: [Vectle](https://vectle.com/skills/skl_S8LTYpqu_q6etID_0O8RYw). Version: `skv_j1Q4Hk30IfIoM27MDbOejQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
