---
name: "comfyui-lumaai-node-generationsresourc-c0a4826e1c249f5d"
description: "Shows how to fix comfyUI LumaAI node: GenerationsResource.create() got an unexpected keyword argument 'model'. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_1UllbG9InwLoCOr_k5ELXw"
  title: "ComfyUI LumaAI node: GenerationsResource.create() got an unexpected keyword argument 'model'"
  version: "skv_O0AlOx0KTjV114zD4QuG-A"
  updated: "2026-10-04T05:34:12.276709+00:00"
  canonical_url: "https://vectle.com/skills/skl_1UllbG9InwLoCOr_k5ELXw"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

## TL;DR

After updating the ComfyUI-LumaAI-API custom node, every image-to-video run failed with "GenerationsResource.create() got an unexpected keyword argument 'model'", regardless of which model was selected. The node was passing a model kwarg that the installed ComfyUI core did not accept.

## Steps

1. After updating the ComfyUI-LumaAI-API custom node, every image-to-video run failed with "GenerationsResource.create() got an unexpected keyword argument 'model'", regardless of which model was selected. The full traceback showed the error surfacing inside ComfyUI's execution pipeline during prompt processing. The node was passing a `model` kwarg that the installed ComfyUI core did not accept.

2. The reporter's own resolution: update ComfyUI itself. The node passes a `model` kwarg that only newer ComfyUI versions handle, so an updated custom node against an outdated ComfyUI core throws this TypeError. After updating ComfyUI, the error went away.

## When to use

You are seeing this: The full traceback showed the error surfacing inside ComfyUI's execution pipeline during prompt processing. Use this skill when you run into "ComfyUI LumaAI node: GenerationsResource.create() got an unexpected keyword argument 'model'".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_1UllbG9InwLoCOr_k5ELXw). Version: `skv_O0AlOx0KTjV114zD4QuG-A`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
