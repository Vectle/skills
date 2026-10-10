---
name: "permission-denied-to-github-actions-bo-efdfdb17abdbaa41"
description: "Fixes 'Permission denied to github-actions[bot]' when a workflow pushes commits. Use when git push with GITHUB_TOKEN gets a 403. Not for PAT scope issues or deploy-key problems."
metadata:
  skill_id: "skl__wlHVBa6S2_J6TF2W0Cxlg"
  title: "Permission denied to github-actions[bot] pushing from a workflow"
  version: "skv_7MDIBlEWUw0qkopBJIgYDA"
  updated: "2026-10-03T05:31:21.489092+00:00"
  canonical_url: "https://vectle.com/skills/skl__wlHVBa6S2_J6TF2W0Cxlg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: Give the job write permission: add permissions: contents: write to the workflow or job that pushes. GITHUB_TOKEN defaults to read-only, so any git push it attempts is rejected as the github-actions bot with a 403.

```text
Permission denied to github-actions[bot]
```

## The fix

1. Add a permissions block to the job (or workflow) that pushes:
   ```yaml
   permissions:
     contents: write
   ```
   Expected: YAML parses; no other change needed.

2. Re-run the failed job.
   Expected: The push step succeeds instead of Permission denied to github-actions[bot].

3. If it still 403s, check branch protection rules: the bot must be allowed to bypass them, or push to an unprotected branch.
   Expected: Push lands on the target branch.

## When this applies

- a workflow step runs git push with GITHUB_TOKEN and gets Permission denied to github-actions[bot]
- deploying docs or built files back to the repo

## When it does NOT apply

- you push with your own PAT (then check that token's scopes instead)
- the error names a different user (that is a deploy-key problem)

## Compatibility

GitHub Actions on GitHub.com and GHES, actions/checkout v2 and later. Since 2023 the default token permission is read-only.

## Variants of this error

### `fatal: unable to access 'https://github.com/...': The requested URL returned error: 403`
What git prints alongside it. Same fix.

### `remote: Permission to [owner]/[repo].git denied to github-actions[bot].`
The full git form of the same rejection. Same fix.

## Why it happens

GitHub changed the default GITHUB_TOKEN to read-only to limit blast radius of compromised workflows. Pushes need an explicit contents: write grant, which many older tutorials predate.

## Edge cases and pitfalls

- actions/checkout with persist-credentials: false removes the token from the local git config; pushes then need an explicit token.
- Tags need contents: write too.
- If the workflow is triggered by a fork PR, write permissions are stripped for safety; use the pull_request_target event carefully instead.

---

Source: [Vectle](https://vectle.com/skills/skl__wlHVBa6S2_J6TF2W0Cxlg). Version: `skv_7MDIBlEWUw0qkopBJIgYDA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
