---
name: "openai-error-code-none-error-message-t-3487be66d4821a9e"
description: "Llama Index: openai:error_code=None error_message='Too many inputs for model None. The max number of inputs is 1.. The verified fix is Fix: Contributor iaalm: set embed_batch_size=1 - e.g. Use this when you hit the symptoms above in llama_index; not for unrelated llama_index errors or general setup questions."
metadata:
  skill_id: "skl_8-GzrTi86yurogU2djVOYw"
  title: "openai:error_code=None error_message='Too many inputs for model None. The max number of inputs is 1."
  version: "skv_KKqV_90e0VFcKr1Id11zDA"
  updated: "2026-10-03T04:44:04.732734+00:00"
  canonical_url: "https://vectle.com/skills/skl_8-GzrTi86yurogU2djVOYw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Fix: Contributor iaalm: set embed_batch_size=1 - e.g. Reporter KeyanatGiggso confirmed the workaround.

## The error

```text
Issue run-llama/llama_index#947 (closed, 23 comments): while using llama_index GPTSimpleVectorIndex I am reading a pdf file using SimpleDirectoryReader. I am unable to create index for the file and it is generating the below error: INFO:openai:error_code=None error_message='Too many inputs for model None. The max number of inputs is 1. We hope to increase the number of inputs per request soon. Please contact us through an Azure support request at: https://go.microsoft.com/fwlink/?linkid=2213926 for further questions.' error_param=None error_type=invalid_request_error message='OpenAI API error received' stream_error=False The code works for some fi
```

## Fix

1. Contributor iaalm: set embed_batch_size=1 - e.g.
2. Reporter KeyanatGiggso confirmed the workaround.

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

- How to fix "openai:error_code=None error_message='Too many inputs for model None. The max number of inputs is 1." in llama_index
- llama_index: openai:error_code=None error_message='Too many inputs for model None. The max number of inputs is 1.

## Source

- https://github.com/run-llama/llama_index/issues/947

---

Source: [Vectle](https://vectle.com/skills/skl_8-GzrTi86yurogU2djVOYw). Version: `skv_KKqV_90e0VFcKr1Id11zDA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
