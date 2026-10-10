---
name: "dbt-cli-credentials-have-expired-run-d-0d8f98172be8e9b7"
description: "Fixes the dbt CLI failing with credentials have expired. Use when dbt commands that need dbt Cloud / platform auth stop working and tell you to run dbt login to re-authenticate. Re-runs dbt login to refresh the platform token, and handles the case where it expires again immediately. Not for warehouse password errors or dbt Core profiles.yml issues."
metadata:
  skill_id: "skl_WnQglHF0PRrHD47AvQLC9g"
  title: "dbt CLI: credentials have expired - run dbt login to re-authenticate"
  version: "skv_dub_uCira6MapOCK_TAp_Q"
  updated: "2026-10-03T05:37:51.331086+00:00"
  canonical_url: "https://vectle.com/skills/skl_WnQglHF0PRrHD47AvQLC9g"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# dbt CLI: credentials have expired - run dbt login to re-authenticate

TL;DR: the cached platform token is stale. Run `dbt login` again in your terminal, complete the browser sign-in, and retry the command. If the expiry message returns immediately, your saved token file is corrupt or being overwritten: clear it and log in fresh. In headless environments use the non-interactive SSO token flow instead of a browser.

```text
Your credentials have expired - run `dbt login` to re-authenticate
```

## Steps

1. Run `dbt login` in a terminal with a browser available. Complete the sign-in in the browser window that opens.

2. Rerun the failing dbt command. Expected: it proceeds past auth without the expiry message.

3. If it expires again right away, the stored token is corrupt. Remove the cached platform auth token and run `dbt login` once more for a clean issuance.

4. Headless or CI: skip the browser flow and use the non-interactive token approach documented in the dbt platform auth chain (a service/SSO token injected into the environment) instead of `dbt login`.

## When this applies

- the exact `credentials have expired - run dbt login to re-authenticate` message
- dbt commands that auth against the dbt platform / dbt Cloud before running
- sessions that worked yesterday and fail today with no config change

## When it doesn't

- Snowflake/postgres password errors — those are warehouse credentials, not platform tokens
- dbt Core with only profiles.yml and no platform auth
- `not authenticated` from the dbt Cloud CLI's dbt_cloud.yml (different file, different fix)

## Compatibility

dbt CLI with platform auth (the dbt-platform-auth chain); interactive browser login and headless token flow. Verified against the dbt-core platform-auth README.

## Variant phrasings

- dbt credentials have expired run dbt login
- dbt login re-authenticate expired
- dbt platform auth token expired

## Root cause

dbt caches a short-lived platform token after `dbt login`. When it expires, every platform-authed command fails with the re-authenticate message until a fresh token is issued. A corrupt cache can make a fresh login write a bad token again, which is why clearing and re-logging-in fixes the loop.

## Edge cases

- `dbt login` needs a browser; over plain SSH without one, use the headless token flow
- multiple dbt installs can fight over the same token cache; use one install per user
- rotating your SSO identity (new laptop, new IdP session) invalidates the cached token

---

Source: [Vectle](https://vectle.com/skills/skl_WnQglHF0PRrHD47AvQLC9g). Version: `skv_dub_uCira6MapOCK_TAp_Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
