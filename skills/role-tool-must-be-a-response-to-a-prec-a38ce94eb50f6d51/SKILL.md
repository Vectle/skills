---
name: "role-tool-must-be-a-response-to-a-prec-a38ce94eb50f6d51"
description: "Llama Index: role 'tool' must be a response to a preceding message with 'tool_calls'. The verified fix is Fix: upgrade the chat-store package (pip install -U llama-index-chat-store-redis) and core (pip install -U llama-index-core); he noted 'I'm like 86% sure this is fixed'. Use this when you hit the symptoms above in llama_index; not for unrelated llama_index errors or general setup questions."
metadata:
  skill_id: "skl_VPr9FQikUDPuk3kId0QRFw"
  title: "Role 'tool' must be a response to a preceding message with 'tool_calls'"
  version: "skv_DAWS8nQlECUO4vR8r98K1w"
  updated: "2026-10-03T04:47:06.937094+00:00"
  canonical_url: "https://vectle.com/skills/skl_VPr9FQikUDPuk3kId0QRFw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/run-llama/llama_index/issues/13715\"]"
---

## TL;DR

Fix: upgrade the chat-store package (pip install -U llama-index-chat-store-redis) and core (pip install -U llama-index-core); he noted 'I'm like 86% sure this is fixed'.

## The error

```text
Issue run-llama/llama_index#13715 (closed, 23 comments): ### Bug Description getting `openai.BadRequestError: Error code: 400 - {'error': {'message': "Invalid parameter: messages with role 'tool' must be a response to a preceeding message with 'tool_calls'` error when using [json chat store](https://docs.llamaindex.ai/en/stable/module_guides/storing/chat_stores/#simplechatstore) with persistent paths, but when i checked the stored json tool_calls is saved before role tool and the chats are also saved by chat_store. I am receiving this error in long chats but only when i am loading the chat store again for specific key, when i tested separately in wh
```

## Fix

1. Fix: upgrade the chat-store package (pip install -U llama-index-chat-store-redis) and core (pip install -U llama-index-core); he noted 'I'm like 86% sure this is fixed'.

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

- How to fix "role 'tool' must be a response to a preceding message with 'tool_calls'" in llama_index
- llama_index: role 'tool' must be a response to a preceding message with 'tool_calls'

## Root cause

Collaborator logan-markewich: this was a known bug in the chat-store memory handling - the memory buffer dropped the assistant/tool message pairs, so a 'tool' role message was sent to OpenAI without a preceding 'tool_calls' assistant message.

## Source

- https://github.com/run-llama/llama_index/issues/13715

---

Source: [Vectle](https://vectle.com/skills/skl_VPr9FQikUDPuk3kId0QRFw). Version: `skv_DAWS8nQlECUO4vR8r98K1w`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
