---
name: "spf-validation-failed-new-subdomain-ma-a3d407eb237c97d5"
description: "SPF validation failed new subdomain mailgun error sending blocked fails"
metadata:
  skill_id: "skl_VxCU_gVoMMxKFFTIOsc8iA"
  title: "SPF validation failed new subdomain mailgun error sending blocked fails"
  version: "skv_atptS4FxM_PXZL4ptaef8Q"
  updated: "2026-11-10T13:54:35.240504+00:00"
  canonical_url: "https://vectle.com/skills/skl_VxCU_gVoMMxKFFTIOsc8iA"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

In Mailgun, open the new domain or subdomain and copy the exact SPF TXT value shown on its DNS records page.

In your DNS provider, create a TXT record on the exact subdomain host that Mailgun lists, not on the root and not on a www host.

Check that the subdomain has only one SPF TXT record.

Count the DNS lookups in the merged SPF record if you also send through other services from the same subdomain.

Wait for propagation, then click verify in Mailgun again.

Send a test message from the subdomain and check its authentication results in the received headers.

---

Source: [Vectle](https://vectle.com/skills/skl_VxCU_gVoMMxKFFTIOsc8iA). Version: `skv_atptS4FxM_PXZL4ptaef8Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
