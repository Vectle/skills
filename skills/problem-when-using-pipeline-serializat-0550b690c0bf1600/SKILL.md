---
name: "problem-when-using-pipeline-serializat-0550b690c0bf1600"
description: "Haystack: problem when using pipeline serialization. The verified fix is Workaround until the fix: disable telemetry with export HAYSTACK_TELEMETRY_ENABLED [False]. Use this when you hit the symptoms above in haystack; not for unrelated haystack errors or general setup questions."
metadata:
  skill_id: "skl_HxwZQIYAF2LcuGBoVTIbqw"
  title: "Problem when using pipeline serialization"
  version: "skv_Es1ypADXyJ30F2f8dBo4NQ"
  updated: "2026-10-03T05:03:07.750823+00:00"
  canonical_url: "https://vectle.com/skills/skl_HxwZQIYAF2LcuGBoVTIbqw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/deepset-ai/haystack/issues/7277\"]"
---

## TL;DR

Workaround until the fix: disable telemetry with export HAYSTACK_TELEMETRY_ENABLED [False].

## The error

```text
Issue deepset-ai/haystack#7277 (closed, 12 comments): Hello, I woul like to use pipeline serialization. Below is my code for the llm ``` llm: init_parameters: huggingface_pipeline_kwargs: model: mistralai/Mixtral-8x7B-Instruct-v0.1 device_map: auto model_kwargs: bnb_4bit_compute_dtype: torch.bfloat16 bnb_4bit_quant_type: nf4 bnb_4bit_use_double_quant: true load_in_4bit: true #task: text-generation stop_words: null type: haystack.components.generators.hugging_face_local.HuggingFaceLocalGenerator ``` this code will generate the below error: ~/.local/lib/python3.9/site-packages/bitsandbytes/nn/modules.py in forward(self, x) 251 inp_dtype = x.dtype 2
```

## Fix

1. Workaround until the fix: disable telemetry with export HAYSTACK_TELEMETRY_ENABLED [False].

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

- How to fix "problem when using pipeline serialization" in haystack
- haystack: problem when using pipeline serialization

## Root cause

Same root cause as issue #7255.

## Source

- https://github.com/deepset-ai/haystack/issues/7277

---

Source: [Vectle](https://vectle.com/skills/skl_HxwZQIYAF2LcuGBoVTIbqw). Version: `skv_Es1ypADXyJ30F2f8dBo4NQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
