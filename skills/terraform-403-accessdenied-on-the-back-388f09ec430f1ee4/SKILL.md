---
name: "terraform-403-accessdenied-on-the-back-388f09ec430f1ee4"
description: "Shows how to fix terraform: 403/AccessDenied on the backend is an IAM problem, not a Terraform problem. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_NTjv8pquG-BXqJHnMJYQqA"
  title: "Terraform: 403/AccessDenied on the backend is an IAM problem, not a Terraform problem"
  version: "skv_yhDAqxo7IBS-qlp4S2OTRQ"
  updated: "2026-10-03T14:13:23.566955+00:00"
  canonical_url: "https://vectle.com/skills/skl_NTjv8pquG-BXqJHnMJYQqA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

For "Error: Failed to get existing workspaces: AccessDenied: Access Denied": check the bucket policy and IAM policy for the four operations state needs: s3:GetObject, s3:PutObject, s3:DeleteObject, s3:ListBucket on the state bucket and key prefix. If locking uses DynamoDB, the identity also needs dynamodb:GetItem/PutItem/DeleteItem on the lock table. A 403 that only appears during apply (not plan) often means the lock table permissions are missing. The S3 403 that survives an IAM fix is usually KMS.

```text
Error: Failed to get existing workspaces: AccessDenied: Access Denied
  status code: 403 ...
```

## When to use

You are seeing this: `` Error: Failed to get existing workspaces: AccessDenied: Access Denied status code: 403... `` or on the S3 backend, 403s during init, plan, or state operations. Use this skill when you run into "Terraform: 403/AccessDenied on the backend is an IAM problem, not a Terraform problem".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## What you are seeing

```
Error: Failed to get existing workspaces: AccessDenied: Access Denied
  status code: 403 ...
```

or on the S3 backend, 403s during init, plan, or state operations. Terraform is telling you the credentials it has cannot read or write the state location. The config is almost certainly fine.

## First response

1. Confirm which credentials Terraform is using. For AWS: check env vars, shared config, instance profile, in that precedence order. `aws sts get-caller-identity` tells you who you actually are.
2. Check the bucket policy and IAM policy for the four operations state needs: s3:GetObject, s3:PutObject, s3:DeleteObject, s3:ListBucket on the state bucket and key prefix. Missing any one of them produces a different confusing failure.
3. If locking uses DynamoDB, the identity also needs dynamodb:GetItem/PutItem/DeleteItem on the lock table. A 403 that only appears during apply (not plan) often means the lock table permissions are missing.
4. KMS-encrypted buckets need kms:Decrypt/kms:GenerateDataKey too. The S3 403 that survives an IAM fix is usually KMS.

## Rules for agents

1. Do not "fix" a 403 by making the bucket public or widening the policy to s3:*. Scope the fix to the state prefix.
2. Never paste long-lived keys into backend config to dodge the issue. Fix the identity, not the config.
3. If it worked yesterday and 403s today, check for expired credentials, rotated keys, or a changed bucket policy before anything else.
4. Reproduce outside Terraform first: `aws s3 ls` on the bucket path. If the CLI 403s, Terraform will too, and you have eliminated Terraform from the suspect list.


---

Source: [Vectle](https://vectle.com/skills/skl_NTjv8pquG-BXqJHnMJYQqA). Version: `skv_yhDAqxo7IBS-qlp4S2OTRQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
