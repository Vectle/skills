---
name: "error-no-access-token-available-please-fd841b11f9998d94"
description: "Fixes flyctl failing in GitHub Actions with Error: No access token available. Please login with flyctl auth login even though FLY_API_TOKEN is set. Use when the token was added as an Environment secret instead of a Repository secret, or the deploy step does not see it. Not for expired local sessions \u2014 run flyctl auth login for those."
metadata:
  skill_id: "skl_RIUa2C6_ZeiESEAIKbTZRA"
  title: "Error: No access token available. Please login with 'flyctl auth login'"
  version: "skv_PBLv5WSEExJmtzkNgtxvDg"
  updated: "2026-10-03T04:44:11.230902+00:00"
  canonical_url: "https://vectle.com/skills/skl_RIUa2C6_ZeiESEAIKbTZRA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# Error: No access token available. Please login with 'flyctl auth login'

TL;DR: in GitHub Actions this almost always means the FLY_API_TOKEN secret is in the wrong place. Move it from Environment secrets to Repository secrets (or scope the job to that environment), and make sure the deploy step actually receives it. Locally, the fix is just `flyctl auth login`.

```text
Error: No access token available. Please login with 'flyctl auth login'
```

## Steps

1. Check where the secret lives: repo Settings → Secrets and variables → Actions. If FLY_API_TOKEN sits under Environment secrets but the job has no `environment:` key, the step cant see it — GitHub only injects environment secrets into jobs that declare that environment.

2. Move it: delete the secret from Environment secrets and re-add it under Repository secrets. Alternative: add the matching `environment: [name]` to the job.

3. Make sure the deploy step exports the secret so flyctl can read it.

4. Re-run the workflow. Expected: `flyctl deploy` proceeds past auth instead of erroring.

5. Local variant:

```bash
flyctl auth login
flyctl auth whoami
```

Expected: whoami prints your email.

## When this applies

- the exact error in GitHub Actions or any CI, with exit code 1
- the secret exists but the step still cant see it (wrong secret scope, or env not wired into the step)

## When it doesnt

- `flyctl auth login` failing on your laptop — that is a browser or terminal problem, not secret placement
- token was revoked in the fly.io dashboard — mint a fresh one and update the secret

## Compatibility

flyctl 0.x, flyctl-actions/setup-flyctl.

## Why it happens

GitHub scopes secret injection by environment. A job without an `environment:` key never receives environment secrets, so FLY_API_TOKEN arrives empty, and flyctl treats empty as absent — hence the misleading "please login" message even though you configured everything.

## Edge cases

- validate the secret is non-empty early in the workflow so the failure message is obvious instead of cryptic
- prefer short-lived deploy tokens over long-lived personal tokens in CI
- never echo the token into logs; GitHub masks secrets but scripts can leak prefixes

## Find this skill again

```bash
curl -s 'https://vectle.com/api/v1/search?q=flyctl+no+access+token+flyctl+auth+login'
```


---

Source: [Vectle](https://vectle.com/skills/skl_RIUa2C6_ZeiESEAIKbTZRA). Version: `skv_PBLv5WSEExJmtzkNgtxvDg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
