---
name: "nda-expiry-error-tracker-misses-agreem-3d3c2920bbb06fc2"
description: "NDA expiry error tracker misses agreements expiring within 30 days"
metadata:
  skill_id: "skl_gE0QKLOYkdIgM0n7gw4y9Q"
  title: "NDA expiry error tracker misses agreements expiring within 30 days"
  version: "skv_ECJ0qiDZKpo9Tn9JiM367A"
  updated: "2026-10-29T13:54:18.093814+00:00"
  canonical_url: "https://vectle.com/skills/skl_gE0QKLOYkdIgM0n7gw4y9Q"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Reproduce the failure on one named run and record the full problem text plus the record involved. Verify: One agreement known to expire within 30 days is opened, its tracker entry is shown missing from the 30 day list, and its expiry date field is empty or does not match the signed document, so the miss is reproduced on demand.

Check the source of truth before changing anything. Verify: Compare the expiry date on the tracker record against the term and end date stated in the signed NDA and against any later extension or renewal document for the same counterparty.

Apply the specific fix described in the TL;DR on that single record first. Verify: the single failing run now behaves as the fix predicts, or the corrected output is visible on the record.

Check neighbouring records or steps that share the same template, library entry or integration setting, because this class of failure rarely affects only one item. Verify: the neighbouring items are listed and each is marked affected or clear.

Rerun the original task on the previously failing scope, watching for the same problem rather than assuming success from a quiet log. Verify: the task completes and the original problem does not appear.

Record the fix, the triggering input and the verification result on the run log so the next occurrence is recognised immediately. Verify: the record names the problem, the fix applied and the rerun result, and it is saved with the run.

---

Source: [Vectle](https://vectle.com/skills/skl_gE0QKLOYkdIgM0n7gw4y9Q). Version: `skv_ECJ0qiDZKpo9Tn9JiM367A`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
