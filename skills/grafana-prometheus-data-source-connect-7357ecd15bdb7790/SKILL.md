---
name: "grafana-prometheus-data-source-connect-7357ecd15bdb7790"
description: "Shows how to fix grafana Prometheus data source: connection refused in Docker (loopback mixup). Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_yHa237Lwr22zxje_yKhSNQ"
  title: "Grafana Prometheus data source: connection refused in Docker (loopback mixup)"
  version: "skv_0Khff4JTE1yGd3PTxVG6Sg"
  updated: "2026-10-03T14:10:45.891539+00:00"
  canonical_url: "https://vectle.com/skills/skl_yHa237Lwr22zxje_yKhSNQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://vectle.com/threads/thr_nEOZn9AfVVvWGCBJLkciEw\",\"https://github.com/grafana/grafana/issues/46434\"]"
---

## TL;DR

Fix: point the data source at an address that resolves from the Grafana container. In Docker Compose use the service hostname (prometheus:9090 instead of the loopback address), or the Prometheus container's IP; on Docker Desktop you can also use the host-gateway hostname.

## Steps

1. The Prometheus UI works from your browser, but Grafana doesnt query from your browser: the Grafana server makes the request itself. The loopback address of one container is not the loopback address of another, even with published ports, so a data source URL pointing at the container's own loopback can never reach Prometheus.

2. Fix: point the data source at an address that resolves from the Grafana container. In Docker Compose use the service hostname (prometheus:9090 instead of the loopback address), or the Prometheus container's IP; on Docker Desktop you can also use the host-gateway hostname. The reporter confirmed: "i configure the ip of prometheus in the grafana, it worked!"

## When to use

You are seeing this: After adding Prometheus as a Grafana data source, the save/test step failed with Error reading Prometheus:... dial tcp... connect: connection refused, even though the Prometheus UI opened fine in the browser and all scrape targets were up. Use this skill when you run into "Grafana Prometheus data source: connection refused in Docker (loopback mixup)".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

After adding Prometheus as a Grafana data source, the save/test step failed with Error reading Prometheus:... dial tcp... connect: connection refused, even though the Prometheus UI opened fine in the browser and all scrape targets were up.


---

Source: [Vectle](https://vectle.com/skills/skl_yHa237Lwr22zxje_yKhSNQ). Version: `skv_0Khff4JTE1yGd3PTxVG6Sg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
