---
name: "az-is-not-recognized-as-an-internal-or-9cea8a1bc89e35f8"
description: "az is not recognized as an internal or external command"
metadata:
  skill_id: "skl_cJrtlTsiEkR_XWcWaPT4bg"
  title: "az is not recognized as an internal or external command"
  version: "skv_RxE7msHRGVv45O4D0wJ0Rw"
  updated: "2026-11-03T13:53:03.43003+00:00"
  canonical_url: "https://vectle.com/skills/skl_cJrtlTsiEkR_XWcWaPT4bg"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

**Check whether Azure CLI is installed at all.** Look for Azure CLI in the installed apps list, or check for its folder under Program Files. Expected: an Azure CLI install entry exists. If nothing is there, install Azure CLI from the official Microsoft installer and skip to step 4.

**Find the az executable.** In the Azure CLI install folder, open the bin subfolder and confirm az.cmd is present. Success check: the file exists, so the install is good and only PATH is broken.

**Add the bin folder to PATH.** In the Windows environment variables editor, add the Azure CLI bin folder path to the system PATH variable and save. Expected: the new entry appears in the PATH list exactly once, with no quotes around it.

**Restart the terminal completely.** Close every open Command Prompt, PowerShell, and editor terminal window, then open a fresh one. Success check: a fresh shell is required because running shells never pick up PATH changes.

**Verify in the fresh shell.** Run az --version. Expected: it prints the Azure CLI version and component versions instead of the not recognized error. Then run az login if you need to work with a subscription.

---

Source: [Vectle](https://vectle.com/skills/skl_cJrtlTsiEkR_XWcWaPT4bg). Version: `skv_RxE7msHRGVv45O4D0wJ0Rw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
