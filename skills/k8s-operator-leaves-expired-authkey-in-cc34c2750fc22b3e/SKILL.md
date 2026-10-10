---
name: "k8s-operator-leaves-expired-authkey-in-cc34c2750fc22b3e"
description: "Fixes the Tailscale Kubernetes operator leaving expired auth keys in proxy Secrets so pods fail to re-authenticate. Use when operator-managed proxies stop working after the auth key expires and the Secret still holds the old key. Covers the verified fix: upgrade the operator past the affected versions. Not for manually created auth keys or non-operator deployments."
metadata:
  skill_id: "skl_ub2ATeM9ob5WbPuPtXn0-g"
  title: "k8s operator leaves expired authkey in proxy Secrets (fix: upgrade operator)"
  version: "skv_xFz_bvRqWHbvl7_Moy-pJQ"
  updated: "2026-10-03T04:41:59.907822+00:00"
  canonical_url: "https://vectle.com/skills/skl_ub2ATeM9ob5WbPuPtXn0-g"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# Fix the k8s operator leaving expired auth keys in proxy Secrets

**TL;DR:** Old operator versions left the expired auth key sitting in the proxy Secret and the pod could not re-authenticate. Upgrade the Tailscale operator and the stale-key problem goes away.

## The error

```text
k8s operator leaving expired authkey in proxy Secrets
```

Symptom level: a Service exposed via the Tailscale operator stops working after key expiry; inspecting the proxy Secret shows the old, expired auth key still there.

## Fix it

### 1. Confirm the operator version

```
kubectl -n tailscale get deployment operator -o jsonpath='{.spec.template.spec.containers[0].image}'
```

Expected: something around 1.6x if you are affected.

### 2. Upgrade the operator

Update your operator manifest or Helm release to a current Tailscale version.

```
helm upgrade tailscale-operator tailscale/tailscale-operator --namespace tailscale
```

(adapt to however you installed it).

Expected: operator pods roll to the new image.

### 3. Recreate the affected proxies

Delete the stale proxy StatefulSet/Secret pair for the broken Service so the operator recreates them fresh:

```
kubectl -n tailscale delete secret [proxy-secret-name]
```

The operator will provision a new ephemeral key on the next reconcile.

Expected: the Service gets a fresh proxy that authenticates cleanly.

### 4. Verify

```
kubectl -n tailscale get pods
tailscale status
```

Expected: proxy pods running, tailnet sees the Service hostname.

## When this applies

- Tailscale Kubernetes operator managed proxies
- Proxy worked, then died around key expiry time
- Secret contains an expired auth key
- Operator version is old (1.6x era)

## When it does not apply

- Hand-rolled tailscaled Deployments (no operator involved)
- Auth keys you created manually and pasted into Secrets
- Proxies that never authenticated in the first place

## Tool compatibility

Tailscale Kubernetes operator, 1.6x affected, fixed in current releases. kubectl 1.25+.

## Variant phrasings

### Proxy Secret has an auth key that no longer works

Same issue. The key is ephemeral and single-use; the fix is the upgrade, not hand-editing the Secret.

## Why it happens

The operator mints ephemeral single-use auth keys per proxy. On affected versions, expiry left the dead key in the Secret and the proxy had no path to get a new one, so it sat unauthenticated.

## Edge cases

- **Do not hand-roll keys into operator Secrets:** the operator owns that lifecycle; manual keys fight the reconciler.
- **StatefulSet vs fresh:** if deleting just the Secret does not trigger recreation, delete the proxy StatefulSet too and let the operator rebuild both.
- **Still stuck after upgrade:** check the operator logs for the reconcile errors; a second, unrelated problem may be hiding behind the first.

---

Source: [Vectle](https://vectle.com/skills/skl_ub2ATeM9ob5WbPuPtXn0-g). Version: `skv_xFz_bvRqWHbvl7_Moy-pJQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
