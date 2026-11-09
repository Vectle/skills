---
name: "bunnycdn-perma-cache-not-working-cache-3e84b9d522681753"
description: "bunnycdn perma-cache not working: cached files never purge, stale content error"
metadata:
  skill_id: "skl_iBzHd8mOX2JsvKy2gOV-qw"
  title: "bunnycdn perma-cache not working: cached files never purge, stale content error"
  version: "skv_F1aYrFRCDVDrVqOVR2SAzw"
  updated: "2026-11-09T01:55:32.380542+00:00"
  canonical_url: "https://vectle.com/skills/skl_iBzHd8mOX2JsvKy2gOV-qw"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Request the file with a fresh network tool or a private browser window and note the cache response header and the file size or version you get back.

Open the Bunny Storage zone linked to the pull zone and check whether a perma-cache copy of that path exists and still holds the old file.

Replace that stored copy with the new file, or delete the stored copy so it is rebuilt from the origin on the next request.

Purge the exact file URL in the pull zone after fixing the stored copy, in that order.

Request the file again fresh and compare its size or a known changed line with the origin file.

---

Source: [Vectle](https://vectle.com/skills/skl_iBzHd8mOX2JsvKy2gOV-qw). Version: `skv_F1aYrFRCDVDrVqOVR2SAzw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
