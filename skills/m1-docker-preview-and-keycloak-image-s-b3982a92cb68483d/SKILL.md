---
name: "m1-docker-preview-and-keycloak-image-s-b3982a92cb68483d"
description: "Shows how to fix m1 docker preview and keycloak 'image's platform (linux/amd64) does not match the detected host platform. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_t2gouVfJ582bFeZmmYgHaQ"
  title: "M1 docker preview and keycloak 'image's platform (linux/amd64) does not match the detected host platform"
  version: "skv_pPkhOGzaFf8MXMCsfjdFZg"
  updated: "2026-10-03T22:32:52.733697+00:00"
  canonical_url: "https://vectle.com/skills/skl_t2gouVfJ582bFeZmmYgHaQ"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

## TL;DR

[li Etzyio (top answer)] You can try to add this while building the docker images `` --platform linux/amd64 ` from https://github.com/google/cadvisor/issues/2763 https://github.com/Y2Data Context: Stack Overflow #66662820 (top answer, 391 votes, 17 answers): I just downloaded Docker Preview v3.1 https://docs.docker.com/docker-for-mac/apple-m1/ and tried running keycloak.

## Steps

1. [li Etzyio (top answer)] You can try to add this while building the docker images

``` --platform linux/amd64 ```

2. from https://github.com/google/cadvisor/issues/2763 https://github.com/Y2Data

``` docker run -p 8080:8080 -e KEYCLOAK_USER=admin -e KEYCLOAK_PASSWORD [your value] quay.io/keycloak/keycloak:12.0.4 WARNING: The requested image's platform (linux/amd64) does not match the detected host platform (linux/arm64/v8) and no specific platform was requested ```

## When to use

Use this skill when you run into "M1 docker preview and keycloak 'image's platform (linux/amd64) does not match the detected host platform".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

Versions mentioned in the source: Preview v3.1, quay.iokeycloakkeycloak 12.0.4. If you are on something much newer or older, the details may have shifted.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.

## Sources

- https://github.com/google/cadvisor/issues/2763

- https://github.com/Y2Data

- https://docs.docker.com/docker-for-mac/apple-m1/


---

Source: [Vectle](https://vectle.com/skills/skl_t2gouVfJ582bFeZmmYgHaQ). Version: `skv_pPkhOGzaFf8MXMCsfjdFZg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
