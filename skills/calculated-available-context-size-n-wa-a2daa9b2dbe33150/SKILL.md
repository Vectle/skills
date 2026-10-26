---
name: "calculated-available-context-size-n-wa-a2daa9b2dbe33150"
description: "Llama Index: calculated available context size -N was not non-negative. The verified fix is Fix: Collaborator logan-markewich diagnosed: the 'Calculated available context size -N' error appears when a custom LLM does not declare an accurate context_window in its LLMMetadata - set context_window to the real model size (e.g. Use this when you hit the symptoms above in llama_index; not for unrelated llama_index errors or general setup questions."
metadata:
  skill_id: "skl_OUeVmL0RwotNAorew8zAwA"
  title: "Calculated available context size -N was not non-negative"
  version: "skv_NIa9cGSjyYNgynunY4uK2g"
  updated: "2026-10-03T04:46:03.373797+00:00"
  canonical_url: "https://vectle.com/skills/skl_OUeVmL0RwotNAorew8zAwA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/run-llama/llama_index/issues/16235\"]"
---

## TL;DR

Fix: Collaborator logan-markewich diagnosed: the 'Calculated available context size -N' error appears when a custom LLM does not declare an accurate context_window in its LLMMetadata - set context_window to the real model size (e.g.

## The error

```text
Issue run-llama/llama_index#16235 (closed, 16 comments): ### Question Validation - [X] I have searched both the documentation and discord for an answer. ### Question Hi, I'm having this issue whenever I reach to the point that my chat exceeds X amount of tokens. I was assuming `as_chat_engine()` set up with `max_prompt` which preserves chat history, would automatically handle this situation. What am I missing ?
```

## Fix

1. Collaborator logan-markewich diagnosed: the 'Calculated available context size -N' error appears when a custom LLM does not declare an accurate context_window in its LLMMetadata - set context_window to the real model size (e.g.

Success check: the symptom above is gone and the original operation completes.

## When to use

- You hit this exact symptom in llama_index.
- You want the verified fix without digging through the thread.

## When not to use

- A different error in llama_index, even a similar-looking one.
- General llama_index setup or credential questions.

## Compatibility

- Llama Index (run-llama/llama_index)

## Variant phrasings

- How to fix "calculated available context size -N was not non-negative" in llama_index
- llama_index: calculated available context size -N was not non-negative

## Edge cases

- If the chat history still overflows, lower the ChatMemoryBuffer token limit, e.g. as_chat_engine(..., memory=ChatMemoryBuffer.from_defaults(token_limit=(50000)).

## Source

- https://github.com/run-llama/llama_index/issues/16235

---

Source: [Vectle](https://vectle.com/skills/skl_OUeVmL0RwotNAorew8zAwA). Version: `skv_NIa9cGSjyYNgynunY4uK2g`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
