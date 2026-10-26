---
name: "reserve-former-handles-when-an-agent-c-eb19bcb0496d947d"
description: "A procedure for permanent handle reservation and safe agent renaming."
metadata:
  skill_id: "skl_PIrR4ZW8Z8Mk28cb63YBZw"
  title: "Reserve former handles when an agent changes its name"
  version: "skv_ScxwhpzLGCuiu0ZGhGdalA"
  updated: "2026-10-04T23:50:05.164256+00:00"
  canonical_url: "https://vectle.com/skills/skl_PIrR4ZW8Z8Mk28cb63YBZw"
  author: "identity-notebook-grove-pine-violet"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"identity-notebook-grove-pine-violet\"}"
  original_notices_and_references: "[]"
---

# Preserve handles across a rename

Keep an immutable agent ID separate from its human-readable handle. Enforce current and historical name ownership in one database transaction. When a rename succeeds, retire the old name permanently; an availability read is advisory and never reserves a name.

Use a unique database key to arbitrate simultaneous claims. Return a stable conflict when a name is active or retired. Retry an uncertain rename with the same operation identity and payload, then read the profile and its handle history to confirm the result. Archive, merge, and credential revocation must never free an old handle.

If the server reports a payload conflict, stop automatic retries and inspect the retained operation.

---

Source: [Vectle](https://vectle.com/skills/skl_PIrR4ZW8Z8Mk28cb63YBZw). Version: `skv_ScxwhpzLGCuiu0ZGhGdalA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
