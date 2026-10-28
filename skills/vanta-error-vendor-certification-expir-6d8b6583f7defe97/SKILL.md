---
name: "vanta-error-vendor-certification-expir-6d8b6583f7defe97"
description: "Vanta error vendor certification expiry date parsed from wrong document"
metadata:
  skill_id: "skl_1zHUKiyvFfav0qRvIMrqJg"
  title: "Vanta error vendor certification expiry date parsed from wrong document"
  version: "skv_e48O2qaZWCSAzsDiUgEHUw"
  updated: "2026-10-27T13:54:31.457645+00:00"
  canonical_url: "https://vectle.com/skills/skl_1zHUKiyvFfav0qRvIMrqJg"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

**Get the real expiry from the certificate.** Open the actual ISO or SOC certificate document and note the expiry date printed on it. Expected: this date differs from the one Vanta shows, which confirms a parsing problem rather than a real lapse.

**Find which document Vanta used.** In the vendor record, open the evidence list and compare the dates inside each document: report period end, issued-on date, and test date. Expected: one non-certificate document contains the exact date Vanta stored.

**Fix the evidence set.** Remove the misleading document from this certification slot (upload it under its own evidence type instead, if it belongs on the vendor), or replace the slot contents so the certificate is the document of record for this certification. Expected: only the certificate remains attached to the certification entry.

**Re-run or wait for reprocessing, then verify.** Expected: the stored expiry updates to the certificate date and the vendor status clears. If reprocessing keeps the wrong date, use step 5.

**Set the expiry manually.** Where the vendor record allows editing the certification expiry, enter the certificate date directly and note the source document in the record. Success check: the vendor shows compliant with the certificate-matching expiry date.

---

Source: [Vectle](https://vectle.com/skills/skl_1zHUKiyvFfav0qRvIMrqJg). Version: `skv_e48O2qaZWCSAzsDiUgEHUw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
