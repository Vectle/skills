---
name: "price-tracker-scraper-blocked-with-403-8af629dc0c5fa575"
description: "price tracker scraper blocked with \"403 Forbidden\" error on retailer site"
metadata:
  skill_id: "skl_zWgc4kBBpxLtPZiCEJNOWA"
  title: "price tracker scraper blocked with \"403 Forbidden\" error on retailer site"
  version: "skv_11KLeSdSm2jXQYfs5dGqgw"
  updated: "2026-11-20T01:52:56.105356+00:00"
  canonical_url: "https://vectle.com/skills/skl_zWgc4kBBpxLtPZiCEJNOWA"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Open the same product URL in a normal browser from the same network.

Check the tracker logs for when 403 responses started and whether every URL or only one retailer is affected.

Reduce the request rate and spread checks out; remove burst polling of many product pages in the same minute.

Send complete standard headers including a truthful user agent that identifies the tracker and a contact where the site requires it, and honour robots and terms for that site.

Where the retailer offers a product feed, affiliate API, or price API, switch that retailer to the official source.

Back off and stop polling a retailer that keeps returning 403, and surface it as unavailable in the tracker instead of retrying aggressively.

---

Source: [Vectle](https://vectle.com/skills/skl_zWgc4kBBpxLtPZiCEJNOWA). Version: `skv_11KLeSdSm2jXQYfs5dGqgw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
