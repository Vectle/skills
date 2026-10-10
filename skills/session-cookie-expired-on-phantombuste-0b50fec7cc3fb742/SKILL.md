---
name: "session-cookie-expired-on-phantombuste-0b50fec7cc3fb742"
description: "Guide Session cookie expired\" on PhantomBuster: re-auth the session via the browser extension: Make sure the PhantomBuster Chrome/Firefox extension is installed; it is how the tool grabs the cookie. Use this when you hit exactly this in Session. Not for different errors or different tools."
metadata:
  skill_id: "skl_PadZq-xYUDMW30ksTGTMcg"
  title: "Session cookie expired\" on PhantomBuster: re-auth the session via the browser extension"
  version: "skv_XMEZATGM-Jh7CDzRdSlKdg"
  updated: "2026-10-03T13:58:23.703661+00:00"
  canonical_url: "https://vectle.com/skills/skl_PadZq-xYUDMW30ksTGTMcg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: Make sure the PhantomBuster Chrome/Firefox extension is installed; it is how the tool grabs the cookie. PhantomBuster - Docs (PhantomBuster help center): the official fix for expired/invalid session cookie errors. ## The fix When a Phantom fails with "Session cookie expired" or login errors, do this: 1. In your browser, manually log out of the target site (LinkedIn, X, etc.) and log right back in.

## Fix
1. Make sure the PhantomBuster Chrome/Firefox extension is installed; it is how the tool grabs the cookie.
   Expected: this specific failure stops.
2. Re-run the Phantom.
   Expected: this specific failure stops.
3. If it keeps failing right after a fresh cookie, check for local interference: aggressive ad-blockers or privacy extensions can break PhantomBuster's page scripts (disable them one by one), and corporate VPNs/firewalls can route traffic through another country, tripping the site's security on a location mismatch with the cookie.
   Expected: this specific failure stops.

## Details
PhantomBuster - Docs (PhantomBuster help center): the official fix for expired/invalid session cookie errors. ## The fix When a Phantom fails with "Session cookie expired" or login errors, do this: 1. In your browser, manually log out of the target site (LinkedIn, X, etc.) and log right back in. 2. 3. On the Phantom's setup page, click the "Connect to..." button and let the extension capture the new active session cookie. 4. Thread: docs:phantombuster-session-cookie-fix

## When to use
You hit exactly this: Session cookie expired" on PhantomBuster: re-auth the session via the browser extension in Session.

## When not to use
A different error, or the same symptom in a different tool. This page only covers the failure above.

## Compatibility
Session.

---

Source: [Vectle](https://vectle.com/skills/skl_PadZq-xYUDMW30ksTGTMcg). Version: `skv_XMEZATGM-Jh7CDzRdSlKdg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
