---
name: "datadog-on-kubernetes-helm-chart-with-b63a113e70805220"
description: "The supported Kubernetes install is the Helm chart: a DaemonSet agent on every node plus the Cluster Agent for cluster-level metadata. The Datadog Operator is the alternative for GitOps shops. Not the full reference manual."
metadata:
  skill_id: "skl_bcT9NApRbc6BFxLtRTYG-Q"
  title: "Datadog on Kubernetes: Helm chart with DaemonSet agent plus Cluster Agent"
  version: "skv_wJ9WvwV0o2tvFAy37yZX-w"
  updated: "2026-10-03T06:02:52.651818+00:00"
  canonical_url: "https://vectle.com/skills/skl_bcT9NApRbc6BFxLtRTYG-Q"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** The supported Kubernetes install is the Helm chart: a DaemonSet agent on every node plus the Cluster Agent for cluster-level metadata. The Datadog Operator is the alternative for GitOps shops. Use the chart, it handles the RBAC, the cluster agent, and the version matrix for you. Note: the docs also cover the Datadog Operator (datadog/datadog-operator chart plus a datadog-agent.yaml custom resource).

# Datadog on Kubernetes with Helm

Do not hand-roll DaemonSets from blog posts. Use the chart, it handles the RBAC, the cluster agent, and the version matrix for you.

## The standard install

```sh
helm repo add datadog https://helm.datadoghq.com
helm repo update
kubectl create secret generic datadog-secret --from-literal api-key [your key value]
helm install datadog-agent datadog/datadog \
  --set datadog.site=[your site] \
  --set datadog.clusterName=[your cluster name]
```

Point the chart value `datadog.apiKeyExistingSecret` at the secret name you created.

What this gives you: an agent DaemonSet on every node (host metrics, container metrics, autodiscovered checks), the Cluster Agent deployment (cluster-level metadata, external metrics for HPA), and kube-state-metrics wiring.

Note: the docs also cover the Datadog Operator (`datadog/datadog-operator` chart plus a `datadog-agent.yaml` custom resource). Same result, GitOps-friendly. Pick one, not both.

## The container config difference that bites

On hosts the agent reads `datadog.yaml`. In containers, config comes from **environment variables**: `DD_API_KEY` and `DD_SITE` are the required pair. Checks are discovered via **Autodiscovery**, not config files. If you mounted a host-style datadog.yaml into the container and wonder why nothing changed, this is why.

## Checks per track

- `kubectl get pods -n default` (or your namespace): agent pods Running on every node, cluster-agent Running.
- `kubectl exec` into an agent pod and run `agent status`: look for Kubernetes and kubelet checks OK.
- In the app: Infrastructure, Containers should show your nodes within minutes. If not, it is the key/secret or the site, see those skills.

## Traps

- Forgetting `--set datadog.site` when your org is not US1. Same ghost-agent symptom as hosts.
- Autodiscovery annotations go on the workload pods (`ad.datadoghq.com/...`), not on the agent. Wrong placement means your redis check never fires and you blame the agent.
- Upgrading the chart across major versions: read the chart changelog. Values get renamed and silent defaults change (log collection, APM) between majors.

## When to use this

- This covers exactly what the title says: Datadog on Kubernetes.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Datadog; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

---

Source: [Vectle](https://vectle.com/skills/skl_bcT9NApRbc6BFxLtRTYG-Q). Version: `skv_wJ9WvwV0o2tvFAy37yZX-w`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
