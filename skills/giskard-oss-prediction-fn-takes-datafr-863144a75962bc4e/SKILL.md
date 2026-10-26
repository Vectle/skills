---
name: "giskard-oss-prediction-fn-takes-datafr-863144a75962bc4e"
description: "Shows how to fix giskard OSS: prediction fn takes DataFrame, returns one output per row. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_VaxbqFuiNTlk_jTvXjsVYw"
  title: "Giskard OSS: prediction fn takes DataFrame, returns one output per row"
  version: "skv_H-M79RoRnQefoTMZNBEf5Q"
  updated: "2026-10-03T14:08:31.22354+00:00"
  canonical_url: "https://vectle.com/skills/skl_VaxbqFuiNTlk_jTvXjsVYw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/Giskard-AI/giskard\"]"
---

## TL;DR

Install with the llm extra, e.g. pip install giskard[llm], pinned to a major version. For RAG evaluation, generate the test set from your knowledge base with generate_testset instead of hand-writing questions.

## Steps

1. To scan with Giskard OSS, wrap your model so it accepts a DataFrame and returns one output per row, and give the Model an informative description plus complete feature_names. For RAG evaluation, generate the test set from your knowledge base with generate_testset instead of hand-writing questions.

## When to use

You are seeing this: To scan with Giskard OSS, wrap your model so it accepts a DataFrame and returns one output per row, and give the Model an informative description plus complete feature_names. Use this skill when you run into "Giskard OSS: prediction fn takes DataFrame, returns one output per row".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_VaxbqFuiNTlk_jTvXjsVYw). Version: `skv_H-M79RoRnQefoTMZNBEf5Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
