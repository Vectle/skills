---
name: "linear-api-dont-poll-use-webhooks-and-94cabc0f1c68e13f"
description: "Keep queries shallow with explicit first: page sizes and server-side filters; a deeply nested query can burn your complexity budget fast. Use this skill when the task matches the title above. Not for unrelated tools or errors; check the tool's own docs for those."
metadata:
  skill_id: "skl_oRy7PfcG4C26DiosQhJ4eQ"
  title: "Linear API: dont poll, use webhooks, and watch query complexity"
  version: "skv_vKVMpPJsdNZyANMBuyK8WQ"
  updated: "2026-10-03T04:43:24.380326+00:00"
  canonical_url: "https://vectle.com/skills/skl_oRy7PfcG4C26DiosQhJ4eQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Keep queries shallow with explicit first: page sizes and server-side filters; a deeply nested query can burn your complexity budget fast. On rate-limit errors, back off until the window resets rather than retrying immediately. Linear specifically discourages polling for updates; use webhooks instead.

## Fix

When you sync Linear data, subscribe to webhooks instead of polling the API on a schedule. Keep queries shallow with explicit first: page sizes and server-side filters; a deeply nested query can burn your complexity budget fast. On rate-limit errors, back off until the window resets rather than retrying immediately.

Context: Linear's rate-limiting docs (quoted in pi-linear-tools): the API uses a leaky bucket limiter. Linear specifically discourages polling for updates; use webhooks instead. Default pagination returns 50 records, and nested queries multiply complexity, so filter server-side and set explicit page sizes.

## Matched source
Source: Published skill
Original query: "Linear API: dont poll, use webhooks, and watch query complexity"
Key terms: complexity, dont, linear, poll, query, watch, webhooks

## When to use this

- Use this when your task, error, or question matches the title above and the setup in the Fix section.

## When not to use this

- Skip it when the error text, tool, or situation is different. Forcing a mismatched fix usually costs more time than searching again.

## Compatibility

The original write-up does not pin tool versions. Treat the commands and UI paths above as reflecting the author's setup, and check your tool's own docs if your version looks different.


---

Source: [Vectle](https://vectle.com/skills/skl_oRy7PfcG4C26DiosQhJ4eQ). Version: `skv_vKVMpPJsdNZyANMBuyK8WQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
