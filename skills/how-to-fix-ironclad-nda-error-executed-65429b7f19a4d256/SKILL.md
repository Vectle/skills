---
name: "how-to-fix-ironclad-nda-error-executed-65429b7f19a4d256"
description: "how to fix Ironclad NDA error executed copy not routed back to requester fails error"
metadata:
  skill_id: "skl_qbMCQEtubrlMvEwnfUM4WQ"
  title: "how to fix Ironclad NDA error executed copy not routed back to requester fails error"
  version: "skv_3rqMnnw_3vksGVYFYBPgJA"
  updated: "2026-10-28T13:52:53.482452+00:00"
  canonical_url: "https://vectle.com/skills/skl_qbMCQEtubrlMvEwnfUM4WQ"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Reproduce the failure on one named run and record the full problem text plus the record involved. Verify: One completed NDA workflow is opened, its activity log shows the executed copy step ran, and no delivery to the requester is recorded, so the failure is reproduced on demand, not only seen in a log.

Check the source of truth before changing anything. Verify: Compare the recipient on the executed-copy routing step against the requester field on the intake form and against where the executed copy actually landed, such as the repository or the workflow owner inbox.

Apply the specific fix described in the TL;DR on that single record first. Verify: the single failing run now behaves as the fix predicts, or the corrected output is visible on the record.

Check neighbouring records or steps that share the same template, library entry or integration setting, because this class of failure rarely affects only one item. Verify: the neighbouring items are listed and each is marked affected or clear.

Rerun the original task on the previously failing scope, watching for the same problem rather than assuming success from a quiet log. Verify: the task completes and the original problem does not appear.

Record the fix, the triggering input and the verification result on the run log so the next occurrence is recognised immediately. Verify: the record names the problem, the fix applied and the evidence of success.

---

Source: [Vectle](https://vectle.com/skills/skl_qbMCQEtubrlMvEwnfUM4WQ). Version: `skv_3rqMnnw_3vksGVYFYBPgJA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
