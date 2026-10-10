---
name: "porter-set-secrets-are-unviewable-one-273433bc9cc0d8f5"
description: "# Porter: secrets are write-only, and editing a shared env group redeploys everything From Porter's official app-configuration docs, two behaviors that surprise teams: 1."
metadata:
  skill_id: "skl_KMX2VBO8jRxnp-62zNeZWg"
  title: "Porter: set secrets are unviewable; one env group edit redeploys every app using it"
  version: "skv_9teZyRCMJolzCtXCRgpWRg"
  updated: "2026-10-03T04:46:39.442593+00:00"
  canonical_url: "https://vectle.com/skills/skl_KMX2VBO8jRxnp-62zNeZWg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# Porter: set secrets are unviewable; one env group edit redeploys every app using it

## TL;DR

Context: Porter official docs (applications/deploy/configuring-application-services.mdx, porter-dev/docs): secrets marked via the lock icon cannot be viewed after they are set , you can update them but not retrieve them. Both variables and secrets are injected into containers at runtime. Environment groups hold variables shared across applications; when you update a variable in an environment group, Porter automatically triggers a deployment for all applications using that group.

Use this when you run into the situation in the title.

**When not to use this skill:** unrelated tasks. It covers only the procedure above.

## Compatibility

The steps above apply to the commands named in them. This skill does not pin a version, so if a flag looks different on your machine, check your installed version's docs first.

## Details

# Porter: secrets are write-only, and editing a shared env group redeploys everything From Porter's official app-configuration docs, two behaviors that surprise teams: 1. Secrets are write-only in the dashboard. Click the lock icon on an env var and its value can never be viewed again: you can update it, but not retrieve it. If you did not store the value elsewhere, rotation means generating a new one, not reading the old one. Both plain variables and secrets are injected into containers at runtime either way. 2. Environment groups are shared and live. Update one variable in a group and Porter automatically triggers a deployment for every application using that group. That is convenient for a database password rotation and dangerous for a typo: one edit redeploys your whole fleet. Related cert note from the same docs: Porter provisions and renews Let's Encrypt certificates for custom domains automatically, and complex routing goes through NGINX ingress annotations (`nginx.ingress.kubernetes.io/` prefix) applied directly to the ingress resource. Check group membership before editing a shared variable, and treat a group edit like a deploy, because it is one.

Porter automatically provisions and renews SSL certificates for custom domains via Let's Encrypt; advanced routing uses NGINX ingress annotations with the nginx.ingress.kubernetes.io/ prefix.


---

Source: [Vectle](https://vectle.com/skills/skl_KMX2VBO8jRxnp-62zNeZWg). Version: `skv_9teZyRCMJolzCtXCRgpWRg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
