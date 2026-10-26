---
name: "gemini-causes-event-loop-is-closed-whe-822dbab8b5691ab4"
description: "Fixes 'Event loop is closed' when running pydantic-ai's Gemini model inside an async context (e.g. Streamlit) by upgrading pydantic-ai past 0.0.46. The maintainer fixed it in 0.0.29, regressed, reverted, and re-shipped the fix in 0.0.46. Use when Gemini models fail in async but OpenAI models work. Not for event loop errors with other providers."
metadata:
  skill_id: "skl_2E1PzXRfFRYnMTiNdJ3Byg"
  title: "Gemini causes 'Event loop is closed' when running inside an async context"
  version: "skv_UM_y3wXaIa-F1vYY1Uo64g"
  updated: "2026-10-03T05:57:15.553626+00:00"
  canonical_url: "https://vectle.com/skills/skl_2E1PzXRfFRYnMTiNdJ3Byg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/pydantic/pydantic-ai/issues/748\"]"
---

Fix first: upgrade pydantic-ai past 0.0.46. The 'Event loop is closed' regression on Gemini models was fixed in 0.0.29, broke again, got reverted, and re-shipped in 0.0.46.

```text
RuntimeError: Event loop is closed
```

1. Upgrade pydantic-ai to 0.0.46 or newer.
2. Re-run your async code (e.g. the Streamlit app). Expected: the Gemini model runs without the RuntimeError.

When to use: Gemini models throw 'Event loop is closed' inside an async context while OpenAI models work fine in the same code.

When not to use: event loop errors with other providers, or Gemini failing outside async contexts.

Compatibility: pydantic-ai 0.0.46+. Reported in pydantic/pydantic-ai#748.

Variants:
- "pydantic-ai gemini event loop is closed"
- "gemini-2.0-flash-exp streamlit async"
- "pydantic ai RuntimeError event loop closed"

Root cause: a regression in the Gemini model's async handling, fixed twice.

Edge cases: if the same code works for openai:gpt-4o but not google-gla:gemini models, it is this bug, not your async code.

---

Source: [Vectle](https://vectle.com/skills/skl_2E1PzXRfFRYnMTiNdJ3Byg). Version: `skv_UM_y3wXaIa-F1vYY1Uo64g`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
