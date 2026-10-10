---
name: "tokens-expire-too-fast-or-sessions-too-59b4281151e1c433"
description: "Symptom: users logged out after minutes, or tokens valid for days against policy. Cause: confusing the four lifetimes (id token, access token, refresh absolute, refresh inactivity, SSO session). Confirmation: decode the token exp and compare with each setting. Not the full reference manual."
metadata:
  skill_id: "skl_3U7f9R9eDPzhFW4VEdP3PA"
  title: "Tokens expire too fast or sessions too long: token lifetime vs session layers"
  version: "skv_JadHGS_5yiV3eVm7_fP3GQ"
  updated: "2026-10-03T13:44:49.604183+00:00"
  canonical_url: "https://vectle.com/skills/skl_3U7f9R9eDPzhFW4VEdP3PA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** Symptom: users logged out after minutes, or tokens valid for days against policy. Cause: confusing the four lifetimes (id token, access token, refresh absolute, refresh inactivity, SSO session). Confirm Decode the access token - exp - iat = the access token lifetime in force. Compare with the API setting.

# Diagnose: token/session lifetime confusion

## Symptom

Users complain about frequent logouts, or security review flags tokens living too long.

## The four lifetimes

1. Access token lifetime: API settings (default 24h for custom APIs, shorter for Management API). `exp` in the token.
2. ID token lifetime: application settings.
3. Refresh token -  absolute lifetime (hard cap from first issuance) and inactivity lifetime (idle expiry). Application > Refresh Token settings.
4. SSO session: tenant session layers (idle timeout, absolute timeout) under Dashboard > Settings > Advanced or Session Management.

## Confirm

Decode the access token -  `exp - iat` = the access token lifetime in force. Compare with the API setting. For sessions, check the tenant session settings and the application's refresh token settings side by side; the SHORTEST applicable lifetime wins the user's experience.

Tenant logs show token issuance; the absence of refresh events after the inactivity window confirms idle expiry is the limiter.

## Fix

- Frequent logouts with a good refresh setup: the inactivity lifetime is too short, or the app is not using the refresh token (relying on the access token alone).
- Too-long sessions: tighten absolute lifetime first (the backstop), then inactivity.
- Never "fix" short sessions by minting 30-day access tokens. Use refresh rotation; access tokens stay short.

## Verify

Set a test user, wait out (or simulate) each boundary, and confirm the behavior matches the intended layer. Document the four numbers in the runbook.

## When to use this

- This covers exactly what the title says: Tokens expire too fast or sessions too long.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Tokens; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current Tokens behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_3U7f9R9eDPzhFW4VEdP3PA). Version: `skv_JadHGS_5yiV3eVm7_fP3GQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
