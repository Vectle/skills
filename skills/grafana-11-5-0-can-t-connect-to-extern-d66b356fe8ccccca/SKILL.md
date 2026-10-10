---
name: "grafana-11-5-0-can-t-connect-to-extern-d66b356fe8ccccca"
description: "Shows how to fix grafana 11.5.0 can't connect to external MySQL database after upgrade from 11.3.1 version. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_EKUC4qJjCQdo_Xsqqw5qJg"
  title: "Grafana 11.5.0 can't connect to external MySQL database after upgrade from 11.3.1 version"
  version: "skv_bdNq2oACvfFAWKEv6j0fnw"
  updated: "2026-10-03T14:17:48.248753+00:00"
  canonical_url: "https://vectle.com/skills/skl_EKUC4qJjCQdo_Xsqqw5qJg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

After upgrade Grafana to 11.5.0 using official Helm chart from 11.3.1 or 11.4.0 versions, the k8s pod can't start successfully returning these errors:

## Steps

1. Grafana 11.5.0 failing to connect to an external MySQL database after upgrading from 11.3.1/11.4.0 was fixed by upgrading to 11.6.1; the reporter confirmed the pod starts and everything works there (also verified with PostgreSQL). If Grafana won't start against your database right after an upgrade, check whether a newer patch release already fixed it before digging into your DB config.

## When to use

Use this skill when you run into "Grafana 11.5.0 can't connect to external MySQL database after upgrade from 11.3.1 version".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

Versions mentioned in the source: 11.5.0, 11.3.1, 11.4.0, 11.6.1. If you are on something much newer or older, the details may have shifted.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_EKUC4qJjCQdo_Xsqqw5qJg). Version: `skv_bdNq2oACvfFAWKEv6j0fnw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
