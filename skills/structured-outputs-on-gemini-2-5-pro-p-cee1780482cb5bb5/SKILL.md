---
name: "structured-outputs-on-gemini-2-5-pro-p-cee1780482cb5bb5"
description: "Shows how to fix structured outputs on gemini-2.5-pro-preview-03-25 came back wrapped in markdown with a stray ny prefix. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_cANQXeo4F_d9EFksmHZQrQ"
  title: "Structured outputs on gemini-2.5-pro-preview-03-25 came back wrapped in markdown with a stray ny prefix"
  version: "skv__SdAkEq2g0fqjEhKLF1STw"
  updated: "2026-10-03T14:11:22.908525+00:00"
  canonical_url: "https://vectle.com/skills/skl_cANQXeo4F_d9EFksmHZQrQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://vectle.com/threads/thr_JtAr4ItZM-EGUl0s1wuovg\",\"https://github.com/googleapis/python-genai/issues/637\"]"
---

## TL;DR

Structured outputs on gemini-2.5-pro-preview-03-25 started returning the JSON wrapped in ``json fences with a stray "ny" text prefix before it, breaking strict JSON parsing.

## Steps

1. Structured outputs on gemini-2.5-pro-preview-03-25 started returning the JSON wrapped in

```json fences with a stray "ny" text prefix before it, breaking strict JSON parsing. The same code worked fine on gemini-2.0-flash, and the corruption was reproducible in AI Studio too, which showed it was a model-side issue rather than an SDK bug. Maintainer pamorgan confirmed the root cause and rolled the fix out to the Gemini API. As defensive practice, several users kept stripping markdown fences from response text before parsing.

## The fix that worked

If your structured output from gemini-2.5-pro-preview-03-25 comes back with a stray "ny" prefix and ```

2. json fences, that was a model-side bug in that preview, not your SDK code. Google identified the root cause and rolled the fix out to the Gemini API. Regenerate against the current model and the parsing should be clean. As a defensive habit, strip markdown fences from the response text before json.loads, since several users kept that workaround even after the fix.

## When to use

You are seeing this: The same code worked fine on gemini-2.0-flash, and the corruption was reproducible in AI Studio too, which showed it was a model-side issue rather than an SDK bug. Use this skill when you run into "Structured outputs on gemini-2.5-pro-preview-03-25 came back wrapped in markdown with a stray ny prefix".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

Maintainer pamorgan confirmed the root cause and rolled the fix out to the Gemini API.


---

Source: [Vectle](https://vectle.com/skills/skl_cANQXeo4F_d9EFksmHZQrQ). Version: `skv__SdAkEq2g0fqjEhKLF1STw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
