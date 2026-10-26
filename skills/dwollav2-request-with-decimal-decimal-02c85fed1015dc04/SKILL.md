---
name: "dwollav2-request-with-decimal-decimal-02c85fed1015dc04"
description: "Shows how to fix dwollav2 request with decimal.Decimal body fails unless simplejson is installed. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_NGIrwZSqJHEd_A23An1BcA"
  title: "dwollav2 request with decimal.Decimal body fails unless simplejson is installed"
  version: "skv_zFwhWtQctozWRorHSvQTNw"
  updated: "2026-10-03T14:16:46.179135+00:00"
  canonical_url: "https://vectle.com/skills/skl_NGIrwZSqJHEd_A23An1BcA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://vectle.com/threads/thr_ZaMMFxeG2LembHU0JYr64w\",\"https://github.com/Dwolla/dwolla-v2-python/issues/55\"]"
---

## TL;DR

The maintainer published the fix in dwollav2 v2.3.0, which serializes Decimal values without needing simplejson.

## Steps

1. Sending a `decimal.Decimal` in a dwollav2 request body failed unless the optional `simplejson` package happened to be installed , and simplejson wasn't listed as a dependency anywhere. The reporter argued a JSONEncoder subclass handles decimals fine and simplejson offers no benefit on modern Python; a PR was submitted. The maintainer published the fix in dwollav2 v2.3.0, which serializes Decimal values without needing simplejson.

2. What actually fixes it (verified in the thread):

3. Fixed in dwollav2 v2.3.0, which the maintainer confirmed was published , Decimal values in request bodies are now serialized without requiring simplejson. Upgrade to v2.3.0+. Source: https://github.com/Dwolla/dwolla-v2-python/issues/55

Expected: What actually fixes it (verified in the thread): Fixed in dwollav2 v2.3.0, which the maintainer confirmed was published , Decimal values in request bodies are now serialized without requiring simplejson.

## When to use

You are seeing this: The reporter argued a JSONEncoder subclass handles decimals fine and simplejson offers no benefit on modern Python; a PR was submitted. Use this skill when you run into "dwollav2 request with decimal.Decimal body fails unless simplejson is installed".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

Versions mentioned in the source: dwollav2 v2.3.0. If you are on something much newer or older, the details may have shifted.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.

## Sources

- https://github.com/Dwolla/dwolla-v2-python/issues/55


---

Source: [Vectle](https://vectle.com/skills/skl_NGIrwZSqJHEd_A23An1BcA). Version: `skv_zFwhWtQctozWRorHSvQTNw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
