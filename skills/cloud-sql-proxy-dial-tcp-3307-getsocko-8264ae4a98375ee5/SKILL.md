---
name: "cloud-sql-proxy-dial-tcp-3307-getsocko-8264ae4a98375ee5"
description: "Fixes Cloud SQL Proxy hanging on 'dial tcp :3307 getsockopt: connection timed out' from a GCE VM. Use this when the proxy has no network path to the instance. Not for auth errors."
metadata:
  skill_id: "skl_41MMDjmbzXwM3HqYYpiWww"
  title: "Cloud SQL Proxy: dial tcp :3307 getsockopt connection timed out"
  version: "skv_XAiv7L_jsKSvsN2ww1NHFQ"
  updated: "2026-10-03T05:10:31.097928+00:00"
  canonical_url: "https://vectle.com/skills/skl_41MMDjmbzXwM3HqYYpiWww"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://vectle.com/threads/thr_5uh-dHmz-Qb166f9OGBt5w\",\"https://github.com/GoogleCloudPlatform/cloud-sql-proxy/issues/164\"]"
---

TL;DR: if connecting to a Cloud SQL MySQL instance through the proxy from a GCE VM hangs forever with `couldn't connect to [instance]: dial tcp [ip]:3307: getsockopt: connection timed out`, the proxy has no network path to the instance. Note the proxy intentionally dials port 3307 (not 3306) to isolate proxy traffic on the instance side; local clients still use 3306. Checklist: allow egress from the proxy host to the instance IP on port 3307; check IP-type reachability (a private-IP instance is only reachable from GCP resources in the same region, so a proxy in another region or outside GCP times out; use an external IP or move the proxy into the same region/VPC). One reporter fixed it by cloning the instance (the original had a broken network path).

```text
couldn't connect to [instance]: dial tcp [ip]:3307: getsockopt: connection timed out
```

## Steps

1. Open egress from the proxy host to the instance IP on port 3307.

2. Confirm region/VPC reachability for the instance's IP type.

3. Retry the connection.

   Expected: the proxy connects. Success check: clients reach the database through the proxy.

## When to use this

- GCE VM to Cloud SQL MySQL via proxy, connection timed out on 3307.
- The service account has the Cloud SQL Client role and ports look open.

## When NOT to use this

- Auth errors; those fail fast, not with timeouts.
- The instance IP is wrong; fix that first.

## Compatibility

- Cloud SQL Proxy (port 3307 behavior).

## Variant phrasings

- "cloud sql proxy 3307 connection timed out"
- "cloud sql proxy dial tcp getsockopt"

## Root cause

No network path from the proxy host to the instance on the proxy's port.

## Edge cases

- Per the maintainer's summary, this error always means no network path; do not chase auth or config.

---

Source: [Vectle](https://vectle.com/skills/skl_41MMDjmbzXwM3HqYYpiWww). Version: `skv_XAiv7L_jsKSvsN2ww1NHFQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
