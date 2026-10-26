---
name: "my-account-edit-address-endpoint-text-f5fa6c44eb81e530"
description: "Fixes the 'Addresses' text missing from the WooCommerce My Account edit-address endpoint in some languages (a translation/plural-form bug) via the filter function from the thread, a manual PO-file plural fix, or a Loco Translate check. Use when the label is missing in a non-English locale. Not for missing endpoints, or for English installs."
metadata:
  skill_id: "skl_veoUb6lFZi-99qLBwlr04Q"
  title: "My Account edit-address endpoint text is missing \"Addresses\"."
  version: "skv_fPw0BECX5xfhn5eg30bGMQ"
  updated: "2026-10-03T04:46:47.044502+00:00"
  canonical_url: "https://vectle.com/skills/skl_veoUb6lFZi-99qLBwlr04Q"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/woocommerce/woocommerce/issues/36490\"]"
---

The 'Addresses' label missing from the My Account edit-address endpoint in some languages is a translation/plural-form bug in WooCommerce, not a settings problem. Community-confirmed workarounds:

1. Check Loco Translate first to see whether the translation exists but isnt rendering.
2. Add the filter function shared in the thread to your theme's functions.php to force the label. Expected: the 'Addresses' text shows up.
3. Or download the PO file and fix the plural form manually. Several users confirmed this. Expected: the label renders in your language.

When to use: the edit-address endpoint label is missing in a non-English locale.

When not to use: the endpoint itself is missing, or your install is English (then something else is wrong).

Compatibility: WooCommerce. Reported in woocommerce/woocommerce#36490 (98 comments).

Variants:
- "woocommerce edit-address addresses text missing"
- "woocommerce my account addresses translation missing"
- "woocommerce addresses plural form bug"

Root cause: a plural-form bug in the translation files for affected languages.

Edge cases: put the filter in a child theme's functions.php so a theme update doesnt wipe it.

---

Source: [Vectle](https://vectle.com/skills/skl_veoUb6lFZi-99qLBwlr04Q). Version: `skv_fPw0BECX5xfhn5eg30bGMQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
