---
name: "nodejs-high-memory-usage-when-using-pn-fe45e3864dfb4dd8"
description: "Railpack: nodeJS high memory usage when using pnpm with devEngines.packageManager. The verified fix is Fix: The reporter's own resolution: remove a stray `.nvmrc` file that was conflicting with version resolution; after that memory stayed at the expected level. Use this when you hit the symptoms above in railpack; not for unrelated railpack errors or general setup questions."
metadata:
  skill_id: "skl_nL36yovKeXkZx79JaC8DLA"
  title: "NodeJS high memory usage when using pnpm with devEngines.packageManager"
  version: "skv_2nVHMSYUASSyRq-IKp0Tfw"
  updated: "2026-10-03T05:09:01.369467+00:00"
  canonical_url: "https://vectle.com/skills/skl_nL36yovKeXkZx79JaC8DLA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/railwayapp/railpack/issues/616\"]"
---

## TL;DR

Fix: The reporter's own resolution: remove a stray `.nvmrc` file that was conflicting with version resolution; after that memory stayed at the expected level.

## The error

```text
Node.js monorepo: switching version management to `devEngines.runtime` + `devEngines.packageManager` in package.json makes Railway report ~3x memory usage (200MB -> 700MB) for the same app.
```

## Fix

1. The reporter's own resolution: remove a stray `.nvmrc` file that was conflicting with version resolution; after that memory stayed at the expected level.

Success check: the symptom above is gone and the original operation completes.

## When to use

- You hit this exact symptom in railpack.
- You want the verified fix without digging through the thread.

## When not to use

- A different error in railpack, even a similar-looking one.
- General railpack setup or credential questions.

## Compatibility

- Railpack (railwayapp/railpack)

## Variant phrasings

- How to fix "nodeJS high memory usage when using pnpm with devEngines.packageManager" in railpack
- railpack: nodeJS high memory usage when using pnpm with devEngines.packageManager

## Source

- https://github.com/railwayapp/railpack/issues/616

---

Source: [Vectle](https://vectle.com/skills/skl_nL36yovKeXkZx79JaC8DLA). Version: `skv_2nVHMSYUASSyRq-IKp0Tfw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
