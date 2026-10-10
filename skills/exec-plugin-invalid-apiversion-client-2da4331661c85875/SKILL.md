---
name: "exec-plugin-invalid-apiversion-client-2da4331661c85875"
description: "Routes kubectl users hitting the removed v1alpha1 exec-plugin auth API. Use when kubectl fails with invalid apiVersion client.authentication.k8s.io/v1alpha1 on any command. Not for v1beta1/v1 exec errors, static token or cert auth problems, or plugin binary crashes."
metadata:
  skill_id: "skl_BsepJeH6D3PGA4HAJhPxNA"
  title: "exec plugin: invalid apiVersion \"client.authentication.k8s.io/v1alpha1\""
  version: "skv_ccCtf2VbhpcSgedQxDK3oA"
  updated: "2026-10-03T05:29:42.706367+00:00"
  canonical_url: "https://vectle.com/skills/skl_BsepJeH6D3PGA4HAJhPxNA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

Your kubeconfig exec plugin entry still uses the v1alpha1 client authentication API, which kubectl removed in v1.26. Bump the apiVersion in that user block to client.authentication.k8s.io/v1beta1 (or v1) - and upgrade the auth plugin binary (aws-iam-authenticator, kubelogin, etc) if it is old. kubectl works again on the next command.

## The error
```text
error: exec plugin: invalid apiVersion "client.authentication.k8s.io/v1alpha1"
```

## What to do
1. Find the offending entry:
```bash
grep -n "client.authentication.k8s.io/v1alpha1" ~/.kube/config
```
   Expected: Shows the user block using the old apiVersion.
2. Edit that user block so the exec stanza reads:
```yaml
users:
- name: [your-user]
  user:
    exec:
      apiVersion: client.authentication.k8s.io/v1beta1
      command: [your-auth-plugin]
```
   Expected: File saves cleanly.
3. If the plugin binary is old, upgrade it too - e.g. `aws-iam-authenticator version`
   Expected: Prints a recent version, no error.
4. Verify:
```bash
kubectl cluster-info
```
   Expected: Prints cluster info instead of the exec plugin error.

## When this applies
- kubectl 1.26 or newer
- kubeconfig users with an exec stanza (EKS, kubelogin, gardener, custom OIDC plugins)
- the exact invalid apiVersion v1alpha1 message

## When it does NOT apply
- exec errors mentioning v1beta1 or v1
- static bearer tokens or client certs in kubeconfig
- plugin binary missing from PATH (different error)

## Works with
kubectl v1.26+; aws-iam-authenticator, kubelogin, gke-gcloud-auth-plugin recent releases

### exec plugin: invalid apiVersion "client.authentication.k8s.io/v1beta1"
Same failure one API version newer. Same fix: move the exec apiVersion to v1.

## Why it happens
Kubernetes deprecated the v1alpha1 exec credential API and kubectl 1.26 stopped parsing it entirely. Old kubeconfig generators (and old plugin docs) still emit v1alpha1, so the config and the client disagree.

## Edge cases
- Managed kubeconfig generators (aws eks update-kubeconfig, gcloud get-credentials) can rewrite the file and reintroduce the old apiVersion - re-check after regenerating.
- Some very old plugins only speak v1alpha1: then the real fix is upgrading the plugin, not editing the version string.

## Resolved from
gh:harishgorla5/project04#1 - https://github.com/harishgorla5/project04/issues/1

---

Source: [Vectle](https://vectle.com/skills/skl_BsepJeH6D3PGA4HAJhPxNA). Version: `skv_ccCtf2VbhpcSgedQxDK3oA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
