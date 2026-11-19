---
name: "cloudflare-custom-hostnames-fallback-o-18070ec9e02f5da9"
description: "cloudflare custom hostnames fallback origin error hostname stuck pending"
metadata:
  skill_id: "skl_zB2R6iwEWy3_54LdL5PyZQ"
  title: "cloudflare custom hostnames fallback origin error hostname stuck pending"
  version: "skv_o1UkzxYYMH91juGIOMDpBQ"
  updated: "2026-11-19T13:52:25.940212+00:00"
  canonical_url: "https://vectle.com/skills/skl_zB2R6iwEWy3_54LdL5PyZQ"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

In the SSL for SaaS settings, confirm a fallback origin is set and is a proxied record in the same zone.

Request the fallback origin directly and check it returns a valid response for a test custom hostname.

Add the custom hostname and copy its exact validation record, either the TXT value or the HTTP validation file details shown for that hostname.

Wait for validation to flip, then check the hostname status and certificate status separately.

If it stays pending, delete and re-add the hostname after fixing the fallback origin, rather than editing the origin under a stuck hostname.

---

Source: [Vectle](https://vectle.com/skills/skl_zB2R6iwEWy3_54LdL5PyZQ). Version: `skv_o1UkzxYYMH91juGIOMDpBQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
