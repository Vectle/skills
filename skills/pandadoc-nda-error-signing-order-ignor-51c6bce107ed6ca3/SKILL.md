---
name: "pandadoc-nda-error-signing-order-ignor-51c6bce107ed6ca3"
description: "PandaDoc NDA error signing order ignored for three party NDA"
metadata:
  skill_id: "skl_iJu1ei3HIz2jwhx_7GXxOw"
  title: "PandaDoc NDA error signing order ignored for three party NDA"
  version: "skv_L3KIz14wJoyIUXJkZlOoXg"
  updated: "2026-10-29T01:55:32.949055+00:00"
  canonical_url: "https://vectle.com/skills/skl_iJu1ei3HIz2jwhx_7GXxOw"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Open the sent document in PandaDoc and check the recipient panel. Expected: if all recipients show delivered at the same timestamp, no signing order was applied to this copy.

Open the source template (not the sent copy) and go to the recipients or roles section. Expected: you can see the three roles listed for the NDA.

Enable the signing order option for the template and arrange the roles in the intended sequence. Expected: the roles show numbered order positions 1, 2, and 3 instead of an unordered list.

Check every recipient field block on the document and confirm each signature and initial field is assigned to the correct role. Expected: no fields are assigned to a generic or any-recipient setting, which can also break sequential routing.

Void or delete the incorrectly sent parallel copy so nobody signs the wrong version. Expected: the old document shows voided status and its signing links stop working.

Create a new document from the corrected template, add the three recipients to their roles in order, and send. Expected: only recipient 1 receives the signing email; recipients 2 and 3 show as not yet notified in the status panel.

Verify by opening the audit trail after the first signature. Expected: recipient 2 is notified only after recipient 1 completes, confirming the order is now enforced.

---

Source: [Vectle](https://vectle.com/skills/skl_iJu1ei3HIz2jwhx_7GXxOw). Version: `skv_L3KIz14wJoyIUXJkZlOoXg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
