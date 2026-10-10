---
name: "anthropic-streaming-tool-calls-accumul-f6383b583f49401f"
description: "Shows how to fix anthropic streaming tool calls: accumulate input_json_delta per block index, parse only at content_block_stop. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_OrLJTmv5FnWwaaLGcBompA"
  title: "Anthropic streaming tool calls: accumulate input_json_delta per block index, parse only at content_block_stop"
  version: "skv__nidtXQL8sLEKkd9_Ehg_A"
  updated: "2026-10-04T02:30:56.034998+00:00"
  canonical_url: "https://vectle.com/skills/skl_OrLJTmv5FnWwaaLGcBompA"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

## TL;DR

For tool\_use content blocks, the stream emits content\_block\_delta events whose delta type is input\_json\_delta, each carrying a partial\_json fragment. These deltas update the input field of the block.

## Steps

1. For `tool_use` content blocks, the stream emits `content_block_delta` events whose delta type is `input_json_delta`, each carrying a `partial_json` fragment. These deltas update the `input` field of the block.
2. Accumulate the fragments per content-block index into a string buffer. Do not share one buffer across blocks; parallel tool calls interleave by index.
3. Only JSON-parse the buffer when you receive `content_block_stop` for that index. The docs state the deltas correspond to updates for the input field; the complete object exists only at block stop.
4. Current models emit one complete key and value property from `input` at a time. Do not assume the whole object arrives in one delta, and do not try to extract individual arguments from partial fragments.
5. If the JSON parse fails at block stop, treat the tool call as failed: log the raw buffer, return an error `tool_result` to the model (so it can retry or explain), and do not execute with a half-parsed object.
6. The same per-index discipline applies to text: `text_delta` fragments belong to their block index. Mixing indices garbles both text and tool arguments.

2. Failure modes this prevents: JSON parsing on a partial fragment throwing mid-stream; cross-talk between parallel tool calls sharing one buffer; executing a tool with truncated arguments.

## When to use

You are seeing this: Accumulate the fragments per content-block index into a string buffer. Use this skill when you run into "Anthropic streaming tool calls: accumulate input_json_delta per block index, parse only at content_block_stop".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_OrLJTmv5FnWwaaLGcBompA). Version: `skv__nidtXQL8sLEKkd9_Ehg_A`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
