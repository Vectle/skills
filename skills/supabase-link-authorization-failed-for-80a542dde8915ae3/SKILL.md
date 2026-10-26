---
name: "supabase-link-authorization-failed-for-80a542dde8915ae3"
description: "Fixes supabase link failing with LegacyLinkAuthTokenError: Authorization failed for the access token and project ref pair. Use when linking the CLI to a project fails even though you are logged in. Refreshes the access token with supabase login and re-links with the correct project ref. Not for database password errors or unlinked-project commands."
metadata:
  skill_id: "skl_6LsUB-HC-nJzlfJGHD8BwA"
  title: "supabase link: Authorization failed for the access token and project ref pair"
  version: "skv_PZ8jPmISwqRWg71H9aCjkw"
  updated: "2026-10-03T05:40:51.438915+00:00"
  canonical_url: "https://vectle.com/skills/skl_6LsUB-HC-nJzlfJGHD8BwA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/kwazema/claude-skills/blob/HEAD/skills/kw-login-supabase-cli/SKILL.md\"]"
---

# supabase link: Authorization failed for the access token and project ref pair

TL;DR: your CLI access token and the project ref you passed do not belong together — the token is stale/revoked, or the ref is for a different project or org than the token can see. Run `supabase login` again to mint a fresh token, copy the project ref from the dashboard URL of the project you actually want, and re-run `supabase link --project-ref [ref]`.

```text
LegacyLinkAuthTokenError: Authorization failed for the access token and project ref pair
```

## Steps

1. Run `supabase login` and complete the browser flow. Expected: login succeeds and a fresh access token is stored.

2. Open the project in the dashboard and copy the project ref from the URL — do not guess it from the project name.

3. Run `supabase link --project-ref [ref]` with that exact ref. Expected: linking succeeds and config.toml records the project.

4. Still failing: check that the logged-in account actually has access to the project (right org, not removed). Tokens cannot see projects they were never granted.

## When this applies

- the exact `Authorization failed for the access token and project ref pair` error on supabase link
- linking after the access token was revoked or the account changed teams
- a ref copied from a different project's dashboard URL

## When it doesn't

- database password failures — those happen after linking succeeds
- `Cannot find project ref` on other commands — the link never completed, fix that
- dashboard access issues in the browser itself

## Compatibility

Supabase CLI supabase login / supabase link; access tokens (sb_token) and project refs. Verified against the kw-login-supabase-cli community skill.

## Variant phrasings

- supabase link authorization failed access token project ref
- supabase LegacyLinkAuthTokenError fix
- supabase link invalid project ref

## Root cause

The CLI validates the token/project-ref pair against the Supabase API at link time. A token minted for account A, or a ref belonging to a project the token cannot access, fails the pair check even though each value looks fine on its own.

## Edge cases

- project refs are not secret but tokens are; never paste the token into the link command output you share
- switching between personal and org accounts needs a fresh `supabase login` each time
- old CLI versions produce less clear variants of this error; upgrade if the message differs

---

Source: [Vectle](https://vectle.com/skills/skl_6LsUB-HC-nJzlfJGHD8BwA). Version: `skv_PZ8jPmISwqRWg71H9aCjkw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
