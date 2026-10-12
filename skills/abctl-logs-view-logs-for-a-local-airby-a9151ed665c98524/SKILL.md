---
name: "abctl-logs-view-logs-for-a-local-airby-a9151ed665c98524"
description: "There is no abctl logs command: abctl only has local, images, and version. A local Airbyte runs inside a kind Kubernetes cluster named airbyte-abctl, so fetch logs with kubectl against the airbyte-abctl namespace. Use for platform/pod logs from abctl local install. Not for Airbyte Cloud logs, UI job history, or self-hosted clusters with custom names."
metadata:
  skill_id: "skl_BTyltpj8HGEMoB6v2uWYwA"
  title: "abctl logs: view logs for a local Airbyte deployment with kubectl"
  version: "skv_mIp0vwRqndEKeWjtTSnF1w"
  updated: "2026-10-11T17:01:48.85081+00:00"
  canonical_url: "https://vectle.com/skills/skl_BTyltpj8HGEMoB6v2uWYwA"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

## TL;DR
There is no `abctl logs` command: abctl only has three commands (`local`, `images`, `version`). Your local Airbyte runs inside a kind Kubernetes cluster called `airbyte-abctl`, so you fetch logs with kubectl against the `airbyte-abctl` namespace: list pods, then `kubectl --namespace airbyte-abctl logs [pod-name]`. Export the kubeconfig first with `kind export kubeconfig -n airbyte-abctl` if kubectl cannot see the cluster.

### Verbatim error

```text
$ abctl logs
Error: unknown command "logs" for "abctl"
```

`abctl --help` confirms the only commands are `local`, `images`, and `version`; nothing prints logs.

## When this applies

- You installed Airbyte locally with `abctl local install` and need logs from the platform pods (server, worker, connector pods).
- You typed `abctl logs` and got `unknown command`.
- You run `abctl local status` but it only shows install state, not pod logs.

## When this does NOT apply

- Airbyte Cloud (remote UI/API) logs: those come from the Cloud API, not abctl.
- Sync/job record logs in the Airbyte UI: open the connection's job history instead; this skill is about platform/pod logs.
- Self-hosted Airbyte on your own Kubernetes: kubectl works the same, but the cluster name and namespace are yours, not `airbyte-abctl`.

## Fix

### 1. Point kubectl at the abctl cluster

```bash
kind export kubeconfig -n airbyte-abctl
```

Expected output: a `Writing "kubeconfig" ...` confirmation, or no output. Now kubectl talks to the cluster abctl created.

### 2. List the running pods

```bash
kubectl --namespace airbyte-abctl get pods
```

Expected output: a table of pods such as `airbyte-abctl-server-...`, `airbyte-abctl-worker-...`. Copy the full pod name you care about.

### 3. Read the logs

```bash
kubectl --namespace airbyte-abctl logs [pod-name]
```

Expected output: the pod's log stream. Flags that help:

```bash
kubectl --namespace airbyte-abctl logs -f [pod-name]         # follow live
kubectl --namespace airbyte-abctl logs --previous [pod-name] # logs from a crashed container
kubectl --namespace airbyte-abctl logs -c [container] [pod-name] # one container in a multi-container pod
```

### 4. (Install problems only) Re-run abctl verbosely

```bash
abctl -v local install
```

Expected output: verbose debug output from abctl itself, useful when the failure is in the install step rather than in a running pod.

## Variant phrasings

### How do I see Airbyte server logs after abctl local install
Same steps: kubectl against namespace `airbyte-abctl` is the only log path; `abctl local status` shows install state, not logs.

### abctl logs unknown command
Expected. `abctl` has three commands: `local`, `images`, `version`. Logs are a kubectl operation, steps above.

### I just want an abctl logs command
There isnt one. If you came here looking for a single command, this is the replacement:

```bash
kubectl --namespace airbyte-abctl logs [pod-name]
```

## Why it happens

abctl is a thin installer: it creates a kind Kubernetes cluster (named `airbyte-abctl`) and Helm-installs the Airbyte chart plus the NGINX ingress into it. All the platform processes run as pods in that cluster, so log access is a Kubernetes operation and abctl never gained a `logs` subcommand.

## Edge cases

- `kubectl get pods` shows nothing or connection refused: the kind cluster is not running; re-run `abctl local install` (it reuses existing state) or `abctl local status` first.
- Multiple containers in a pod (e.g. init containers): kubectl prints an error naming the containers; pick one with `-c`.
- Long-dead pods: `--previous` only covers the last terminated container; for historical crashes, check the persistence volume or re-run and reproduce.

## Tool compatibility

abctl v0.x (`local`, `images`, `version` commands) on Linux/macOS/Windows; requires kind and kubectl CLIs. Namespace is `airbyte-abctl` on default installs; custom installs may differ, check `abctl -v local status` for the cluster name.

## Related skills
- how to read abctl logs for a broken local deployment: https://vectle.com/skills/skl_U1_6jcOXB6KZUJLP9Aj1Xg
- Tekton: debugging a failed PipelineRun - standard kubectl recipe: https://vectle.com/skills/skl_7kqplu1XHEEFJvIwpv3jHw
- how to read Kubernetes events for root cause: https://vectle.com/skills/skl_3ojfqLJZsGcgEOk6SrJWYw

## Provenance
Command list verified against the official abctl docs (abctl has three commands: local, images, version) and the Airbyte developing-locally guide.


---

Source: [Vectle](https://vectle.com/skills/skl_BTyltpj8HGEMoB6v2uWYwA). Version: `skv_mIp0vwRqndEKeWjtTSnF1w`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
