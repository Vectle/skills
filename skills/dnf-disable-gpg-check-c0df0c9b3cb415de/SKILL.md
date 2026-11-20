---
name: "dnf-disable-gpg-check-c0df0c9b3cb415de"
description: "dnf disable gpg check"
metadata:
  skill_id: "skl_DezXxeAz5MI28-tkIsvc7g"
  title: "dnf disable gpg check"
  version: "skv_cK_bqrGIiDYO4ckBmZ4iDg"
  updated: "2026-11-20T13:52:46.713385+00:00"
  canonical_url: "https://vectle.com/skills/skl_DezXxeAz5MI28-tkIsvc7g"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Confirm why the signature check is failing and that you trust the package source, for example a package you built locally or an internal mirror you control.

For a single install, run the install command with the nogpgcheck flag added.

For a single repository that is unsigned by design, edit only that repository definition and set its gpgcheck option to 0.

Verify the setting scope by reviewing which repo files changed and confirming the main dnf configuration was not edited.

After a temporary bypass, remove the repo level change once the repository publishes signed packages.

---

Source: [Vectle](https://vectle.com/skills/skl_DezXxeAz5MI28-tkIsvc7g). Version: `skv_cK_bqrGIiDYO4ckBmZ4iDg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
