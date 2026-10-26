---
name: "neonctl-in-ci-browser-auth-opens-set-n-f6b2591f2a56c9e7"
description: "Fixes neonctl hanging in CI by opening a browser for OAuth. Use when pipelines or SSH sessions stall because neonctl tries interactive browser authentication with nobody to click. Sets NEON_API_KEY so the CLI authenticates non-interactively. Not for invalid-key 401s or local interactive use."
metadata:
  skill_id: "skl_AFJysTD6cqNZZyee9L97Sg"
  title: "neonctl in CI: browser auth opens, set NEON_API_KEY instead"
  version: "skv_v8VYIMfKKx9mI6SFPYpMag"
  updated: "2026-10-03T05:54:03.361142+00:00"
  canonical_url: "https://vectle.com/skills/skl_AFJysTD6cqNZZyee9L97Sg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/neondatabase/neonctl/blob/HEAD/README.md\",\"https://dev.to/evoleinik/how-i-run-neon-postgres-in-ci-for-integration-tests-5h7a\"]"
---

# neonctl in CI: browser auth opens, set NEON_API_KEY instead

TL;DR: neonctl defaults to browser-based login, which hangs forever where no browser exists. Create an API key in the Neon console and export it as NEON_API_KEY in the CI job (as a secret, never inline in logs). The CLI picks it up automatically and skips the browser entirely.

```text
neonctl hangs waiting for browser authentication in CI
```

## Steps

1. In the Neon console, create an API key and copy it.

2. Add it to the CI system as a secret env var named NEON_API_KEY. Expected: the job environment contains it without printing it.

3. Rerun the pipeline. Expected: neonctl commands authenticate immediately with no browser step.

4. Still hanging: confirm the variable name is exactly NEON_API_KEY and that the step exporting it runs before the neonctl call.

## When this applies

- neonctl hanging in CI, Docker builds, or headless SSH waiting on browser auth
- scheduled jobs that worked locally but stall on the runner
- any non-interactive environment where neonctl previously relied on a cached browser session

## When it doesn't

- `Authentication failed` with NEON_API_KEY already set — the key itself is bad, fix that
- local interactive use where the browser flow is fine
- permission errors after successful auth (key scope problem)

## Compatibility

neonctl; NEON_API_KEY env var; CI secret stores. Verified against the neonctl README and the community CI setup article.

## Variant phrasings

- neonctl CI headless authentication
- neonctl NEON_API_KEY environment variable
- neonctl browser auth hang CI

## Root cause

neonctl's default auth is an OAuth browser dance. In CI there is no browser and no one to complete the dance, so the CLI waits indefinitely. The env-var key path bypasses OAuth completely.

## Edge cases

- never echo the key in job logs; mark the variable secret/masked in the CI UI
- cached browser credentials on a self-hosted runner can mask this until the cache expires
- rotate CI keys on a schedule; a leaked build log can expose them

---

Source: [Vectle](https://vectle.com/skills/skl_AFJysTD6cqNZZyee9L97Sg). Version: `skv_v8VYIMfKKx9mI6SFPYpMag`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
