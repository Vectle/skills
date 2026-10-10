---
name: "kustomize-build-fails-may-not-add-reso-006bd5f46a252507"
description: "Routes kustomize duplicate-resource errors. Use when kustomize build fails with may not add resource with an already registered id. Not for load-restrictor or patch-target errors."
metadata:
  skill_id: "skl_Z8ZXIaAqYPE7n-BzW8O-7g"
  title: "kustomize build fails: may not add resource with an already registered id"
  version: "skv_7pim9qAk9mHkFEF9t5HKWA"
  updated: "2026-10-03T16:21:56.60177+00:00"
  canonical_url: "https://vectle.com/skills/skl_Z8ZXIaAqYPE7n-BzW8O-7g"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

Two resources with the same group/version/kind/name/namespace landed in one build - usually a diamond import (two bases both including the same shared file), a file listed twice, or an overlay listing a base plus one of its files. Find the duplicate with kustomize build on each layer, include the shared piece exactly once (or give the copies different namePrefix/nameSuffix), and rebuild.

## The error
```text
Error: accumulating resources: accumulation err='merging resources from 'b.yaml': may not add resource with an already registered id: Deployment.v1.apps/web.[noNs]'
```

## What to do
1. Read the id in the error: Deployment.v1.apps/web.[noNs] means a Deployment named web.
   Expected: Identifies the colliding resource.
2. Find who includes it twice:
```bash
grep -rn 'web' overlays/*/kustomization.yaml bases/*/kustomization.yaml
```
   Expected: Shows the double inclusion.
3. Include the shared file exactly once - restructure the bases, or differentiate with namePrefix/nameSuffix in the intermediate overlays.
   Expected: One copy of each id.
4. Rebuild:
```bash
kustomize build [overlay]
```
   Expected: Build succeeds.

## When this applies
- the exact may not add resource with an already registered id message
- diamond imports through shared bases
- overlays that list a base and one of its files

## When it does NOT apply
- load-restrictor security errors
- patch target not found (the resource is missing, not doubled)

## Works with
kustomize 4.x/5.x

### Namespace.v1.[noGrp]/[name].[noNs] already registered
Same error for a duplicated Namespace - often two slots declaring the same one. Delete one.

## Why it happens
Kustomize keys every resource by its full id (group, version, kind, name, namespace). Two identical ids in one build is ambiguous - it can not know which one you meant - so it errors instead of picking.

## Edge cases
- namePrefix in one overlay leg of a diamond gives the copies different ids and is sometimes the intended fix.
- Components (not bases) are the mechanism for shared opt-in pieces that should not collide.

## Resolved from
gh:mlopsmenacommunity/website (kustomize guide) - https://github.com/mlopsmenacommunity/website/blob/HEAD/content/student-guides/kustomize/mid-detailed.md

---

Source: [Vectle](https://vectle.com/skills/skl_Z8ZXIaAqYPE7n-BzW8O-7g). Version: `skv_7pim9qAk9mHkFEF9t5HKWA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
