---
name: "anyscale-gated-hf-models-need-hf-token-1ca68680ee049166"
description: "Guide Anyscale: gated HF models need HF_TOKEN via runtime_env on the deployment (ray_serve_llm_auth): Context: Ray Serve LLM troubleshooting FAQ: to use gated Hugging Face models, pass the access token through runtime_env env vars on the deployment, not baked into the image. Use this when you hit exactly this in Anyscale. Not for different errors or different tools."
metadata:
  skill_id: "skl_fP0gDPwqh5ak6fx3H6KN_A"
  title: "Anyscale: gated HF models need HF_TOKEN via runtime_env on the deployment (ray_serve_llm_auth)"
  version: "skv_lhLtVpRod94d-fi57EA5XA"
  updated: "2026-10-03T05:12:53.547224+00:00"
  canonical_url: "https://vectle.com/skills/skl_fP0gDPwqh5ak6fx3H6KN_A"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: Context: Ray Serve LLM troubleshooting FAQ: to use gated Hugging Face models, pass the access token through runtime_env env vars on the deployment, not baked into the image. [Ray Serve LLM troubleshooting FAQ]: for gated Hugging Face models, hand the token in through runtime_env env vars on the deployment, dont bake it into the image.

## Fix
1. Context: Ray Serve LLM troubleshooting FAQ: to use gated Hugging Face models, pass the access token through runtime_env env vars on the deployment, not baked into the image.
   Expected: this specific failure stops.
2. Use the get_deployment_options method on the LLMServer class to see the deployment options for each class.
   Expected: the request routes instead of erroring.

## Details
[Ray Serve LLM troubleshooting FAQ]: for gated Hugging Face models, hand the token in through runtime_env env vars on the deployment, dont bake it into the image. Build your LLMConfig with the model id and source, deployment autoscaling config, accelerator type, and runtime_env env_vars carrying HF_TOKEN. The LLMServer class get_deployment_options method shows you the options per deployment class. The pattern is runtime_env with env_vars carrying HF_TOKEN, plus the accelerator type you want, inside the LLMConfig.

## When to use
You hit exactly this: Anyscale: gated HF models need HF_TOKEN via runtime_env on the deployment (ray_serve_llm_auth) in Anyscale.

## When not to use
A different error, or the same symptom in a different tool. This page only covers the failure above.

## Compatibility
Anyscale.

---

Source: [Vectle](https://vectle.com/skills/skl_fP0gDPwqh5ak6fx3H6KN_A). Version: `skv_lhLtVpRod94d-fi57EA5XA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
