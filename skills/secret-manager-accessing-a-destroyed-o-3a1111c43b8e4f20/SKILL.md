---
name: "secret-manager-accessing-a-destroyed-o-3a1111c43b8e4f20"
description: "Shows how to fix secret Manager: accessing a destroyed or disabled version errors. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_LuQk4sGge3fU3_9BvFkr1w"
  title: "Secret Manager: accessing a destroyed or disabled version errors"
  version: "skv_9a7is62c0AIWtDFUd3MZDw"
  updated: "2026-10-03T14:11:56.020829+00:00"
  canonical_url: "https://vectle.com/skills/skl_LuQk4sGge3fU3_9BvFkr1w"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://cloud.google.com/secret-manager/docs/access-secret\",\"https://cloud.google.com/secret-manager/docs/managing-secrets\"]"
---

## TL;DR

Use this for "stop using this value" without deleting. - Destroyed: permanently gone. Error on access_secret_version: NotFound or FailedPrecondition, depending on whether the version is destroyed or disabled.

## Steps

1. Version states:
- Enabled: accessible.
- Disabled: exists but access fails. Re-enable it and access works again. Use this for "stop using this value" without deleting.
- Destroyed: permanently gone. No undelete, no recovery. The name stays in the version list as a tombstone.

2. How agents get here:
- Rotation scripts that destroy the old version immediately after creating the new one, while running services still pin the old version number. Access starts failing on next restart or next fetch.
- Cleanup jobs that destroy "old" versions by age without checking what is pinned where.
- Using `latest` during a rotation: latest flips to the new version mid-deploy and half your fleet reads old, half reads new.

3. Rules:
1. Never destroy a version until nothing references it. Disabled is the safe intermediate state.
2. In production, pin version numbers and bump them deliberately. `latest` is for dev.
3. If you must rotate under `latest`, make the new value backward compatible or accept a mixed fleet briefly.
4. Destroyed means destroyed. If the value mattered, your recovery is "create a new version with a new value", not undelete.

4. Verify: `gcloud secrets versions describe [VERSION] --secret [ID]` shows state before you touch anything; after rotation, confirm the running config points at an enabled version.

## When to use

You are seeing this: The name stays in the version list as a tombstone. Use this skill when you run into "Secret Manager: accessing a destroyed or disabled version errors".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_LuQk4sGge3fU3_9BvFkr1w). Version: `skv_9a7is62c0AIWtDFUd3MZDw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
