---
name: "how-to-log-denied-traffic-from-kuberne-be5311ad4de57ff2"
description: "how to log denied traffic from Kubernetes network policies"
metadata:
  skill_id: "skl_56Le4CeNdBrebxTmImAttA"
  title: "how to log denied traffic from Kubernetes network policies"
  version: "skv_BqLNuFsLzAQaAyn3tD2EdQ"
  updated: "2026-10-26T21:02:38.922391+00:00"
  canonical_url: "https://vectle.com/skills/skl_56Le4CeNdBrebxTmImAttA"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Identify the CNI before anything else: run `kubectl get daemonset -n kube-system` and note the agent (cilium, calico-node, kube-router, or another). Expected: one networking DaemonSet; every later step depends on which one it is, because NetworkPolicy enforcement and logging live in the CNI, not in Kubernetes.

On Cilium, watch denied flows live: run `hubble observe --verdict DROPPED --namespace [namespace]` (or `kubectl exec -n kube-system ds/cilium -- cilium-dbg monitor --type drop` without Hubble). Expected: one line per dropped packet with source, destination, and the policy verdict, so you can see exactly which policy denied the flow.

On Cilium, make it persistent: confirm Hubble is enabled with `kubectl get pods -n kube-system -l k8s-app=hubble-relay` and keep the relay and UI deployed; flow records are retained by Hubble so denied traffic stays queryable after the fact instead of only while you watch. Expected: hubble observe returns historical DROPPED records, not just live ones.

On Calico, add logging at the policy layer: create a GlobalNetworkPolicy ordered just before the denying policy with a rule that matches the same traffic and uses `action: Log`, followed by the existing deny. Expected: Felix logs each matching packet on the node before the deny applies, so denied traffic is recorded even though plain NetworkPolicy drops are silent.

On Calico, read the log on the node: run `kubectl logs -n kube-system -l k8s-app=calico-node -c calico-node` and check the node syslog for the Felix deny entries (fields include src, dst, and the policy tier). Expected: one entry per denied packet once the Log rule is in place; if nothing appears, the Log policy is ordered after the deny or is not matching, so fix the order first.

On any other CNI (or when the steps above show nothing), fall back to the node: reproduce the traffic from a test pod with `curl -v --max-time 5 SERVICE_IP:PORT` from an affected pod (substitute the blocked service IP and port), and at the same time capture on the node interface for that pod IP. Expected: SYNs leaving the pod with no reply and no reset confirm a silent policy drop rather than an application refusal.

Verify end to end: generate one deliberately denied connection (a pod and port your policy blocks) and confirm a corresponding line appears in the Hubble output, the Calico node log, or the capture within a few seconds. Expected: the log line names the same source, destination, and port as your test, which proves the logging path works before you rely on it during a real incident.

---

Source: [Vectle](https://vectle.com/skills/skl_56Le4CeNdBrebxTmImAttA). Version: `skv_BqLNuFsLzAQaAyn3tD2EdQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
