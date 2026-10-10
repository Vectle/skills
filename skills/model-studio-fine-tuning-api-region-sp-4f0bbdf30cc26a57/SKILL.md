---
name: "model-studio-fine-tuning-api-region-sp-4f0bbdf30cc26a57"
description: "Guide Model Studio fine-tuning API: region-specific keys and the workspace-scoped OpenAI base URL: Point the OpenAI client at the compatible-mode path, not the raw console URL. Store the key in DASHSCOPE_API_KEY, not in code. Use this when you hit exactly this in Model Studio fine-tuning API. Not for different errors or different tools."
metadata:
  skill_id: "skl_6t6ABf0QuGS9g04gPgCEsw"
  title: "Model Studio fine-tuning API: region-specific keys and the workspace-scoped OpenAI base URL"
  version: "skv_rTvTHMrKJ43gaGjZmqLxPg"
  updated: "2026-10-03T05:08:09.118228+00:00"
  canonical_url: "https://vectle.com/skills/skl_6t6ABf0QuGS9g04gPgCEsw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: Point the OpenAI client at the compatible-mode path, not the raw console URL. Store the key in DASHSCOPE_API_KEY, not in code. Build the base URL with your workspace ID as the first label under ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1; swapping regions without swapping keys is the classic silent 401.

## Fix
1. Point the OpenAI client at the compatible-mode path, not the raw console URL.
   Expected: this specific failure stops.

## Details
Store the key in DASHSCOPE_API_KEY, not in code. Build the base URL with your workspace ID as the first label under ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1; swapping regions without swapping keys is the classic silent 401.

## When to use
You hit exactly this: Model Studio fine-tuning API: region-specific keys and the workspace-scoped OpenAI base URL in Model Studio fine-tuning API.

## When not to use
A different error, or the same symptom in a different tool. This page only covers the failure above.

## Compatibility
Model Studio fine-tuning API (versions mentioned here: v1).

---

Source: [Vectle](https://vectle.com/skills/skl_6t6ABf0QuGS9g04gPgCEsw). Version: `skv_rTvTHMrKJ43gaGjZmqLxPg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
