---
name: "drata-error-vendor-criticality-not-syn-6a540f852b7f6abb"
description: "Drata error vendor criticality not synced from asset inventory"
metadata:
  skill_id: "skl_z8uOSh6qMF7_uXXrHCHc6Q"
  title: "Drata error vendor criticality not synced from asset inventory"
  version: "skv_zxKk27zTQE0S0G7eUVFAJg"
  updated: "2026-10-30T01:56:21.999757+00:00"
  canonical_url: "https://vectle.com/skills/skl_z8uOSh6qMF7_uXXrHCHc6Q"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Reproduce the failure on one named vendor and record the full problem text plus the record involved. Verify: the asset inventory shows one criticality value for the vendor, Drata shows a different or blank value, and both are noted, so the failure is reproduced on demand.

Check the source of truth before changing anything. Verify: compare the vendor name, domain and criticality in the asset inventory against the Drata vendor record and against a similar vendor whose criticality synced correctly.

Check the sync mapping and scope. Verify: the criticality field in the inventory is mapped to the criticality field in Drata, the vendor is inside the sync scope, and the last sync run for this vendor completed without a skipped or unmatched note.

Apply the specific fix described in the TL;DR on that single vendor first. Verify: the single failing vendor now shows the correct criticality in Drata, or the corrected output is visible on the record.

Check neighbouring vendors from the same inventory import that share the same name or domain pattern, because this class of failure rarely affects only one item. Verify: the neighbouring items are listed and each is marked affected or clear.

Rerun the sync on the previously failing scope, watching for the same problem rather than assuming success from a quiet log. Verify: the sync completes and the original problem does not appear on the corrected vendors.

Record the fix, the triggering input and the verification result on the run log so the next occurrence is recognised immediately. Verify: the record names the problem, the fix applied and the rerun result, and it is saved with the run.

---

Source: [Vectle](https://vectle.com/skills/skl_z8uOSh6qMF7_uXXrHCHc6Q). Version: `skv_zxKk27zTQE0S0G7eUVFAJg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
