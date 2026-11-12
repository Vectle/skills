---
name: "fivetran-sync-fails-with-error-failed-07f786bfc0e4b1e2"
description: "fivetran sync fails with error \"failed to connect to source\""
metadata:
  skill_id: "skl_jw1hBY7WPD59ZvTfpH27DA"
  title: "fivetran sync fails with error \"failed to connect to source\""
  version: "skv_T03JBcfAKy2E-etm7ZztVw"
  updated: "2026-11-12T01:55:18.622499+00:00"
  canonical_url: "https://vectle.com/skills/skl_jw1hBY7WPD59ZvTfpH27DA"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Open the connector status page and read the full sync failure detail, noting the host, port, and time of the failed attempt.

From a machine inside the same network as the source, confirm the source service is running and answering on that host and port.

Check the source firewall, security group, or database allowlist and confirm the Fivetran IP addresses for your destination region are allowed inbound on that port.

If the connection uses a tunnel or a proxy, confirm that host is running and that its own access to the source still works.

In the connector setup, run the connection test without changing any other setting.

Trigger a manual sync and watch the first extraction step.

---

Source: [Vectle](https://vectle.com/skills/skl_jw1hBY7WPD59ZvTfpH27DA). Version: `skv_T03JBcfAKy2E-etm7ZztVw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
