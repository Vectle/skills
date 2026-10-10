---
name: "unable-to-locate-executable-file-docke-72cd2659127aaf80"
description: "Fixes 'Unable to locate executable file: docker' in workflow runs. Use when a step fails because the binary is not on the runner PATH. Not for daemon connection errors."
metadata:
  skill_id: "skl_5CqqCQ6v8P0ZH2cSXhWCYw"
  title: "Unable to locate executable file: docker in GitHub Actions"
  version: "skv_02cB19R68SWoGu4IyZKrOQ"
  updated: "2026-10-03T05:35:27.188091+00:00"
  canonical_url: "https://vectle.com/skills/skl_5CqqCQ6v8P0ZH2cSXhWCYw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: Install the Docker client in the job before using it, or move the job to a runner image that ships docker on PATH. The step assumes docker exists, but minimal runner images (and many self-hosted setups) do not put a docker client on PATH.

```text
Error: Unable to locate executable file: docker.
```

## The fix

1. Confirm which runner the job landed on and whether docker is present: add a debug step with which docker || echo MISSING.
   ```bash
   which docker || echo MISSING
   ```
   Expected: You see MISSING on the failing runner.

2. Either install the client in the job (apt-get install -y docker-ce-cli on Debian runners) or change runs-on to an image that includes it (e.g. ubuntu-latest for GitHub-hosted).
   Expected: docker --version prints a version.

3. Re-run the job.
   Expected: The docker step proceeds past executable lookup.

## When this applies

- a run step fails immediately with Unable to locate executable file: docker
- self-hosted or custom container runners

## When it does NOT apply

- docker exists but the daemon refuses (that is Cannot connect to the Docker daemon, a different error)
- the error names a different binary (same pattern, but check that tool's install docs)

## Compatibility

GitHub Actions on self-hosted runners and container jobs; GitHub-hosted ubuntu/macos/windows images already ship docker.

## Variants of this error

### `##[error]Unable to locate executable file: pnpm`
Same pattern when the package manager is not on PATH; install it or fix the step order.

### `Error: Unable to locate executable file: unzip.`
Same runner-image gap for unzip; install the package the same way.

## Why it happens

The runner resolves every bare command through PATH at step start. Stock and minimal images deliberately omit tools the maintainer did not ask for, so the lookup fails before anything runs.

## Edge cases and pitfalls

- Installing the client is not enough if there is no daemon; that surfaces as a daemon connection error next.
- In container jobs, the tool must exist inside the container, not on the runner host.
- PATH changes via $GITHUB_PATH only affect later steps, not the current one.

---

Source: [Vectle](https://vectle.com/skills/skl_5CqqCQ6v8P0ZH2cSXhWCYw). Version: `skv_02cB19R68SWoGu4IyZKrOQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
