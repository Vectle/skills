---
name: "az-is-not-recognized-as-an-internal-or-6fd190c8df23bcd2"
description: "az' is not recognized as an internal or external command, operable program or batch file."
metadata:
  skill_id: "skl_61zGmPgvlBUag6oMWHZytw"
  title: "az' is not recognized as an internal or external command, operable program or batch file."
  version: "skv_KaWNkWwlW4_rTBW2Y1W5kA"
  updated: "2026-11-08T13:53:55.086077+00:00"
  canonical_url: "https://vectle.com/skills/skl_61zGmPgvlBUag6oMWHZytw"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Confirm Azure CLI is actually installed by looking for the Azure CLI folder under Program Files on Windows.

Close every open terminal. Terminals keep the PATH they started with.

Open a new terminal and run az --version again.

If it still fails, open the environment variables editor, check the system PATH contains the Azure CLI wbin folder, and add it if it is missing, saving your change.

If there is no install folder at all, download and run the current Azure CLI installer for Windows, then repeat steps 2 and 3.

---

Source: [Vectle](https://vectle.com/skills/skl_61zGmPgvlBUag6oMWHZytw). Version: `skv_KaWNkWwlW4_rTBW2Y1W5kA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
