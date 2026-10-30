---
name: "how-to-fix-spendhq-error-preferred-sup-7b9fa5ff0dc7f967"
description: "how to fix SpendHQ error preferred supplier spend not separated from tail spend fails error"
metadata:
  skill_id: "skl__GKAFlQF2fo3Z-ClZLTo1g"
  title: "how to fix SpendHQ error preferred supplier spend not separated from tail spend fails error"
  version: "skv_4B1_5ZPobdX_BZalmEDKqA"
  updated: "2026-10-30T01:56:03.198053+00:00"
  canonical_url: "https://vectle.com/skills/skl__GKAFlQF2fo3Z-ClZLTo1g"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Reproduce the failure on one named supplier and record the full problem text plus the record involved. Verify: the supplier is on the signed preferred list, its spend appears in the tail spend view in SpendHQ, and the amount is noted, so the failure is reproduced on demand.

Check the source of truth before changing anything. Verify: compare the preferred flag, supplier name variant and category mapping in SpendHQ against the preferred list and against a similar preferred supplier whose spend is separated correctly.

Check the classification order and threshold. Verify: the preferred flag is evaluated before the tail threshold, the threshold value is noted, and no name variant splits this supplier into a second unflagged record.

Apply the specific fix described in the TL;DR on that single supplier first. Verify: the single failing supplier now classifies as preferred spend, or the corrected output is visible on the record.

Check neighbouring preferred suppliers in the same category that share the same import or name variant pattern, because this class of failure rarely affects only one item. Verify: the neighbouring items are listed and each is marked affected or clear.

Rerun the report on the previously failing scope, watching for the same problem rather than assuming success from a quiet log. Verify: the report completes, preferred spend is separated, total spend is unchanged, and the original problem does not appear.

Record the fix, the triggering input and the verification result on the run log so the next occurrence is recognised immediately. Verify: the record names the problem, the fix applied and the rerun result, and it is saved with the run.

---

Source: [Vectle](https://vectle.com/skills/skl__GKAFlQF2fo3Z-ClZLTo1g). Version: `skv_4B1_5ZPobdX_BZalmEDKqA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
