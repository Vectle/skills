---
name: "phase-3-staging-e2e-test-matrix-stagin-774038ef0ee8ae68"
description: "Phase 3: Staging E2E test matrix , staging.waaiio.com + WhatsApp +1 240-471-2139: ## B1 Meta webhook blocker , ROOT CAUSE CONFIRMED AND FIXED (2026-09-25) Independent verification performed through Meta's official WhatsApp Business Tools MCP. Use when hitting this exact issue with Phase 3. Not for unrelated errors."
metadata:
  skill_id: "skl_HoSRrpBH70oa0XnHvGw0oQ"
  title: "Phase 3: Staging E2E test matrix , staging.waaiio.com + WhatsApp +1 240-471-2139"
  version: "skv_LweAF5EfHMgSbYCaMWcfxw"
  updated: "2026-10-03T14:13:34.367641+00:00"
  canonical_url: "https://vectle.com/skills/skl_HoSRrpBH70oa0XnHvGw0oQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

## B1 Meta webhook blocker , ROOT CAUSE CONFIRMED AND FIXED (2026-09-25) Independent verification performed through Meta's official WhatsApp Business Tools MCP. ### Root cause The **waaiio-staging** WhatsApp Business Account was **not subscribed** to the **Waaiio Staging app (1722212455524293)**. The app-level callback URL existed and the app was published, but without the account-level subscription Meta did not route real inbound events to the staging app. ### Fix applied Subscribed account **waaiio-staging (26396269840042214)** to **Waaiio Staging (1722212455524293)**. ### Post-fix Meta verification For staging number **+1 240-471-2139**: - Correct Phone Number ID: `1347202708469075` - Number: registered / linked - App callback: configured - Subscribed field: `messages` - Account subscription to Waaiio Staging: DONE - Waaiio Staging app: published/live Important ID correction: `1073724449163537` is **not** +1 240-471-2139; Meta reports it belongs to **+1 202-922-6251 (Waaiio USA)**. ### Runtime proof Owner sent a **fresh inbound `Hi`** to +1 240-471-2139 after the subscription was applied and **received a Waaiio response**. This is separate from th

[cipherhq]: ## B1 Meta webhook blocker , ROOT CAUSE CONFIRMED AND FIXED (2026-09-25) Independent verification performed through Meta's official WhatsApp Business Tools MCP. ### Root cause The **waaiio-staging** WhatsApp Business Account was **not subscribed** to the **Waaiio Staging app (1722212455524293)**. The app-level callback URL existed and the app was published, but without the account-level subscription Meta did not route real inbound events to the staging app. ### Fix applied Subscribed account **waaiio-staging (26396269840042214)** to **Waaiio Staging (1722212455524293)**. ### Post-fix Meta verification For staging number **+1 240-471-2139**: - Correct Phone Number ID: `1347202708469075` - Number: registered / linked - App callback: configured - Subscribed field: `messages` - Account subscription to Waaiio Staging: DONE - Waaiio Staging app: published/live Important ID correction: `1073724449163537` is **not** +1 240-471-2139; Meta reports it belongs to **+1 202-922-6251 (Waaiio USA)**. ### Runtime proof Owner sent a **fresh inbound `Hi`** to +1 240-471-2139 after the subscription was applied and **received a Waaiio response**. This confirms the real inbound/outbound staging path is functioning after the Meta subscription fix. ### Remaining Meta item Meta's onboarding checklist currently reports a payment-method TODO for billable outbound messages. This is separate from th

Context: GitHub issue cipherhq/waaiio#401 (open, 40 comments, reported 2026-09-25): ## Phase 3: Corrected Staging E2E Test Matrix (v2) **CTO corrections incorporated.** Saved-card semantics, reservation policy, regression tests, Paystack requirement, fixture audit, and production-isolation placement all corrected. **Staging:** `https://staging.waaiio.com` | WhatsApp: `+1 240-471-2139` | Supabase: `tqjvrzopvtczxfxiwmnz` **Admin:** `https://admin-staging.waaiio.com` **Test user:** `[recipient email]` / `Test1234!` **Admin user:** `[recipient email]` / `AdminTest1234!` (role=admin) **Status:** PLAN ONLY , no tests executed --- ## STAGING FIXTURE AUDI

## Matched source
Source: GitHub issue: https://github.com/cipherhq/waaiio/issues/401
Original query: "Phase 3: Staging E2E test matrix , staging.waaiio.com + WhatsApp +1 240-471-2139"
Key terms: 2139, matrix, phase, staging, test, waaiio, whatsapp

## When to use

- You hit this exact issue with Phase 3.
- The symptom matches: Staging E2E test matrix , staging.waaiio.com + WhatsApp +1 240-471-2139.

## When NOT to use

- A different error or symptom from Phase 3; the cause here is specific to this one.

## Compatibility

Reported against Phase 3.

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- If the fix does not help, capture the full error output and check the source link for updates.

## Source

GitHub issue: https://github.com/cipherhq/waaiio/issues/401

---

Source: [Vectle](https://vectle.com/skills/skl_HoSRrpBH70oa0XnHvGw0oQ). Version: `skv_LweAF5EfHMgSbYCaMWcfxw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
