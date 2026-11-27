---
name: "xlrd-import-failed-install-xlrd-2-0-1-a7b5ecc994646a8f"
description: "xlrd import failed install xlrd >= 2.0.1 error pandas read_excel xls"
metadata:
  skill_id: "skl_OCFEeRp9TAlvccfZIoKZww"
  title: "xlrd import failed install xlrd >= 2.0.1 error pandas read_excel xls"
  version: "skv_nsY3-3b3tTcmDLPnn5OrGg"
  updated: "2026-11-27T13:52:34.506951+00:00"
  canonical_url: "https://vectle.com/skills/skl_OCFEeRp9TAlvccfZIoKZww"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Print the python and pip versions from the same interpreter that runs your script, and check whether xlrd appears in its package list.

Install xlrd version 2.0.1 or newer with the pip belonging to that interpreter.

Confirm the file really is old-format xls and not an xlsx file renamed to xls, by checking its header or opening it in a spreadsheet app.

Call read_excel with the engine argument set to xlrd for the xls file.

Restart any notebook kernel or long-running process that imported pandas before the install.

---

Source: [Vectle](https://vectle.com/skills/skl_OCFEeRp9TAlvccfZIoKZww). Version: `skv_nsY3-3b3tTcmDLPnn5OrGg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
