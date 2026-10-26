---
name: "dbt-250001-failed-to-connect-to-db-inc-810657fb69b112fe"
description: "Fixes dbt failing against Snowflake with 250001 Incorrect username or password was specified. Use when dbt debug or dbt run cannot open the Snowflake session even though the account and warehouse look right. Checks the profiles.yml credentials for typos, picks the right authenticator (password vs key pair vs SSO), and handles expired Snowflake passwords. Not for network or role/warehouse-not-found errors."
metadata:
  skill_id: "skl_4U4AnNExneV6pHvpMd3Lpw"
  title: "dbt: 250001 Failed to connect to DB: Incorrect username or password was specified"
  version: "skv_CfynugZvY1v7WLfKsvGKMQ"
  updated: "2026-10-03T05:36:26.872588+00:00"
  canonical_url: "https://vectle.com/skills/skl_4U4AnNExneV6pHvpMd3Lpw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/mwhitaker/dbt-action/issues/44\"]"
---

# dbt: 250001 Failed to connect to DB: Incorrect username or password was specified

TL;DR: Snowflake rejected the username/password in your profile. First rule out typos in profiles.yml (trailing spaces are a classic), then check whether the password expired or the account uses SSO or key-pair auth instead of a password. If your org requires SSO, set `authenticator: externalbrowser`; if it requires key pairs, switch to private_key auth.

```text
250001 (08001): Failed to connect to DB: [account].snowflakecomputing.com:443. Incorrect username or password was specified.
```

## Steps

1. Open profiles.yml and re-read the user and password lines character by character; strip trailing spaces. Rerun `dbt debug`. Expected: either it connects or the error persists with clean input.

2. Log into Snowflake in a browser with the same username and password. If that fails too, the password is wrong or expired: reset it (or ask your admin to) and update profiles.yml.

3. If browser login works but uses SSO, your profile must not use password auth. Set `authenticator: externalbrowser` in the profile and rerun; a browser window opens for the SSO flow.

4. If your org uses key-pair auth, replace the password with the private_key settings in the profile. Expected: `dbt debug` shows `Connection test: OK`.

## When this applies

- the exact `Incorrect username or password was specified` (250001) error from dbt debug or dbt run against Snowflake
- CI pipelines where the Snowflake password rotated but profiles.yml still has the old one
- orgs that moved to SSO while profiles still say password

## When it doesn't

- `Incorrect role` or warehouse-not-found errors — those mean auth succeeded and object access failed
- network/timeout errors reaching the Snowflake host
- expired private keys (different error: JWT / key mismatch)

## Compatibility

dbt Core and Fusion CLIs with the dbt-snowflake adapter; password, externalbrowser (SSO), and key-pair authenticators. Verified against the dbt-action issue thread.

## Variant phrasings

- dbt snowflake incorrect username or password was specified
- dbt 250001 failed to connect to db
- dbt snowflake password expired fix

## Root cause

Error 250001 comes from Snowflake's login endpoint, not from dbt: the credential bundle (user + password, or the authenticator choice) did not match what Snowflake expects for that user. dbt just surfaces it.

## Edge cases

- passwords with special characters are fine in YAML but must be quoted if they start with special chars
- SSO with externalbrowser does not work in headless CI; use key-pair auth there
- a locked-out Snowflake user gives a different error; unlock via the admin console

---

Source: [Vectle](https://vectle.com/skills/skl_4U4AnNExneV6pHvpMd3Lpw). Version: `skv_CfynugZvY1v7WLfKsvGKMQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
