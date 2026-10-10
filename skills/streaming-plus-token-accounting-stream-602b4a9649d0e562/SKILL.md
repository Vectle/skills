---
name: "streaming-plus-token-accounting-stream-602b4a9649d0e562"
description: "Stream an agent with the v3 event-streaming API for typed projections, and collect token usage with UsageMetadataCallbackHandler so you know what every run cost. Not the full reference manual."
metadata:
  skill_id: "skl_afj9TxgsQ7Rt7GSLWP-EBA"
  title: "Streaming plus token accounting: stream_events v3 with usage callbacks"
  version: "skv_DTrCdALiYTQpj4p8YyuBMQ"
  updated: "2026-10-03T05:55:34.277132+00:00"
  canonical_url: "https://vectle.com/skills/skl_afj9TxgsQ7Rt7GSLWP-EBA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** Stream an agent with the v3 event-streaming API for typed projections, and collect token usage with UsageMetadataCallbackHandler so you know what every run cost. Log it per run; it is your cost ledger. - OpenAI streaming needs an explicit opt-in for usage metadata in streaming chunks.

## The fix

1. `stream.messages` is the text projection; `stream.output` is the final state. Consume projections independently instead of branching on chunk types.

2. Pass the callback in the config so every model call in the run reports into it. `get_usage_metadata_callback` gives you the same as a context manager.

3. usage_metadata is keyed by model name, with input/output/total tokens plus provider details (cache reads, reasoning tokens). Log it per run; it is your cost ledger.

4. OpenAI streaming needs an explicit opt-in for usage metadata in streaming chunks. If usage is empty on OpenAI streams, that is the missing step.

## When to use this

- This covers exactly what the title says: Streaming plus token accounting.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Streaming; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current Streaming behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_afj9TxgsQ7Rt7GSLWP-EBA). Version: `skv_DTrCdALiYTQpj4p8YyuBMQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
