---
name: "codecov-error-failed-to-properly-uploa-d9f99efd62410186"
description: "Fixes Codecov coverage uploads failing in GitHub Actions with 'Error: failed to properly upload'. Use this when the upload step pings the endpoint but never completes, especially on tokenless setups. Not for coverage generation failures or for Codecov UI issues."
metadata:
  skill_id: "skl_3Q3xUgpUpKCVl7LQsbKVdA"
  title: "Codecov Error failed to properly upload in GitHub Actions"
  version: "skv_tAvs_K6EZm5JPD-XM7heKg"
  updated: "2026-10-03T04:34:29.566166+00:00"
  canonical_url: "https://vectle.com/skills/skl_3Q3xUgpUpKCVl7LQsbKVdA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: if Codecov uploads fail in GitHub Actions with `Error: failed to properly upload`, stop going tokenless. Create a Codecov upload token for the repo, save it as a repository secret (Settings > Secrets and variables > Actions), and reference it from the codecov-action step. Tokenless uploads made Codecov locate the build via the unauthenticated GitHub API, which rate-limited and failed cryptically.

```text
Error: failed to properly upload
```

## Steps

1. In Codecov, generate an upload token for the repo.

2. Save it as a repository secret under Settings > Secrets and variables > Actions.

   Note: it must be a repository secret, not just an environment variable; v4 in particular reports "Codecov token not found" otherwise.

3. Reference the secret from the codecov-action step in your workflow.

4. Re-run the workflow.

   Expected: the upload completes. Success check: coverage appears on the Codecov dashboard for the commit.

## When to use this

- Coverage uploads fail in GitHub Actions with the failed-to-properly-upload error.
- You run tokenless or the token is missing/misconfigured.

## When NOT to use this

- Coverage never gets generated locally; fix the coverage tool first.
- The failure is in the Codecov UI rather than the upload step.

## Compatibility

- codecov-action on GitHub Actions, including v4 (which is stricter about the token).

## Variant phrasings

- "codecov failed to properly upload github actions"
- "codecov token not found v4"
- "codecov tokenless upload fails"

## Root cause

Tokenless uploads required Codecov to locate the build through the GitHub Actions API without authentication, hitting GitHub's rate limit and failing the upload cryptically. A real token removes that dependency.

## Edge cases

- After upgrading to v4, "Codecov token not found" almost always means the secret is saved at the wrong level; double-check it is a repository secret.

---

Source: [Vectle](https://vectle.com/skills/skl_3Q3xUgpUpKCVl7LQsbKVdA). Version: `skv_tAvs_K6EZm5JPD-XM7heKg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
