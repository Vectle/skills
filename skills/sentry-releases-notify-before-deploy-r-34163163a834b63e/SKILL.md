---
name: "sentry-releases-notify-before-deploy-r-34163163a834b63e"
description: "Releases connect issues to deploys: regression detection, suspect commits, and resolve-in-release. Wire the release identifier in the SDK and notify Sentry from CI before deploy. Not the full reference manual."
metadata:
  skill_id: "skl_0ZgXrHk_9oWoShe4dc6BVg"
  title: "Sentry releases: notify before deploy, resolve in release"
  version: "skv_LifVtkZgmPwH9uKztbx-kA"
  updated: "2026-10-03T04:33:41.270721+00:00"
  canonical_url: "https://vectle.com/skills/skl_0ZgXrHk_9oWoShe4dc6BVg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.sentry.io/product/releases/\",\"https://docs.sentry.io/platforms/python/configuration/options/\",\"https://docs.sentry.io/cli/configuration/\"]"
---

**TL;DR:** Releases connect issues to deploys: regression detection, suspect commits, and resolve-in-release. Wire the release identifier in the SDK and notify Sentry from CI before deploy. Whatever you choose, it must be identical across every service and the CI upload step, or Sentry treats them as different releases. Notify from CI before deploy Note the scoping: org goes on the releases command, project on the subcommand. set-commits --auto associates the commit range so Sentry can predict suspect commits and authors.

## Set the identifier in the SDK

```python
sentry_sdk.init(release="myapp@1.2.3")
```

Or skip it: the SDK reads the `SENTRY_RELEASE` env var, else infers the git commit SHA. A human-readable `name@version` beats a bare SHA when you are scanning the releases page. Whatever you choose, it must be identical across every service and the CI upload step, or Sentry treats them as different releases.

## Notify from CI before deploy

```
sentry-cli releases -o [your org] new -p [your project] myapp@1.2.3
sentry-cli releases -o [your org] -p [your project] set-commits myapp@1.2.3 --auto
sentry-cli releases -o [your org] -p [your project] deploys myapp@1.2.3 new -e production
```

Note the scoping: org goes on the `releases` command, project on the subcommand. `set-commits --auto` associates the commit range so Sentry can predict suspect commits and authors. If you skip this, Sentry still auto-creates a release entity when the first event arrives, but with no commits and no deploy record.

## What releases buy you

- New-issue and regression detection per release on the releases page, with crash-free user and session percentages.
- Suspect commits: Sentry predicts which commit caused an issue and who likely owns it.
- Resolve in release: on an issue, Resolve > Resolved in the next release (or current). With semver, Sentry unresolves the issue if it reappears in a later version; without semver it compares release creation dates.

## Verification

After a deploy, open the Releases page and confirm the version appears with commits and the deploy marker. If events carry a release that never shows, the identifier differs between SDK and CLI (trailing whitespace and `v` prefixes are the usual culprits).

## When to use this

- This covers exactly what the title says: Sentry releases.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Sentry; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

---

Source: [Vectle](https://vectle.com/skills/skl_0ZgXrHk_9oWoShe4dc6BVg). Version: `skv_LifVtkZgmPwH9uKztbx-kA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
