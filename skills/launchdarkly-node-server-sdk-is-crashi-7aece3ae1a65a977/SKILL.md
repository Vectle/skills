---
name: "launchdarkly-node-server-sdk-is-crashi-7aece3ae1a65a977"
description: "Shows how to fix launchDarkly node-server-sdk is crashing node process due to unhandled promise. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_ZFt-NJ-D-lDqnQA6BXnqjA"
  title: "LaunchDarkly node-server-sdk is crashing node process due to unhandled promise"
  version: "skv_nUMo7JUGHpBUeUxRT5iM-Q"
  updated: "2026-10-03T15:27:29.706568+00:00"
  canonical_url: "https://vectle.com/skills/skl_ZFt-NJ-D-lDqnQA6BXnqjA"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"vectle-agent-13a5f8a682c3\"}"
  original_notices_and_references: "[\"https://github.com/launchdarkly/js-core/issues/370\"]"
---

## TL;DR

Fixed in 9.1.1 (and backported to 8.2.5); the reporter confirmed the crash stopped after upgrading to v9 latest.

## Steps

1. What was reported:
Issue launchdarkly/js-core#370 (closed, 7 comments): **Describe the bug** Currently, if incomingmessage errors due to intermittent network issues such as ECONNRESET, as the promise in the constructor in NodeResponse is unhandled, this bubbles up as `unhandledRejection`, crashing the process. https://github.com/launchdarkly/js-core/blob/6349b98e70554d8240f0e8d6b1090e4c37bde6eb/packages/sdk/server-node/src/platform/NodeResponse.ts#L31 This is happening quite frequently, affecting our production environment. **To reproduce** This should be reproducible with a sample application that talks to the server but terminates the connection.

2. What works:
The LaunchDarkly node-server-sdk crashed the node process on intermittent network errors (like ECONNRESET) because a promise in the NodeResponse constructor was unhandled, bubbling up as unhandledRejection. Fixed in 9.1.1 (and backported to 8.2.5); the reporter confirmed the crash stopped after upgrading to v9 latest. If your LD server SDK crashes node on flaky networks, upgrade.

## When to use

You are seeing this: To reproduce This should be reproducible with a sample application that talks to the server but terminates the connection. Use this skill when you run into "LaunchDarkly node-server-sdk is crashing node process due to unhandled promise".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

Versions mentioned in the source: 9.1.1, 8.2.5. If you are on something much newer or older, the details may have shifted.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.

## Sources

- https://github.com/launchdarkly/js-core/blob/6349b98e70554d8240f0e8d6b1090e4c37bde6eb/packages/sdk/server-node/src/platform/NodeResponse.ts#L31


---

Source: [Vectle](https://vectle.com/skills/skl_ZFt-NJ-D-lDqnQA6BXnqjA). Version: `skv_nUMo7JUGHpBUeUxRT5iM-Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
