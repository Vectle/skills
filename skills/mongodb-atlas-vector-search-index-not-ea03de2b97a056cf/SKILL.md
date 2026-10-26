---
name: "mongodb-atlas-vector-search-index-not-ea03de2b97a056cf"
description: "MongoDB Atlas Vector Search: index not found is usually a name or status problem. Add filter-type fields for metadata paths like workspace_id to enable pre-filtering before the vector search. Use when hitting this exact issue with MongoDB Atlas Vector Search. Not for unrelated errors or different features."
metadata:
  skill_id: "skl_RoZFHUU82CxmSEdb7QuMDw"
  title: "MongoDB Atlas Vector Search: index not found is usually a name or status problem"
  version: "skv_6EcpxmwqS5G_dkalD4WqQA"
  updated: "2026-10-03T05:42:35.055347+00:00"
  canonical_url: "https://vectle.com/skills/skl_RoZFHUU82CxmSEdb7QuMDw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/cristiantumani/corteza.app/blob/HEAD/setup-vector-search.md\"]"
---

## TL;DR

Add filter-type fields for metadata paths like workspace_id to enable pre-filtering before the vector search. The index name is case-sensitive and must match exactly what the query references.

## Fix

1. Add filter-type fields for metadata paths like workspace_id to enable pre-filtering before the vector search.
   Expected: You get the expected result; the problem is gone.

## When to use

- You are setting up or using this MongoDB Atlas Vector Search feature.
- The symptom matches: index not found is usually a name or status problem.

## When NOT to use

- Unrelated MongoDB Atlas Vector Search issues (different feature, different failure).
- You need general documentation for the tool; check the official docs instead.

## Compatibility

Reported against MongoDB Atlas Vector Search. Source: https://github.com/cristiantumani/corteza.app/blob/HEAD/setup-vector-search.md.

## Variant phrasings

### index not found is usually a name or status problem

## Why it happens

Empty results or 'Cannot find index' errors almost always trace to the index name, its build status, or the dimension config.

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- If the fix does not help, capture the full error output and check the source link for updates.

## Source

https://github.com/cristiantumani/corteza.app/blob/HEAD/setup-vector-search.md

---

Source: [Vectle](https://vectle.com/skills/skl_RoZFHUU82CxmSEdb7QuMDw). Version: `skv_6EcpxmwqS5G_dkalD4WqQA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
