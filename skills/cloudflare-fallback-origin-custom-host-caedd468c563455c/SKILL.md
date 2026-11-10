---
name: "cloudflare-fallback-origin-custom-host-caedd468c563455c"
description: "cloudflare fallback origin custom hostnames not working"
metadata:
  skill_id: "skl_RX04_1TQQUQIN1janfBduA"
  title: "cloudflare fallback origin custom hostnames not working"
  version: "skv_64s9wyBcHkThvtHuQUl2wQ"
  updated: "2026-11-10T01:54:44.908594+00:00"
  canonical_url: "https://vectle.com/skills/skl_RX04_1TQQUQIN1janfBduA"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Open the zone in Cloudflare, go to SSL/TLS and then Custom Hostnames, and read the fallback origin value shown there.

Go to DNS for the zone and find the record for that fallback origin hostname.

Open the fallback origin hostname directly in a browser or with a simple HTTPS request from your own machine.

In the Custom Hostnames list, check the status and certificate status of one failing hostname.

Confirm the zone SSL mode is Full or Full (Strict) and that the origin presents a certificate covering the fallback origin hostname.

Create one fresh test custom hostname, wait for it to show active, and request it.

---

Source: [Vectle](https://vectle.com/skills/skl_RX04_1TQQUQIN1janfBduA). Version: `skv_64s9wyBcHkThvtHuQUl2wQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
