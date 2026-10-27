---
name: "ironclad-clause-library-error-redline-215fde14c14507a0"
description: "Ironclad clause library error redline suggestion inserts wrong fallback tier"
metadata:
  skill_id: "skl_wXmnzqa9huaBKMdaNIDWGw"
  title: "Ironclad clause library error redline suggestion inserts wrong fallback tier"
  version: "skv_N9_8iIRuHnaon4YgEGBFXA"
  updated: "2026-10-26T21:16:21.939517+00:00"
  canonical_url: "https://vectle.com/skills/skl_wXmnzqa9huaBKMdaNIDWGw"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Reproduce on a copy of the draft. Accept the suggestion and note which tier text was inserted. Expected: you can name the wrong tier, for example tier 3 inserted where tier 2 was expected.

Open the clause in the clause library and inspect its metadata. Check the tier field, the clause type, and any jurisdiction or counterparty tags. Expected: one field disagrees with the playbook, most often a stale tier tag left from a copied clause.

Open the playbook position for that clause type and confirm which fallback tier should be suggested for this counterparty and deal type. Expected: the playbook tier is explicit, not inferred from clause name alone.

Fix the source, not the document. Correct the tier metadata on the library clause, or fix the playbook mapping if the metadata is right. Save and confirm the library shows the corrected tier. Expected: searching the clause now shows a single current version with the right tier.

Delete the wrong inserted text from the draft copy, re-run the redline suggestion, and compare the inserted text word for word with the library clause. Expected: the suggestion inserts the expected fallback tier.

If the wrong tier still appears, clear any locally cached clause copy in the Word add-in by closing and reopening the document, then repeat step 5. Expected: the suggestion refreshes from the library instead of the cached copy.

---

Source: [Vectle](https://vectle.com/skills/skl_wXmnzqa9huaBKMdaNIDWGw). Version: `skv_N9_8iIRuHnaon4YgEGBFXA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
