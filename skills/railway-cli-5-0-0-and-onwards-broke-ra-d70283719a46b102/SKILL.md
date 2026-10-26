---
name: "railway-cli-5-0-0-and-onwards-broke-ra-d70283719a46b102"
description: "CLI: railway/cli:5.0.0 and onwards broke RAILWAY_TOKEN deployments. The verified fix is Fix: Takeaway for agents: pin the CLI version in CI (`npm install -g @railway/cli@5.2.0` / pin the docker tag) instead of `latest` so a bad release can't break deploys. Use this when you hit the symptoms above in cli; not for unrelated cli errors or general setup questions."
metadata:
  skill_id: "skl_60cwoj4mOcOBuBqbrYcsfw"
  title: "Railway/cli:5.0.0 and onwards broke RAILWAY_TOKEN deployments"
  version: "skv_zvXB0wyk6c2ravh7yiXHGA"
  updated: "2026-10-03T05:05:02.940113+00:00"
  canonical_url: "https://vectle.com/skills/skl_60cwoj4mOcOBuBqbrYcsfw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/railwayapp/cli/issues/947\"]"
---

## TL;DR

Fix: Takeaway for agents: pin the CLI version in CI (`npm install -g @railway/cli@5.2.0` / pin the docker tag) instead of `latest` so a bad release can't break deploys.

## The error

```text
CI deploys using `railway/cli:latest` with the `RAILWAY_TOKEN` env var broke from 5.0.0 onward: `railway up --service=api` fails with `Not signed in. Run railway login`. Pinning to 4.65.0 works.
```

## Fix

1. Takeaway for agents: pin the CLI version in CI (`npm install -g @railway/cli@5.2.0` / pin the docker tag) instead of `latest` so a bad release can't break deploys.

Success check: the symptom above is gone and the original operation completes.

## When to use

- You hit this exact symptom in cli.
- You want the verified fix without digging through the thread.

## When not to use

- A different error in cli, even a similar-looking one.
- General cli setup or credential questions.

## Compatibility

- CLI (railwayapp/cli) Reported against version 5.4.2.

## Variant phrasings

- How to fix "railway/cli:5.0.0 and onwards broke RAILWAY_TOKEN deployments" in cli
- cli: railway/cli:5.0.0 and onwards broke RAILWAY_TOKEN deployments

## Root cause

Maintainer codyde owned it as his regression and maintainer m-abdelwahab shipped the fix; reporters confirmed version 5.4.2 works again.

## Source

- https://github.com/railwayapp/cli/issues/947

---

Source: [Vectle](https://vectle.com/skills/skl_60cwoj4mOcOBuBqbrYcsfw). Version: `skv_zvXB0wyk6c2ravh7yiXHGA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
