---
name: "pre-launch-polish-fix-launch-strip-nav-2fd2196aad5fae47"
description: "PRE-LAUNCH POLISH: Fix launch strip/navbar overlap + restore Meta Partner trust: ## AGREE , root cause confirmed, implementing bounded fix ### Evidence **Stacking problem confirmed in source:** - `SiteAnnouncement` renders in normal document flow (`app/(marketing)/layout.tsx:39` Use when hitting this exact issue with PRE-LAUNCH POLISH. Not for unrelated errors."
metadata:
  skill_id: "skl_4xTIcvKmaQQ4fPJjALVyEg"
  title: "PRE-LAUNCH POLISH: Fix launch strip/navbar overlap + restore Meta Partner trust"
  version: "skv_OOnCxnUOXK2U-8Z-Eqsxcw"
  updated: "2026-10-03T14:10:48.848625+00:00"
  canonical_url: "https://vectle.com/skills/skl_4xTIcvKmaQQ4fPJjALVyEg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/cipherhq/waaiio/issues/469\"]"
---

## TL;DR

## AGREE , root cause confirmed, implementing bounded fix ### Evidence **Stacking problem confirmed in source:** - `SiteAnnouncement` renders in normal document flow (`app/(marketing)/layout.tsx:39`) - `Navbar` is `fixed left-0 right-0 top-0 z-40` (`Navbar.tsx:43`) - Both occupy `top-0` , navbar overlaps the announcement strip because `fixed` removes it from flow - "Get notified" button is hidden behind the navbar **Meta Partner asset confirmed:** - `public/meta-business-partner.svg` exists (15.8KB, last modified Apr 30) - Trust strip at `HomeClient.tsx:367-384` shows WhatsApp + Stripe + Paystack but missing Meta Partner ### Implementation plan **Fix 1: Launch strip / navbar stacking** - Make launch strip `fixed top-0 left-0 right-0 z-50` (above navbar z-40) - SiteAnnouncement measures its height via ref, sets `--announcement-h` CSS custom property on `document.documentElement` - Navbar offsets its `top` by `var(--announcement-h, 0px)` instead of hardcoded `top-0` - On dismiss: set `--announcement-h` to `0px` , navbar slides back to `top-0` - On unmount: cleanup CSS custom property **Fix 2: Restore Meta Partner trust element** - Add `[img src="/meta-business-partner.svg" alt="Meta Business Partner" /]` to trust strip - Keep visual balance with WhatsApp, Stripe, Paystack - Responsive on mobile **Preserved:** /launch suppression, modal session behavior, launch config autho

[cipherhq]: ## AGREE , root cause confirmed, implementing bounded fix ### Evidence **Stacking problem confirmed in source:** - `SiteAnnouncement` renders in normal document flow (`app/(marketing)/layout.tsx:39`) - `Navbar` is `fixed left-0 right-0 top-0 z-40` (`Navbar.tsx:43`) - Both occupy `top-0` , navbar overlaps the announcement strip because `fixed` removes it from flow - "Get notified" button is hidden behind the navbar **Meta Partner asset confirmed:** - `public/meta-business-partner.svg` exists (15.8KB, last modified Apr 30) - Trust strip at `HomeClient.tsx:367-384` shows WhatsApp + Stripe + Paystack but missing Meta Partner ### Implementation plan **Fix 1: Launch strip / navbar stacking** - Make launch strip `fixed top-0 left-0 right-0 z-50` (above navbar z-40) - SiteAnnouncement measures its height via ref, sets `--announcement-h` CSS custom property on `document.documentElement` - Navbar offsets its `top` by `var(--announcement-h, 0px)` instead of hardcoded `top-0` - On dismiss: set `--announcement-h` to `0px` , navbar slides back to `top-0` - On unmount: cleanup CSS custom property **Fix 2: Restore Meta Partner trust element** - Add `[img src="/meta-business-partner.svg" alt="Meta Business Partner" /]` to trust strip - Keep visual balance with WhatsApp, Stripe, Paystack - Responsive on mobile **Preserved:** /launch suppression, modal session behavior, launch config autho

Context: GitHub issue cipherhq/waaiio#469 (closed, 2 comments, reported 2026-09-29): ## Parent - #460 launch experience polish - #286 master tracker - Priority: launch polish / before production ## Owner-reported staging issues ### 1. Launch strip visibility / overlap Screenshot evidence from staging shows the top launch strip colliding visually with the fixed navbar. Observed: - Waaiio logo/nav sits on top of the launch strip; - launch text/countdown are compressed into the same vertical space; - yellow **Get notified** CTA is partially obscured / visually hidden; - dismiss control remains at far right. Root layout cause is visible in current structure: - `SiteAnnouncemen

## Matched source
Source: GitHub issue: https://github.com/cipherhq/waaiio/issues/469
Original query: "PRE-LAUNCH POLISH: Fix launch strip/navbar overlap + restore Meta Partner trust"
Key terms: launch, meta, navbar, overlap, partner, polish, restore, strip, trust

## When to use

- You hit this exact issue with PRE-LAUNCH POLISH.
- The symptom matches: Fix launch strip/navbar overlap + restore Meta Partner trust.

## When NOT to use

- A different error or symptom from PRE-LAUNCH POLISH; the cause here is specific to this one.

## Compatibility

Reported against PRE-LAUNCH POLISH.

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- If the fix does not help, capture the full error output and check the source link for updates.

## Source

GitHub issue: https://github.com/cipherhq/waaiio/issues/469

---

Source: [Vectle](https://vectle.com/skills/skl_4xTIcvKmaQQ4fPJjALVyEg). Version: `skv_OOnCxnUOXK2U-8Z-Eqsxcw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
