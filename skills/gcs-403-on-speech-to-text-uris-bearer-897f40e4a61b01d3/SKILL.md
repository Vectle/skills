---
name: "gcs-403-on-speech-to-text-uris-bearer-897f40e4a61b01d3"
description: "Shows how to fix gCS 403 on Speech-to-Text URIs: Bearer token and bucket IAM, not Basic auth. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_xbtxvHMwUFCKY51RvffUcg"
  title: "GCS 403 on Speech-to-Text URIs: Bearer token and bucket IAM, not Basic auth"
  version: "skv_OBDqTGrrIb23rRZdHsmDow"
  updated: "2026-10-03T14:03:53.518124+00:00"
  canonical_url: "https://vectle.com/skills/skl_xbtxvHMwUFCKY51RvffUcg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

The recommendation is to use a client library with Application Default Credentials instead of hand-rolled HTTP.

## Steps

1. If Speech-to-Text from a GCS URI returns 403 storage.objects.get, authenticate with an OAuth2 Bearer token, not Basic auth, and grant your service account read access on the bucket in IAM. Prefer the client library with Application Default Credentials so auth and token refresh are handled for you.

## When to use

You are seeing this: If Speech-to-Text from a GCS URI returns 403 storage.objects.get, authenticate with an OAuth2 Bearer token, not Basic auth, and grant your service account read access on the bucket in IAM. Use this skill when you run into "GCS 403 on Speech-to-Text URIs: Bearer token and bucket IAM, not Basic auth".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_xbtxvHMwUFCKY51RvffUcg). Version: `skv_OBDqTGrrIb23rRZdHsmDow`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
