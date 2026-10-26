---
name: "no-expansion-has-been-registered-for-m-feb7293338a07288"
description: "Fixes the 'no expansion has been registered for module' panic in OpenTofu v1.12.0-beta1 by upgrading to v1.12.0-rc1 or the final v1.12.0. It was a regression in the beta line and was reverted. Use when the panic hits on the beta. Not for other OpenTofu panics."
metadata:
  skill_id: "skl_1vVkWoAoQGNddpGvTovOJg"
  title: "\"no expansion has been registered for module\" panic in v1.12.0-beta1"
  version: "skv_c5SU8CEyUub4aYU4vmUFvw"
  updated: "2026-10-03T05:36:42.206133+00:00"
  canonical_url: "https://vectle.com/skills/skl_1vVkWoAoQGNddpGvTovOJg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/opentofu/opentofu/issues/4019\"]"
---

Fix first: upgrade to v1.12.0-rc1 or the final v1.12.0. This was a regression in the v1.12.0 beta line; it was reverted and the fix is included in v1.12.0-rc1 and later.

```text
no expansion has been registered for module (panic)
```

1. Upgrade OpenTofu to v1.12.0-rc1 or newer.
2. Re-run. Expected: no panic.

When to use: the 'no expansion has been registered for module' panic on v1.12.0-beta1.

When not to use: other OpenTofu panics (different causes).

Compatibility: OpenTofu v1.12.0-beta1 (broken), v1.12.0-rc1+ (fixed). Reported in opentofu/opentofu#4019.

Variants:
- "opentofu no expansion has been registered for module"
- "opentofu 1.12 beta panic"
- "opentofu module expansion panic"

Root cause: a beta-line regression, reverted upstream.

Edge cases: do not stay on the affected beta; there is no workaround worth using when the fixed release exists.

---

Source: [Vectle](https://vectle.com/skills/skl_1vVkWoAoQGNddpGvTovOJg). Version: `skv_c5SU8CEyUub4aYU4vmUFvw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
