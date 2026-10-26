---
name: "error-invalid-token-vercel-cli-03231439134545dc"
description: "Fixes Vercel CLI failing with Error: Invalid token. Use when vercel commands that used to work start failing because the stored token expired or was revoked, including CI runs with a stale VERCEL_TOKEN. Generates a fresh token and re-authenticates. Not for Error: No token found, which means never logged in, or team-not-found errors, which are wrong org ids."
metadata:
  skill_id: "skl_Xe01hmO_UJQ3RsxIaf_gkQ"
  title: "Error: Invalid token (Vercel CLI)"
  version: "skv_xfUc6XHaoYuG8LHw4D827A"
  updated: "2026-10-03T04:46:04.033128+00:00"
  canonical_url: "https://vectle.com/skills/skl_Xe01hmO_UJQ3RsxIaf_gkQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/pauldx/claudifying/blob/HEAD/plugins/saas-packs/vercel-pack/skills/vercel-install-auth/SKILL.md\"]"
---

# Error: Invalid token (Vercel CLI)

TL;DR: your Vercel token expired or was revoked. Make a new one at vercel.com/account/tokens, then either run `vercel login` or set the new value as VERCEL_TOKEN. Verify with `vercel whoami`.

```text
Error: Invalid token
```

## Steps

1. Confirm the symptom:

```bash
vercel whoami
```

Expected on success: your username. `Error: Invalid token` means the stored credential is dead.

2. Generate a fresh token from the Vercel dashboard under Settings → Tokens → Create. Give it full access if the CLI needs to deploy.

3. Use it. Interactive:

```bash
vercel login
```

Expected: follow the prompts until it reports you are logged in. Headless or CI: set VERCEL_TOKEN in the environment to the new value. If you are unsure the token is right, test one call with it inline first: `vercel list --token [your token]`.

4. Verify:

```bash
vercel whoami
```

Expected: prints your account name.

## When this applies

- the exact `Error: Invalid token` on commands that used to work
- CI failures right after someone rotated or revoked tokens in the dashboard
- a token copied from an old machine that has since been regenerated

## When it doesnt

- `Error: No token found` — run `vercel login`; there is no token at all
- `Error: Team not found` — wrong VERCEL_ORG_ID, that is org config not auth
- fetch or network failures — that is connectivity, not credentials

## Compatibility

Vercel CLI 28 and up.

## Why it happens

The CLI stores one long-lived token, in the global config or in VERCEL_TOKEN. Vercel invalidates it on expiry, manual revocation, or regeneration — and the CLI has no refresh flow, so every call fails until you replace the token.

## Edge cases

- tokens for CI should be short-lived (90 days) and rotated on a schedule
- never commit the token — it is a full-access credential; store it as a CI secret
- if the team enforces SSO, the interactive login must go through the SSO flow or the new token wont be accepted

## Find this skill again

```bash
curl -s 'https://vectle.com/api/v1/search?q=vercel+cli+error+invalid+token'
```


---

Source: [Vectle](https://vectle.com/skills/skl_Xe01hmO_UJQ3RsxIaf_gkQ). Version: `skv_xfUc6XHaoYuG8LHw4D827A`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
