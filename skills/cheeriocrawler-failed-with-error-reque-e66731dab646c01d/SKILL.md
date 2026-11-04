---
name: "cheeriocrawler-failed-with-error-reque-e66731dab646c01d"
description: "cheeriocrawler failed with error request loop detected in crawlee"
metadata:
  skill_id: "skl_KZwzvY1f4-YY2D8Kb2mAPw"
  title: "cheeriocrawler failed with error request loop detected in crawlee"
  version: "skv_p00ZMwcJY7HfaMybvUuC7w"
  updated: "2026-11-04T13:58:08.445708+00:00"
  canonical_url: "https://vectle.com/skills/skl_KZwzvY1f4-YY2D8Kb2mAPw"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Reproduce with a small crawl: set a low maximum requests per crawl value such as 50 and log every enqueued URL.

Inspect the differing URLs for query parameters, session fragments, trailing slashes, and http versus https variants.

Normalize before enqueueing: strip tracking parameters, force one host and scheme, and remove the trailing slash consistently in the link extraction step.

Confirm dedupe is active: do not override the request unique key unless the replacement still hashes the normalized URL.

Skip enqueueing from redirect and error pages: check the response status in the handler and only extract links from successful HTML responses.

Re-run the bounded crawl, then raise the maximum requests per crawl.

---

Source: [Vectle](https://vectle.com/skills/skl_KZwzvY1f4-YY2D8Kb2mAPw). Version: `skv_p00ZMwcJY7HfaMybvUuC7w`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
