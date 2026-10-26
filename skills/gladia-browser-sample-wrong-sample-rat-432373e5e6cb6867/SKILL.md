---
name: "gladia-browser-sample-wrong-sample-rat-432373e5e6cb6867"
description: "Shows how to fix gladia browser sample: wrong sample rate breaks audio on some devices. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_lJo9zz1Za0wbKZ8EAfUTrw"
  title: "Gladia browser sample: wrong sample rate breaks audio on some devices"
  version: "skv_MulOMxjlGeLXM3Le4jMNYQ"
  updated: "2026-10-03T14:19:48.834022+00:00"
  canonical_url: "https://vectle.com/skills/skl_lJo9zz1Za0wbKZ8EAfUTrw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://vectle.com/threads/thr_SnS2rKocbgT3Vynh9PbQGw\",\"https://github.com/gladiaio/gladia-samples/issues/63\"]"
---

## TL;DR

In the JS browser example you set both sampleRate and desiredSampleRate of RecordRTC to the same value. Removing the sampleRate line fixes it, and we put up a PR to change the sample accordingly.

## Steps

1. In the JS browser example you set both sampleRate and desiredSampleRate of RecordRTC to the same value. Setting sampleRate tells RecordRTC to parse the source audio as if it were already that rate, which breaks on devices whose mic runs at a different rate, like a MacBook with AirPods. I followed the docs exactly and my requests work on other endpoints. Is there something different about how this endpoint validates input?

2. You are right, that was a bug in the sample. desiredSampleRate is the one that asks RecordRTC to resample toward the rate you send to Gladia, but forcing sampleRate to the same value makes it misinterpret the source audio on any device whose mic runs at a different rate. Removing the sampleRate line fixes it, and we put up a PR to change the sample accordingly. Thanks for the report.

## When to use

You are seeing this: Setting sampleRate tells RecordRTC to parse the source audio as if it were already that rate, which breaks on devices whose mic runs at a different rate, like a MacBook with AirPods. Use this skill when you run into "Gladia browser sample: wrong sample rate breaks audio on some devices".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

In the JS browser example you set both sampleRate and desiredSampleRate of RecordRTC to the same value.


---

Source: [Vectle](https://vectle.com/skills/skl_lJo9zz1Za0wbKZ8EAfUTrw). Version: `skv_MulOMxjlGeLXM3Le4jMNYQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
