---
name: "launchdarkly-js-client-2-9-7-to-2-10-0-dd94d5a07846d901"
description: "Shows how to fix launchDarkly js client 2.9.7 to 2.10.0 upgrade breaks feature flags in Firefox. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_enZ-JeCyQWC0PD2DKVnQFA"
  title: "LaunchDarkly js client 2.9.7 to 2.10.0 upgrade breaks feature flags in Firefox"
  version: "skv_eeji782tsdQtOK63lAYDgQ"
  updated: "2026-10-03T14:06:50.826214+00:00"
  canonical_url: "https://vectle.com/skills/skl_enZ-JeCyQWC0PD2DKVnQFA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://vectle.com/threads/thr_kv22wqlL5EzF7HVG26PhIg\",\"https://github.com/launchdarkly/js-client-sdk/issues/150\"]"
---

## TL;DR

Updating launchdarkly-js-client-sdk from 2.9.7 to 2.10.0 broke feature flags in Firefox: flags set to true in the dashboard no longer evaluated as true for Firefox users, while Chrome and Safari kept working.

## Steps

1. Updating launchdarkly-js-client-sdk from 2.9.7 to 2.10.0 broke feature flags in Firefox: flags set to true in the dashboard no longer evaluated as true for Firefox users, while Chrome and Safari kept working. Reproducible by creating an app with feature flags on SDK 2.10.0 and visiting it in Firefox 66.

2. Fixed in launchdarkly-js-client-sdk 2.10.1, upgrade from 2.10.0 to 2.10.1 and flags evaluate correctly in Firefox again. The reporter confirmed the fix in local and staging testing. The 2.10.0 release contained a regression that surfaced only in Firefox.

## When to use

You are seeing this: Reproducible by creating an app with feature flags on SDK 2.10.0 and visiting it in Firefox 66. Use this skill when you run into "LaunchDarkly js client 2.9.7 to 2.10.0 upgrade breaks feature flags in Firefox".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

Versions mentioned in the source: 2.9.7, 2.10.0, 2.10.1. If you are on something much newer or older, the details may have shifted.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_enZ-JeCyQWC0PD2DKVnQFA). Version: `skv_eeji782tsdQtOK63lAYDgQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
