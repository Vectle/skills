---
name: "lago-one-click-docker-an-error-occured-bf714f1b24d6f1e3"
description: "Shows how to fix lago one-click Docker: 'An error occured, please restart the application' when adding Stripe integration. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_lB07_0bxVszMf_uAxELKWA"
  title: "Lago one-click Docker: 'An error occured, please restart the application' when adding Stripe integration"
  version: "skv_HL8n5yrrMxO3qImfB6QVjg"
  updated: "2026-10-03T13:45:51.831074+00:00"
  canonical_url: "https://vectle.com/skills/skl_lB07_0bxVszMf_uAxELKWA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://vectle.com/threads/thr_0MJD3lrrpBDmrSHLqGQE3g\",\"https://github.com/getlago/lago/issues/515\"]"
---

## TL;DR

Running Lago's single Docker image (v1.25.0 and 1.24.1) via docker run --rm -it --name lago -p 80:80 -p 3000:3000 getlago/lago:v1.25.0, clicking Integrations > Stripe and entering a Stripe test secret key produced the UI toast 'An error occured, please restart the application' plus an API 500.

## Steps

1. Running Lago's single Docker image (v1.25.0 and 1.24.1) via `docker run --rm -it --name lago -p 80:80 -p 3000:3000 getlago/lago:v1.25.0`, clicking Integrations > Stripe and entering a Stripe test secret key produced the UI toast 'An error occured, please restart the application' plus an API 500. The logs showed a Segment-related error. The same Stripe keys worked fine on the Docker Compose deployment, so it was specific to the one-click image.

2. The 500 came from Lago's Segment analytics call, not from Stripe. Workaround confirmed by the reporter: disable Segment by adding `-e LAGO_DISABLE_SEGMENT="true"` to the docker run command - the Segment error disappears after that. The maintainer acknowledged it as a bug and said a fix would ship in the next release. Note: if the integration still isn't created after disabling Segment, check the /graphql response on its own - a later commenter hit a separate 500 tied to their Stripe key. Source: https://github.com/getlago/lago/issues/515

## When to use

You are seeing this: The logs showed a Segment-related error. Use this skill when you run into "Lago one-click Docker: 'An error occured, please restart the application' when adding Stripe integration".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

Versions mentioned in the source: v1.25.0, 1.24.1. If you are on something much newer or older, the details may have shifted.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.

## Edge cases

- Note: if the integration still isn't created after disabling Segment, check the /graphql response on its own - a later commenter hit a separate 500 tied to their Stripe key.

## Sources

- https://github.com/getlago/lago/issues/515


---

Source: [Vectle](https://vectle.com/skills/skl_lB07_0bxVszMf_uAxELKWA). Version: `skv_HL8n5yrrMxO3qImfB6QVjg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
