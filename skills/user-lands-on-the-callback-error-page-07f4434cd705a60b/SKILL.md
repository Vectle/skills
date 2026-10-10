---
name: "user-lands-on-the-callback-error-page-07f4434cd705a60b"
description: "Symptom: the app redirects to /callback?error=... Cause is usually upstream of the app. Confirmation: the failed-login log event (type f) with the same timestamp. Fix follows the log's details.error. Not for different error messages."
metadata:
  skill_id: "skl_mpwFeVjuXew1sYT9sqKqUw"
  title: "User lands on the callback error page: read the tenant log type f event"
  version: "skv_f7cRIQqp0tJFWT2JdNX3LQ"
  updated: "2026-10-03T14:04:04.679536+00:00"
  canonical_url: "https://vectle.com/skills/skl_mpwFeVjuXew1sYT9sqKqUw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** Symptom: the app redirects to /callback?error=... Cause is usually upstream of the app. Confirm Dashboard > Monitoring > Logs. Filter by the user's email or type:f (failed login).

## The error

```text
?error=access_denied
```

## The fix

# Diagnose: callback error page

## Symptom

User completes login at Auth0, returns to your callback URL, and sees an error page or `?error=access_denied` / `?error=server_error` in the URL.

## Likely causes

1. An Action or Rule denied the login (api.access.deny).
2. Consent denied by the user.
3. Account blocked by attack protection.
4. Misconfigured connection or organization requirement.

## Confirm

Dashboard > Monitoring > Logs. Filter by the user's email or `type:f` (failed login). Match the timestamp to the failing attempt within a minute. Open the event: `details.error` gives the machine reason, `connection` and `client` name the actors, and `details` shows whether an extensibility point (Action/Rule) fired.

If there is NO failed-login event at the timestamp, Auth0 succeeded and the failure is in YOUR callback handler (code exchange, session write). Move debugging to the app.

## Fix

- Action denial: edit the Action's deny condition, redeploy, retest.
- Consent: handle gracefully; only fixable via skip-consent config for first-party apps.
- Blocked account: unblock via user management or the unblock email flow.

## Verify

Repeat the login with the same user and connection. Confirm a successful login event (type `s`) appears in the logs and the callback completes with a session. Watch one full cycle in an incognito window.

## When to use this

- You are seeing this exact error message; match the block above, not just part of it.
- The failing call matches the scenario in the title: User lands on the callback error page.
- You want the fastest verified fix before digging through logs.

## When not to use this

- Your error text differs from the block above; close cousins often have different causes.
- The stack trace points at a different component than the one in the title.
- You already applied this fix and the error persists; look for a second cause instead of reapplying.

## Compatibility

- Not pinned to a specific version; follows current User behavior.

## Also seen as

- `?error=server_error`
- `details.error`

---

Source: [Vectle](https://vectle.com/skills/skl_mpwFeVjuXew1sYT9sqKqUw). Version: `skv_f7cRIQqp0tJFWT2JdNX3LQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
