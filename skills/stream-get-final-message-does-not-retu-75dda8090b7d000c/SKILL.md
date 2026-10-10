---
name: "stream-get-final-message-does-not-retu-75dda8090b7d000c"
description: "Anthropic SDK Python: stream.get_final_message() does not return the correct usage of output_tokens. The verified fix is Contributor RobertCraigie: the current behavior is correct - the final message_delta usage already equals the total, identical to a non-streaming request's usage; the initial message_start usage can be ignored. Use this when you hit the symptoms above in anthropic-sdk-python; not for unrelated anthropic-sdk-python errors or general setup questions."
metadata:
  skill_id: "skl_UW8InT325kBCziW0hSLc3w"
  title: "stream.get_final_message() does not return the correct usage of output_tokens"
  version: "skv_D0ydLLysGDtxTc0pLpJ2Nw"
  updated: "2026-10-03T05:54:15.825134+00:00"
  canonical_url: "https://vectle.com/skills/skl_UW8InT325kBCziW0hSLc3w"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Contributor RobertCraigie: the current behavior is correct - the final message_delta usage already equals the total, identical to a non-streaming request's usage; the initial message_start usage can be ignored. Reporter confirmed understanding.

## The error

```text
Issue anthropics/anthropic-sdk-python#424 (closed, 9 comments): After streaming, stream.get_final_message() usage showed output_tokens that did not match expectations - the reporter expected to sum message_start and message_delta usage.
```

## Fix

1. Contributor RobertCraigie: the current behavior is correct - the final message_delta usage already equals the total, identical to a non-streaming request's usage; the initial message_start usage can be ignored.
2. Reporter confirmed understanding.

Success check: the symptom above is gone and the original operation completes.

## When to use

- You hit this exact symptom in anthropic-sdk-python.
- You want the verified fix without digging through the thread.

## When not to use

- A different error in anthropic-sdk-python, even a similar-looking one.
- General anthropic-sdk-python setup or credential questions.

## Compatibility

- Anthropic SDK Python (anthropics/anthropic-sdk-python)

## Variant phrasings

- How to fix "stream.get_final_message() does not return the correct usage of output_tokens" in anthropic-sdk-python
- anthropic-sdk-python: stream.get_final_message() does not return the correct usage of output_tokens

## Source

- https://github.com/anthropics/anthropic-sdk-python/issues/424

---

Source: [Vectle](https://vectle.com/skills/skl_UW8InT325kBCziW0hSLc3w). Version: `skv_D0ydLLysGDtxTc0pLpJ2Nw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
