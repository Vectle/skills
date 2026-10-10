---
name: "foundry-deploymentnotfound-the-deploym-0e16d1ceb0681ecc"
description: "Guide Foundry DeploymentNotFound: the deployment name must match the dashboard exactly: Keep endpoint and deployment name in environment config and fail fast at startup if either is unset, so the error surfaces before the first call. Use this when you hit exactly this in Foundry DeploymentNotFound. Not for different errors or different tools."
metadata:
  skill_id: "skl_DCAT8UOrCtUQ4BAAG2c1yw"
  title: "Foundry DeploymentNotFound: the deployment name must match the dashboard exactly"
  version: "skv_Z1a3M6Myt_qp1wkuIeWGOA"
  updated: "2026-10-03T05:04:40.841853+00:00"
  canonical_url: "https://vectle.com/skills/skl_DCAT8UOrCtUQ4BAAG2c1yw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: Keep endpoint and deployment name in environment config and fail fast at startup if either is unset, so the error surfaces before the first call. When a Foundry sample or agent fails to connect, diff your config against the project dashboard character by character. The project endpoint must be the full project URL from the portal, and the model deployment name must match the deployment exactly, including version or custom suffixes.

When a Foundry sample or agent fails to connect, diff your config against the project dashboard character by character. The project endpoint must be the full project URL from the portal, and the model deployment name must match the deployment exactly, including version or custom suffixes. A common trap: the dashboard shows the model name (e.g. gpt-4o) but the deployment was named something else (e.g. gpt-4o-prod); using the model name gives a 404 DeploymentNotFound. Keep endpoint and deployment name in environment config and fail fast at startup if either is unset, so the error surfaces before the first call.

## When to use
You hit exactly this: Foundry DeploymentNotFound: the deployment name must match the dashboard exactly in Foundry DeploymentNotFound.

## When not to use
A different error, or the same symptom in a different tool. This page only covers the failure above.

## Compatibility
Foundry DeploymentNotFound.

## Edge cases
- The project endpoint must be the full project URL from the portal, and the model deployment name must match the deployment exactly, including version or custom suffixes.
- A common trap: the dashboard shows the model name (e.g. gpt-4o) but the deployment was named something else (e.g. gpt-4o-prod); using the model name gives a 404 DeploymentNotFound.

---

Source: [Vectle](https://vectle.com/skills/skl_DCAT8UOrCtUQ4BAAG2c1yw). Version: `skv_Z1a3M6Myt_qp1wkuIeWGOA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
