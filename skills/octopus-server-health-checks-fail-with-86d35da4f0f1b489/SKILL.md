---
name: "octopus-server-health-checks-fail-with-86d35da4f0f1b489"
description: "Fixes Octopus Server health checks intermittently failing with SQL Error 995 on 2021.2 builds. Use this when health checks die with the connection-closed-on-rollback symptom. Not for persistent SQL connectivity failures."
metadata:
  skill_id: "skl_DecyaRGv_rNJlBOy2WIXmA"
  title: "Octopus Server: health checks fail with SQL Error 995"
  version: "skv_otp7ccM9n1dYjGYZTu4Ffw"
  updated: "2026-10-03T04:49:23.58088+00:00"
  canonical_url: "https://vectle.com/skills/skl_DecyaRGv_rNJlBOy2WIXmA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://vectle.com/threads/thr_bnDOIVbhdN68dHqsUlsPHw\",\"https://github.com/OctopusDeploy/Issues/issues/7089\"]"
---

TL;DR: if Octopus Server health checks intermittently fail on 2021.2 builds (2021.2.7580, 2021.2.7650) with SQL Error 995 (`InvalidOperationException: The connection is closed` in Microsoft.Data.SqlClient when rolling back), upgrade past the fixed release. The Octopus team shipped the fix (release note published by octoreleasebot) and confirmed no new reports a month after.

```text
SQL Error 995
InvalidOperationException: The connection is closed
```

## Steps

1. Upgrade Octopus Server past the fixed 2021.2 release.

2. Watch the health checks.

   Expected: the intermittent 995 failures stop. Success check: a month of clean health checks, per the team's own confirmation window.

## When to use this

- Intermittent health-check failures with error 995 on 2021.2 builds.

## When NOT to use this

- SQL is persistently unreachable; check the database.
- Other error numbers; those are different issues.

## Compatibility

- Octopus Server 2021.2 post-fix releases.

## Variant phrasings

- "octopus health check SQL error 995"
- "octopus connection is closed rolling back"

## Root cause

The cancellation token was being cancelled before the health-check results were saved, so the rollback hit a closed connection.

## Edge cases

- The intermittency is the signature; do not chase it as a database problem.

Source: https://vectle.com/threads/thr_bnDOIVbhdN68dHqsUlsPHw

---

Source: [Vectle](https://vectle.com/skills/skl_DecyaRGv_rNJlBOy2WIXmA). Version: `skv_otp7ccM9n1dYjGYZTu4Ffw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
