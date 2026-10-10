---
name: "unrecognized-named-value-secrets-c31eb62c737644a9"
description: "Why GitHub Actions rejects a workflow with Unrecognized named-value: 'secrets' and the run shows zero jobs. Use when a run shows the workflow file path as its name with zero jobs, or the annotation names secrets, env, or vars."
metadata:
  skill_id: "skl_CylOdXECxiYHx6SodOBbuw"
  title: "Unrecognized named-value: 'secrets'"
  version: "skv_wGMTcOuRabB-qn3XGIZMqA"
  updated: "2026-10-03T05:57:20.717813+00:00"
  canonical_url: "https://vectle.com/skills/skl_CylOdXECxiYHx6SodOBbuw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: Move the secret into a job-level env: block, then check env.MY_TOKEN in the step if: instead. GitHub evaluates if: conditions before the secrets context exists for that expression, so the whole workflow fails at parse time and the run shows the file path as its name with zero jobs.

```text
Unrecognized named-value: 'secrets'
```

## The fix

1. Find the offending if: - it is usually a job-level or step-level condition gating on a secret value ```yaml
   # broken
   if: ${{ secrets.OVSX_PAT != '' }}
   ```

2. Map the secret through env: at the job level, then gate the step on the env var:
   ```yaml
   jobs:
     publish:
       runs-on: ubuntu-latest
       env:
         OVSX_PAT: ${{ secrets.OVSX_PAT }}
       steps:
         - run: ./publish.sh
           if: ${{ env.OVSX_PAT != '' }}
   ```

3. The same rule applies inside composite actions: they have no secrets context at all, so the caller must pass the token as an action input or env var.

4. Push and confirm the run now schedules jobs instead of failing with the file path as the run name.

## When this applies

- a run shows the workflow file path as its name with zero jobs
- the annotation says Unrecognized named-value: 'secrets' or 'env' or 'vars'
- you gate a job or step on whether a secret is set

## When it does NOT apply

- the error is inside run: or with: - secrets works fine there, the bug is elsewhere

## Compatibility

All runners; context availability rules are server-side, the same for GitHub-hosted and self-hosted.

## Variants of this error

### `Unrecognized named-value: 'env'`
The same rejection for the env context in a job-level if:.

### `Unrecognized named-value: 'vars'`
The same rejection for the vars context inside a composite action.

## Why it happens

GitHub's expression contexts are only available where the docs' availability table says they are. if: on jobs and steps is evaluated before the job runs, and secrets is deliberately excluded there so secret values never leak into expression evaluation. The parser rejects the whole file rather than one job, which is why zero jobs appear.

## Edge cases and pitfalls

- YAML linters cannot catch this - the file is valid YAML; only GitHub's expression validation sees it. actionlint does encode the context rules and catches it.
- Composite actions cannot read secrets or vars at all - pass them in as inputs from the calling workflow.

---

Source: [Vectle](https://vectle.com/skills/skl_CylOdXECxiYHx6SodOBbuw). Version: `skv_wGMTcOuRabB-qn3XGIZMqA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
