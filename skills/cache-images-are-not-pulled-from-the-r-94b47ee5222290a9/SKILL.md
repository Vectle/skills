---
name: "cache-images-are-not-pulled-from-the-r-94b47ee5222290a9"
description: "Railpack: cache images are not pulled from the registry. The verified fix is Fix: Maintainer iloveitaly (building on community fix PR #595 from mvanhorn plus review from mabadir): fixed the frontend import cache and added cache import/export support to the `railpack build` command, included in the next release. Use this when you hit the symptoms above in railpack; not for unrelated railpack errors or general setup questions."
metadata:
  skill_id: "skl_8JJnpW8OEY-1w6FzZkN3jQ"
  title: "Cache images are not pulled from the registry"
  version: "skv_z2BGAnVtJrlZXAuQRIhORg"
  updated: "2026-10-03T05:11:28.236331+00:00"
  canonical_url: "https://vectle.com/skills/skl_8JJnpW8OEY-1w6FzZkN3jQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Fix: Maintainer iloveitaly (building on community fix PR #595 from mvanhorn plus review from mabadir): fixed the frontend import cache and added cache import/export support to the `railpack build` command, included in the next release.

## The error

```text
Using Railpack locally with BuildKit (`docker buildx build ... --build-arg BUILDKIT_SYNTAX=...` with a local registry): cache images are pushed after the build but never pulled before it, so every build is cold. `frontend.go`'s `Build()` never set `CacheImports` on its internal `client.Solve()` call.
```

## Fix

1. Maintainer iloveitaly (building on community fix PR #595 from mvanhorn plus review from mabadir): fixed the frontend import cache and added cache import/export support to the `railpack build` command, included in the next release.

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

- How to fix "cache images are not pulled from the registry" in railpack
- railpack: cache images are not pulled from the registry

## Source

- https://github.com/railwayapp/railpack/issues/557

---

Source: [Vectle](https://vectle.com/skills/skl_8JJnpW8OEY-1w6FzZkN3jQ). Version: `skv_z2BGAnVtJrlZXAuQRIhORg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
