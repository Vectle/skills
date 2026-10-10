---
name: "can-t-find-action-yml-action-yaml-or-d-76c2bf5ac818e3e1"
description: "Why a local action step fails with Cant find action.yml, action.yaml or Dockerfile, and the one-step checkout fix. Use when a uses: ./.github/actions/... step fails with this error."
metadata:
  skill_id: "skl_uEhBU4yr9O41irPZIvFSMQ"
  title: "Can't find 'action.yml', 'action.yaml' or 'Dockerfile'"
  version: "skv_e32aPJ7R2evIen-Tvvp9DA"
  updated: "2026-10-03T05:54:34.007384+00:00"
  canonical_url: "https://vectle.com/skills/skl_uEhBU4yr9O41irPZIvFSMQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: Run actions/checkout before any uses: ./.github/actions/... step. On a fresh runner nothing exists until the checkout clones it. The full error is: Cant find 'action.yml', 'action.yaml' or 'Dockerfile' for './.github/actions/...'. Did you forget to run actions/checkout before running your local action?

```text
Can't find 'action.yml', 'action.yaml' or 'Dockerfile'
```

## The fix

1. Put actions/checkout as the first step of the job, before any uses: ./... step:
   ```yaml
   steps:
     - uses: actions/checkout@v4
     - uses: ./.github/actions/my-action
   ```

2. If you only need the action dir and not the whole repo, sparse-checkout keeps the clone fast:
   ```yaml
   - uses: actions/checkout@v4
     with:
       sparse-checkout: .github/actions/my-action
   ```

3. Rerun the job. The local action now resolves because its action.yml is on disk.

## When this applies

- a uses: ./.github/actions/... or uses: ./path step fails with this error
- a new workflow that calls a local composite or Docker action
- the workflow worked in another job that has a checkout and fails in one that does not

## When it does NOT apply

- the action is remote (owner/repo@ref) - that error means the ref does not exist, not a missing checkout
- the path in uses: is misspelled - check the path spelling first

## Compatibility

All runners; actions/checkout v4.

## Variants of this error

### `Can't find 'action.yml' ... Did you forget to run actions/checkout before running your local action?`
The full message including the hint GitHub appends.

## Why it happens

Local actions resolve to a path on the runner filesystem. A fresh runner starts empty; without a checkout step the path does not exist, so the runner cannot find action.yml there. The error is the runner telling you the directory is missing, not that the file inside it is malformed.

## Edge cases and pitfalls

- Composite actions nested inside the local action also need their files present - the checkout covers the whole repo, so this is handled.
- If checkout uses path: into a subdirectory, the local action path must be relative to that subdirectory.

---

Source: [Vectle](https://vectle.com/skills/skl_uEhBU4yr9O41irPZIvFSMQ). Version: `skv_e32aPJ7R2evIen-Tvvp9DA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
