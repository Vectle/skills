---
name: "frontegg-android-hosted-login-needs-ma-9d08d44276034db6"
description: "Shows how to fix frontegg Android hosted login needs manifest activity toggles. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_nsA7Bp0O0JPlB3cJ5RSJVQ"
  title: "Frontegg Android hosted login needs manifest activity toggles"
  version: "skv_E4pqi68n04iDzhmahoXoCw"
  updated: "2026-10-03T14:11:51.709774+00:00"
  canonical_url: "https://vectle.com/skills/skl_nsA7Bp0O0JPlB3cJ5RSJVQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/frontegg/frontegg-android-kotlin/blob/HEAD/docs/usage.md\"]"
---

## TL;DR

To use hosted login on Android, add both activity entries to the manifest with the enabled flags flipped and tools replace set, otherwise the SDK keeps using the embedded WebView. For tenant switching, read tenantIds from the current user session and pass one to switchTenant.

## Steps

1. To use hosted login on Android, add both activity entries to the manifest with the enabled flags flipped and tools replace set, otherwise the SDK keeps using the embedded WebView.

2. For tenant switching, read tenantIds from the current user session and pass one to switchTenant.

## When to use

Use this skill when you run into "Frontegg Android hosted login needs manifest activity toggles".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_nsA7Bp0O0JPlB3cJ5RSJVQ). Version: `skv_E4pqi68n04iDzhmahoXoCw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
