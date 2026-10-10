---
name: "promise-from-vwo-isfeatureenabled-is-n-112b48e92a797e85"
description: "Shows how to fix promise from VWO isFeatureEnabled is not always resolved. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_V9pHtZhVA1_V0TbPylhX_g"
  title: "Promise from VWO isFeatureEnabled is not always resolved"
  version: "skv_XJgLyhM-K-Wm0rH5VUygHw"
  updated: "2026-10-03T14:06:11.664889+00:00"
  canonical_url: "https://vectle.com/skills/skl_V9pHtZhVA1_V0TbPylhX_g"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

What fixed it Fixed in vwo-node-sdk v1.33.0, which covers all the promise paths for isFeatureEnabled, including the stored-variation and returning-user cases. What was going on The promise returned by isFeatureEnabled in the VWO Node SDK sometimes never resolves.

## Steps

1. What was going on
The promise returned by isFeatureEnabled in the VWO Node SDK sometimes never resolves. The underlying function could return a plain boolean in some paths while the caller only handled object returns, so the promise hung. A follow-up also showed the tracking request callback was not always awaited before resolving.

## When to use

You are seeing this: The underlying function could return a plain boolean in some paths while the caller only handled object returns, so the promise hung. Use this skill when you run into "Promise from VWO isFeatureEnabled is not always resolved".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

Versions mentioned in the source: vwo-node-sdk v1.33.0. If you are on something much newer or older, the details may have shifted.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_V9pHtZhVA1_V0TbPylhX_g). Version: `skv_XJgLyhM-K-Wm0rH5VUygHw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
