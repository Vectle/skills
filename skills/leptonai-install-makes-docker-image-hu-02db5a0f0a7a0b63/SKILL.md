---
name: "leptonai-install-makes-docker-image-hu-02db5a0f0a7a0b63"
description: "Shows how to fix leptonai install makes Docker image huge - use the slim package. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_Ms5JGIqlXR_sMfnZa519Ng"
  title: "leptonai install makes Docker image huge - use the slim package"
  version: "skv_7LgbPtw-Cws1_pB-1vYQNA"
  updated: "2026-10-03T14:00:07.788006+00:00"
  canonical_url: "https://vectle.com/skills/skl_Ms5JGIqlXR_sMfnZa519Ng"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://vectle.com/threads/thr_fnhdm_vqFl1BZ0bauy-hJw\",\"https://github.com/leptonai/leptonai/issues/346\"]"
---

## TL;DR

Yes, this was fixed in 0.18.0. Installing leptonai via poetry made my Docker image 10x bigger because of all the extra dependencies like CUDA.

## Steps

1. Installing leptonai via poetry made my Docker image 10x bigger because of all the extra dependencies like CUDA. Deployment takes forever now. Is there a lighter install option?

2. Yes, this was fixed in 0.18.0. The package was split in two: plain leptonai has no CUDA dependencies and stays small, while leptonai[runtime] has the full set. If you only need the client and deployment tooling in your image, install leptonai without the runtime extra and your image size drops back down.

## When to use

You are seeing this: Deployment takes forever now. Use this skill when you run into "leptonai install makes Docker image huge - use the slim package".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

Versions mentioned in the source: 0.18.0. If you are on something much newer or older, the details may have shifted.

## Why this happens

Installing leptonai via poetry made my Docker image 10x bigger because of all the extra dependencies like CUDA.


---

Source: [Vectle](https://vectle.com/skills/skl_Ms5JGIqlXR_sMfnZa519Ng). Version: `skv_7LgbPtw-Cws1_pB-1vYQNA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
