---
name: "list-objects-fails-with-sio-error-auth-5aa5b556ee7fddec"
description: "Shows how to fix list objects fails with sio.Error 'authentication failed'. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_AABHLAsiiWrQ6W4Kdm6Aew"
  title: "List objects fails with sio.Error 'authentication failed'"
  version: "skv_ozbyAiJcXI98Nj28aVfMBQ"
  updated: "2026-10-03T14:06:11.723082+00:00"
  canonical_url: "https://vectle.com/skills/skl_AABHLAsiiWrQ6W4Kdm6Aew"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/minio/minio/issues/17377\"]"
---

## TL;DR

I should be able to list objects -- recursively or not -- for a specific prefix. At least one object from a prefix consistently prevents me from listing objects.

## Steps

1. I should be able to list objects -- recursively or not -- for a specific prefix. At least one object from a prefix consistently prevents me from listing objects. The list objects request fails with the following error message: MinIO is running as a systemd service.

2. If listing a specific prefix fails with 'sio: authentication failed' while other prefixes work, those objects were encrypted with the wrong data key due to a KES bug and cannot be decrypted. The maintainer's guidance: purge the affected objects with mc rm --purge --force on the path. New writes with a fixed KES are not affected.

## When to use

You are seeing this: The list objects request fails with the following error message: MinIO is running as a systemd service. Use this skill when you run into "List objects fails with sio.Error 'authentication failed'".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_AABHLAsiiWrQ6W4Kdm6Aew). Version: `skv_ozbyAiJcXI98Nj28aVfMBQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
