---
name: "cannot-establish-control-of-object-alr-5ef02edee4efae3f"
description: "Fixes Crossplane v2 provider upgrades failing with 'cannot establish control of object, already controlled by ProviderRevision'. Use this when the new ProviderRevision cannot take over CRDs. Not for other install failures."
metadata:
  skill_id: "skl_Fhy3wVLxwCiGUWojM5_bNQ"
  title: "cannot establish control of object, already controlled by ProviderRevision on Crossplane v2 upgrade"
  version: "skv_m0rsWgKFAQmUfRE0kJ38gA"
  updated: "2026-10-03T05:39:54.597623+00:00"
  canonical_url: "https://vectle.com/skills/skl_Fhy3wVLxwCiGUWojM5_bNQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: if upgrading providers under Crossplane v2 fails with `cannot establish control of object: [crd] is already controlled by ProviderRevision [old-revision]`, the CRDs still carry ownerReferences pointing at the old ProviderRevision. Upgrade to the patched v2.0/v2.1 release containing PR #6934. Before the patch, the workaround is to manually delete the old inactive ProviderRevision after upgrading the provider (`kubectl delete providerrevision [old-name]`), which lets the new revision take control. Multiple reporters confirmed this is much less destructive than deleting the CRDs.

```text
cannot establish control of object: [crd] is already controlled by ProviderRevision [old-revision]
```

## Steps

1. Upgrade Crossplane to the patched v2.0/v2.1 release (PR #6934).

2. Or as a workaround: `kubectl delete providerrevision [old-name]` after the provider upgrade.

   Expected: the new revision takes control. Success check: providers install cleanly.

## When to use this

- Provider upgrades under Crossplane v2 fail with the control error.

## When NOT to use this

- Other install errors; read the message.
- Crossplane v1; the revision mechanics differ.

## Compatibility

- Crossplane v2 patched releases.

## Variant phrasings

- "crossplane cannot establish control of object"
- "crossplane ProviderRevision already controlled"

## Root cause

Stale ownerReferences on CRDs block the new revision from adopting them.

## Edge cases

- Deleting the CRD outright works but is the nuclear option; prefer deleting the old revision.

---

Source: [Vectle](https://vectle.com/skills/skl_Fhy3wVLxwCiGUWojM5_bNQ). Version: `skv_m0rsWgKFAQmUfRE0kJ38gA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
