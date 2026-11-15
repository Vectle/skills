---
name: "substack-email-not-delivered-spf-authe-4970cb9a6a1c45e8"
description: "Substack email not delivered SPF authentication failed error"
metadata:
  skill_id: "skl_bDU24R4Q8SKwH2Igt0jUJg"
  title: "Substack email not delivered SPF authentication failed error"
  version: "skv_GqQr_6upw0XNw6rXaRd_1Q"
  updated: "2026-11-14T01:55:07.362051+00:00"
  canonical_url: "https://vectle.com/skills/skl_bDU24R4Q8SKwH2Igt0jUJg"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Open the delivery report or a bounced message header and note the exact sending domain and the authentication results for SPF, DKIM, and DMARC.

Look up the TXT records for that domain and count the SPF records, meaning records that start with the SPF version tag.

Check that the single SPF record includes the sending service the newsletter platform uses for custom domain sending, following the platform current custom domain setup instructions.

Merge any duplicate records into one, keeping the total DNS lookup count in the record under the SPF limit of ten lookups, and remove senders the domain no longer uses.

Confirm DKIM is enabled for the custom domain in the newsletter platform and that its DNS record is published, then check that the DMARC record for the domain does not reject mail that passes DKIM but fails SPF.

Wait for DNS propagation, verify with an external mail authentication checker by sending a test message to it, and only then resend the newsletter post.

---

Source: [Vectle](https://vectle.com/skills/skl_bDU24R4Q8SKwH2Igt0jUJg). Version: `skv_GqQr_6upw0XNw6rXaRd_1Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
