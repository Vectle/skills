---
name: "google-custom-search-api-unregistered-8b6b19f207428716"
description: "google custom search api unregistered caller error fix"
metadata:
  skill_id: "skl_TrnAB1s6dXv_ZQyoQlvvdg"
  title: "google custom search api unregistered caller error fix"
  version: "skv_OjyIe9NNTht0nbZa3p-_Mw"
  updated: "2026-11-10T13:53:18.226508+00:00"
  canonical_url: "https://vectle.com/skills/skl_TrnAB1s6dXv_ZQyoQlvvdg"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Read the full error body returned with the 403 response and note the reason field.

In Google Cloud Console, open the project you think the key belongs to and check that Custom Search API is listed as enabled under APIs and Services.

Check the request itself and confirm it sends both the key parameter and the cx parameter, with no stray spaces or line breaks in either value.

Open the key under Credentials and read its application restrictions.

Create a fresh unrestricted test key in the same project, wait a few minutes, and retry one simple query.

Confirm the cx value belongs to a Programmable Search Engine that is still active and set to search the sites you expect.

---

Source: [Vectle](https://vectle.com/skills/skl_TrnAB1s6dXv_ZQyoQlvvdg). Version: `skv_OjyIe9NNTht0nbZa3p-_Mw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
