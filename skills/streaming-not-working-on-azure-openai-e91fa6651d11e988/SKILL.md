---
name: "streaming-not-working-on-azure-openai-e91fa6651d11e988"
description: "Haystack: streaming not working on Azure OpenAI. The verified fix is Fix: Reporter jambudipa, after investigation with the maintainers: 'No changes to Haystack required, I was passing the stream handler in the wrong place.' The fix is to pass model_kwargs={'stream': True, 'stream_handler': custom_handler} on the PromptNode while constructing the PromptModel with the handler too - i.e. create the streaming PromptModel via create_streaming_*_prompt_model(custom_handler) rather than attaching the h"
metadata:
  skill_id: "skl_OtGWjt-Ljw8Ozvm8FLHNkA"
  title: "Streaming not working on Azure OpenAI"
  version: "skv_B8yoGXt7vSeHrzp-BFtIZA"
  updated: "2026-10-03T05:07:53.510445+00:00"
  canonical_url: "https://vectle.com/skills/skl_OtGWjt-Ljw8Ozvm8FLHNkA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/deepset-ai/haystack/issues/5896\"]"
---

## TL;DR

Fix: Reporter jambudipa, after investigation with the maintainers: 'No changes to Haystack required, I was passing the stream handler in the wrong place.' The fix is to pass model_kwargs={'stream': True, 'stream_handler': custom_handler} on the PromptNode while constructing the PromptModel with the handler too - i.e. create the streaming PromptModel via create_streaming_*_prompt_model(custom_handler) rather than attaching the handler only at the PromptNode level.

## The error

```text
Issue deepset-ai/haystack#5896 (closed, 12 comments): **Describe the bug** The `model_kwargs={"stream": True, "stream_handler": custom_handler}` on `PromptNode` has no effect when using a `PromptModel` based on an Azure OpenAI model. **Expected behavior** The answer output should stream as it does when using other prompt models. **Additional context** The following code works fine: ``` prompt_node = PromptNode( "gpt-3.5-turbo-16k", default_prompt_template=lfqa_prompt, api_key [your value], max_length= 3072, model_kwargs={"stream": True} ) ``` This streams as expected. **To Reproduce** Changing the prompt model like this: ``` # new prompt_azure_
```

## Fix

1. Reporter jambudipa, after investigation with the maintainers: 'No changes to Haystack required, I was passing the stream handler in the wrong place.' The fix is to pass model_kwargs={'stream': True, 'stream_handler': custom_handler} on the PromptNode while constructing the PromptModel with the handler too - i.e. create the streaming PromptModel via create_streaming_*_prompt_model(custom_handler) rather than attaching the handler only at the PromptNode level.

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

- How to fix "streaming not working on Azure OpenAI" in haystack
- haystack: streaming not working on Azure OpenAI

## Source

- https://github.com/deepset-ai/haystack/issues/5896

---

Source: [Vectle](https://vectle.com/skills/skl_OtGWjt-Ljw8Ozvm8FLHNkA). Version: `skv_B8yoGXt7vSeHrzp-BFtIZA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
