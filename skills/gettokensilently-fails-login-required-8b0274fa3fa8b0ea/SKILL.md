---
name: "gettokensilently-fails-login-required-8b0274fa3fa8b0ea"
description: "Silent token renewal fails with a named error telling you exactly what interaction is needed. Each maps to a different fix; retrying silently never works."
metadata:
  skill_id: "skl_i_1QyyBdaiyY--giInbsBA"
  title: "getTokenSilently fails: login_required, consent_required, interaction_required"
  version: "skv_KbLmyQQDFG3NwGeEaigxWg"
  updated: "2026-10-03T14:14:06.083553+00:00"
  canonical_url: "https://vectle.com/skills/skl_i_1QyyBdaiyY--giInbsBA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://auth0.com/docs/quickstart/spa/react\"]"
---

**TL;DR:** Silent token renewal fails with a named error telling you exactly what interaction is needed. Each maps to a different fix; retrying silently never works. Fix: interactive login. - consent_required: consent needed and cannot be skipped (third-party, YOUR_HOST, new audience). Fix: interactive login with consent. - interaction_required: something needs the user (MFA, Rules/Action redirect, password change required).

## The error

```text
text
missing_refresh_token
```

## The fix

**TL;DR:** Silent token renewal fails with a named error telling you exactly what interaction is needed. Each maps to a different fix; retrying silently never works. Fix: interactive login. - consent_required: consent needed and cannot be skipped (third-party, YOUR_HOST, new audience). Fix: interactive login with consent. - interaction_required: something needs the user (MFA, Rules/Action redirect, password change required).

## The error

```text
missing_refresh_token
```

## The fix

# Silent auth failures

## The errors (from getTokenSilently / checkSession)

- `login_required`: no Auth0 session (logged out, session expired, or cookie blocked). Fix: interactive login.
- `consent_required`: consent needed and cannot be skipped (third-party, YOUR_HOST, new audience). Fix: interactive login with consent.
- `interaction_required`: something needs the user (MFA, Rules/Action redirect, password change required). Fix: interactive login.

## Pattern

```
try {
  tok = await getAccessTokenSilently();
} catch (e) {
  if (["login_required","consent_required","interaction_required","missing_refresh_token"].includes(e.error)) {
    await loginWithRedirect({ authorizationParams: { audience: "[your api]" } });
  } else { throw e; }
}
```

Never loop getTokenSilently on these errors; each attempt fails identically and burns rate limit.

## Cookie angle

Silent auth uses a hidden iframe + the Auth0 session cookie. Blocked third-party cookies produce `login_required` even when the user HAS a session. Custom domains fix it (first-party cookie). Rotating refresh tokens are the other fix: with `useRefreshTokens`, the SDK renews without the iframe at all.

## missing_refresh_token

The SDK has no refresh token to use: offline_access was not requested, rotation is off, or storage was cleared. Fix the login call, then re-login.

## Checklist

- Every silent-auth error has an interactive fallback.
- No retry loops on interaction errors.

## When to use this

- You are seeing this exact error message; match the block above, not just part of it.
- The failing call matches the scenario in the title: getTokenSilently fails.
- You want the fastest verified fix before digging through logs.

## When not to use this

- Your error text differs from the block above; close cousins often have different causes.
- The stack trace points at a different component than the one in the title.
- You already applied this fix and the error persists; look for a second cause instead of reapplying.

## Compatibility

- Not pinned to a specific version; follows current getTokenSilently behavior.

## Also seen as

- `## The fix

# Silent auth failures

## The errors (from getTokenSilently / checkSession)

-`
- `: consent needed and cannot be skipped (third-party, YOUR_HOST, new audience). Fix: interactive login with consent.
-`

---

Source: [Vectle](https://vectle.com/skills/skl_i_1QyyBdaiyY--giInbsBA). Version: `skv_KbLmyQQDFG3NwGeEaigxWg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
