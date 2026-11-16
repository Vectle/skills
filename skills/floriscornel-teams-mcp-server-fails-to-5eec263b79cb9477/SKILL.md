---
name: "floriscornel-teams-mcp-server-fails-to-5eec263b79cb9477"
description: "floriscornel/teams-mcp server fails to start error config missing"
metadata:
  skill_id: "skl_D-DJuHF9zRBb-86rmqeMsg"
  title: "floriscornel/teams-mcp server fails to start error config missing"
  version: "skv_J7mQptpmLfntcriR-Eu9ZA"
  updated: "2026-11-16T13:53:49.259792+00:00"
  canonical_url: "https://vectle.com/skills/skl_D-DJuHF9zRBb-86rmqeMsg"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Open the MCP client config file and find the server entry for teams-mcp.

Compare that entry with the configuration section in the floriscornel/teams-mcp project readme.

Add the missing values inside that server entry, in the environment section the client passes to the server process.

Confirm the command in the entry resolves by running the same launcher command in a terminal.

Restart the MCP client completely so it respawns the server.

Ask the client to list tools for the Teams server.

---

Source: [Vectle](https://vectle.com/skills/skl_D-DJuHF9zRBb-86rmqeMsg). Version: `skv_J7mQptpmLfntcriR-Eu9ZA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
