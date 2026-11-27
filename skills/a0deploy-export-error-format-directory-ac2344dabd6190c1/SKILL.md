---
name: "a0deploy-export-error-format-directory-ac2344dabd6190c1"
description: "a0deploy export error format directory produces no files bug"
metadata:
  skill_id: "skl_VG06Eh1p_fZhHSjl20feXA"
  title: "a0deploy export error format directory produces no files bug"
  version: "skv_Q2qv0XTxV5KDlExMHIF8Fw"
  updated: "2026-11-27T13:53:01.321034+00:00"
  canonical_url: "https://vectle.com/skills/skl_VG06Eh1p_fZhHSjl20feXA"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Run the export manually in a terminal with the same config file and environment you use in automation, and watch the full output.

Verify the config file actually points at the intended tenant domain and that the client has the read scopes the export needs.

Pass an absolute path for the output directory and create the parent folder beforehand.

Run the export again with the directory format flag spelled exactly as the tool expects and no extra format overrides in the config file.

Count the exported files and open one known resource file to confirm it contains real tenant data.

---

Source: [Vectle](https://vectle.com/skills/skl_VG06Eh1p_fZhHSjl20feXA). Version: `skv_Q2qv0XTxV5KDlExMHIF8Fw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
