---
name: "access-denied-on-the-callback-url-cons-53c2292e4122f77e"
description: "When the callback URL shows ?error=access_denied, the login was refused after authentication. The description parameter names the cause; tenant logs confirm it. Not for different error messages."
metadata:
  skill_id: "skl_hWsSBhyRHUc5rg2jtEUEcQ"
  title: "access_denied on the callback URL: consent, email domains, and connection denials"
  version: "skv_-nTHjbQIVsrVLs-hJoKT5g"
  updated: "2026-10-03T15:22:52.163381+00:00"
  canonical_url: "https://vectle.com/skills/skl_hWsSBhyRHUc5rg2jtEUEcQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://auth0.com/docs/deploy-monitor/logs\",\"https://auth0.com/docs/customize/actions/triggers/post-login\"]"
---

**TL;DR:** When the callback URL shows ?error=access_denied, the login was refused after authentication. The description parameter names the cause; tenant logs confirm it. Read the description first - "User did not consent" or consent prompt denied: the user clicked Deny on the consent screen. Confirm in tenant logs Dashboard > Monitoring > Logs.

## The error

```text
?error=access_denied&error_description=...
```

# access_denied on callback

## The error

The browser lands on your callback URL with `?error=access_denied&error_description=...`. The user authenticated fine; something refused to issue the authorization.

## Read the description first

- "User did not consent" or consent prompt denied: the user clicked Deny on the consent screen. Third-party apps always show consent; first-party apps show it when the API's "Allow Skipping User Consent" is off or YOUR_HOST is involved.
- Email domain or signup policy: an Action or Rule denied the login (e.g. `api.access.deny("end_users_not_allowed")`). The description often carries the custom message.
- Connection-level denial: enterprise connections can deny based on IdP claims.

## Confirm in tenant logs

Dashboard > Monitoring > Logs. Filter `type:f` (failed login) around the timestamp. The log entry's `details.error` repeats the description and names the connection and client. If a Rule/Action denied it, the log shows the extensibility point.

## Fix by cause

- Consent denied by the user: nothing to fix; handle the error in your callback route with a friendly page, not a stack trace.
- Consent showing when it should not: Dashboard > Applications > APIs > your API > enable "Allow Skipping User Consent" for first-party apps. Note consent cannot be skipped for YOUR_HOST or third-party clients.
- Action/Rule denial: read the deny reason, adjust the policy (domain allowlist, role check) in the Action, redeploy, and re-test.
- Wrong connection: the app may be offering a database connection to users who should use SSO. Limit the app's enabled connections or pass the `connection` parameter.

## Checklist

- Callback route handles error params gracefully.
- The deny reason is identified in logs before changing policy.

## When to use this

- You are seeing this exact error message; match the block above, not just part of it.
- The failing call matches the scenario in the title: access_denied on the callback URL.
- You want the fastest verified fix before digging through logs.

## When not to use this

- Your error text differs from the block above; close cousins often have different causes.
- The stack trace points at a different component than the one in the title.
- You already applied this fix and the error persists; look for a second cause instead of reapplying.

## Compatibility

- Not pinned to a specific version; follows current access_denied behavior.

## Also seen as

- `details.error`

---

Source: [Vectle](https://vectle.com/skills/skl_hWsSBhyRHUc5rg2jtEUEcQ). Version: `skv_-nTHjbQIVsrVLs-hJoKT5g`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
