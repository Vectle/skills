---
name: "error-from-server-forbidden-pods-is-fo-b7e76c1e4cc5a300"
description: "Routes kubectl RBAC Forbidden errors. Use when the API server answers Forbidden and names a user or service account that cannot perform a verb on a resource. Not for Unauthorized (auth failed) or connection errors."
metadata:
  skill_id: "skl_wPuDJ_ItysZMadO9oI0UVw"
  title: "Error from server (Forbidden): pods is forbidden"
  version: "skv_4QryCzd6QQTQjxVvY55h7A"
  updated: "2026-10-03T05:34:31.979164+00:00"
  canonical_url: "https://vectle.com/skills/skl_wPuDJ_ItysZMadO9oI0UVw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

Your identity has no RBAC rule allowing that verb on that resource. Nothing is broken - the API server is doing its job. Read the error like a sentence: it names the identity, the verb, the resource, and the scope. Get a Role plus RoleBinding (or ClusterRole plus ClusterRoleBinding for cluster scope) granting it, confirm with kubectl auth can-i, and the same command succeeds.

## The error
```text
Error from server (Forbidden): pods is forbidden: User "system:serviceaccount:dev:deployer" cannot list resource "pods" in API group "" in the namespace "dev"
```

## What to do
1. Reproduce it as a yes/no:
```bash
kubectl auth can-i list pods -n dev
```
   Expected: Prints `no`, confirming the denial.
2. Have an admin grant the permission, e.g.:
```bash
kubectl create role pod-reader --verb=get,list,watch --resource=pods -n dev
kubectl create rolebinding pod-reader-binding --role=pod-reader --serviceaccount=dev:deployer -n dev
```
   Expected: Role and binding created.
3. Re-check:
```bash
kubectl auth can-i list pods -n dev
```
   Expected: Prints `yes`.
4. Re-run the original command.
   Expected: Resource list instead of Forbidden.

## When this applies
- any Error from server (Forbidden) naming a user or service account
- CI service accounts with too-narrow roles
- new namespaces where bindings were never created

## When it does NOT apply
- Unauthorized / invalid bearer token (authentication failed, not authorization)
- connection refused or TLS errors

## Works with
all kubectl versions against RBAC-enabled clusters

### secrets is forbidden: User ... cannot get resource "secrets"
Same shape, different resource. Same fix: grant the verb on that resource.

### ... is forbidden: User ... cannot list resource ... at the cluster scope
Cluster scope means you need a ClusterRole plus ClusterRoleBinding, not a namespaced Role.

## Why it happens
RBAC is deny-by-default and additive: without a rule that matches identity, verb, resource, and scope, the API server returns 403. The error message already contains every field you need to write the missing rule.

## Edge cases
- A RoleBinding can only reference a ClusterRole for cluster-wide grants via a ClusterRoleBinding - a RoleBinding pointing at a ClusterRole still only grants within its namespace.
- Impersonation headers (--as) are great for testing: kubectl auth can-i ... --as=system:serviceaccount:dev:deployer.

## Resolved from
gh:aixintan90/errdex (k8s error index) - https://github.com/aixintan90/errdex/blob/HEAD/db/k8s/forbidden-cannot-list-resource.md

---

Source: [Vectle](https://vectle.com/skills/skl_wPuDJ_ItysZMadO9oI0UVw). Version: `skv_4QryCzd6QQTQjxVvY55h7A`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
