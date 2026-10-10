---
name: "nv-2314-bug-report-many-warnings-durin-d1d760ae5adb825e"
description: "Shows how to fix [NV-2314] \ud83d\udc1b Bug Report: Many warnings during webpack compile process. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_5lqrUDAv4zbaMPupgbqTwg"
  title: "[NV-2314] \ud83d\udc1b Bug Report: Many warnings during webpack compile process"
  version: "skv_DmqFaNbr0YBmcDX42D3O0g"
  updated: "2026-10-03T20:31:56.357985+00:00"
  canonical_url: "https://vectle.com/skills/skl_5lqrUDAv4zbaMPupgbqTwg"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

## TL;DR

Upgrade to the Inbox component and use the updated docker images and the warnings go away. [scopsy (commenter)]: The webpack compile warnings (source-map parse failures from @novu/notification-center 0.14.0) were resolved by the new Inbox component.

## Steps

1. [scopsy (commenter)]: The webpack compile warnings (source-map parse failures from @novu/notification-center 0.14.0) were resolved by the new Inbox component. Upgrade to the Inbox component and use the updated docker images and the warnings go away.

2. https://github.com/novuhq/novu/issues/3400: Issue novuhq/novu#3400 (closed, 42 comments): ### 📜 Description Hi, we use `"@novu/notification-center": "0.14.0"` for our web application and there are many warnings during webpack compile process. ### 👟 Reproduction steps 1. just try to run the application id dev mode with `"@novu/notification-center": "0.14.0"` ### 👍 Expected behavior There should not be warnings ### 👎 Actual Behavior with Screenshots ``` WARNING in ./node_modules/@novu/notification-center/dist/esm/index.js Module Warning (from ./node_modules/source-map-loader/dist/cjs.js): Failed to parse source map from...

## When to use

Use this skill when you run into "[NV-2314] 🐛 Bug Report: Many warnings during webpack compile process".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

Versions mentioned in the source: novunotification-center 0.14.0. If you are on something much newer or older, the details may have shifted.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.

## Sources

- https://github.com/novuhq/novu/issues/3400:


---

Source: [Vectle](https://vectle.com/skills/skl_5lqrUDAv4zbaMPupgbqTwg). Version: `skv_DmqFaNbr0YBmcDX42D3O0g`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
