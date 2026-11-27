---
name: "aikido-firewall-fails-with-error-unsup-724725a8a2bb0e20"
description: "aikido firewall fails with error unsupported framework on install"
metadata:
  skill_id: "skl_sseqMJwxarf0A7mB-o2RaA"
  title: "aikido firewall fails with error unsupported framework on install"
  version: "skv_Focb0Lx6G_1H9aHnl2207Q"
  updated: "2026-11-27T13:53:41.043215+00:00"
  canonical_url: "https://vectle.com/skills/skl_sseqMJwxarf0A7mB-o2RaA"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Identify the exact language package and version you installed and the framework and version your app actually runs.

Compare them against the supported frameworks list in the Aikido firewall documentation for that package.

Check where the firewall is initialized in your code relative to where the framework app is created.

If the framework version is out of range, upgrade or pin the framework or the firewall package to a mutually supported combination in a test environment.

Start the app and send one normal request and one obviously malicious test request, such as a simple SQL injection string in a query parameter.

---

Source: [Vectle](https://vectle.com/skills/skl_sseqMJwxarf0A7mB-o2RaA). Version: `skv_Focb0Lx6G_1H9aHnl2207Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
