---
name: "clause-metadata-error-jurisdiction-tag-7b1a787eb323f623"
description: "clause metadata error jurisdiction tag missing on data protection clause"
metadata:
  skill_id: "skl_a-xaOJYWNNV03xXCnforjQ"
  title: "clause metadata error jurisdiction tag missing on data protection clause"
  version: "skv_L1xOdNk5XgO7oP8IbbFItg"
  updated: "2026-10-27T13:54:01.04778+00:00"
  canonical_url: "https://vectle.com/skills/skl_a-xaOJYWNNV03xXCnforjQ"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

**Open the clause in the library editor and expand the metadata panel.** Expected: the jurisdiction field is empty or shows an unmapped free-text value, and it is marked required for the data protection clause type.

**Set the jurisdiction from the taxonomy, not free text.** Pick the value from the dropdown (for example the value your library uses for the European Union, the United Kingdom, or a specific US state). Expected: the value saves without a mapping warning. Free-typed values that are not in the taxonomy still fail validation.

**Check the variants.** If the clause has jurisdiction-specific variants (for example a GDPR variant and a CCPA variant), each variant needs its own jurisdiction tag; the parent clause tag does not cascade. Expected: every variant shows a jurisdiction value in its metadata.

**Check inherited metadata conflicts.** If the clause was cloned from another clause, clear any inherited region or regime tags that contradict the jurisdiction you just set. Expected: validation no longer reports conflicting metadata.

**Save and re-run validation, then publish.** Success check: the metadata error clears, the clause status moves to published, and the clause appears in search filtered by that jurisdiction.

---

Source: [Vectle](https://vectle.com/skills/skl_a-xaOJYWNNV03xXCnforjQ). Version: `skv_L1xOdNk5XgO7oP8IbbFItg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
