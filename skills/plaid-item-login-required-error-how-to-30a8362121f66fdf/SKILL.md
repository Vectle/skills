---
name: "plaid-item-login-required-error-how-to-30a8362121f66fdf"
description: "plaid item_login_required error how to fix link update mode fails"
metadata:
  skill_id: "skl_FB7geIdNmfZMXS6KAnZo0w"
  title: "plaid item_login_required error how to fix link update mode fails"
  version: "skv_y3m9A9XTdZRqp3seKm3a3g"
  updated: "2026-11-15T01:53:23.562856+00:00"
  canonical_url: "https://vectle.com/skills/skl_FB7geIdNmfZMXS6KAnZo0w"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Confirm the item error from the item get response or the ITEM ERROR webhook and record the item identifier and institution.

Stop retrying data sync for that item until relink completes, and mark the item as needs relink in your own state.

Create a link token for update mode using the access credential tied to that same item, not a fresh Link flow.

Present Link to the account owner and have them re-enter credentials and complete any MFA challenge at their institution.

Exchange nothing new in update mode and do not rotate the item access credential unless Plaid returns a new one for this flow in your integration.

Resume sync for the item and request a small transactions or auth pull to confirm data flows again.

Watch for the follow up webhook indicating the item error is resolved, and clear the needs relink flag only after a successful pull.

---

Source: [Vectle](https://vectle.com/skills/skl_FB7geIdNmfZMXS6KAnZo0w). Version: `skv_y3m9A9XTdZRqp3seKm3a3g`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
