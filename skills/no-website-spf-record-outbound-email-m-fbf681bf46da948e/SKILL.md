---
name: "no-website-spf-record-outbound-email-m-fbf681bf46da948e"
description: "no website spf record outbound email mailgun error deliverability fails"
metadata:
  skill_id: "skl_dlCt_XGvkxSsgX2RnYOvOA"
  title: "no website spf record outbound email mailgun error deliverability fails"
  version: "skv_O9XpNZSf3eK4bL4gzIa8Kg"
  updated: "2026-11-20T13:52:02.44387+00:00"
  canonical_url: "https://vectle.com/skills/skl_dlCt_XGvkxSsgX2RnYOvOA"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

In Mailgun, open the sending domain and copy the SPF value shown under domain verification and DNS records.

Check what DNS currently returns for the exact sending domain or subdomain you send from, not just the root website domain.

Publish one SPF record on the sending host in your DNS provider, using the value from step 1.

If the host already has an SPF record for another sender, merge the Mailgun include into that existing record instead of creating a duplicate.

Wait for propagation, re-run the DNS check, and send a test message to a mailbox you control.

---

Source: [Vectle](https://vectle.com/skills/skl_dlCt_XGvkxSsgX2RnYOvOA). Version: `skv_O9XpNZSf3eK4bL4gzIa8Kg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
