---
name: "openai-apitimeouterror-openai-requests-6df127e78d3f9f62"
description: "Shows how to fix (openai.APITimeoutError) OpenAI requests time out, but Gemini/Anthropic requests work fine. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_PlC0yL1YO_m5f-L0fA5eSQ"
  title: "(openai.APITimeoutError) OpenAI requests time out, but Gemini/Anthropic requests work fine"
  version: "skv_CkZ_4K2GX0xSRbBWG25P9A"
  updated: "2026-10-03T15:11:42.379266+00:00"
  canonical_url: "https://vectle.com/skills/skl_PlC0yL1YO_m5f-L0fA5eSQ"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

## TL;DR

For "APITimeoutError": the maintainer's read was that this is usually a slow or intermittent OpenAI response rather than a pydantic-ai bug, so tune the timeout to your workload instead of retrying blindly.

```text
APITimeoutError
```

## Steps

1. Raise the model timeout. The default is too short for slow OpenAI responses:

2. from pydantic_ai import Agent
from pydantic_ai.models import ModelSettings
agent = Agent(model, model_settings=ModelSettings(timeout=300))

3. Multiple users confirmed the timeouts stopped after setting a larger timeout. The maintainer's read was that this is usually a slow or intermittent OpenAI response rather than a pydantic-ai bug, so tune the timeout to your workload instead of retrying blindly.

## When to use

You are seeing this: The default is too short for slow OpenAI responses: from pydantic_ai import Agent from pydantic_ai.models import ModelSettings agent = Agent(model, model_settings=ModelSettings(timeout=300)) Multiple users confirmed the timeouts stopped after setting a... Use this skill when you run into "(openai.APITimeoutError) OpenAI requests time out, but Gemini/Anthropic requests work fine".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_PlC0yL1YO_m5f-L0fA5eSQ). Version: `skv_CkZ_4K2GX0xSRbBWG25P9A`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
