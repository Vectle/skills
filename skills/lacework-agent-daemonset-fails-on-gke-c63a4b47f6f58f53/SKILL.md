---
name: "lacework-agent-daemonset-fails-on-gke-c63a4b47f6f58f53"
description: "Fixes the Lacework agent daemonset failing admission on GKE Autopilot with GKE Warden constraint violations. Use this when the daemonset is rejected even with the autopilot flag set. Not for non-Autopilot GKE or for agent runtime errors."
metadata:
  skill_id: "skl_HGJviRHgjxXSv7O_EO2UJQ"
  title: "Lacework agent daemonset fails on GKE Autopilot with GKE Warden constraint violations"
  version: "skv_dcDaWDhfVPYzYkwuXj-63Q"
  updated: "2026-10-03T05:57:02.996322+00:00"
  canonical_url: "https://vectle.com/skills/skl_HGJviRHgjxXSv7O_EO2UJQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://vectle.com/threads/thr_vDypAeIiOUcziKXWPuXLow\",\"https://github.com/lacework/helm-charts/issues/191\"]"
---

TL;DR: if the Lacework agent daemonset fails admission on GKE Autopilot with GKE Warden constraint violations (even with the autopilot setting on), set `image.overrideValue=lacework/datacollector:latest` so the image comes from the whitelisted source and the Warden checks are skipped, plus `cloudservice.gke.autopilot=true`, `priorityClassCreate=true`, and cpu/memory resource requests. As helm flags:

```sh
helm install ... \
  --set image.overrideValue=lacework/datacollector:latest \
  --set cloudservice.gke.autopilot=true \
  --set priorityClassCreate=true \
  --set resources.requests.cpu=100m \
  --set resources.requests.memory=512Mi
```

The reporter confirmed this deployed successfully.

## Steps

1. Apply the helm flags above.

2. Verify the daemonset passes admission.

   Expected: pods schedule. Success check: the agent runs on Autopilot nodes.

## When to use this

- GKE Autopilot, Lacework agent daemonset rejected by Warden constraints.

## When NOT to use this

- Standard GKE; Warden constraints do not apply.
- The agent runs but misbehaves; that is a runtime issue.

## Compatibility

- Lacework agent on GKE Autopilot.

## Variant phrasings

- "lacework GKE autopilot warden"
- "lacework daemonset autopilot constraint violation"

## Root cause

The default daemonset spec pulled the image from a registry path the Warden does not accept and missed Autopilot-required pod settings.

## Edge cases

- Pin the image tag in production rather than floating on latest.

Source: https://vectle.com/threads/thr_vDypAeIiOUcziKXWPuXLow

---

Source: [Vectle](https://vectle.com/skills/skl_HGJviRHgjxXSv7O_EO2UJQ). Version: `skv_dcDaWDhfVPYzYkwuXj-63Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
