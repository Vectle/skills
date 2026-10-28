---
name: "sap-ariba-error-invoice-matched-agains-192a1881f3b3d13e"
description: "SAP Ariba error invoice matched against expired purchase order version"
metadata:
  skill_id: "skl_uamllAY5sVNaWz-gNIiGRw"
  title: "SAP Ariba error invoice matched against expired purchase order version"
  version: "skv_BCeq3fNtSbxBjjmNAolO5Q"
  updated: "2026-10-27T13:54:19.456761+00:00"
  canonical_url: "https://vectle.com/skills/skl_uamllAY5sVNaWz-gNIiGRw"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

**Open the PO and read the version history.** Expected: version 3 (or later) shows what changed, for example amounts, dates, or lines. If the change does not affect the invoiced lines, re-matching is safe.

**Open the invoice reconciliation document and find the match reference.** Expected: the header or line match points at the expired version number shown in the error.

**Confirm the current version covers the invoice.** Compare line items, quantities, and amounts on the invoice against the current PO version. Success check before proceeding: every invoice line exists on the current version at the billed amount or within tolerance.

**Re-match to the current version.** In the reconciliation, use the action to reconcile or match against the current PO version, then submit. Expected: the expired-version exception clears and the invoice moves to reconciled or paying status.

**If re-match is not offered, copy the invoice.** Cancel the stuck reconciliation, copy the invoice so it is created fresh against the current PO version, and submit the copy. Expected: the new invoice references the current version and passes matching.

---

Source: [Vectle](https://vectle.com/skills/skl_uamllAY5sVNaWz-gNIiGRw). Version: `skv_BCeq3fNtSbxBjjmNAolO5Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
