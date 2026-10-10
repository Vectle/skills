---
name: "kotlin-android-supabase-intent-filter-fb520a56685623f6"
description: "Supabase auth on Android: the browser handoff works but the user never returns to the app. Covers the intent filter in AndroidManifest.xml, the handler activity, the dashboard redirect URL, and the internet permission. Not for iOS or web auth flows."
metadata:
  skill_id: "skl_p9tAok3doGpk1Sl8TlSeKA"
  title: "Kotlin Android + Supabase: intent-filter deep links for OAuth and magic-link return"
  version: "skv_H4B1Hc3Hi0F8nvOeYE8gTA"
  updated: "2026-10-03T05:04:56.512969+00:00"
  canonical_url: "https://vectle.com/skills/skl_p9tAok3doGpk1Sl8TlSeKA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: The Supabase Android quickstart works up to the moment the user taps sign in, then the browser opens, auth succeeds, and nothing brings the user back, because the manifest has no intent filter for your scheme. Pick a scheme and host for auth callbacks, add the full redirect URL to the dashboard Redirect URLs, add an intent filter to AndroidManifest.xml on your auth handler activity (action.VIEW, category.BROWSABLE, data element matching scheme and host), and create the handler activity: it receives the deep link intent, hands the URL to the Supabase client to create the session, then navigates into the app.

What it looks like:

```text
Symptom: OAuth succeeds in the browser, but the app never reopens. Or the
browser shows "page not found" or just stays open.
```

Steps:

1. Pick a scheme and host for auth callbacks and add the full redirect URL to the dashboard Redirect URLs. Success: the URL is registered.
2. Add the intent filter to AndroidManifest.xml on the auth handler activity with action.VIEW, category.BROWSABLE, and a data element matching your scheme and host. Success: the filter matches the registered URL.
3. Create the handler activity the docs describe: it receives the deep link intent, hands the URL to the Supabase client to create the session, then navigates into the app. Success: the session is created from the link.
4. Add the internet permission to the manifest. Release builds without it fail with network errors that look like Supabase outages. Success: the permission is present.
5. Keep the publishable key in the app and the service role key out of it. The APK can be decompiled; anything in it is public. Success: no service role key in the app.

When to use: Supabase OAuth or magic-link auth on Android where the browser handoff loses the user.

When not to use: iOS or web auth flows (different mechanisms), or auth failures inside the browser (different problem).

Compatibility: Supabase Android client, Kotlin, AndroidManifest.xml.

Variants:
- supabase android oauth deep link not returning
- supabase androidmanifest intent filter auth
- supabase magic link android app not opening

Root cause: the missing intent filter. Android has no way to route the callback URL back to your app without it, so the browser just sits there after a successful auth.

Edge cases:
- Quick test: on a real device, start OAuth, complete it in the browser, and confirm the app reopens signed in. If the browser shows "page not found" or stays open, the intent filter or dashboard redirect URL is mismatched.
- Scheme collisions with other apps cause the disambiguation dialog. Pick a distinctive scheme.

---

Source: [Vectle](https://vectle.com/skills/skl_p9tAok3doGpk1Sl8TlSeKA). Version: `skv_H4B1Hc3Hi0F8nvOeYE8gTA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
