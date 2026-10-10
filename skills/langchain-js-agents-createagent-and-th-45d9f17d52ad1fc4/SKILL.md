---
name: "langchain-js-agents-createagent-and-th-45d9f17d52ad1fc4"
description: "The JS v1 agent factory is createAgent imported from langchain. Every error the SDK throws carries an lc_error_code property that maps to the documented error code pages. Not for different error messages."
metadata:
  skill_id: "skl_9IOiWmCUZzPLg5ohYyPkow"
  title: "LangChain JS agents: createAgent and the lc_error_code on errors"
  version: "skv_6rGiarE9aZ6xQoukIirF1w"
  updated: "2026-10-03T14:30:57.431618+00:00"
  canonical_url: "https://vectle.com/skills/skl_9IOiWmCUZzPLg5ohYyPkow"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** The JS v1 agent factory is createAgent imported from langchain. Every error the SDK throws carries an lc_error_code property that maps to the documented error code pages.

## The error

```text
text
lc_error_code
```

## The fix

1. Import `createAgent` and `tool` from `"langchain"`. Model classes come from the scoped provider packages (`@langchain/openai`, `@langchain/anthropic`), not from `"langchain"`.

2. When an error is thrown, read its `lc_error_code` property first. It maps to one of the documented codes (GRAPH_RECURSION_LIMIT, INVALID_CHAT_HISTORY, MODEL_AUTHENTICATION, MODEL_RATE_LIMIT, OUTPUT_PARSING_FAILURE, and the rest) on the common errors page.

3. The JS docs mirror the Python error pages, so a Python-indexed diagnostic usually applies to the JS equivalent with the same code.

4. You are seeing this exact error message; match the block above, not just part of it.

5. The failing call matches the scenario in the title: LangChain JS agents.

6. You want the fastest verified fix before digging through logs.

7. Your error text differs from the block above; close cousins often have different causes.

8. The stack trace points at a different component than the one in the title.

9. You already applied this fix and the error persists; look for a second cause instead of reapplying.

10. Mentions 5.5 in the original; behavior may differ on much older or newer releases.

## When to use this

- You are seeing this exact error message; match the block above, not just part of it.
- The failing call matches the scenario in the title: LangChain JS agents.
- You want the fastest verified fix before digging through logs.

## When not to use this

- Your error text differs from the block above; close cousins often have different causes.
- The stack trace points at a different component than the one in the title.
- You already applied this fix and the error persists; look for a second cause instead of reapplying.

## Compatibility

- Mentions 5.5 in the original; behavior may differ on much older or newer releases.

## Also seen as

- `lc_error_code`

---

Source: [Vectle](https://vectle.com/skills/skl_9IOiWmCUZzPLg5ohYyPkow). Version: `skv_6rGiarE9aZ6xQoukIirF1w`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
