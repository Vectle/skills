---
name: "crawlee-browser-crawler-fails-with-pag-06e7a81f94b40889"
description: "crawlee browser crawler fails with page timeout error after 60 seconds"
metadata:
  skill_id: "skl_RbEuCS0wFSGCrg4KumfhoA"
  title: "crawlee browser crawler fails with page timeout error after 60 seconds"
  version: "skv_uV08BV29hAw9GMoozQk_LA"
  updated: "2026-11-20T01:52:23.635287+00:00"
  canonical_url: "https://vectle.com/skills/skl_RbEuCS0wFSGCrg4KumfhoA"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Open the failing URL in a normal browser and time how long the main content takes to appear.

Reproduce with one URL and verbose logging and note whether the timeout is on navigation or on a later page operation.

Change the wait strategy to wait for a specific content selector instead of waiting for the network to go idle.

Set an explicit navigation timeout that matches the site, for example longer for known slow pages, and keep a per request retry limit.

If only some pages time out, check proxy latency and whether the site serves a consent or bot check page to the browser crawler.

---

Source: [Vectle](https://vectle.com/skills/skl_RbEuCS0wFSGCrg4KumfhoA). Version: `skv_uV08BV29hAw9GMoozQk_LA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
