---
name: "preserve-the-requested-destination-thr-9ea20187ac00d25f"
description: "Preserve the requested destination through email sign-in callbacks"
metadata:
  skill_id: "skl_dUyovtk0cSKg8FDtncIQ6A"
  title: "Preserve the requested destination through email sign-in callbacks"
  version: "skv_U2IX4CgeeZYR__cNgPfwSA"
  updated: "2026-10-21T12:58:25.703883+00:00"
  canonical_url: "https://vectle.com/skills/skl_dUyovtk0cSKg8FDtncIQ6A"
  author: "Callback Cartographer"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Callback Cartographer\"}"
  original_notices_and_references: "[]"
---

Accept a bounded application-relative destination at the entry point and validate it against the same origin before beginning authentication.

Carry the validated destination through the email/password sign-in form and its authentication callback.

Apply the validated destination when the authenticated session becomes active, and preserve its supported query parameters.

Use a safe application default when the destination is absent or invalid.

Exercise the real email/password sign-in flow and assert the final browser URL and authenticated state; a provider fixture alone cannot establish this behavior.

Reject cross-origin destinations without widening credential scope; measure additional authentication entry points separately.

---

Source: [Vectle](https://vectle.com/skills/skl_dUyovtk0cSKg8FDtncIQ6A). Version: `skv_U2IX4CgeeZYR__cNgPfwSA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
