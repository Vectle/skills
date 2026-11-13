---
name: "mcp-client-failed-to-connect-accept-he-3109f02f3bb3e265"
description: "mcp client failed to connect accept header text/event-stream error"
metadata:
  skill_id: "skl_9HX7tB8ORZdETVoAc7KUZA"
  title: "mcp client failed to connect accept header text/event-stream error"
  version: "skv_etG1SK5l4sGjoY0UkREIBw"
  updated: "2026-11-13T13:54:17.119568+00:00"
  canonical_url: "https://vectle.com/skills/skl_9HX7tB8ORZdETVoAc7KUZA"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Confirm the server is a streamable HTTP server and not a stdio server, by checking the server URL and transport in the client configuration.

Send a manual initialize request to the server endpoint with an Accept header that lists both application/json and text/event-stream, in that order.

Update the client configuration or client code so every request to that server carries the combined Accept header, not only the first request.

If a proxy, gateway, or local tunnel sits between client and server, check that it passes the Accept header through unchanged and does not buffer the event stream response.

Reconnect from the MCP client and list the server tools.

Record the working header and the server transport type in the project notes.

---

Source: [Vectle](https://vectle.com/skills/skl_9HX7tB8ORZdETVoAc7KUZA). Version: `skv_etG1SK5l4sGjoY0UkREIBw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
