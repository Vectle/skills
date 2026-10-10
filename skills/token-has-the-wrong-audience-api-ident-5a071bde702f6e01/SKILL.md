---
name: "token-has-the-wrong-audience-api-ident-5a071bde702f6e01"
description: "An access token minted for one audience is rejected by another API. The usual mixup: the SPA requested the Management API audience (or none) and sent the token to your API. Not for different error messages."
metadata:
  skill_id: "skl_vuuYMRZr_l2vjy1lgI1l3w"
  title: "Token has the wrong audience: API identifier vs Management API audience"
  version: "skv_9LEWWLSSeBr86kXj19lcYg"
  updated: "2026-10-03T14:09:09.114001+00:00"
  canonical_url: "https://vectle.com/skills/skl_vuuYMRZr_l2vjy1lgI1l3w"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** An access token minted for one audience is rejected by another API. The usual mixup: the SPA requested the Management API audience (or none) and sent the token to your API. Validate aud in the API middleware (express-oauth2-jwt-bearer does this from the audience option). If the app needs both your API and the Management API, it needs two tokens (two audience requests), and the Management API audience should only ever be requested by trusted backend code, never the SPA directly.

# Wrong audience

## The error

Your API returns 401, and decoding the token shows `aud` is not your API identifier. Common values seen: the Management API audience (`YOUR_HOST/api/v2/`), or an opaque token (no aud at all, just a random string).

## Why

- No audience requested: Auth0 returns an opaque token usable only against /userinfo. Your API cannot validate it.
- Wrong audience requested: the app asked for the Management API audience (often copied from a quickstart) and sends that token to your API. Audiences are not interchangeable.
- Multiple APIs: the app calls API A with a token minted for API B. One token, one audience (plus the /userinfo sidecar).

## Fix

1. At login / token request, set `audience` to YOUR API's identifier, exactly as registered under Applications > APIs.
2. Validate `aud` in the API middleware (express-oauth2-jwt-bearer does this from the `audience` option).
3. If the app needs both your API and the Management API, it needs two tokens (two audience requests), and the Management API audience should only ever be requested by trusted backend code, never the SPA directly.

## The node-auth0 variant

Calling the Management API from Node requires the Management API audience AND the right scopes (`read:users` etc). "Bad audience" there means the token was minted for your custom API. Separate token, separate audience.

## Checklist

- aud in the decoded token equals the API identifier, character for character.
- Management API tokens never minted for or sent by the frontend.

## When to use this

- You are seeing this exact error message; match the block above, not just part of it.
- The failing call matches the scenario in the title: Token has the wrong audience.
- You want the fastest verified fix before digging through logs.

## When not to use this

- Your error text differs from the block above; close cousins often have different causes.
- The stack trace points at a different component than the one in the title.
- You already applied this fix and the error persists; look for a second cause instead of reapplying.

## Compatibility

- Not pinned to a specific version; follows current Token behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_vuuYMRZr_l2vjy1lgI1l3w). Version: `skv_9LEWWLSSeBr86kXj19lcYg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
