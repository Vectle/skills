---
name: "how-to-fix-nda-expiry-error-tracker-mi-44fdef2918ce6c4f"
description: "how to fix NDA expiry error tracker misses agreements expiring within 30 days fails error"
metadata:
  skill_id: "skl_oaxvfFxBPHDWQDofNC_mGg"
  title: "how to fix NDA expiry error tracker misses agreements expiring within 30 days fails error"
  version: "skv_WQEMkfi_ghK2SRlzB19Qug"
  updated: "2026-10-30T01:54:46.974993+00:00"
  canonical_url: "https://vectle.com/skills/skl_oaxvfFxBPHDWQDofNC_mGg"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Reproduce the failure on one named agreement and record the full problem text plus the record involved. Verify: the agreement shows an expiry date within 30 days in the source record and does not appear in the tracker output, so the miss is reproduced on demand.

Check the source of truth before changing anything. Verify: compare the expiry date, term and status in the signed agreement and its tracker record against a similar agreement that the tracker did catch in the same window.

Check the window and filter logic. Verify: the 30 day window includes today plus 30 days inclusive, the run timezone matches the tracker timezone, and no status filter excludes agreements in renewal or pending countersignature.

Apply the specific fix described in the TL;DR on that single record first. Verify: the single failing agreement now appears in the 30 day list, or the corrected output is visible on the record.

Check neighbouring agreements expiring in the same month that share the same template, source import or status, because this class of failure rarely affects only one item. Verify: the neighbouring items are listed and each is marked affected or clear.

Rerun the tracker on the previously failing scope, watching for the same problem rather than assuming success from a quiet log. Verify: the tracker completes and all agreements expiring within 30 days appear and the original problem does not appear.

Record the fix, the triggering input and the verification result on the run log so the next occurrence is recognised immediately. Verify: the record names the problem, the fix applied and the rerun result, and it is saved with the run.

---

Source: [Vectle](https://vectle.com/skills/skl_oaxvfFxBPHDWQDofNC_mGg). Version: `skv_WQEMkfi_ghK2SRlzB19Qug`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
