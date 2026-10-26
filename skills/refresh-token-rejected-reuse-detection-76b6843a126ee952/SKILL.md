---
name: "refresh-token-rejected-reuse-detection-76b6843a126ee952"
description: "A rejected refresh token is Auth0 telling you the grant is dead. Retrying the same token is useless; the correct response is a fresh login. Not for different error messages."
metadata:
  skill_id: "skl_MBDci4scpNOwZ6eN8LXPcg"
  title: "Refresh token rejected: reuse detection, absolute lifetime, revoked grants"
  version: "skv_YPEecpE0DZBi8KNKZTs7Zw"
  updated: "2026-10-03T14:40:52.217549+00:00"
  canonical_url: "https://vectle.com/skills/skl_MBDci4scpNOwZ6eN8LXPcg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://auth0.com/docs/secure/tokens/refresh-tokens/refresh-token-rotation\"]"
---

**TL;DR:** A rejected refresh token is Auth0 telling you the grant is dead. Retrying the same token is useless; the correct response is a fresh login. Grant revoked: user changed password, admin revoked via Management API, or the user logged out everywhere. A mutex is cheaper than debugging reuse false positives. - On invalid_grant, never retry with the same token.

## The error

```text
text
invalid_grant
```

## The fix

**TL;DR:** A rejected refresh token is Auth0 telling you the grant is dead. Retrying the same token is useless; the correct response is a fresh login. Grant revoked: user changed password, admin revoked via Management API, or the user logged out everywhere. A mutex is cheaper than debugging reuse false positives. - On invalid_grant, never retry with the same token.

## The error

```text
invalid_grant
```

# Refresh token rejected

## The error

`/oauth/token` with `grant_type=refresh_token` returns `invalid_grant`. Descriptions vary: "Invalid refresh token", "refresh token already used", or the grant was revoked.

## Causes

1. Reuse detection fired. With rotation on, using an old refresh token revokes the entire grant. Common trigger: two tabs refreshing concurrently, or a persisted old token being replayed after a network retry. The reuse leeway setting covers small races, not replays.
2. Absolute lifetime expired. The chain has a hard cap from first issuance; after that every refresh fails. This is working as configured.
3. Inactivity lifetime expired. Idle too long, grant gone.
4. Grant revoked: user changed password, admin revoked via Management API, or the user logged out everywhere.
5. Wrong audience or client: refresh tokens are bound to the client and audience they were issued for.

## Correct handling

```
try:
    pair = refresh(old_refresh_token)
    persist(pair.refresh_token)   # BEFORE using it
except invalid_grant:
    clear_stored_tokens()
    redirect_to_login()           # fresh authorize, do not retry
```

- Persist the NEW refresh token before the first use. Crash between use and persist strands the session.
- Serialize refreshes across tabs (leader election or a shared lock). A mutex is cheaper than debugging reuse false positives.
- On invalid_grant, never retry with the same token. Go to login.

## Checklist

- Refresh calls are single-flight.
- invalid_grant always routes to fresh login, never a retry loop.

## When to use this

- You are seeing this exact error message; match the block above, not just part of it.
- The failing call matches the scenario in the title: Refresh token rejected.
- You want the fastest verified fix before digging through logs.

## When not to use this

- Your error text differs from the block above; close cousins often have different causes.
- The stack trace points at a different component than the one in the title.
- You already applied this fix and the error persists; look for a second cause instead of reapplying.

## Compatibility

- Not pinned to a specific version; follows current Refresh behavior.

## Also seen as

- `# Refresh token rejected

## The error`

---

Source: [Vectle](https://vectle.com/skills/skl_MBDci4scpNOwZ6eN8LXPcg). Version: `skv_YPEecpE0DZBi8KNKZTs7Zw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
