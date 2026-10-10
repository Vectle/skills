---
name: "gemma-4-openairesponsechatgenerator-to-50a1fff33091a617"
description: "Haystack: gemma 4 - OpenAIResponseChatGenerator Tool Input error. The verified fix is Fix: Maintainer anakin87: don't use OpenAIResponsesChatGenerator against non-OpenAI APIs - use the targeted Ollama integration (OllamaChatGenerator) instead, and for reasoning models like Gemma set think=True. Use this when you hit the symptoms above in haystack; not for unrelated haystack errors or general setup questions."
metadata:
  skill_id: "skl_g3pGrA8ccwM5gMcTVbD7tg"
  title: "Gemma 4 - OpenAIResponseChatGenerator Tool Input error"
  version: "skv_XTKaO0h7HiRO2sJnzi3lWg"
  updated: "2026-10-03T05:12:02.758336+00:00"
  canonical_url: "https://vectle.com/skills/skl_g3pGrA8ccwM5gMcTVbD7tg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Fix: Maintainer anakin87: don't use OpenAIResponsesChatGenerator against non-OpenAI APIs - use the targeted Ollama integration (OllamaChatGenerator) instead, and for reasoning models like Gemma set think=True.

## The error

```text
Issue deepset-ai/haystack#11040 (closed, 14 comments): **Describe the bug** When running the ResponseChatGenerator in an Agent WITHOUT the exit conditions being a tool (So the tool feeds back into the generator) you get the following. haystack.core.errors.PipelineRuntimeError: The following component failed to run: Component name: 'Agent' Component type: 'Agent' Error: The following component failed to run: Component name: 'chat_generator' Component type: 'OpenAIResponsesChatGenerator' Error: Error code: 400 - {'error': {'message': 'input[3]: json: cannot unmarshal array into Go struct field ResponsesFunctionCallOutput.output of type string', 'typ
```

## Fix

1. Maintainer anakin87: don't use OpenAIResponsesChatGenerator against non-OpenAI APIs - use the targeted Ollama integration (OllamaChatGenerator) instead, and for reasoning models like Gemma set think=True.

Success check: the symptom above is gone and the original operation completes.

## When to use

- You hit this exact symptom in haystack.
- You want the verified fix without digging through the thread.

## When not to use

- A different error in haystack, even a similar-looking one.
- General haystack setup or credential questions.

## Compatibility

- Haystack (deepset-ai/haystack)

## Variant phrasings

- How to fix "gemma 4 - OpenAIResponseChatGenerator Tool Input error" in haystack
- haystack: gemma 4 - OpenAIResponseChatGenerator Tool Input error
- gemma 4 - OpenAIResponseChatGenerator Tool Input problem

## Source

- https://github.com/deepset-ai/haystack/issues/11040

---

Source: [Vectle](https://vectle.com/skills/skl_g3pGrA8ccwM5gMcTVbD7tg). Version: `skv_XTKaO0h7HiRO2sJnzi3lWg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
