---
name: "can-parallel-search-include-or-exclude-1ebb36edc55b4ff9"
description: "can parallel search include or exclude specific domains from results? error policy ignored fails"
metadata:
  skill_id: "skl_AcZtRFnOJ25JlUk6fiZFVg"
  title: "can parallel search include or exclude specific domains from results? error policy ignored fails"
  version: "skv_9HpTnxFkNZjTl89lwPc7Hw"
  updated: "2026-11-15T13:54:27.233182+00:00"
  canonical_url: "https://vectle.com/skills/skl_AcZtRFnOJ25JlUk6fiZFVg"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Reproduce with one query and one clearly excluded domain that currently appears in results, and save that result set.

Check whether the policy was set in a dashboard or profile while the API request sends no domain fields. Most APIs do not inherit dashboard rules.

Add the include or exclude domain lists to every search request, using the exact field names for the API version in use.

Confirm the search mode or depth in use supports domain filtering; some fast or cached modes skip it.

Use bare domains without scheme or path, for example example.com rather than a full page address, unless the docs require otherwise.

Re-run the reproduction query and check whether the excluded domain is gone and included domains are eligible.

Add a client-side post-filter that drops results outside the policy as a safety net, and log any drops so silent policy failures stay visible.

---

Source: [Vectle](https://vectle.com/skills/skl_AcZtRFnOJ25JlUk6fiZFVg). Version: `skv_9HpTnxFkNZjTl89lwPc7Hw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
