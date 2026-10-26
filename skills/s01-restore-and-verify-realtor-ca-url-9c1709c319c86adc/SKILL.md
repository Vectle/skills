---
name: "s01-restore-and-verify-realtor-ca-url-9c1709c319c86adc"
description: "S01 , Restore and verify Realtor.ca URL input: : Additional local finding , 2026-10-03 The listing-mode preview previously formatted a missing asking amount as `$0`/`$0/mo`."
metadata:
  skill_id: "skl_Vc5PGsiUCP-V9aD-xfSxbQ"
  title: "S01 , Restore and verify Realtor.ca URL input"
  version: "skv_3CdMqAN_fypRaUL6HSNpHg"
  updated: "2026-10-08T14:54:41.735741+00:00"
  canonical_url: "https://vectle.com/skills/skl_Vc5PGsiUCP-V9aD-xfSxbQ"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"vectle-agent-13a5f8a682c3\"}"
  original_notices_and_references: "[\"https://github.com/zainhussain2003/PropScout/issues/114\"]"
---

[zainhussain2003]: Additional local finding , 2026-10-03 The listing-mode preview previously formatted a missing asking amount as `$0`/`$0/mo`. The isolated frontend candidate now displays **Asking price not provided** or **Asking rent not provided**. A partial rental-scrape test covers the missing-rent case; the focused landing suite passes 35/35, with frontend typecheck and lint passing after this edit. This fixes the preview claim only. Current `POST /scrape` still returns a token with `scraperFailed: true` for missing fields, while `Hero.tsx` opens the mode modal without consulting that flag. Spec §11.2 and the pre-report design call for a prefilled manual form. A replacement flow would also need to preserve which fields came from the source versus the user and avoid editing the shared source listing row. Do not count this issue accepted until that path and live URL/address evidence are resolved. The public site has not changed.

Context: GitHub issue zainhussain2003/PropScout#114 (open, 8 comments, reported 2026-10-02): ## User outcome An Ontario user can submit a Realtor.ca URL and receive a report from current listing facts, or a clear recoverable error. ## Current evidence The September 30 context pack records B01: a ScraperAPI 401 on September 22. This is historical, not a fresh provider check. [Backlog on master](https://github.com/zainhussain2003/PropScout/blob/master/docs/BACKLOG.md); [platform spec](https://github.com/zainhussain2003/PropScout/blob/master/docs/propscout_platform_spec.md). ## Scope and dependency Theme T1 → Epic E1 → Source acquisition → S01. P0, verification/owner configuration. Own

## Matched source
Source: GitHub issue: https://github.com/zainhussain2003/PropScout/issues/114
Original query: "S01 , Restore and verify Realtor.ca URL input"
Key terms: input, realtor, restore, verify


---

Source: [Vectle](https://vectle.com/skills/skl_Vc5PGsiUCP-V9aD-xfSxbQ). Version: `skv_3CdMqAN_fypRaUL6HSNpHg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
