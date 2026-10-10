---
name: "sentry-the-dsn-is-public-the-auth-toke-4e6e3b21a69be3f3"
description: "The DSN is a public ingest address that belongs in SDK init code. The auth token is a secret that belongs in CI. Mixing them up either breaks uploads or leaks credentials into client bundles. Not the full reference manual."
metadata:
  skill_id: "skl__Ke08t1KE7DJG9TDKfHbvw"
  title: "Sentry: the DSN is public, the auth token is secret"
  version: "skv_YgZWyNaC_MkQVCp103Jb9w"
  updated: "2026-10-03T05:10:56.601675+00:00"
  canonical_url: "https://vectle.com/skills/skl__Ke08t1KE7DJG9TDKfHbvw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** The DSN is a public ingest address that belongs in SDK init code. The auth token is a secret that belongs in CI. It goes in CI secrets as SENTRY_AUTH_TOKEN, never in application code and never in a client bundle. Use when org tokens cannot do the job (e.g. programmatically creating projects). - Personal token - bound to you.

## Two credentials, two jobs

- **DSN**: the ingest address, made of the public key, the org ingest host, and the project ID. It goes in `Sentry.init()` / `sentry_sdk.init()`. It is meant to be visible, including in frontend bundles. It can only send events to one project; it cannot read anything or upload anything.
- **Auth token**: the credential for sentry-cli, source map uploads, release management, and the API. It goes in CI secrets as `SENTRY_AUTH_TOKEN`, never in application code and never in a client bundle.

## Pick the right token type

- **Organization token**: limited permissions, designed for CI and sentry-cli. Default choice for uploads. Visible only once at creation; org owners get a security email when one is created.
- **Internal integration token**: custom permissions, full API access on behalf of the org. Use when org tokens cannot do the job (e.g. programmatically creating projects).
- **Personal token**: bound to you. Stops working if you leave the org. Never use in CI; it is the most common cause of uploads breaking months later when someone offboards.

## The failure shapes

- Uploads fail with 401: the token is wrong, expired, revoked, or lacks scope. Check `sentry-cli info`.
- Events rejected with no clear error: the DSN points at the wrong project or org. Sentry validates DSN and project before parsing anything.
- Auth token found in a shipped JS bundle: rotate it immediately. It was never meant to be there.

## Hygiene

One token per use case (uploads token != API automation token), so a compromise lets you revoke surgically. Scope CLI commands with `SENTRY_ORG` and `SENTRY_PROJECT` rather than relying on whatever the CI machine last used.

## When to use this

- This covers exactly what the title says: Sentry.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Sentry; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current Sentry behavior.

---

Source: [Vectle](https://vectle.com/skills/skl__Ke08t1KE7DJG9TDKfHbvw). Version: `skv_YgZWyNaC_MkQVCp103Jb9w`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
