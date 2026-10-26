---
name: "invalid-state-after-social-login-cooki-08587c5896acee95"
description: "The state parameter protects the login flow from CSRF. Invalid state means the response did not match the request the SDK remembers, and the usual culprit is the SDK's cookie or storage being unavailable."
metadata:
  skill_id: "skl_edlujULSkTymwn64o8QY1Q"
  title: "Invalid state after social login: cookies blocked, clock skew, mismatched redirect"
  version: "skv_sqbWteyf9zEJbdKRuPW5UQ"
  updated: "2026-10-03T14:38:16.371526+00:00"
  canonical_url: "https://vectle.com/skills/skl_edlujULSkTymwn64o8QY1Q"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://auth0.com/docs/quickstart/spa/react\",\"https://auth0.com/docs/get-started/applications/application-settings\"]"
---

**TL;DR:** The state parameter protects the login flow from CSRF. Invalid state means the response did not match the request the SDK remembers, and the usual culprit is the SDK's cookie or storage being unavailable. The code exchange never happens. Fix with a custom domain (first-party cookies) or cacheLocation adjustments.

## The error

```text
text
Invalid state
```

## The fix

**TL;DR:** The state parameter protects the login flow from CSRF. Invalid state means the response did not match the request the SDK remembers, and the usual culprit is the SDK's cookie or storage being unavailable. The code exchange never happens. Fix with a custom domain (first-party cookies) or cacheLocation adjustments.

## The error

```text
Invalid state
```

# Invalid state after social login

## The error

After returning from Google/GitHub/etc, the app throws "Invalid state" (auth0-react) or the callback fails state validation. The code exchange never happens.

## Causes in order of likelihood

1. Third-party cookies blocked. The SDK stores the state/nonce/verifier in a cookie (or storage) before redirecting; on return it compares. Safari ITP, Brave shields, or Chrome third-party-cookie blocking deletes it between the two hops. Fix with a custom domain (first-party cookies) or `cacheLocation` adjustments.
2. Multiple tabs or double-click login. Two authorize calls overwrite each other's state; the first return then fails. Debounce the login button.
3. Redirect URI mismatch mid-flow: the authorize call used one redirect_uri and the callback handler another (e.g. www vs apex, or port drift). The SDK ties state to the request; mismatched handlers fail closed.
4. Clock skew on the server (regular web apps): the state cookie's expiry is time-based; a server clock minutes off invalidates it. Sync with NTP.
5. Custom `state` passed by your code that the SDK does not round-trip: let the SDK generate state; pass app state via a separate param or encode it yourself and restore after.

## Diagnose

- Repro in an incognito window with default cookie settings: if it works there but not in the user's browser, it is cookie blocking.
- Check devtools: the `auth0` transaction cookie present before redirect, gone after, means blocking.
- Tenant logs show a successful login (type `s`) with no code exchange: the failure is client-side, after Auth0 did its job.

## Checklist

- Custom domain for first-party cookies where possible.
- One authorize call per login attempt; SDK-generated state.

## When to use this

- You are seeing this exact error message; match the block above, not just part of it.
- The failing call matches the scenario in the title: Invalid state after social login.
- You want the fastest verified fix before digging through logs.

## When not to use this

- Your error text differs from the block above; close cousins often have different causes.
- The stack trace points at a different component than the one in the title.
- You already applied this fix and the error persists; look for a second cause instead of reapplying.

## Compatibility

- Not pinned to a specific version; follows current Invalid behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_edlujULSkTymwn64o8QY1Q). Version: `skv_sqbWteyf9zEJbdKRuPW5UQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
