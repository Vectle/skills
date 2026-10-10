---
name: "preflight-options-requests-fail-even-w-448627ba8c657a4b"
description: "Fixes preflight (OPTIONS) requests failing on Flipt v2 even with CORS enabled, by upgrading past the v2 beta builds where this was a bug. Use when the OPTIONS request does not get the same CORS settings as GET. Not for CORS misconfigurations in your own reverse proxy."
metadata:
  skill_id: "skl_PiqUYCeqlhPcxAtrKGrEmg"
  title: "Preflight (OPTIONS) Requests Fail even with CORs set"
  version: "skv_eDvc29OszVF0kaua8ypZqw"
  updated: "2026-10-03T04:23:53.805482+00:00"
  canonical_url: "https://vectle.com/skills/skl_PiqUYCeqlhPcxAtrKGrEmg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Upgrade Flipt past the v2 beta builds: preflight (OPTIONS) requests failing despite CORS being enabled was a bug in the v2 betas, fixed in the stable v2 release. If you are on a beta, upgrading is the fix.

## The problem

With `cors: enabled: true` in the Flipt YAML config, GET requests work but the OPTIONS preflight request does not supply the same CORS settings, so flipt-web (or any browser client) fails.

## Fix it

1. Check your Flipt version.
   Success check: you are on a v2 beta build, confirming the bug applies.

2. Upgrade to the stable v2 release or newer.
   Success check: the installed version is past the beta line.

3. Re-run the browser flow that failed.
   Success check: the OPTIONS preflight returns the CORS headers and the request succeeds.

## When this applies

- Flipt v2 beta with `cors: enabled: true` in config.
- GET works, OPTIONS preflight fails.

## When it does not apply

- Flipt v1; the bug is v2-beta-specific.
- CORS failures caused by your own reverse proxy stripping headers.
- Non-browser clients (no preflight involved).

## Compatibility

- Flipt v2 stable+ (fixed). Affected: v2 beta builds.

## Variant phrasings

- Flipt preflight OPTIONS fail CORS set
- flipt-web CORS preflight failure
- Flipt v2 beta CORS bug

## Why it happens

The v2 beta server did not apply the CORS middleware to OPTIONS requests, only to the main routes. The stable release applies it uniformly.

## Edge cases

- If it persists on stable v2, check for a proxy in front of Flipt stripping the headers.
- Source: https://github.com/flipt-io/flipt/issues/4620


---

Source: [Vectle](https://vectle.com/skills/skl_PiqUYCeqlhPcxAtrKGrEmg). Version: `skv_eDvc29OszVF0kaua8ypZqw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
