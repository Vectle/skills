---
name: "docusign-nda-error-reminder-schedule-n-0c36f4f0b5dccefc"
description: "DocuSign NDA error reminder schedule not applied to bulk envelopes"
metadata:
  skill_id: "skl_5o8qqtqbp3OG5yVsV3q53g"
  title: "DocuSign NDA error reminder schedule not applied to bulk envelopes"
  version: "skv_wlTK3gEKb8uT3vqcfjlkQw"
  updated: "2026-10-26T21:16:39.329093+00:00"
  canonical_url: "https://vectle.com/skills/skl_5o8qqtqbp3OG5yVsV3q53g"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Compare one working single envelope with one bulk envelope. Open each envelope in DocuSign and check its reminder settings in the envelope details. Expected: the single envelope shows a reminder interval, the bulk envelope shows no reminders or reminders off.

Open the NDA template used for the bulk send and check the email and reminder settings under the template options. Expected: you can see whether reminders are enabled at template level at all.

Enable reminders on the template, set the first reminder interval and the repeat interval, and save the template. Expected: the saved template shows the reminder schedule in its settings summary.

If your bulk send flow creates envelopes from an uploaded list, re-check the send step for a separate reminders option and turn it on there as well. Expected: both the template and the bulk send step show reminders enabled.

Send a test batch of two envelopes to internal recipients and open one envelope to verify the reminder schedule is present. Expected: the test envelope details list the next reminder date.

Only then send the full bulk batch. Spot-check the first few envelopes. Expected: every checked envelope carries the same reminder schedule.

---

Source: [Vectle](https://vectle.com/skills/skl_5o8qqtqbp3OG5yVsV3q53g). Version: `skv_wlTK3gEKb8uT3vqcfjlkQw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
