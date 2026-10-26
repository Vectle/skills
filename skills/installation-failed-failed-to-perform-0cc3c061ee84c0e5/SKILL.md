---
name: "installation-failed-failed-to-perform-0cc3c061ee84c0e5"
description: "Routes helm OCI chart pull 401s. Use when helm install from an oci:// URL fails with FetchReference unauthorized. Not for unknown chart tags, DNS failures, or non-OCI repos."
metadata:
  skill_id: "skl_XAlmIoBJuC3hwZNQP1LdfQ"
  title: "INSTALLATION FAILED: failed to perform \"FetchReference\": unauthorized: authentication required"
  version: "skv_iLacxUmGa1TaflwytKjcVQ"
  updated: "2026-10-03T06:09:42.493312+00:00"
  canonical_url: "https://vectle.com/skills/skl_XAlmIoBJuC3hwZNQP1LdfQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/openova-io/openova/commit/6f9ee43a9d5eb622a5bff930269aab4588d8a5eb\"]"
---

The OCI registry hosting the chart needs a login and helm has none cached - usually a private package (GHCR, ACR, ECR). Run helm registry login [registry-host] with a token that has package read permission. For GHCR that is a token with packages read scope. Then re-run the install - the fetch succeeds.

## The error
```text
Error: INSTALLATION FAILED: failed to perform "FetchReference" on source: GET "https://ghcr.io/v2/[org]/[chart]/manifests/[tag]": unexpected status code 401: unauthorized: authentication required
```

## What to do
1. Log in to the registry:
```bash
echo [token] | helm registry login ghcr.io -u [username] --password-stdin
```
   Expected: Prints `Login Succeeded`.
2. Re-run the install:
```bash
helm install [release] oci://ghcr.io/[org]/[chart] --version [tag]
```
   Expected: Install starts instead of the 401.
3. In CI, grant the job packages read and log in with the job token before install.
   Expected: Green run.

## When this applies
- helm install/upgrade/template against oci:// chart URLs
- the exact FetchReference 401 unauthorized message
- private GHCR/ACR/ECR chart packages

## When it does NOT apply
- 404 or MANIFEST_UNKNOWN (wrong chart path or tag)
- classic chart repository 401s (use helm repo add credentials instead)

## Works with
helm 3.8+ (OCI GA); any OCI registry

### failed to authorize: failed to fetch anonymous token -  unexpected status code 401
Same missing-login cause on registries with token auth. Same helm registry login fix.

## Why it happens
OCI registries answer 401 to anonymous pulls of private artifacts. Helm keeps registry credentials in ~/.config/helm/registry/config.json - empty on a fresh machine or CI runner, so the pull is anonymous and rejected.

## Edge cases
- helm registry login credentials expire with the token - CI must log in on every run.
- GHCR fine-grained PATs need the right repository access; a token without package read still 401s after a successful login.

## Resolved from
gh:openova-io/openova (preflight CI fix commit) - https://github.com/openova-io/openova/commit/6f9ee43a9d5eb622a5bff930269aab4588d8a5eb

---

Source: [Vectle](https://vectle.com/skills/skl_XAlmIoBJuC3hwZNQP1LdfQ). Version: `skv_iLacxUmGa1TaflwytKjcVQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
