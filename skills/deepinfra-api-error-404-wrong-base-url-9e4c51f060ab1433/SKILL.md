---
name: "deepinfra-api-error-404-wrong-base-url-9e4c51f060ab1433"
description: "deepinfra api error 404 wrong base url endpoint fails"
metadata:
  skill_id: "skl_BetLFxz8ZH0yte1Np-wTeg"
  title: "deepinfra api error 404 wrong base url endpoint fails"
  version: "skv_cxLIquPI4VIxTBHt1_KX7w"
  updated: "2026-11-20T01:53:22.839157+00:00"
  canonical_url: "https://vectle.com/skills/skl_BetLFxz8ZH0yte1Np-wTeg"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Print the full request URL your client is sending, with the key value removed.

Set the client base URL to the DeepInfra OpenAI compatible API root exactly as documented, with no operation or model suffix.

Keep the model identifier in the model field of the request body, not in the URL.

Send one minimal chat request with a short prompt.

If a 404 remains, compare the model identifier character for character with the model page and check for a trailing slash difference in the base URL.

---

Source: [Vectle](https://vectle.com/skills/skl_BetLFxz8ZH0yte1Np-wTeg). Version: `skv_cxLIquPI4VIxTBHt1_KX7w`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
