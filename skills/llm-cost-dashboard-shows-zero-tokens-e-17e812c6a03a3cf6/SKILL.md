---
name: "llm-cost-dashboard-shows-zero-tokens-e-17e812c6a03a3cf6"
description: "LLM cost dashboard shows zero tokens error tracking fails"
metadata:
  skill_id: "skl_IE0mzNXpjuaoXIsw007x2w"
  title: "LLM cost dashboard shows zero tokens error tracking fails"
  version: "skv_O5cFaFCRF5N-bM8Pzr_fZw"
  updated: "2026-11-27T13:53:13.487554+00:00"
  canonical_url: "https://vectle.com/skills/skl_IE0mzNXpjuaoXIsw007x2w"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Pick one recent successful request and find its row in the usage or tracking store.

Log the raw provider response for a single non-streaming test request and read its usage fields.

If you stream responses, check whether your provider only returns usage in a final chunk when the stream usage option is enabled, and enable it.

Check the model name recorded by the tracker against the pricing table keys, character for character.

Remove or log any silent error handling around the tracking call, then send another test request.

---

Source: [Vectle](https://vectle.com/skills/skl_IE0mzNXpjuaoXIsw007x2w). Version: `skv_O5cFaFCRF5N-bM8Pzr_fZw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
