---
name: "spaces-api-php-only-works-with-us-east-b75fce2544fe844e"
description: "Fixes SociallyDev Spaces-API v3.5.0 throwing SpaceDoesntExistException in every region except us-east-1. Use this when a bucket that exists in sfo2 reports as missing. Not for genuinely missing buckets or for other S3 clients."
metadata:
  skill_id: "skl_GX1naAjcTl4DgHZomoMIsg"
  title: "Spaces-API PHP only works with us-east-1: SpaceDoesntExistException in other regions"
  version: "skv_IG_r9GsOPUrbC1WLwp063Q"
  updated: "2026-10-03T05:54:07.87014+00:00"
  canonical_url: "https://vectle.com/skills/skl_GX1naAjcTl4DgHZomoMIsg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://vectle.com/threads/thr_MdlmZLkYhsJl6CP8amiplQ\",\"https://github.com/SociallyDev/Spaces-API/issues/85\"]"
---

TL;DR: if SociallyDev/Spaces-API v3.5.0 throws `SpaceDoesntExistException` for buckets in any region except us-east-1 (e.g. a bucket in sfo2 reports `Space 'assets-storage' does not exist`), the constructor accepts a region argument but the Spaces class hardcoded us-east-1 when instantiating the underlying S3 client, so the endpoint URL and the client region disagreed. Until it is fixed upstream, patch the hardcoded region in the S3 client instantiation to your region (e.g. sfo2) and construct with the region argument and a space name that exists there. The reporter confirmed this fixed sfo2 access.

```text
SpaceDoesntExistException: Space 'assets-storage' does not exist
```

## Steps

1. Patch the hardcoded us-east-1 in the Spaces class's S3 client instantiation to your region.

2. Construct with the region and an existing space name in that region.

3. Retry the operation.

   Expected: the bucket resolves. Success check: reads/writes work in sfo2 (or your region).

## When to use this

- Spaces-API v3.5.0, non-us-east-1 region, bucket exists but reports missing.

## When NOT to use this

- The bucket genuinely does not exist; check the name.
- us-east-1 works and you can use it; no patch needed.

## Compatibility

- SociallyDev/Spaces-API v3.5.0; the maintainer acknowledged the bug and invited a PR.

## Variant phrasings

- "spaces-api SpaceDoesntExistException region"
- "digitalocean spaces php wrong region"

## Root cause

The region argument fed the endpoint URL but the S3 client itself was hardcoded to us-east-1, so lookups ran against the wrong region.

## Edge cases

- Keep the patch minimal so you can drop it when upstream fixes it.

---

Source: [Vectle](https://vectle.com/skills/skl_GX1naAjcTl4DgHZomoMIsg). Version: `skv_IG_r9GsOPUrbC1WLwp063Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
