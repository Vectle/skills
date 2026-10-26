---
name: "dependabot-triggered-github-actions-ca-9162925679db9e53"
description: "Fixes Dependabot-triggered GitHub Actions failing from missing secrets or a read-only token by switching the workflow to the pull_request_target event, which runs in the base-branch context. Use when Dependabot PRs from forks break CI steps that push, publish, or call external services. Not for non-Dependabot PR failures."
metadata:
  skill_id: "skl_cbc4HS4lcveR-vMzs4_aJQ"
  title: "Dependabot triggered GitHub Actions cannot access secrets or use a writable token"
  version: "skv_Cg2slYBeyce5e3BeAljzTA"
  updated: "2026-10-03T04:24:01.980241+00:00"
  canonical_url: "https://vectle.com/skills/skl_cbc4HS4lcveR-vMzs4_aJQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://vectle.com/threads/thr_sJUM_fa51r6VZYUyjH2i6Q\",\"https://github.com/dependabot/dependabot-core/issues/3253\"]"
---

## TL;DR

This is intended GitHub behavior: Dependabot PRs from forks run with a read-only token and no secrets. Use the `pull_request_target` event instead of `pull_request` for workflows that need secrets or a writable token; it runs in the base-branch context. Only check out and run the untrusted dependency-update code in a separate `pull_request` workflow.

## The problem

Workflows triggered by Dependabot pull requests fail because the default `GITHUB_TOKEN` is read-only and secrets are not passed to runs triggered from forks. CI steps that need to push, publish, or call external services break.

## Fix it

1. Identify the failing workflow: it triggers on `pull_request` and needs secrets or write permissions.
   Success check: the failing runs are all on Dependabot PRs.

2. Change the trigger to `pull_request_target`:
   ```yaml
   on:
     pull_request_target:
       types: [opened, synchronize]
   ```
   Success check: the workflow file is updated on the base branch.

3. Keep untrusted code isolated: check out and run the dependency update itself only in a separate `pull_request` workflow.
   Success check: secrets-bearing steps never execute fork-supplied code.

4. Re-run the Dependabot PR checks.
   Success check: secrets are available and the token can write.

## When this applies

- Dependabot PRs from forks failing on secret access or write operations.
- Workflows that push, publish, or call external services on PRs.

## When it does not apply

- Non-Dependabot PRs failing; check the workflow permissions instead.
- Dependabot PRs from branches (not forks); secrets are available there.

## Compatibility

- GitHub Actions (any runner). Documented in the official guide "Automating Dependabot with GitHub Actions".

## Variant phrasings

- Dependabot GitHub Actions no secrets
- GITHUB_TOKEN read-only Dependabot PR
- pull_request_target vs pull_request Dependabot

## Why it happens

Dependabot PRs from forks run with limited permissions on purpose: the token is read-only and secrets are withheld so malicious dependency updates cannot exfiltrate them. `pull_request_target` runs the workflow from the base branch, restoring secrets and write access.

## Edge cases

- `pull_request_target` with a checkout of the PR head runs untrusted code with secrets; always gate or separate it.


---

Source: [Vectle](https://vectle.com/skills/skl_cbc4HS4lcveR-vMzs4_aJQ). Version: `skv_Cg2slYBeyce5e3BeAljzTA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
