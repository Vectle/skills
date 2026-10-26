---
name: "social-button-missing-on-login-connect-5f461776ea0f08bc"
description: "Symptom: the Universal Login page does not show the Google/GitHub button. Cause: the connection is not enabled for the application, or the connection itself is misconfigured. Confirmation: the application's Connections tab."
metadata:
  skill_id: "skl_A5gpjkPfCgUYrtNfSEvkDA"
  title: "Social button missing on login: connection enabled on the application"
  version: "skv_MpkAAS8Pq1Yrj6CRzIXGMg"
  updated: "2026-10-03T13:49:08.169393+00:00"
  canonical_url: "https://vectle.com/skills/skl_A5gpjkPfCgUYrtNfSEvkDA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://auth0.com/docs/manage-users/organizations\"]"
---

**TL;DR:** Symptom: the Universal Login page does not show the Google/GitHub button. Cause: the connection is not enabled for the application, or the connection itself is misconfigured. Confirm - Application > Connections: is the social connection toggled on? Fix Enable the connection in all three places that apply (tenant, application, organization), fill in provider keys, save.

## The error

```text
the Universal Login page does not show the Google/GitHub button. Cause: the connection is not enabled for the application, or the connection itself is misconfigured. Confirm - Application > Connections: is the social connection toggled on? Fix Enable the connection in all three places that apply (te
```

## The fix

**TL;DR:** Symptom: the Universal Login page does not show the Google/GitHub button. Cause: the connection is not enabled for the application, or the connection itself is misconfigured. Confirm - Application > Connections: is the social connection toggled on? Fix Enable the connection in all three places that apply (tenant, application, organization), fill in provider keys, save.

# Diagnose: social button missing

## Symptom

Universal Login renders only username/password (or nothing) where a social button is expected.

## Likely causes

1. Connection not enabled for the application (most common). Connections are per-app opt-in.
2. Social connection missing its own keys: Google/GitHub/etc need a client id/secret in the connection settings; without them the connection stays inert.
3. Organization login: org logins only show connections enabled on the ORGANIZATION. App-level enablement is not enough.
4. Identifier-first flow: the button appears only after the user types an email whose domain routes to the social connection (home realm discovery). This is by design in identifier-first.
5. Display configuration: the new Universal Login shows social buttons based on enabled connections automatically; custom HTML can hide them.

## Confirm

- Application > Connections: is the social connection toggled on? If not, found it.
- Authentication > Social > the connection: are provider keys filled in and the connection enabled at tenant level?
- For orgs: Organizations > your org > Connections: enabled there?
- Tenant logs: a login attempt with `connection` set to the social connection failing means the app tried it but it is not enabled.

## Fix

Enable the connection in all three places that apply (tenant, application, organization), fill in provider keys, save.

## Verify

Incognito login page shows the button; complete a full social login and confirm the success event names the social connection.

## When to use this

- You are seeing this exact error message; match the block above, not just part of it.
- The failing call matches the scenario in the title: Social button missing on login.
- You want the fastest verified fix before digging through logs.

## When not to use this

- Your error text differs from the block above; close cousins often have different causes.
- The stack trace points at a different component than the one in the title.
- You already applied this fix and the error persists; look for a second cause instead of reapplying.

## Compatibility

- Not pinned to a specific version; follows current Social behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_A5gpjkPfCgUYrtNfSEvkDA). Version: `skv_MpkAAS8Pq1Yrj6CRzIXGMg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
