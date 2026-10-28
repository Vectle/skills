---
name: "ironclad-nda-error-executed-copy-not-r-30b3d87a92c6d7c6"
description: "Ironclad NDA error executed copy not routed back to requester"
metadata:
  skill_id: "skl_siBvrSbXhRm4U4ecoMUvzA"
  title: "Ironclad NDA error executed copy not routed back to requester"
  version: "skv_AO5lkybnt5NRpVG9PD9Q5w"
  updated: "2026-10-27T13:54:10.17457+00:00"
  canonical_url: "https://vectle.com/skills/skl_siBvrSbXhRm4U4ecoMUvzA"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

**Open the completed workflow record and confirm the executed copy exists.** Download it from the record yourself first. Expected: a signed PDF is attached to the record, which proves execution and storage worked and only routing failed.

**Check the requester field on the workflow.** Expected: it names an active individual user. If it names a group alias, a shared mailbox entry, or a deactivated user, the completion email had no valid recipient. Note the correct requester.

**Resend from the record.** Use the workflow activity or documents menu to send the executed copy to the correct requester. Success check: the activity log shows a delivery entry and the requester confirms receipt.

**Check the workflow template completion step.** In the template, confirm the completion or archive step still includes sending the executed copy to the requester, and that it runs on the fully executed status, not on an earlier status. Expected: the step is present and addressed to the requester role, not a hard-coded person.

**Check notification settings for the requester.** If the requester turned off workflow completion emails, the copy is in their Ironclad inbox but no email arrived. Expected: they can see the completed workflow in the app even with email off.

---

Source: [Vectle](https://vectle.com/skills/skl_siBvrSbXhRm4U4ecoMUvzA). Version: `skv_AO5lkybnt5NRpVG9PD9Q5w`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
