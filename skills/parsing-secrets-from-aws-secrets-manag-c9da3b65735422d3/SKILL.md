---
name: "parsing-secrets-from-aws-secrets-manag-c9da3b65735422d3"
description: "Shows how to fix parsing secrets from AWS secrets manager using AWS cli. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_CQMIgf1qvde5C3kyZAhACg"
  title: "Parsing secrets from AWS secrets manager using AWS cli"
  version: "skv_QZKsBTzMS8p8eOzAPevpDQ"
  updated: "2026-10-03T16:26:17.93817+00:00"
  canonical_url: "https://vectle.com/skills/skl_CQMIgf1qvde5C3kyZAhACg"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"vectle-agent-13a5f8a682c3\"}"
  original_notices_and_references: "[\"https://stackoverflow.com/questions/50911540\"]"
---

## TL;DR

[helloV (accepted answer)] Use the --query option of the CLI to extract just the secret. `` aws secretsmanager get-secret-value --secret-id secrets --query SecretString --output text ` Context: Stack Overflow #50911540 (accepted answer, 150 votes, 16 answers): I am retrieving secrets I have stored in AWS secrets manager with the AWS cli like this: ` aws secretsmanager get-secret-value --secret-id secrets ` Which returns ` arn:aws:secretsmanager[ID]:secret - my\_secrets [number] my\_secrets {"API\_KEY":"ABCDEFGHI"} [UUID string] VERSIONSTAGES AWSCURRENT `` Does anyone know how I only get the se

## Steps

1. [helloV (accepted answer)] Use the --query option of the CLI to extract just the secret.

``` aws secretsmanager get-secret-value --secret-id secrets --query SecretString --output text ```

``` aws secretsmanager get-secret-value --secret-id secrets ```

``` arn:aws:secretsmanager[ID]:secret - my_secrets [number] my_secrets {"API_KEY":"ABCDEFGHI"} [UUID string] VERSIONSTAGES AWSCURRENT ```

2. Does anyone know how I only get the secret ("API_KEY": "ABCDEFGHI")? I need to move these secrets to my register-task-definition environment variables. The best way would be to store them in a file and delete it after us or store them in variable. It is running on a linux machine.

## When to use

You are seeing this: I need to move these secrets to my register-task-definition environment variables. Use this skill when you run into "Parsing secrets from AWS secrets manager using AWS cli".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_CQMIgf1qvde5C3kyZAhACg). Version: `skv_QZKsBTzMS8p8eOzAPevpDQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
