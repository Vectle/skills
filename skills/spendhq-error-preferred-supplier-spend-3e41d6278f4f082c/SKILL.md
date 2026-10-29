---
name: "spendhq-error-preferred-supplier-spend-3e41d6278f4f082c"
description: "SpendHQ error preferred supplier spend not separated from tail spend"
metadata:
  skill_id: "skl_BkRYKdPwdu8D7OAv-rdfnA"
  title: "SpendHQ error preferred supplier spend not separated from tail spend"
  version: "skv_8KJCdlq6tiYv2Vd104n3EA"
  updated: "2026-10-29T13:54:48.342826+00:00"
  canonical_url: "https://vectle.com/skills/skl_BkRYKdPwdu8D7OAv-rdfnA"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Reproduce the failure on one named run and record the full problem text plus the record involved. Verify: The SpendHQ report is opened, a supplier known to be preferred is shown inside tail spend, and the preferred flag or list entry for that supplier is shown missing or mismatched, so the error is reproduced on demand.

Check the source of truth before changing anything. Verify: Compare the suppliers classed as preferred in the report against the current preferred supplier register and check the normalised supplier names on both sides for mismatches.

Apply the specific fix described in the TL;DR on that single record first. Verify: the single failing run now behaves as the fix predicts, or the corrected output is visible on the record.

Check neighbouring records or steps that share the same template, library entry or integration setting, because this class of failure rarely affects only one item. Verify: the neighbouring items are listed and each is marked affected or clear.

Rerun the original task on the previously failing scope, watching for the same problem rather than assuming success from a quiet log. Verify: the task completes and the original problem does not appear.

Record the fix, the triggering input and the verification result on the run log so the next occurrence is recognised immediately. Verify: the record names the problem, the fix applied and the rerun result, and it is saved with the run.

---

Source: [Vectle](https://vectle.com/skills/skl_BkRYKdPwdu8D7OAv-rdfnA). Version: `skv_8KJCdlq6tiYv2Vd104n3EA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
