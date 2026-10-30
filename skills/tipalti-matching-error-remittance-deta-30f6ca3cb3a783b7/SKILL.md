---
name: "tipalti-matching-error-remittance-deta-30f6ca3cb3a783b7"
description: "Tipalti matching error remittance detail missing purchase order reference"
metadata:
  skill_id: "skl_TYLZBf4gGXMd0XV-kFLoFA"
  title: "Tipalti matching error remittance detail missing purchase order reference"
  version: "skv_wE2mk7BhjVTsJvP14lemcQ"
  updated: "2026-10-30T13:54:38.490791+00:00"
  canonical_url: "https://vectle.com/skills/skl_TYLZBf4gGXMd0XV-kFLoFA"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

**Find the approved purchase order first.** Search purchase orders for the vendor and amount and note the exact PO number, including any prefix. Expected: one open PO matches the vendor, amount, and date range.

**Open the unmatched invoice or remittance record.** Check the PO reference field; it is blank, or it holds an internal request number instead of the PO number. Expected: the mismatch is visible in the reference field, not in the amounts.

**Enter the exact PO number.** Copy the number from the purchase order record rather than typing it from the supplier paperwork, which often truncates prefixes. Expected: the field validates and the vendor on the PO matches the vendor on the invoice.

**Re-run matching.** Trigger matching again and watch the status. Expected: the invoice moves from unmatched to matched, and any remaining hold names a different reason such as quantity or tax.

**Document supplier-submitted cases.** If the supplier sent remittance detail with no PO because none was issued, attach the approval or exception note to the record instead of adding a false reference. Success check: the record is matched or exception-approved, with the PO number or the exception visible in the audit history.

---

Source: [Vectle](https://vectle.com/skills/skl_TYLZBf4gGXMd0XV-kFLoFA). Version: `skv_wE2mk7BhjVTsJvP14lemcQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
