---
name: "datastax-astra-db-namespace-does-not-e-04cccf4ce50d0091"
description: "DataStax Astra DB: NAMESPACE_DOES_NOT_EXIST on default_keyspace. Token role does not fix this: an Organization Administrator token still fails when the namespace is missing. Use when hitting this exact issue with DataStax Astra DB. Not for unrelated errors or different features."
metadata:
  skill_id: "skl_JCBsHRaGVuvfa4F6YLiXHQ"
  title: "DataStax Astra DB: NAMESPACE_DOES_NOT_EXIST on default_keyspace"
  version: "skv_721wMExZiPGc8HgFBr16nA"
  updated: "2026-10-03T13:54:04.064114+00:00"
  canonical_url: "https://vectle.com/skills/skl_JCBsHRaGVuvfa4F6YLiXHQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/langflow-ai/langflow/issues/1770\"]"
---

## TL;DR

Token role does not fix this: an Organization Administrator token still fails when the namespace is missing. The Data API call is pointed at a namespace that was never created in that database.

## Fix

1. Token role does not fix this: an Organization Administrator token still fails when the namespace is missing.
   Expected: You get the expected result; the problem is gone.

## When to use

- You are setting up or using this DataStax Astra DB feature.
- The symptom matches: NAMESPACE_DOES_NOT_EXIST on default_keyspace.

## When NOT to use

- Unrelated DataStax Astra DB issues (different feature, different failure).
- You need general documentation for the tool; check the official docs instead.

## Compatibility

Reported against DataStax Astra DB. Source: https://github.com/langflow-ai/langflow/issues/1770.

## Variant phrasings

### NAMESPACE_DOES_NOT_EXIST on default_keyspace

## Why it happens

The Data API returns errors with errorCode NAMESPACE_DOES_NOT_EXIST and message Unknown namespace default_keyspace, you must create it first.

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- If the fix does not help, capture the full error output and check the source link for updates.

## Source

https://github.com/langflow-ai/langflow/issues/1770

---

Source: [Vectle](https://vectle.com/skills/skl_JCBsHRaGVuvfa4F6YLiXHQ). Version: `skv_721wMExZiPGc8HgFBr16nA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
