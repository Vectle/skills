---
name: "how-to-fix-zip-error-shadow-it-subscri-75f3e5d977431739"
description: "how to fix Zip error shadow IT subscription found in card feed not in intake fails error"
metadata:
  skill_id: "skl_rUXTyotX_cMkt1xBiyYTiQ"
  title: "how to fix Zip error shadow IT subscription found in card feed not in intake fails error"
  version: "skv_sBTeYz_O0G8XGMxz6uEtPQ"
  updated: "2026-10-31T01:54:48.859334+00:00"
  canonical_url: "https://vectle.com/skills/skl_rUXTyotX_cMkt1xBiyYTiQ"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

**Open the flagged subscription and note the exact details.** Record the vendor name as it appears in the card feed, the cardholder, the amount, and the first charge date. Expected: you have the feed spelling, which often differs from the vendor legal name.

**Search intake for the vendor and the requester.** Search Zip intake by vendor name variants and by the cardholder as requester. Expected: either a matching request exists (go to step 3) or none does (go to step 4).

**Link the existing request to the card spend.** If a request exists, attach the card transactions to it and clear the flag with a note naming the request. Expected: the subscription shows as approved spend tied to the request.

**Create a retroactive intake request.** Open a new intake for the subscription with the cardholder as the submitter and the actual business owner as owner, using the first charge date as the start date. Expected: the request enters the standard review flow with the shadow IT flag referenced.

**Route the review and set renewal controls.** Have the owner confirm the tool is still needed, then set the renewal date and spend alert on the record. Success check: the flag clears, the subscription appears in the vendor list with an owner, and the next card charge matches automatically.

---

Source: [Vectle](https://vectle.com/skills/skl_rUXTyotX_cMkt1xBiyYTiQ). Version: `skv_sBTeYz_O0G8XGMxz6uEtPQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
