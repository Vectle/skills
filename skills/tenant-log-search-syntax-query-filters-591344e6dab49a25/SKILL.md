---
name: "tenant-log-search-syntax-query-filters-591344e6dab49a25"
description: "Symptom: drowning in tenant logs. Cause: not using the search query syntax. Confirmation is the point: the right query isolates the failing user, client, and event type in seconds."
metadata:
  skill_id: "skl_p-YikzjTCCcgEODaPgMIEg"
  title: "Tenant log search syntax: query filters that find the exact failure"
  version: "skv_okhcS4ZzV9CnleyaCqLk7Q"
  updated: "2026-10-03T13:47:19.979505+00:00"
  canonical_url: "https://vectle.com/skills/skl_p-YikzjTCCcgEODaPgMIEg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** Symptom: drowning in tenant logs. Cause: not using the search query syntax. Log retention Retention depends on the subscription tier (days to months). Verify Run the query for a known recent login and confirm it returns the event.

## The error

```text
drowning in tenant logs. Cause: not using the search query syntax. Log retention Retention depends on the subscription tier (days to months). Verify Run the query for a known recent login and confirm it returns the event.
```

## The fix

**TL;DR:** Symptom: drowning in tenant logs. Cause: not using the search query syntax. Log retention Retention depends on the subscription tier (days to months). Verify Run the query for a known recent login and confirm it returns the event.

## The error

```text
failed logins;
```

## The fix

# Tenant log search

## The syntax

Monitoring > Logs search box accepts Lucene-style queries. The ones that matter:

- `type:f` failed logins; `type:s` successes. Full type codes are in the docs.
- `user_id:"auth0|abc123"` exact user. `user_name:"[the user email]"`.
- `client_id:"YOUR_CLIENT_ID"` scope to one app.
- `connection:"google-oauth2"` or `connection:"Username-Password-Authentication"`.
- `description:*denied*` wildcard on the description.
- Date ranges: the dashboard picker, or `date:[2026-09-26 TO 2026-09-27]` in API queries.
- Combine: `type:f AND client_id:"xxx" AND user_name:"y@"` finds one user's failures on one app.

## Management API search

`GET /api/v2/logs?q=type:f AND user_id:"auth0|123"&per_page=50&sort=date:-1`. Script this; the dashboard is for humans, the API is for incidents.

## Log retention

Retention depends on the subscription tier (days to months). If the incident is older than retention, the logs are gone; this is the argument for log streaming to your SIEM before you need it.

## PII

Logs can contain PII. The docs describe PII handling and obfuscation options for streams. Do not paste raw log lines into public issues.

## Verify

Run the query for a known recent login and confirm it returns the event. Save the team's top five queries in the runbook so incidents start from a template, not a blank box.

## When to use this

- You are seeing this exact error message; match the block above, not just part of it.
- The failing call matches the scenario in the title: Tenant log search syntax.
- You want the fastest verified fix before digging through logs.

## When not to use this

- Your error text differs from the block above; close cousins often have different causes.
- The stack trace points at a different component than the one in the title.
- You already applied this fix and the error persists; look for a second cause instead of reapplying.

## Compatibility

- Not pinned to a specific version; follows current Tenant behavior.

## Also seen as

- `description:*denied*`

---

Source: [Vectle](https://vectle.com/skills/skl_p-YikzjTCCcgEODaPgMIEg). Version: `skv_okhcS4ZzV9CnleyaCqLk7Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
