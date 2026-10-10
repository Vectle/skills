---
name: "imagetoimage-errors-on-models-that-onl-62d710977aebc30d"
description: "Shows how to fix imageToImage errors on models that only support text-to-image. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_7YebN9S-X_bfBd7cT41mEQ"
  title: "imageToImage errors on models that only support text-to-image"
  version: "skv_9LUNbyfkrysgc_U821XHyQ"
  updated: "2026-10-03T14:13:37.715982+00:00"
  canonical_url: "https://vectle.com/skills/skl_7YebN9S-X_bfBd7cT41mEQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

The fix is to match the call to what the model actually supports: either switch to hf.textToImage() with that model, or pick a model whose page lists the image-to-image pipeline as supported and point imageToImage at that one.

## Steps

1. Not a client bug. Per maintainer coyotte508, stabilityai/stable-diffusion-2-1 only exposes text-to-image through the Inference API, so any image-to-image call against it will fail no matter how you shape the inputs. The fix is to match the call to what the model actually supports: either switch to hf.textToImage() with that model, or pick a model whose page lists the image-to-image pipeline as supported and point imageToImage at that one. General rule before wiring up any inference call: check the model's supported tasks on its model page first, because the API silently supports fewer tasks per model than the client library's method list suggests.

## When to use

You are seeing this: The imageToImage example from the docs does not work. Use this skill when you run into "imageToImage errors on models that only support text-to-image".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_7YebN9S-X_bfBd7cT41mEQ). Version: `skv_9LUNbyfkrysgc_U821XHyQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
