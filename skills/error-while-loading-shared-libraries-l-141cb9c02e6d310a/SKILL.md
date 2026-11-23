---
name: "error-while-loading-shared-libraries-l-141cb9c02e6d310a"
description: "error while loading shared libraries: libcudart.so.12: cannot open shared object file: no such file or directory"
metadata:
  skill_id: "skl_I_qEjbYvz-RI2VJXQszGZw"
  title: "error while loading shared libraries: libcudart.so.12: cannot open shared object file: no such file or directory"
  version: "skv_QrxcMnL_18XOTUhqBtjwLw"
  updated: "2026-11-23T01:54:01.461564+00:00"
  canonical_url: "https://vectle.com/skills/skl_I_qEjbYvz-RI2VJXQszGZw"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Confirm the loader really cannot find the library.

Search the disk for an existing CUDA runtime.

If nothing was found, install a CUDA 12 runtime.

Put that directory on the loader search path.

Relaunch the program.

---

Source: [Vectle](https://vectle.com/skills/skl_I_qEjbYvz-RI2VJXQszGZw). Version: `skv_QrxcMnL_18XOTUhqBtjwLw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
