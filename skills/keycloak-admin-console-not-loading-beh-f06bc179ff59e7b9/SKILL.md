---
name: "keycloak-admin-console-not-loading-beh-f06bc179ff59e7b9"
description: "Shows how to fix keycloak admin console not loading behind reverse proxy (hostname/proxy misconfiguration). Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_dDygqA2kQmLqx3mAAPfzIg"
  title: "Keycloak admin console not loading behind reverse proxy (hostname/proxy misconfiguration)"
  version: "skv_00AhtMl0ZLRTpoXSGU6UNQ"
  updated: "2026-10-03T14:18:13.851896+00:00"
  canonical_url: "https://vectle.com/skills/skl_dDygqA2kQmLqx3mAAPfzIg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Set KC_PROXY=edge so Keycloak builds frontend URLs from the incoming request, and do NOT set KC_HOSTNAME_PORT=443 when the proxy already terminates TLS on 443; remove that setting, since the explicit port gets injected into every generated URL and breaks the console.

## Steps

1. The new Keycloak admin console failed to load (blank page / stuck loading) when Keycloak ran behind a reverse proxy. The recurring root cause across dozens of reports was hostname/proxy misconfiguration: Keycloak built frontend URLs with the wrong host, port, or scheme. A classic trigger was setting hostname-port=443 explicitly while also terminating TLS at the proxy, which injected :443 into every generated URL and broke the console.

2. Set KC_PROXY=edge so Keycloak builds frontend URLs from the incoming request, and do NOT set KC_HOSTNAME_PORT=443 when the proxy already terminates TLS on 443; remove that setting, since the explicit port gets injected into every generated URL and breaks the console. Multiple reporters confirmed this exact combination fixed the blank admin console. If it still fails, run with --hostname-debug=true and check the generated URLs for a wrong port or scheme.

## When to use

You are seeing this: The new Keycloak admin console failed to load (blank page / stuck loading) when Keycloak ran behind a reverse proxy. Use this skill when you run into "Keycloak admin console not loading behind reverse proxy (hostname/proxy misconfiguration)".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The recurring root cause across dozens of reports was hostname/proxy misconfiguration: Keycloak built frontend URLs with the wrong host, port, or scheme.


---

Source: [Vectle](https://vectle.com/skills/skl_dDygqA2kQmLqx3mAAPfzIg). Version: `skv_00AhtMl0ZLRTpoXSGU6UNQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
