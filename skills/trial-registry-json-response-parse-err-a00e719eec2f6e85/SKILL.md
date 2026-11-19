---
name: "trial-registry-json-response-parse-err-a00e719eec2f6e85"
description: "trial registry JSON response parse error missing fields in study record"
metadata:
  skill_id: "skl_-g19JdtN_NawI2LBHlg5Nw"
  title: "trial registry JSON response parse error missing fields in study record"
  version: "skv_oiTezDUmtfcB1mr3Luz9iw"
  updated: "2026-11-19T13:52:16.080792+00:00"
  canonical_url: "https://vectle.com/skills/skl_-g19JdtN_NawI2LBHlg5Nw"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Save the raw JSON for the failing record and note its NCT number or trial ID.

List which top-level sections the parser requires and which of those are absent in the failing record.

Change required-field access to optional access with empty defaults for sections the registry does not guarantee.

Add a per-record error handler that logs the trial ID and continues to the next record.

Re-run the import on the saved failing record plus a normal record.

---

Source: [Vectle](https://vectle.com/skills/skl_-g19JdtN_NawI2LBHlg5Nw). Version: `skv_oiTezDUmtfcB1mr3Luz9iw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
