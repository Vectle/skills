---
name: "az-the-term-az-is-not-recognized-as-th-28e3ac7c29cd769a"
description: "az : the term 'az' is not recognized as the name of a cmdlet error powershell fails"
metadata:
  skill_id: "skl_nGhsnYNCLfseQDho9Pza4A"
  title: "az : the term 'az' is not recognized as the name of a cmdlet error powershell fails"
  version: "skv_giaJpugKYmqpY56kW4IxkA"
  updated: "2026-11-18T01:54:54.550039+00:00"
  canonical_url: "https://vectle.com/skills/skl_nGhsnYNCLfseQDho9Pza4A"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Close every PowerShell window and open a fresh one, then run the az version command again.

Check whether the Azure CLI install folder exists under Program Files and contains the az executable files.

If the folder exists, check the machine path environment variable includes that install folder, add it if missing, and open a new terminal.

If the folder is missing, reinstall Azure CLI with the current Windows installer, accepting the default location, then test in a new terminal.

If you use Windows Terminal or an editor-integrated terminal, restart that host app too, since it can cache the environment of its first launch.

---

Source: [Vectle](https://vectle.com/skills/skl_nGhsnYNCLfseQDho9Pza4A). Version: `skv_giaJpugKYmqpY56kW4IxkA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
