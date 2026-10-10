---
name: "langchain-js-setup-npm-packages-node-2-e0ae4f8ceaab5d16"
description: "On JavaScript you install langchain plus @langchain/core, and each model provider is its own scoped package. The runtime needs Node.js 22 or newer. Not the full reference manual."
metadata:
  skill_id: "skl_NYipio5hkMAYMIs2t6Rs6g"
  title: "LangChain JS setup: npm packages, Node 22, and the split from the old single package"
  version: "skv_xG1QYQJ3k3-Kis8mnqDdkg"
  updated: "2026-10-03T14:18:54.405624+00:00"
  canonical_url: "https://vectle.com/skills/skl_NYipio5hkMAYMIs2t6Rs6g"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** On JavaScript you install langchain plus @langchain/core, and each model provider is its own scoped package. The runtime needs Node.js 22 or newer. Log it; it tells you which doc page to read.

## The fix

1. Do not import model classes from the bare `langchain` package. They live in `@langchain/openai`, `@langchain/anthropic`, and friends.

2. Keep the key in the environment (OPENAI_API_KEY, ANTHROPIC_API_KEY). The classes read it from there by default.

3. Errors thrown by the JS SDK carry an `lc_error_code` property that maps to the documented error codes. Log it; it tells you which doc page to read.

## When to use this

- This covers exactly what the title says: LangChain JS setup.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with LangChain; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current LangChain behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_NYipio5hkMAYMIs2t6Rs6g). Version: `skv_xG1QYQJ3k3-Kis8mnqDdkg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
