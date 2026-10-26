---
name: "secret-manager-rotation-schedules-pub-fc6220cd116d3797"
description: "Shows how to fix secret Manager rotation: schedules, Pub/Sub notifications, and rotation functions. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_A2ejMLN8is6SEH4sm5XM-g"
  title: "Secret Manager rotation: schedules, Pub/Sub notifications, and rotation functions"
  version: "skv_xUtchKofFlyV3CWmHR12ag"
  updated: "2026-10-03T14:18:36.952607+00:00"
  canonical_url: "https://vectle.com/skills/skl_A2ejMLN8is6SEH4sm5XM-g"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://cloud.google.com/secret-manager/docs/secret-rotation\"]"
---

## TL;DR

How it works: you set a rotation schedule on the secret; Secret Manager publishes a SECRET_ROTATE message to your Pub/Sub topic at each rotation time. YOUR subscriber does the actual rotation (generate value, add version, update the external system).

## When to use

You are seeing this: Goal: credentials rotate automatically without humans pasting new values. Use this skill when you run into "Secret Manager rotation: schedules, Pub/Sub notifications, and rotation functions".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

Goal: credentials rotate automatically without humans pasting new values.

How it works: you set a rotation schedule on the secret; Secret Manager publishes a SECRET_ROTATE message to your Pub/Sub topic at each rotation time. YOUR subscriber does the actual rotation (generate value, add version, update the external system).

Setup:

```
gcloud secrets create [ID] --replication-policy automatic   --rotation-period [PERIOD]   --next-rotation-time [ISO-TIME]   --topics projects/[P]/topics/[TOPIC]
```

Then deploy a subscriber (Cloud Run function or service) on that topic that:
1. Receives SECRET_ROTATE.
2. Generates the new credential value (or calls the external system's API to rotate).
3. Adds it as a new secret version.
4. Optionally disables the old version after consumers have picked up the new one.

Traps:
- Secret Manager does NOT generate the new value. If nothing subscribes to the topic, rotations "happen" and nothing changes. Monitor the subscriber.
- Consumers reading `latest` flip to the new value immediately; consumers pinning versions do not. Coordinate the consumer strategy with the rotation (see the destroyed-version error skill).
- The rotation function needs secretmanager.admin-ish rights on the secret (add versions) but consumers only need secretAccessor. Separate identities.
- Test rotation end to end in a sandbox secret before pointing it at production credentials. A broken rotator that adds garbage versions is worse than no rotation.
- Rotation period minimums and the next_rotation_time format (ISO 8601) are strict; invalid values fail at set time.

Verify: force a rotation on a test secret, confirm a new enabled version appears and consumers pick it up, then enable the production schedule.


---

Source: [Vectle](https://vectle.com/skills/skl_A2ejMLN8is6SEH4sm5XM-g). Version: `skv_xUtchKofFlyV3CWmHR12ag`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
