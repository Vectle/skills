---
name: "client-must-accept-both-application-js-faa58d2622b8b080"
description: "client must accept both application/json and text/event-stream error mcp"
metadata:
  skill_id: "skl_D7WTPRcRovROsabr1P-7jQ"
  title: "client must accept both application/json and text/event-stream error mcp"
  version: "skv_wXnC7vYzexOs6tcTiCgvSg"
  updated: "2026-11-06T13:54:30.44806+00:00"
  canonical_url: "https://vectle.com/skills/skl_D7WTPRcRovROsabr1P-7jQ"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

**Confirm the transport.** Check the server config is an http or streamable http URL, not a stdio command. Expected: this fix only applies to the HTTP transport.

**Inspect the header the client sends.** If the client allows custom headers, look at its configured Accept value. Success check: it lists only one media type, or no Accept value is set at all.

**Set the combined Accept header.** Configure the header value as application/json, text/event-stream with both types present and comma separated. Expected: the saved client config shows both types in one header.

**Reconnect and initialize.** Restart the client connection so the new header is used from the first initialize request. Success check: the server returns a session response instead of the not acceptable error.

**Verify a tools call.** List tools or call a harmless read only tool. Expected: a normal result returns over the same connection, proving the header fix holds beyond initialization.

**Check for a proxy stripping headers.** If the error persists with the header set, test the same server URL without any local proxy or gateway in between. Success check: a direct connection initializes, pointing at the intermediary as the place the header is lost.

---

Source: [Vectle](https://vectle.com/skills/skl_D7WTPRcRovROsabr1P-7jQ). Version: `skv_wXnC7vYzexOs6tcTiCgvSg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
