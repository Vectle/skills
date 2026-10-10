---
name: "pscale-auth-login-hangs-browser-doesn-32bba340b40b7bb6"
description: "Fixes pscale auth login hanging when no browser opens. Use when the PlanetScale CLI login stalls on headless servers, in CI, or over SSH without browser forwarding. Switches to service-token auth instead of the interactive browser flow. Not for auth failures after a successful login."
metadata:
  skill_id: "skl_Jjpv4itEZ8T1ZMH8ExSEMw"
  title: "pscale auth login hangs / browser doesn't open - use service tokens"
  version: "skv_svi-YKeHtxItTVY8Aywcsg"
  updated: "2026-10-03T05:57:52.039281+00:00"
  canonical_url: "https://vectle.com/skills/skl_Jjpv4itEZ8T1ZMH8ExSEMw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# pscale auth login hangs / browser doesn't open - use service tokens

TL;DR: the browser-based login needs a local browser, which headless environments do not have. Create a service token in the PlanetScale dashboard (settings > service tokens) with the permissions the job needs, then authenticate non-interactively with the token id and token instead of `pscale auth login`.

```text
pscale auth login hangs with no browser opening
```

## Steps

1. In the PlanetScale dashboard, create a service token with the minimum permissions the job needs. Copy the token id and the token value.

2. Provide them to the CLI as the service-token env vars (or the CLI's service-token flags) instead of running the browser login.

3. Rerun the pscale command. Expected: it authenticates without any browser step.

4. Still stuck: confirm the token has grants on the target database/branch — a valid token with no grants fails later, not at login.

## When this applies

- `pscale auth login` hanging on a headless server, in CI, or over SSH
- Docker builds that need pscale access
- any automation that cannot click through a browser

## When it doesn't

- `Authentication failed` after a completed login — the session is the problem, not the browser
- local laptops where the browser opens fine
- service-token permission errors (fix the grants, not the login method)

## Compatibility

pscale CLI; PlanetScale dashboard service tokens. Verified against the pscale-auth community skill.

## Variant phrasings

- pscale auth login hangs
- pscale auth login browser doesn't open
- planetscale service token CLI headless

## Root cause

The interactive login opens a YOUR_HOST callback in your browser; with no browser the CLI waits on a callback that never comes. Service tokens are static credentials with explicit grants, designed for exactly this non-interactive case.

## Edge cases

- service tokens cannot do the interactive OAuth dance; keep one login method per environment
- give the token the narrowest grants the job needs; broad tokens in CI are a leak waiting to happen
- rotating a service token means updating every place it is stored

---

Source: [Vectle](https://vectle.com/skills/skl_Jjpv4itEZ8T1ZMH8ExSEMw). Version: `skv_svi-YKeHtxItTVY8Aywcsg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
