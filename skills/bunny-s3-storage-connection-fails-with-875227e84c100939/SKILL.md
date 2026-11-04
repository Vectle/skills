---
name: "bunny-s3-storage-connection-fails-with-875227e84c100939"
description: "bunny s3 storage connection fails with signature does not match error"
metadata:
  skill_id: "skl_PavSNftV8mqM3S46uEOjFw"
  title: "bunny s3 storage connection fails with signature does not match error"
  version: "skv_eonrERjYEjPNxMhF0D8l8g"
  updated: "2026-11-04T01:57:54.707329+00:00"
  canonical_url: "https://vectle.com/skills/skl_PavSNftV8mqM3S46uEOjFw"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

**Confirm which secret the client is using.** Bunny storage S3 access signs with the storage zone password, not the main account API key and not the pull zone token key. Expected: the client config names the storage zone password for this exact zone.

**Match the endpoint to the zone region.** Point the client at the storage endpoint for the region shown on the storage zone page, not the default global endpoint when the zone lives elsewhere. Success check: the endpoint host matches the zone region in the dashboard.

**Use the zone name as the bucket.** Set the bucket to the exact storage zone name, with no extra prefix or path segment. Expected: a list request returns the zone contents instead of a signature or not found error.

**Check the client clock.** Compare the client machine time with a reliable time source; a skew of more than a few minutes breaks request signing. Success check: after correcting the clock, the same request signs and succeeds.

**Verify with a small read, then a small write.** List the bucket, upload one small test file, and download it back. Expected: all three succeed with the same config, proving the signing path is fixed end to end.

---

Source: [Vectle](https://vectle.com/skills/skl_PavSNftV8mqM3S46uEOjFw). Version: `skv_eonrERjYEjPNxMhF0D8l8g`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
