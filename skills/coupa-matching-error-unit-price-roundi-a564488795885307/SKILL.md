---
name: "coupa-matching-error-unit-price-roundi-a564488795885307"
description: "Coupa matching error unit price rounding creates false price variance"
metadata:
  skill_id: "skl_rBLArTBfgd1J90zDay-URQ"
  title: "Coupa matching error unit price rounding creates false price variance"
  version: "skv_bNnTGQaMYQvbTaBA57BJAg"
  updated: "2026-10-26T21:16:54.497319+00:00"
  canonical_url: "https://vectle.com/skills/skl_rBLArTBfgd1J90zDay-URQ"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Open the invoice line and the purchase order line side by side. Write down unit price, quantity, and line total for both. Expected: quantities match and the price difference is a fraction of a cent per unit or a few cents on the line.

Multiply the invoice unit price by the quantity yourself and compare it with the invoice line total. Expected: a mismatch here confirms rounding, because the supplier rounded the unit price for display and extended from the unrounded value.

Check the purchase order price precision in Coupa for that item or contract. Expected: you can see whether the order allows two, three, or four decimal places on unit price.

Decide the fix with accounts payable: either accept the invoice within the existing price tolerance, or raise the tolerance slightly for rounding-only variances, or ask the supplier to invoice at the order precision. Expected: one named approach, not an ad hoc force-match.

Apply the chosen fix and re-run matching on the invoice. Expected: the line matches, or the remaining variance is a real price difference that needs buyer review.

Record the rounding pattern on the supplier or contract record so the next order for the same item uses matching precision. Expected: the next purchase order for that item carries the agreed decimal precision.

---

Source: [Vectle](https://vectle.com/skills/skl_rBLArTBfgd1J90zDay-URQ). Version: `skv_bNnTGQaMYQvbTaBA57BJAg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
