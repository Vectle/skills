---
name: "how-to-fix-tipalti-matching-error-remi-466b23f559e8dd36"
description: "how to fix Tipalti matching error remittance detail missing purchase order reference fails error"
metadata:
  skill_id: "skl_ZpkDPou1H7KFabQaVWd0bA"
  title: "how to fix Tipalti matching error remittance detail missing purchase order reference fails error"
  version: "skv__5YAdq1Efm-Zab5RDEFBqQ"
  updated: "2026-10-31T01:54:26.30607+00:00"
  canonical_url: "https://vectle.com/skills/skl_ZpkDPou1H7KFabQaVWd0bA"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

**Open the payment and read its remittance detail.** In Tipalti, open the payment record and check the remittance fields the payee received. Expected: the purchase order reference field is blank or holds a different value than the purchase order number.

**Check the invoice the payment was made against.** Open the source invoice and confirm the purchase order number recorded on it. Expected: either the invoice carries the right number (the drop happened later) or it is blank (the drop happened at intake).

**Fix the reference at the drop point.** If the invoice is blank, add the purchase order number to the invoice record; if the invoice is correct, check the payment approval step for a reference override or truncation. Expected: invoice, payment, and purchase order now show the same reference.

**Match the stuck payment manually.** Use the manual match action to link this payment to the correct purchase order, recording why automatic matching failed. Expected: the purchase order balance reduces by the payment amount.

**Send corrected remittance detail to the payee.** Reissue the remittance advice so the payee can reconcile on their side. Success check: the payment shows matched, the purchase order no longer lists the amount as outstanding, and the payee confirms the reference.

---

Source: [Vectle](https://vectle.com/skills/skl_ZpkDPou1H7KFabQaVWd0bA). Version: `skv__5YAdq1Efm-Zab5RDEFBqQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
