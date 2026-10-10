---
name: "atlas-error-serverselectiontimeouterro-afef264975cde332"
description: "MongoDB driver cannot reach any Atlas cluster node: ServerSelectionTimeoutError or no suitable servers found. Covers the IP access list check, paused clusters, DNS, and firewalls. Not for auth failures, wrong connection strings, or replica-set config errors on self-hosted Mongo."
metadata:
  skill_id: "skl_QU75pWHZcCco11bSNOu24Q"
  title: "Atlas error: ServerSelectionTimeoutError, no suitable servers"
  version: "skv_nalDTq6rQshsLPBXBXzlpw"
  updated: "2026-10-03T04:39:19.477085+00:00"
  canonical_url: "https://vectle.com/skills/skl_QU75pWHZcCco11bSNOu24Q"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: The driver found the cluster topology but could not establish a working connection to any node. On Atlas this is the IP access list nine times out of ten. Check the client's egress IP is listed (it is the egress IP, not the IP you think, for CI, VPNs, and containers), then check for a paused cluster, DNS, and local firewall. Then retry.

The error, verbatim:

```text
ServerSelectionTimeoutError: [host]:[port] timed out
No suitable servers found
```

Steps:

1. IP access list: Security, Network Access in Atlas. Is the client's egress IP listed? Success: the egress IP is on the list (add it with an expiry for temporary access).
2. Cluster state: is the cluster paused? A paused cluster refuses connections with timeouts, not a clear error. Success: the cluster is running.
3. DNS: can the machine resolve the SRV record? `nslookup -type=SRV _mongodb._tcp.[cluster-host]`. If not, use the standard connection string form. Success: SRV resolves or the standard string works.
4. Local firewall or proxy blocking outbound 27017. Success: the port is reachable.
5. Retry with a startup ping from the failing network. Success: the ping succeeds.

When to use: ServerSelectionTimeoutError or no suitable servers against MongoDB Atlas.

When not to use: authentication failures (wrong error), malformed connection strings, or self-hosted replica sets (different failure modes).

Compatibility: MongoDB drivers (any language), MongoDB Atlas.

Variants:
- mongodb atlas connection timeout
- no suitable servers found atlas
- serverselectiontimeouterror atlas fix

Root cause: the driver knows where the cluster is but cannot open a socket to any node. Atlas's network gate is the access list, and the client IP is almost always the surprise: CI runners, VPNs, and containers egress from IPs nobody configured.

Edge cases:
- It works from your laptop but not the deploy target: the difference is the network path, and the IP access list is still suspect number one.
- A paused cluster looks exactly like a network failure. Check state before debugging DNS.
- For temporary access, add the IP with an expiry so the list does not accumulate stale entries.

---

Source: [Vectle](https://vectle.com/skills/skl_QU75pWHZcCco11bSNOu24Q). Version: `skv_nalDTq6rQshsLPBXBXzlpw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
