---
name: "spinnaker-jenkins-integration-fails-wi-ca8679159df3571e"
description: "Shows how to fix spinnaker Jenkins integration fails with 403 No valid crumb was included in the request. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_fJRTif1OihQefK0uvkGb1Q"
  title: "Spinnaker Jenkins integration fails with 403 No valid crumb was included in the request"
  version: "skv_D6nHp9tTj4QjWgVdQobA2A"
  updated: "2026-10-03T14:14:50.497547+00:00"
  canonical_url: "https://vectle.com/skills/skl_fJRTif1OihQefK0uvkGb1Q"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://vectle.com/threads/thr_cg3h7oiv5wDc--_7kZKvNA\",\"https://github.com/spinnaker/spinnaker/issues/2067\"]"
---

## TL;DR

The Jenkins credentials (URL, username, password) were configured via hal config ci jenkins master add.

## Steps

1. Integrating Jenkins with Spinnaker through Halyard, every pipeline failed with: 403 No valid crumb was included in the request. The Jenkins credentials (URL, username, password) were configured via `hal config ci jenkins master add`. Jenkins CSRF protection rejects requests without a valid crumb, and Spinnaker's Jenkins integration did not handle crumb issuance, so all Jenkins-triggered stages failed.

2. Multiple community-verified fixes: (1) Use a Jenkins API token instead of the user password in the Halyard Jenkins master config - several users confirmed this alone resolved it. (2) If Jenkins sits behind a reverse proxy, enable "Enable Proxy Compatibility" under Jenkins Global Security Settings > CSRF Protection, then log out and back in. (3) Verify the Jenkins URL in Manage Jenkins > Configure System matches the public URL, not an internal cluster address. A code fix for crumb handling landed via spinnaker/igor#222 as well.

## When to use

You are seeing this: Integrating Jenkins with Spinnaker through Halyard, every pipeline failed with: 403 No valid crumb was included in the request. Use this skill when you run into "Spinnaker Jenkins integration fails with 403 No valid crumb was included in the request".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_fJRTif1OihQefK0uvkGb1Q). Version: `skv_D6nHp9tTj4QjWgVdQobA2A`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
