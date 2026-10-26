---
name: "frontegg-admin-portal-shows-applicatio-2591006bbeef8e40"
description: "Shows how to fix frontegg admin portal shows Application not found without appId. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_9dqpv4ml7mV4jqWydd5l5Q"
  title: "Frontegg admin portal shows Application not found without appId"
  version: "skv_sYAZMXhYa8Ep4rRIiZ61dQ"
  updated: "2026-10-03T14:12:36.137852+00:00"
  canonical_url: "https://vectle.com/skills/skl_9dqpv4ml7mV4jqWydd5l5Q"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/frontegg/frontegg-react-native/blob/HEAD/docs/advanced.md\"]"
---

## TL;DR

For multi-app workspaces, set the applicationId in your native configuration so the portal URL includes the appId parameter, and pin the SDK to an exact version since the admin portal is still in beta.

## Steps

1. For multi-app workspaces, set the applicationId in your native configuration so the portal URL includes the appId parameter, and pin the SDK to an exact version since the admin portal is still in beta. Single-app workspaces are unaffected. If users report seeing Application not found right after signing in, check the portal URL before debugging auth.

## When to use

You are seeing this: Single-app workspaces are unaffected. Use this skill when you run into "Frontegg admin portal shows Application not found without appId".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_9dqpv4ml7mV4jqWydd5l5Q). Version: `skv_sYAZMXhYa8Ep4rRIiZ61dQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
