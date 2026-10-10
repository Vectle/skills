---
name: "chatanthropic-integration-install-mode-cd30eba293dba3df"
description: "The Anthropic integration ships in langchain-anthropic. Model names are the plain Claude identifiers, and the key comes from ANTHROPIC_API_KEY in the environment. Not the full reference manual."
metadata:
  skill_id: "skl_FYzQJTsBiWG-uBvX6zd9fA"
  title: "ChatAnthropic integration: install, model names, and key handling"
  version: "skv_EmuHZJsu0fxLAOdZjX8VDA"
  updated: "2026-10-03T15:13:04.624055+00:00"
  canonical_url: "https://vectle.com/skills/skl_FYzQJTsBiWG-uBvX6zd9fA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** The Anthropic integration ships in langchain-anthropic. Model names are the plain Claude identifiers, and the key comes from ANTHROPIC_API_KEY in the environment.

## The fix

1. The key comes from ANTHROPIC_API_KEY in the environment. If auth fails, check the variable is actually set in the process environment (dotenv loading order bites people) before assuming the key is bad.

2. Claude is one of the providers that supports standard content blocks (`message.content_blocks`), so prefer that accessor when you want reasoning or tool-use content in a provider-agnostic shape.

3. For long agentic runs, bump `max_retries` (default 6) and set a checkpointer so a transient failure does not lose the conversation.

4. This covers exactly what the title says: ChatAnthropic integration.

5. You are setting this up for the first time, or auditing an existing setup.

6. You want the key gotchas in one place before you start.

7. You are doing a different workflow with ChatAnthropic; these steps are specific to the title above.

8. You need the full reference docs; this is the short path, not the manual.

9. Not pinned to a specific version; follows current ChatAnthropic behavior.

## When to use this

- This covers exactly what the title says: ChatAnthropic integration.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with ChatAnthropic; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

---

Source: [Vectle](https://vectle.com/skills/skl_FYzQJTsBiWG-uBvX6zd9fA). Version: `skv_EmuHZJsu0fxLAOdZjX8VDA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
