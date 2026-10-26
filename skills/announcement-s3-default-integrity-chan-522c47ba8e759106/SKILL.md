---
name: "announcement-s3-default-integrity-chan-522c47ba8e759106"
description: "Fixes XAmzContentSHA256Mismatch failures after boto3 1.36.0 enabled default S3 integrity checksums, by pinning back to boto3<1.36.0 as a stopgap or upgrading and keeping checksums on. Use when PutObject calls start failing after a boto3 upgrade. Not for other S3 signature errors."
metadata:
  skill_id: "skl_kyzCEFsNeLvjYNbeIfe-wg"
  title: "Announcement: S3 default integrity change"
  version: "skv_M1TjOsK9YBlpJxkXP2wNTQ"
  updated: "2026-10-03T04:11:30.556732+00:00"
  canonical_url: "https://vectle.com/skills/skl_kyzCEFsNeLvjYNbeIfe-wg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/boto/boto3/issues/4392\"]"
---

## TL;DR

boto3 1.36.0 turned on default S3 integrity checksums. If `PutObject` now fails with `XAmzContentSHA256Mismatch`, pin back to `boto3<1.36.0, botocore<1.36.0, s3transfer<0.11.0` as a stopgap. Longer term, upgrade and keep the checksums on; only disable the default integrity behavior per the AWS docs if you have a specific reason.

## The error

```text
XAmzContentSHA256Mismatch: The Content-SHA256 you specified did not match what we received.
```

Starts after upgrading to boto3 1.36.0 or newer.

## Fix it

1. Confirm the boto3 version:
   ```bash
   pip show boto3 | grep Version
   ```
   Success check: version is 1.36.0 or newer, confirming the behavior change applies.

2. Stopgap: pin the previous minor line:
   ```text
   boto3<1.36.0
   botocore<1.36.0
   s3transfer<0.11.0
   ```
   Success check: `PutObject` succeeds again after reinstalling.

3. Proper fix: upgrade to the latest boto3 and keep default integrity on.
   Success check: puts succeed with checksums enabled (they protect S3 integrity).

4. Only if you have a specific reason, disable the default integrity behavior per the AWS SDK docs on data integrity.
   Success check: puts succeed; document why checksums are off.

## When this applies

- `PutObject`/`upload_file` fails with `XAmzContentSHA256Mismatch` right after a boto3 upgrade to 1.36.0+.
- Proxies or middleware that rewrite request bodies, which invalidates the checksum.

## When it does not apply

- Signature errors like `SignatureDoesNotMatch`; those are credential or region problems.
- You are on boto3 below 1.36.0 and never enabled checksums.
- GetObject failures; the new defaults also validate on Get, but the fix path differs.

## Compatibility

- boto3/botocore 1.36.0+ and s3transfer 0.11.0+: default integrity on.
- AWS SDK for Python only; other SDKs have their own timelines.

## Variant phrasings

- XAmzContentSHA256Mismatch boto3
- boto3 1.36.0 S3 checksum failure
- S3 default integrity change PutObject fails
- disable boto3 S3 checksum validation

## Why it happens

In 1.36.0 the S3 client started adding a checksum to every Put and validating checksums on Get by default. Anything that mutates the request body in flight (proxies, middleware) breaks the checksum match, and some older patterns that worked without checksums now fail.

## Edge cases

- Disabling integrity globally is a security regression; scope it to the specific client or operation.
- Source: https://github.com/boto/boto3/issues/4392 and https://docs.aws.amazon.com/sdkref/latest/guide/feature-dataintegrity.html


---

Source: [Vectle](https://vectle.com/skills/skl_kyzCEFsNeLvjYNbeIfe-wg). Version: `skv_M1TjOsK9YBlpJxkXP2wNTQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
