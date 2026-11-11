---
name: "application-id-not-found-error-aadsts7-d389b3a13476cf11"
description: "application id not found error aadsts700016 entra sign-in fails bug"
metadata:
  skill_id: "skl_FJ6NyunXUcIgjXTcwvL00w"
  title: "application id not found error aadsts700016 entra sign-in fails bug"
  version: "skv_EcVEQA5TI_7SNO1rcPoGvg"
  updated: "2026-11-11T13:54:13.196624+00:00"
  canonical_url: "https://vectle.com/skills/skl_FJ6NyunXUcIgjXTcwvL00w"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Copy the client id from the failing request or your app configuration and search for it under App registrations in the Entra admin center for the tenant users sign in to.

Read the authority or tenant value in the app configuration and confirm it is the tenant id or domain of that same tenant, not a development tenant or the word common with a tenant specific expectation.

If the app registration exists in another tenant, open Enterprise applications in the target tenant and check for its service principal. If it is missing, have a tenant admin consent to the app once so the service principal is created.

If the registration was deleted, check the deleted applications list. Restore it if it is still within the restore window, otherwise create a new registration and update every client with the new client id.

Retry sign in in a private browser window so a cached session for a different tenant cannot confuse the result.

---

Source: [Vectle](https://vectle.com/skills/skl_FJ6NyunXUcIgjXTcwvL00w). Version: `skv_EcVEQA5TI_7SNO1rcPoGvg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
