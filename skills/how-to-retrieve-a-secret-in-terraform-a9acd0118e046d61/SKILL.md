---
name: "how-to-retrieve-a-secret-in-terraform-a9acd0118e046d61"
description: "Walks through retrieve a secret in terraform from aws secret manager, step by step. Use it when you need to do exactly this. Not a troubleshooting guide, so skip it if you are here because of an error."
metadata:
  skill_id: "skl_rPEFJullD2vFjOE_MiWzHQ"
  title: "How to retrieve a secret in terraform from aws secret manager"
  version: "skv_zwLLQhBcOClTbSURwRol6A"
  updated: "2026-10-03T16:25:39.110538+00:00"
  canonical_url: "https://vectle.com/skills/skl_rPEFJullD2vFjOE_MiWzHQ"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

## TL;DR

By default, aws_secretsmanager_secret_version retrieves information based on the AWSCURRENT label (a.k.a. the latest version): `` data "aws\_secretsmanager\_secret" "secrets" { arn = "arn:aws:secretsmanager:us-east-1:123456789012:secret - my\_secrety\_name-123456" } data "aws\_secretsmanager\_secret\_version" "current" { secret\_id [your value] } ` And use data.aws\_secretsmanager\_secret\_version.current.secret\_string to get the secret.

## Steps

1. [pabloxio (top answer)] Here is an example. By default, aws_secretsmanager_secret_version retrieves information based on the AWSCURRENT label (a.k.a. the latest version):

``` data "aws_secretsmanager_secret" "secrets" { arn = "arn:aws:secretsmanager:us-east-1:123456789012:secret - my_secrety_name-123456" } data "aws_secretsmanager_secret_version" "current" { secret_id [your value] } ```

2. And use data.aws_secretsmanager_secret_version.current.secret_string to get the secret. If you want to retrieve a specific value inside that secret like DATABASE_URL you can use the built-in function jsondecode:

``` jsondecode(data.aws_secretsmanager_secret_version.current.secret_string)["DATABASE_URL"] ```

``` data "aws_secretsmanager_secret" "by-arn" { arn = "arn:aws:secretsmanager:us-east-1:123456789012:secret - example-123456" } ```

3. How do I then retrieve the value? Meaning what is the "get-value" equivalent in terraform for an EC2 isntance?

## When to use

You are seeing this: [pabloxio (top answer)] Here is an example. Use this skill when you run into "How to retrieve a secret in terraform from aws secret manager".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_rPEFJullD2vFjOE_MiWzHQ). Version: `skv_zwLLQhBcOClTbSURwRol6A`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
