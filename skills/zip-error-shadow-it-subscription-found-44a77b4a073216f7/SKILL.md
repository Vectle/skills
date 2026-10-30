---
name: "zip-error-shadow-it-subscription-found-44a77b4a073216f7"
description: "Zip error shadow IT subscription found in card feed not in intake"
metadata:
  skill_id: "skl_MPUIxF2aGq6OmeZWBfv4xA"
  title: "Zip error shadow IT subscription found in card feed not in intake"
  version: "skv_4J-0Bi36At3B-Fn9-7MJng"
  updated: "2026-10-30T13:54:59.418137+00:00"
  canonical_url: "https://vectle.com/skills/skl_MPUIxF2aGq6OmeZWBfv4xA"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

**Verify the card transaction is real company spend.** Open the flagged item and confirm the merchant, amount, cardholder, and first charge date. Expected: the charge maps to a named employee and a real subscription, not a test or duplicate feed entry.

**Find the owner and business need.** Ask the cardholder which tool it is and who uses it. Expected: you have an owner, a user count, and a renewal date before touching intake.

**Search intake and vendor records for duplicates.** Check whether the same tool exists under a variant vendor name or a parent company name. Expected: either a matching record you can link, or a confirmed absence.

**Create the intake or renewal record and link the spend.** Open an intake request for the subscription with the owner and amount, complete the required security and legal fields, and link the card transactions to the resulting vendor record. Expected: the shadow IT flag clears once the link saves.

**Or record the offboarding decision.** If the tool is not approved, note the decision on the flagged item, cancel the subscription with the vendor, and set the card to decline that merchant if your policy allows. Success check: the item is either linked to an approved record or closed with a documented offboarding decision.

---

Source: [Vectle](https://vectle.com/skills/skl_MPUIxF2aGq6OmeZWBfv4xA). Version: `skv_4J-0Bi36At3B-Fn9-7MJng`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
