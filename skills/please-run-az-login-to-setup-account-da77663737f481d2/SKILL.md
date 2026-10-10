---
name: "please-run-az-login-to-setup-account-da77663737f481d2"
description: "Fixes Azure CLI commands failing with Please run 'az login' to setup account. Use when the cached login expired \u2014 sessions go stale after about 90 days \u2014 or the account cache was cleared. Drops the stale cache and re-authenticates. Not for AADSTS Conditional Access blocks or wrong-tenant errors."
metadata:
  skill_id: "skl_7aKi9fDg6cP5dqjxQPgTHA"
  title: "Please run 'az login' to setup account."
  version: "skv_DcNnNgcj2R6ylotYN0Kdxw"
  updated: "2026-10-03T04:43:35.436066+00:00"
  canonical_url: "https://vectle.com/skills/skl_7aKi9fDg6cP5dqjxQPgTHA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# Please run 'az login' to setup account.

TL;DR: your CLI session died. Cached tokens expire after about 90 days, and az wont tell you gracefully — it just says to set up your account. Run `az account clear` to drop the stale cache, then `az login` to sign in fresh. Verify with `az account show`.

```text
Please run 'az login' to setup account.
```

## Steps

1. Confirm the session is dead:

```bash
az account show
```

Expected: the same error instead of account JSON.

2. Clear the stale cache:

```bash
az account clear
```

Expected: no output.

3. Log in fresh:

```bash
az login
```

Expected: browser opens; after sign-in the CLI lists your subscriptions. Headless box: `az login --use-device-code`. Multiple tenants: add `--tenant [tenant id]`.

4. Verify:

```bash
az account show
```

Expected: JSON with your subscription, tenant ID, and user name.

5. If you have several subscriptions, pick the right one:

```bash
az account list --output table
az account set --subscription [name or id]
```

## When this applies

- the exact `Please run 'az login' to setup account.` error
- commands that worked months ago and now fail everywhere
- after a password change, or after the ~/.azure cache was deleted or moved

## When it doesnt

- AADSTS53003 from Conditional Access — that is policy blocking the login, re-running az login wont help until the policy allows it
- AADSTS50020 (account does not exist in tenant) — you are in the wrong tenant; use `az login --tenant [tenant id]`
- `az login` itself hanging with no browser — that is the headless case, use `az login --use-device-code`

## Compatibility

Azure CLI 2.x, all platforms.

## Why it happens

The CLI caches tokens under ~/.azure and silently refreshes them until the refresh token itself dies (about 90 days, sooner after a password change). Once it is dead every command fails with the setup-account message, which reads like you never logged in.

## Edge cases

- `az account get-access-token` forces a refresh check and shows the real error when the cache is half-dead
- AZURE_CONFIG_DIR isolates caches per terminal: logging in in one terminal doesnt log in the other
- service principal logins expire too — re-run `az login --service-principal` with fresh credentials, not plain `az login`

## Find this skill again

```bash
curl -s 'https://vectle.com/api/v1/search?q=az+please+run+az+login+to+setup+account'
```


---

Source: [Vectle](https://vectle.com/skills/skl_7aKi9fDg6cP5dqjxQPgTHA). Version: `skv_DcNnNgcj2R6ylotYN0Kdxw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
