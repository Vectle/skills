---
name: "failed-to-refresh-token-oauth2-invalid-b680bc713ce7adb5"
description: "Routes kubectl OIDC refresh-token failures via kubelogin-style plugins. Use when kubectl fails with failed to refresh token and an oauth2 invalid_grant. Not for initial login failures, missing client config, or non-OIDC auth."
metadata:
  skill_id: "skl_5RSe0S4uy9-SioJsLnBd0g"
  title: "failed to refresh token -  oauth2: \"invalid_grant\""
  version: "skv_rCcExo5Zxvc-kZ-0wqR02g"
  updated: "2026-10-03T05:33:17.802078+00:00"
  canonical_url: "https://vectle.com/skills/skl_5RSe0S4uy9-SioJsLnBd0g"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

Your OIDC refresh token is dead - expired, revoked, or the identity provider rotated its keys - so the plugin can not mint a new access token. Delete the cached token file kubelogin keeps under ~/.kube/cache/kubelogin and run any kubectl command to trigger a fresh login. The new token pair gets cached and commands work again.

## The error
```text
error: failed to refresh token -  oauth2: "invalid_grant" "Token has been expired or revoked."
```

## What to do
1. Look at the cache:
```bash
ls ~/.kube/cache/kubelogin/
```
   Expected: Shows cached token files keyed by issuer.
2. Drop the stale cache:
```bash
rm -rf ~/.kube/cache/kubelogin/
```
   Expected: No output.
3. Trigger re-auth:
```bash
kubectl get pods
```
   Expected: Browser or device-code login prompt appears.
4. Complete the login, then retry the command.
   Expected: Resource list, no token error.

## When this applies
- kubeconfig users with an OIDC exec plugin (kubelogin, dex-backed setups)
- the exact failed to refresh token / invalid_grant message
- tokens that worked yesterday and broke today

## When it does NOT apply
- first-time login failures (check client ID, issuer URL, redirect)
- token expired and refresh token is not set (enable offline access / refresh tokens at the IdP)

## Works with
kubectl with int128/kubelogin or similar OIDC exec plugins; dex identity providers

### failed to refresh token -  oauth2: token expired and refresh token is not set
The IdP never issued a refresh token. Request the offline_access scope or enable refresh tokens in the client config, then re-authenticate.

### failed to get token -  oauth2: "invalid_grant"
Same dead-token cause during the initial grant. Same cache-clear and re-login fix.

## Why it happens
OIDC access tokens are short-lived; the plugin trades a long-lived refresh token for new ones. When the IdP kills the refresh token (expiry, revocation, key rotation), the trade fails and every kubectl call fails with it.

## Edge cases
- If the IdP application/client itself was deleted or its secret rotated, re-login fails too - check with your cluster admin.
- Corporate proxies that MITM TLS can break the token endpoint; the error then usually mentions x509 instead.

## Resolved from
gh:int128/kubelogin#85 (see also gh:dexidp/dex#2613) - https://github.com/int128/kubelogin/issues/85

---

Source: [Vectle](https://vectle.com/skills/skl_5RSe0S4uy9-SioJsLnBd0g). Version: `skv_rCcExo5Zxvc-kZ-0wqR02g`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
