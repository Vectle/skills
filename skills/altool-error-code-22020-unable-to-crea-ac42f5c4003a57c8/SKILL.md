---
name: "altool-error-code-22020-unable-to-crea-ac42f5c4003a57c8"
description: "Shows how to fix altool error code -22020 unable to create an authenticated session on App Store Connect. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_0jdkyBX5cjJaZyAg0z0Vsw"
  title: "altool error code -22020 unable to create an authenticated session on App Store Connect"
  version: "skv_A4bI_40R3Nop7zeWkg0-Jw"
  updated: "2026-10-04T07:45:55.782142+00:00"
  canonical_url: "https://vectle.com/skills/skl_0jdkyBX5cjJaZyAg0z0Vsw"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

## TL;DR

Use an app-specific password for App Store Connect instead of the regular Apple ID password. This is now documented in the Codemagic docs after a docs PR merged the guidance.

## Steps

1. Use an app-specific password for App Store Connect instead of the regular Apple ID password. This is now documented in the Codemagic docs after a docs PR merged the guidance. App-specific passwords are generated from the Apple ID account page.

## When to use

You are seeing this: Validating or publishing an iOS archive to App Store Connect fails with error code -22020, unable to create an authenticated session. Use this skill when you run into "altool error code -22020 unable to create an authenticated session on App Store Connect".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

This looks like a code signing problem at first glance but it is not.


---

Source: [Vectle](https://vectle.com/skills/skl_0jdkyBX5cjJaZyAg0z0Vsw). Version: `skv_A4bI_40R3Nop7zeWkg0-Jw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
