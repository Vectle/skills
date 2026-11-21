---
name: "aadsts700016-error-application-not-fou-88349752ffb4cb87"
description: "aadsts700016 error application not found in tenant directory authentication fails"
metadata:
  skill_id: "skl_1Qgu7C8IN3hR3Nxx2DK_2Q"
  title: "aadsts700016 error application not found in tenant directory authentication fails"
  version: "skv_oug2htGrfXXpQIScd2mJvA"
  updated: "2026-11-21T13:52:40.340223+00:00"
  canonical_url: "https://vectle.com/skills/skl_1Qgu7C8IN3hR3Nxx2DK_2Q"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Read the full error and note both values: the identifier and the directory named in the message.

Open the app registrations list in that named tenant and search for the identifier.

If it is absent, switch to the tenant where the app was registered and compare the authority in your app config.

Copy the application (client) id fresh from the registration overview page and update your config.

For a multi-tenant app failing in a customer tenant, have a tenant admin consent once so the service principal is created.

---

Source: [Vectle](https://vectle.com/skills/skl_1Qgu7C8IN3hR3Nxx2DK_2Q). Version: `skv_oug2htGrfXXpQIScd2mJvA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
