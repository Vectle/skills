---
name: "weave-type-does-not-work-with-pydantic-ea7a4262b12777ac"
description: "Shows how to fix `@weave.type()` does not work with pydantic `BaseModel`. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_v4aFHkToSfBzqd-uq1kEuA"
  title: "`@weave.type()` does not work with pydantic `BaseModel`"
  version: "skv_2z6utePsMTC_FZzm5yccxg"
  updated: "2026-10-03T14:08:36.292528+00:00"
  canonical_url: "https://vectle.com/skills/skl_v4aFHkToSfBzqd-uq1kEuA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/wandb/weave/issues/1380\"]"
---

## TL;DR

If Weave throws a 500 ('too many values to unpack') when tracing a function that takes a nested pydantic model, check whether one of the fields is called 'name'. The maintainers confirmed 'name' is reserved and used to build internal weave-trace-internal URIs.

## Steps

1. If Weave throws a 500 ('too many values to unpack') when tracing a function that takes a nested pydantic model, check whether one of the fields is called 'name'. The maintainers confirmed 'name' is reserved and used to build internal weave-trace-internal URIs. Renaming the field (for example to first_name) works around it. You also do not need @weave.type() or weave.Object on your models: just put @weave.op on the function you want to trace.

2. _Source: https://github.com/wandb/weave/issues/1380 (Weights & Biases Weave)_

## When to use

You are seeing this: If Weave throws a 500 ('too many values to unpack') when tracing a function that takes a nested pydantic model, check whether one of the fields is called 'name'. Use this skill when you run into "`@weave.type()` does not work with pydantic `BaseModel`".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.

## Sources

- https://github.com/wandb/weave/issues/1380


---

Source: [Vectle](https://vectle.com/skills/skl_v4aFHkToSfBzqd-uq1kEuA). Version: `skv_2z6utePsMTC_FZzm5yccxg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
