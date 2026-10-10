---
name: "failed-to-create-helm-release-with-err-efb1a373347d0804"
description: "Routes helm install --create-namespace RBAC failures. Use when helm reports namespaces is forbidden and the user cannot create resource namespaces. Not for other forbidden resources or chart render errors."
metadata:
  skill_id: "skl_MF4pro6YzwLW4OvGDefoDQ"
  title: "failed to create helm release with error namespaces is forbidden: user cannot create resource \"namespaces\""
  version: "skv_rpnghCMi7Urk-gEzGEP-IQ"
  updated: "2026-10-03T06:04:17.838556+00:00"
  canonical_url: "https://vectle.com/skills/skl_MF4pro6YzwLW4OvGDefoDQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

Your kubeconfig identity can not create namespaces, so helm install --create-namespace dies on the RBAC check before anything installs. Pre-create the namespace yourself (kubectl create namespace [name]) and drop the flag, or get the create verb on namespaces added to your role. Re-run the install and it proceeds.

## The error
```text
failed to create helm release with error namespaces "default" is forbidden: user cannot create resource "namespaces" in API group "" at the cluster scope
```

## What to do
1. Confirm the gap:
```bash
kubectl auth can-i create namespaces
```
   Expected: Prints `no`.
2. Pre-create the namespace (needs someone with rights):
```bash
kubectl create namespace [name]
```
   Expected: namespace/[name] created.
3. Re-run without the flag:
```bash
helm install [release] [chart] -n [name]
```
   Expected: Install proceeds past the namespace check.
4. Lasting fix: have an admin add `create` on `namespaces` to your ClusterRole, then `kubectl auth can-i create namespaces`
   Expected: Prints `yes`.

## When this applies
- helm install with --create-namespace
- the exact namespaces is forbidden message
- locked-down clusters where users get narrow roles

## When it does NOT apply
- forbidden on other resources (deployments, clusterroles) - different rule needed
- namespace already exists (drop the flag)

## Works with
helm 3.x; RBAC-enabled clusters

### INSTALLATION FAILED: ... is forbidden on deployments, serviceaccounts, etc
Same RBAC shape, different resource. Grant the verb on that resource instead.

## Why it happens
--create-namespace makes helm call the namespaces create API before rendering anything. Cluster-scoped, so it needs a ClusterRole rule - a namespaced Role can never grant it.

## Edge cases
- In CI, prefer pre-creating namespaces in a setup step over granting namespace-create to deploy identities.
- Some platforms forbid namespace creation entirely - then the namespace must come from the platform team.

## Resolved from
gh:helm/helm#32511 - https://github.com/helm/helm/issues/32511

---

Source: [Vectle](https://vectle.com/skills/skl_MF4pro6YzwLW4OvGDefoDQ). Version: `skv_rpnghCMi7Urk-gEzGEP-IQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
