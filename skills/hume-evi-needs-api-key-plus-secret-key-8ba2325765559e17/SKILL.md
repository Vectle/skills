---
name: "hume-evi-needs-api-key-plus-secret-key-8ba2325765559e17"
description: "Keep both credentials server-side and mint short-lived tokens for browser clients rather than exposing the keys. Use this skill when the task matches the title above. Not for unrelated tools or errors; check the tool's own docs for those."
metadata:
  skill_id: "skl_hJzAwuIGYVJdHxZuYC3OPA"
  title: "Hume EVI needs API key plus secret key, and tools need a config with the tool ID"
  version: "skv_4FTegqpcVC1jkNw8yy0J0Q"
  updated: "2026-10-03T05:29:53.493083+00:00"
  canonical_url: "https://vectle.com/skills/skl_hJzAwuIGYVJdHxZuYC3OPA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/humeai/hume-api-examples/blob/HEAD/evi/evi-typescript-function-calling/README.md\"]"
---

## TL;DR

Keep both credentials server-side and mint short-lived tokens for browser clients rather than exposing the keys. Running EVI needs both an API key and a secret key in the environment; the secret key is used for token authentication when the client connects. Tool use adds more steps: create the tool via the API to get a tool ID, create an EVI config that includes the tool, then put the config ID in the environment.

## Fix

Set both the API key and the secret key before connecting to EVI; the key alone will not authenticate the WebSocket. For function calling, create the tool first, then the config referencing the tool ID, then connect with that config ID. Keep both credentials server-side and mint short-lived tokens for browser clients rather than exposing the keys.

Context: Official Hume docs (EVI TypeScript function-calling example): documents the two-credential setup agents get wrong. Running EVI needs both an API key and a secret key in the environment; the secret key is used for token authentication when the client connects. Tool use adds more steps: create the tool via the API to get a tool ID, create an EVI config that includes the tool, then put the config ID in the environment. Agents that wire up only the API key, or skip the config step, fail at connect time with auth errors.

## Matched source
Source: Published skill
Original query: "Hume EVI needs API key plus secret key, and tools need a config with the tool ID"
Key terms: config, hume, need, needs, plus, secret, tool, tools

## When to use this

- Use this when your task, error, or question matches the title above and the setup in the Fix section.

## When not to use this

- Skip it when the error text, tool, or situation is different. Forcing a mismatched fix usually costs more time than searching again.

## Compatibility

The original write-up does not pin tool versions. Treat the commands and UI paths above as reflecting the author's setup, and check your tool's own docs if your version looks different.


---

Source: [Vectle](https://vectle.com/skills/skl_hJzAwuIGYVJdHxZuYC3OPA). Version: `skv_4FTegqpcVC1jkNw8yy0J0Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
