---
name: "middleware-on-kubernetes-one-daemonset-8f423015d54a28c5"
description: "Guide Middleware on Kubernetes: one DaemonSet per cluster, name each cluster: On Kubernetes, run exactly one Middleware agent DaemonSet per cluster; a second install fights the first and data goes missing. Use this when you hit exactly this in Middleware on Kubernetes. Not for different errors or different tools."
metadata:
  skill_id: "skl_1JJRlHOJrb68wIYl6KWoHQ"
  title: "Middleware on Kubernetes: one DaemonSet per cluster, name each cluster"
  version: "skv_eL2-ytQHFpg5_vaFs_7CSQ"
  updated: "2026-10-03T04:40:34.36575+00:00"
  canonical_url: "https://vectle.com/skills/skl_1JJRlHOJrb68wIYl6KWoHQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: On Kubernetes, run exactly one Middleware agent DaemonSet per cluster; a second install fights the first and data goes missing. If you manage several clusters from one context, set a distinct cluster name per install so data lands under the right cluster. CrashLoopBackOff with OOMKilled means the memory limit is too low, raise it rather than restarting and hoping.

On Kubernetes, run exactly one Middleware agent DaemonSet per cluster; a second install fights the first and data goes missing. If you manage several clusters from one context, set a distinct cluster name per install so data lands under the right cluster. CrashLoopBackOff with OOMKilled means the memory limit is too low, raise it rather than restarting and hoping. Check the agent pod logs with kubectl logs on the DaemonSet pods; missing data with healthy pods usually means the cluster name or API key is wrong. Keep the API key in a secret, not inline in the manifest.

Context: Official docs (docs.middleware.io, Kubernetes agent): documents the Kubernetes install traps: only one DaemonSet per cluster, a distinct cluster name for clusters that share a context, and crash loops from memory limits.

## When to use
You hit exactly this: Middleware on Kubernetes: one DaemonSet per cluster, name each cluster in Middleware on Kubernetes.

## When not to use
A different error, or the same symptom in a different tool. This page only covers the failure above.

## Compatibility
Middleware on Kubernetes.

---

Source: [Vectle](https://vectle.com/skills/skl_1JJRlHOJrb68wIYl6KWoHQ). Version: `skv_eL2-ytQHFpg5_vaFs_7CSQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
