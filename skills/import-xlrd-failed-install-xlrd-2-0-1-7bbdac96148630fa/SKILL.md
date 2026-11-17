---
name: "import-xlrd-failed-install-xlrd-2-0-1-7bbdac96148630fa"
description: "import xlrd` failed. install xlrd >= 2.0.1 for xls excel support"
metadata:
  skill_id: "skl_2umoyXRZpDpf5yw2EraMMg"
  title: "import xlrd` failed. install xlrd >= 2.0.1 for xls excel support"
  version: "skv_BB8vGrPmd1szO4TSd_-nMg"
  updated: "2026-11-17T01:54:01.99224+00:00"
  canonical_url: "https://vectle.com/skills/skl_2umoyXRZpDpf5yw2EraMMg"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Confirm the file is a legacy xls workbook and not an xlsx file with a renamed extension.

Print the Python executable and the pandas version in the environment that runs the failing script.

Install xlrd at the required minimum version or newer into that environment using its package manager.

In the same environment, import xlrd and print its version.

Rerun the read, naming the xlrd engine explicitly in the read_excel call.

If the import still fails in a notebook or service, restart that kernel or service so it picks up the newly installed package.

---

Source: [Vectle](https://vectle.com/skills/skl_2umoyXRZpDpf5yw2EraMMg). Version: `skv_BB8vGrPmd1szO4TSd_-nMg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
