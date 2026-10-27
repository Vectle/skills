---
name: "onetrust-error-vendor-evidence-request-6ce163452c05b665"
description: "OneTrust error vendor evidence request sent to outdated contact"
metadata:
  skill_id: "skl_X3B9Zs9mapXtHGFeVZqMAg"
  title: "OneTrust error vendor evidence request sent to outdated contact"
  version: "skv_kFhkh5dEAfirxR8Z9Hwy5g"
  updated: "2026-10-26T21:17:26.165672+00:00"
  canonical_url: "https://vectle.com/skills/skl_X3B9Zs9mapXtHGFeVZqMAg"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Open the sent evidence request in OneTrust and note the exact recipient it used. Expected: you have the outdated name and address the system actually sent to.

Open the vendor record and inspect the primary contact and any assessment contact fields. Expected: the outdated contact appears in at least one of those fields, which is where the request pulled it from.

Update the vendor record with the current vendor contact, confirmed from a recent email thread or the vendor portal admin list, and save. Expected: the vendor record now shows the new primary contact.

Search for in-flight assessments for that vendor and check the contact captured on each one. Assessments often snapshot the contact at launch, so fix those records as well. Expected: no open assessment still points at the old contact.

Resend the evidence request and read the confirmation screen before sending. Expected: the recipient shown is the updated contact.

Ask the new contact to confirm receipt, and log the contact change on the vendor record. Expected: confirmation arrives and the change is visible in the record history.

---

Source: [Vectle](https://vectle.com/skills/skl_X3B9Zs9mapXtHGFeVZqMAg). Version: `skv_kFhkh5dEAfirxR8Z9Hwy5g`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
