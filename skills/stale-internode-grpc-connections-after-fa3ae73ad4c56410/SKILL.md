---
name: "stale-internode-grpc-connections-after-fa3ae73ad4c56410"
description: "Fixes Temporal servers keeping stale internode gRPC connections after Kubernetes pod termination (continuous dial tcp i/o timeout errors) by upgrading the server to v1.31.1 or later. Use after scale-downs, rolling updates, or node drains. Not for client-side connection issues."
metadata:
  skill_id: "skl_GOg3c1CMv3f5Vaw8dcAgiQ"
  title: "Stale internode gRPC connections after pod termination when using Kubernetes Deployments"
  version: "skv__6PEhrtpz3pgG_p2Qp1vDA"
  updated: "2026-10-03T04:48:34.320189+00:00"
  canonical_url: "https://vectle.com/skills/skl_GOg3c1CMv3f5Vaw8dcAgiQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

Fix first: upgrade the Temporal server to v1.31.1 or later. That patch release closes and removes references to stale connections, which the maintainer verified.

```text
dial tcp ... i/o timeout
```

1. Upgrade your Temporal server to v1.31.1 or later.
2. Run a scale-down or rolling update and watch the logs. Expected: no more repeated dial attempts to stale pod IPs.

When to use: Temporal servers keep dialing stale pod IPs after Kubernetes scale-downs, rolling updates, or node drains.

When not to use: client-side connection issues (this is server-to-server internode traffic).

Compatibility: Temporal server v1.31.1+. Reported in temporalio/temporal#8719.

Variants:
- "temporal stale grpc connections kubernetes"
- "temporal dial tcp i/o timeout pod termination"
- "temporal internode connections scale down"

Root cause: the server didnt drop internode gRPC connections to pods removed from the membership ring, so it kept redialing dead IPs.

Edge cases: the client SDK version doesnt matter here; the fix is server-side.

---

Source: [Vectle](https://vectle.com/skills/skl_GOg3c1CMv3f5Vaw8dcAgiQ). Version: `skv__6PEhrtpz3pgG_p2Qp1vDA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
