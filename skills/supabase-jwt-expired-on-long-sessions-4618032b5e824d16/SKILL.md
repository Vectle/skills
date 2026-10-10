---
name: "supabase-jwt-expired-on-long-sessions-4618032b5e824d16"
description: "Shows how to fix supabase JWT expired on long sessions: refresh before you verify, not after you fail. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_-jFIL6_WSFVe6kCq0bEKgg"
  title: "Supabase JWT expired on long sessions: refresh before you verify, not after you fail"
  version: "skv_oJCCJbfkRWO5FjvhfiKmNA"
  updated: "2026-10-03T14:00:02.185445+00:00"
  canonical_url: "https://vectle.com/skills/skl_-jFIL6_WSFVe6kCq0bEKgg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Check the error message and the token's expiry claim. For long-lived background jobs, use a service-role client or re-authenticate; never stretch a user JWT past its design.

## Steps

1. Confirm the error is expiry, not invalidity. An expired token refreshes; a malformed or revoked one does not. Check the error message and the token's expiry claim.
2. Call `auth.refreshSession()` (or let the client's auto-refresh do it) and retry the failed request once. If it succeeds, the session was fine and only the token was stale.
3. Only treat the user as logged out when the refresh itself fails. Refresh-token rotation means an old refresh token is single-use; concurrent refreshes can race, so one retry of the refresh is reasonable before giving up.
4. In server code, do not cache the user object across the expiry boundary. Re-verify with `auth.getClaims()` per request so each request uses a fresh token state.
5. For long-lived background jobs, use a service-role client or re-authenticate; never stretch a user JWT past its design.

2. Simulate expiry: set a short token lifetime in a test project, wait it out, and confirm the app refreshes silently with no visible logout. Then revoke the session server-side and confirm the app now signs out cleanly.

## When to use

You are seeing this: Confirm the error is expiry, not invalidity. Use this skill when you run into "Supabase JWT expired on long sessions: refresh before you verify, not after you fail".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

Confirm the error is expiry, not invalidity.


---

Source: [Vectle](https://vectle.com/skills/skl_-jFIL6_WSFVe6kCq0bEKgg). Version: `skv_oJCCJbfkRWO5FjvhfiKmNA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
