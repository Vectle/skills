---
name: "error-you-must-be-logged-in-to-the-ser-602649215f327476"
description: "Fixes every kubectl command failing with error: You must be logged in to the server (Unauthorized). Use when the kubeconfig is stale, points at the wrong cluster, or the cloud token expired. Re-fetches provider kubeconfig for EKS, AKS, and GKE, checks current-context, and verifies identity. Not for connection refused, which means the API is unreachable, or x509 unknown authority, which is a CA mismatch."
metadata:
  skill_id: "skl_GDoQVSlh8UWMvNB-7Gm3Hw"
  title: "error: You must be logged in to the server (Unauthorized)"
  version: "skv_j3XGQqd11MOy0rEoIaVSxg"
  updated: "2026-10-03T04:45:25.075244+00:00"
  canonical_url: "https://vectle.com/skills/skl_GDoQVSlh8UWMvNB-7Gm3Hw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/langchain-ai/terraform/blob/HEAD/modules/aws/TROUBLESHOOTING.md\"]"
---

# error: You must be logged in to the server (Unauthorized)

TL;DR: your kubeconfig credentials are stale or point at the wrong place. First check `kubectl config current-context` — half the time you are aimed at the wrong cluster. Then re-fetch the kubeconfig from your provider: `aws eks update-kubeconfig`, `az aks get-credentials`, or `gcloud container clusters get-credentials`.

```text
error: You must be logged in to the server (Unauthorized)
```

## Steps

1. Check where you are pointed:

```bash
kubectl config get-contexts
kubectl config current-context
```

Expected: the context you actually intend. If not, switch:

```bash
kubectl config use-context [name]
```

2. Inspect the active user entry:

```bash
kubectl config view --minify
```

3. Re-fetch the kubeconfig from your provider. EKS:

```bash
aws eks update-kubeconfig --region [region] --name [cluster-name]
```

AKS: `az aks get-credentials --resource-group [resource group] --name [cluster name]`. GKE: `gcloud container clusters get-credentials [cluster name] --region [region]`.

Expected: `Added new context` or `Merged` confirmation.

4. Confirm the cloud identity matches what the cluster expects:

```bash
aws sts get-caller-identity
kubectl cluster-info
```

Expected: cluster-info returns without the Unauthorized error.

5. EKS only: if the cluster was created by a different IAM principal, add yourself to the aws-auth ConfigMap in kube-system — the API server authorizes through it.

## When this applies

- the exact error on all kubectl commands
- after IAM role changes, SSO re-login, or cluster recreation under the same name
- exec-plugin tokens expired (cloud providers mint short-lived ones)

## When it doesnt

- `The connection to the server was refused` — the API is down or the endpoint is wrong, that is reachability not auth
- `x509: certificate signed by unknown authority` — CA mismatch; re-fetching the config also fixes it, but the cause differs
- `forbidden` on one specific resource — RBAC; the login is fine, ask the cluster admin for the role

## Compatibility

kubectl 1.2x and up, EKS/AKS/GKE managed clusters, kubeadm.

## Why it happens

kubectl sends whatever credential the kubeconfig holds: an exec-plugin token, an OIDC token, or a client cert. Cloud exec plugins mint short-lived tokens from your cloud identity; when that identity changes or the cached token expires, the API answers 401 and kubectl prints this generic line.

## Edge cases

- in CI use a dedicated service account token instead of a human kubeconfig
- the KUBECONFIG env var can shadow ~/.kube/config — check it when the context looks right but auth still fails
- on EKS, `aws sts get-caller-identity` is the fastest way to prove which identity you are before blaming kubectl

## Find this skill again

```bash
curl -s 'https://vectle.com/api/v1/search?q=kubectl+must+be+logged+in+server+unauthorized'
```


---

Source: [Vectle](https://vectle.com/skills/skl_GDoQVSlh8UWMvNB-7Gm3Hw). Version: `skv_j3XGQqd11MOy0rEoIaVSxg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
