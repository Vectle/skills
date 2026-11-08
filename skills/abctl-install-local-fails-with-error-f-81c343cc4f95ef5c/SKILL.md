---
name: "abctl-install-local-fails-with-error-f-81c343cc4f95ef5c"
description: "abctl install local fails with error \"failed to install the airbyte helm releases\""
metadata:
  skill_id: "skl_51BsvTP0Dd19xpPdwgIKFg"
  title: "abctl install local fails with error \"failed to install the airbyte helm releases\""
  version: "skv_DwkoKXSelepylPOmupycOw"
  updated: "2026-11-08T01:52:20.33049+00:00"
  canonical_url: "https://vectle.com/skills/skl_51BsvTP0Dd19xpPdwgIKFg"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Check Docker is running and has at least 8 GB memory allocated.

List the local Kubernetes context abctl is using.

Remove the failed local install with the abctl local uninstall or delete command for your version.

Check free disk space.

Re-run the install command: abctl local install

Check pod status until the main Airbyte pods are Running.

---

Source: [Vectle](https://vectle.com/skills/skl_51BsvTP0Dd19xpPdwgIKFg). Version: `skv_DwkoKXSelepylPOmupycOw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
