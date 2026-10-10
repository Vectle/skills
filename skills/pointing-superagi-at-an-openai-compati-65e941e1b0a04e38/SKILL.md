---
name: "pointing-superagi-at-an-openai-compati-65e941e1b0a04e38"
description: "Shows how to fix pointing SuperAGI at an OpenAI-compatible endpoint (OPENAI_API_BASE). Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_TWbAb32t4OUbb0UUzjcVmA"
  title: "Pointing SuperAGI at an OpenAI-compatible endpoint (OPENAI_API_BASE)"
  version: "skv_neBufmbkryxuQ__UTuCfsw"
  updated: "2026-10-03T14:19:20.351675+00:00"
  canonical_url: "https://vectle.com/skills/skl_TWbAb32t4OUbb0UUzjcVmA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

What was reported: Issue TransformerOptimus/SuperAGI#243 (closed, 25 comments): Add support for the OPENAI_API_BASE endpoint environment variable. Ideally add input for "OpenAI API Endpoint" in GUI TopBar / Settings under "Open-AI API Key".

## Steps

1. What was reported:
Issue TransformerOptimus/SuperAGI#243 (closed, 25 comments): Add support for the OPENAI_API_BASE endpoint environment variable. Ideally add input for "OpenAI API Endpoint" in GUI TopBar / Settings under "Open-AI API Key". This is important because it will allow pointing to any OpenAI API compatible drop-in: ChatGPT-to-API, llama-cpp-python, oobabooga text-generation-webui.

2. What works:
[kenfink (reporter)]: Workaround until native support lands: in llms/openai.py, under the line that sets the API key, add openai.api_base pointing at your compatible endpoint. Then in the web UI, put your endpoint URL (e.g. https://example.com no trailing slash, the backend adds it) into the OpenAI API Key field. Confirmed working for OpenAI-compatible drop-ins like llama-cpp-python.

## When to use

You are seeing this: Then in the web UI, put your endpoint URL (e.g. https://example.com no trailing slash, the backend adds it) into the OpenAI API Key field. Use this skill when you run into "Pointing SuperAGI at an OpenAI-compatible endpoint (OPENAI_API_BASE)".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.

## Sources

- https://example.com


---

Source: [Vectle](https://vectle.com/skills/skl_TWbAb32t4OUbb0UUzjcVmA). Version: `skv_neBufmbkryxuQ__UTuCfsw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
