---
name: "terraform-backend-initialization-requi-0b8aa02b59ef5a60"
description: "Shows how to fix terraform: \"Backend initialization required, please run terraform init\". Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_GZgL5pjILyUygnDAm8PzjA"
  title: "Terraform: \"Backend initialization required, please run terraform init\""
  version: "skv_76i8Ip1JfaeACgErvT7fag"
  updated: "2026-10-03T13:53:41.423829+00:00"
  canonical_url: "https://vectle.com/skills/skl_GZgL5pjILyUygnDAm8PzjA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://opentofu.org/docs/cli/commands/init/\"]"
---

## TL;DR

`` Error: Backend initialization required, please run "terraform init" Reason: Unset backend "s3"... ` The.terraform/ directory is missing or incomplete: no backend configured locally, providers not installed, or modules not fetched. That is the fix in the common case.

```text
Error: Backend initialization required, please run "terraform init"

Reason: Unset backend "s3"
...
```

## Steps

1. ```
Error: Backend initialization required, please run "terraform init"

Reason: Unset backend "s3"
...
```

2. The `.terraform/` directory is missing or incomplete: no backend configured locally, providers not installed, or modules not fetched. Common after a fresh clone, a CI workspace without cache, or someone deleting `.terraform`.

3. Run `terraform init`. That is the fix in the common case.
2. But first, check what init will bind: read the `backend` block and any `-backend-config` the project expects. Init against the wrong backend binds you to the wrong state, which is worse than the error.
3. In CI, check whether the project documents a specific init invocation (backend config files, env vars). Repos that need `init -backend-config=backends/prod.hcl` will fail or misbehave with bare `init`.

## When to use

You are seeing this: Common after a fresh clone, a CI workspace without cache, or someone deleting.terraform`. Use this skill when you run into "Terraform: "Backend initialization required, please run terraform init"".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_GZgL5pjILyUygnDAm8PzjA). Version: `skv_76i8Ip1JfaeACgErvT7fag`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
