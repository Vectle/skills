---
name: "dropbox-get-refresh-token-13bc4dc6d05b0241"
description: "dropbox get refresh token"
metadata:
  skill_id: "skl_NsAIjpWb2MQeOmAL_DWDtA"
  title: "dropbox get refresh token"
  version: "skv_UYCeRex_9c3TUNYnAu3G-Q"
  updated: "2026-11-11T13:53:31.850495+00:00"
  canonical_url: "https://vectle.com/skills/skl_NsAIjpWb2MQeOmAL_DWDtA"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Build the authorize URL for your app and include the offline access option so Dropbox knows to issue a refresh value alongside the access value.

Exchange the authorization code at the Dropbox token endpoint as soon as it arrives, using your app key and app secret for a standard server side app, or the code verifier for a PKCE app.

Store the refresh value in your app secret store, separate from any access value you keep in memory.

When an API call returns an expired access error, post the refresh value with a refresh grant to the token endpoint and use the new access value it returns.

Test the full cycle once in a staging app by forcing an access expiry and confirming the refresh call succeeds.

---

Source: [Vectle](https://vectle.com/skills/skl_NsAIjpWb2MQeOmAL_DWDtA). Version: `skv_UYCeRex_9c3TUNYnAu3G-Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
