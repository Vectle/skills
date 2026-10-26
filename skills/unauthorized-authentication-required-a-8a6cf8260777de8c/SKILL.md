---
name: "unauthorized-authentication-required-a-8a6cf8260777de8c"
description: "Diagnoses 'unauthorized: authentication required' when pushing or pulling images to Azure Container Registry. Use when an agent sees this from docker push or pull against an ACR login server. Covers az acr login, expired tokens, admin user settings, and managed identity auth. Not for network or DNS failures reaching the registry."
metadata:
  skill_id: "skl_q5jdSBAOkNGWROoT2qpSow"
  title: "unauthorized: authentication required (Azure Container Registry push)"
  version: "skv_50zkvjW-syaRBTimla-Hjg"
  updated: "2026-10-03T04:50:07.819715+00:00"
  canonical_url: "https://vectle.com/skills/skl_q5jdSBAOkNGWROoT2qpSow"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/microsoft/build26-lab512-hands-on-with-the-latest-cobalt-vms-from-code-to-cloud-deployment/blob/HEAD/docs/troubleshooting.md\"]"
---

# unauthorized: authentication required (Azure Container Registry push)

## TL;DR
Docker is talking to the registry anonymously. Log in first with `az acr login`, and if that does not stick, check that the admin user is enabled or use a service principal with pull/push rights. Expired tokens cause this too.

## The error
```
unauthorized: authentication required
```
(on `docker push [registry].azurecr.io/[image]` or `docker pull`.)

## Fix it
1. Log in: `az acr login --name [registry]`. Expected: "Login Succeeded".
2. Retry the push or pull. Expected: it works.
3. If login succeeds but the push still fails, the token may be expiring mid-run. Log in again right before the push. Expected: the push completes.
4. For CI, use a service principal with the AcrPush role instead of the admin user: `docker login [registry].azurecr.io -u [app-id] -p [client-secret]`. Expected: non-interactive auth works.
5. If you rely on the admin user, confirm it is enabled: registry Settings, Access keys. Expected: the admin user toggle is on and the credentials work.

## When to use this
- An agent sees "unauthorized: authentication required" on docker push or pull to ACR.
- CI pipelines that push images to Azure Container Registry.

## When NOT to use this
- DNS or network errors reaching the login server. Those fail before auth.
- "repository does not exist" errors. Those are naming problems after successful auth.

## Compatibility
- Azure Container Registry, Docker CLI, Azure CLI.

### Variant phrasings
- "unauthorized: authentication required"
- "no basic auth credentials" on ACR push

## Root cause
ACR rejects anonymous pushes and pulls on private registries. The usual triggers are never having logged in, an expired token from an earlier `az acr login`, or the admin user being disabled while the pipeline still uses it.

## Edge cases
- Tokens from `az acr login` last about 3 hours. Long builds that push at the end fail with this.
- Private endpoints change nothing about auth. If DNS resolves privately but auth fails, it is still a login problem.


---

Source: [Vectle](https://vectle.com/skills/skl_q5jdSBAOkNGWROoT2qpSow). Version: `skv_50zkvjW-syaRBTimla-Hjg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
