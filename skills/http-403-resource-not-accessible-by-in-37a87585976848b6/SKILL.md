---
name: "http-403-resource-not-accessible-by-in-37a87585976848b6"
description: "Fixes gh CLI calls failing with HTTP 403 Resource not accessible by integration. Use when gh api, gh pr, gh workflow run, or gh release commands fail with this 403 while other commands work. Covers adding missing token scopes with gh auth refresh and the GitHub Actions case where GITHUB_TOKEN can never cover the endpoint. Not for 401 Bad credentials or 404s."
metadata:
  skill_id: "skl_laQKCofr1DdmojGpIra5vg"
  title: "HTTP 403: Resource not accessible by integration (gh CLI)"
  version: "skv_U63Sg9zYnvkjInhbN0lQqw"
  updated: "2026-10-03T04:41:37.2791+00:00"
  canonical_url: "https://vectle.com/skills/skl_laQKCofr1DdmojGpIra5vg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# HTTP 403: Resource not accessible by integration (gh CLI)

TL;DR: your token is missing the scope that endpoint needs. Run `gh auth refresh -s repo -s workflow` and retry — that fixes it in most cases. In GitHub Actions, the automatic GITHUB_TOKEN can never cover some endpoints no matter what permissions you grant, so use a personal access token stored as a repository secret there instead.

```text
HTTP 403: Resource not accessible by integration
```

## Steps

1. Check what your token can do:

```bash
gh auth status
```

Expected: shows your account and the granted scopes. If `workflow` or `repo` is missing for the endpoint you are hitting, that is the problem.

2. Add the missing scopes:

```bash
gh auth refresh -s repo -s workflow
```

Expected: a success message. Re-run `gh auth status` and confirm repo and workflow are now listed.

3. Retry the failing command.

4. In GitHub Actions, if it still 403s: replace `secrets.GITHUB_TOKEN` with a personal access token secret (classic PAT with repo scope, or a fine-grained token with Administration read and write). GITHUB_TOKEN has no permission covering repository administration endpoints, so it always 403s there regardless of the workflow permissions block.

## When this applies

- `gh api`, `gh workflow run`, `gh release`, branch protection or ruleset calls fail with this exact 403
- other gh commands with the same token work fine
- you recently switched from a classic PAT to a fine-grained token or to GITHUB_TOKEN

## When it doesnt

- `Bad credentials` (401) — your token is expired or invalid, re-authenticate with `gh auth login`
- `Must have admin rights to Repository` — you genuinely lack admin on the repo, ask an owner
- 404s — usually a wrong repo name or missing access, not a scope problem

## Compatibility

GitHub CLI 2.x against github.com and GitHub Enterprise Server.

## Why it happens

GitHub checks the token's granted scopes per endpoint, and this 403 names no missing permission. Fine-grained tokens and the Actions GITHUB_TOKEN carry narrower grants than a classic PAT with repo scope, so calls that used to work start failing with an opaque message.

## Edge cases

- `gh auth login --scopes "repo,workflow"` sets scopes at login time if you prefer that over refresh
- organization SSO: if the org enforces SAML, authorize the token for the org after refreshing scopes
- in Actions, the PAT must be stored as a repository secret — never print it into logs

## Find this skill again

```bash
curl -s 'https://vectle.com/api/v1/search?q=gh+resource+not+accessible+by+integration'
```


---

Source: [Vectle](https://vectle.com/skills/skl_laQKCofr1DdmojGpIra5vg). Version: `skv_U63Sg9zYnvkjInhbN0lQqw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
