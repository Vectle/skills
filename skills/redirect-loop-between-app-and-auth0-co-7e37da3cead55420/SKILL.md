---
name: "redirect-loop-between-app-and-auth0-co-7e37da3cead55420"
description: "Symptom: browser bounces between the app and Auth0 until it errors. Cause: the app never establishes its session, or an Action/Rule bounces the user back. Confirmation: count the hops and check whether any /callback ever completes."
metadata:
  skill_id: "skl_JoKRDtY8XPFS7R_xdnRnyw"
  title: "Redirect loop between app and Auth0: cookies, rules/actions, default login route"
  version: "skv_4Gp6oOCysyVuCKubcgcWOw"
  updated: "2026-10-03T13:56:07.002163+00:00"
  canonical_url: "https://vectle.com/skills/skl_JoKRDtY8XPFS7R_xdnRnyw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://auth0.com/docs/customize/actions/triggers/post-login\"]"
---

**TL;DR:** Symptom: browser bounces between the app and Auth0 until it errors. Cause: the app never establishes its session, or an Action/Rule bounces the user back. Session cookie not sticking: the app sets its session cookie on /callback but the browser rejects it (Secure flag on http, SameSite, or the AUTH0_SECRET rotating per deploy so the cookie never decrypts). Confirm - DevTools network tab: count the hops.

# Diagnose: redirect loop

## Symptom

Infinite or long redirect chain: app -> Auth0 -> app -> Auth0, ending in ERR_TOO_MANY_REDIRECTS.

## Likely causes

1. Session cookie not sticking: the app sets its session cookie on /callback but the browser rejects it (Secure flag on http, SameSite, or the AUTH0_SECRET rotating per deploy so the cookie never decrypts).
2. Auth guard misconfigured: the app's "requires auth" check runs on the callback route itself, so the freshly authenticated user is bounced back to login.
3. An Action/Rule redirects (`api.redirect.sendUserTo`) without a resume path, or denies then the app retries login.
4. Default login route misconfigured: Auth0's "configure default login routes" sends unauthenticated users to the app login, which sends them back.

## Confirm

- DevTools network tab: count the hops. If /callback returns 302 back to /authorize every time, the app session is not sticking: check the Set-Cookie response and whether the browser stores it.
- If the loop includes an Action redirect URL, the Action is the bouncer: check Actions > Flows and the tenant logs for the redirect event.
- Tenant logs: a successful login (s) followed immediately by another authorize with no token use means the app discarded the session.

## Fix

- Cookie: https in production, stable AUTH0_SECRET/SECRET, correct cookie domain.
- Exclude the callback route from the auth guard.
- Action redirects must call api.redirect with a resume and handle the resume callback; or remove the redirect.

## Verify

One clean login in incognito: authorize -> callback -> app page, three hops, session cookie present, no further redirects on refresh.

## When to use this

- This covers exactly what the title says: Redirect loop between app and Auth0.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Redirect; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current Redirect behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_JoKRDtY8XPFS7R_xdnRnyw). Version: `skv_4Gp6oOCysyVuCKubcgcWOw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
