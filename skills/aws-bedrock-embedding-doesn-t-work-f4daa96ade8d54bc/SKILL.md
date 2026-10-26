---
name: "aws-bedrock-embedding-doesn-t-work-f4daa96ade8d54bc"
description: "Shows how to fix aWS Bedrock Embedding doesn't work. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_R3KtRQnMrI0f5qgouW5H4A"
  title: "AWS Bedrock Embedding doesn't work"
  version: "skv_H6vUOZE0WTmFAar6-Jvp-A"
  updated: "2026-10-03T14:04:54.388268+00:00"
  canonical_url: "https://vectle.com/skills/skl_R3KtRQnMrI0f5qgouW5H4A"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/weaviate/weaviate/issues/3940\"]"
---

## TL;DR

--- version: '3.4' services: weaviate: command: - --host - the all-interfaces address - --port - '8080' - --scheme - http image: semitechnologies/weaviate:1.23.0 ports: - 8080:8080 - 50051:50051 volumes: -./weaviate_data/var/lib/weaviate restart: on-failure:0 environment: QUERY_DEFAULTS_LIMIT: 25 AUTHENTICATION_APIKEY_ENABLED: 'true' PERSISTENCE_DATA_PATH: '/var/lib/weaviate' DEFAULT_VECTORIZER_MODULE: 'text2vec-aws'...

## Steps

1. The fix
If Weaviate's text2vec-aws module fails against AWS Bedrock (context canceled on the invoke call), upgrade to v1.24.12 or later. The Bedrock support fix also added session-token auth: pass AWS_SESSION_TOKEN as an env var, or X-Aws-Session-Token as a request header.

## When to use

You are seeing this: AWS Bedrock Embedding doesn't work What was going on Issue weaviate/weaviate#3940 (closed, 13 comments): ### How to reproduce this bug? Use this skill when you run into "AWS Bedrock Embedding doesn't work".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

Versions mentioned in the source: semitechnologiesweaviate 1.23.0, v1.24.12. If you are on something much newer or older, the details may have shifted.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_R3KtRQnMrI0f5qgouW5H4A). Version: `skv_H6vUOZE0WTmFAar6-Jvp-A`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
