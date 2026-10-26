---
name: "support-aws-s3-new-checksums-8d4d58a24f3ad721"
description: "Shows how to fix support AWS S3 new checksums. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_W-hXZ8BGPEcd1xu3Fh8b8A"
  title: "Support AWS S3 new checksums"
  version: "skv_8cfR9kk0piBzLEbnd0UDtQ"
  updated: "2026-10-03T05:08:51.744103+00:00"
  canonical_url: "https://vectle.com/skills/skl_W-hXZ8BGPEcd1xu3Fh8b8A"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/minio/minio/issues/20845\"]"
---

## TL;DR

New AWS SDK v2 (2.30.0) allows configuring request/response checksum validation. when: `` s3client.requestChecksumCalculation(RequestChecksumCalculation.WHEN\_REQUIRED); s3client.responseChecksumValidation(ResponseChecksumValidation.WHEN\_REQUIRED); ` `` DeleteObjectsRequest request = DeleteObjectsRequest.builder()...

## Steps

1. New AWS SDK v2 (2.30.0) allows configuring request/response checksum validation.

```
 s3client.requestChecksumCalculation(RequestChecksumCalculation.WHEN_REQUIRED);
 s3client.responseChecksumValidation(ResponseChecksumValidation.WHEN_REQUIRED);
```

2. ```
DeleteObjectsRequest request = DeleteObjectsRequest.builder()
 ...

3. New AWS SDK v2 checksum validation (requestChecksumCalculation / responseChecksumValidation) broke against older MinIO releases. Fixed in MinIO RELEASE.2025-01-20T14-49-07Z; the reporter confirmed it works, and a follow-up PR (#20878) covered remaining weird checksum settings. If your AWS SDK v2 checksum operations fail against MinIO, upgrade the server past that release.

## When to use

You are seeing this: Issue minio/minio#20845 (closed, 22 comments): ## NOTE If this case is urgent, please subscribe to Subnet so that our 24/7 support team may help you faster. [!--- Provide a general summary of the issue in the Title above --] Use this skill when you run into "Support AWS S3 new checksums".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

Versions mentioned in the source: 2.30.0. If you are on something much newer or older, the details may have shifted.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.

## Sources

- https://min.io/pricing


---

Source: [Vectle](https://vectle.com/skills/skl_W-hXZ8BGPEcd1xu3Fh8b8A). Version: `skv_8cfR9kk0piBzLEbnd0UDtQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
