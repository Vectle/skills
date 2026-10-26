---
name: "multiple-mgt-web-parts-on-one-page-cra-9f1f10e3b7a3820b"
description: "Fixes multiple Microsoft Graph Toolkit SPFx web parts on one SharePoint page crashing with 'mgt-person already used with this registry'. Use this when the second web part fails while the first loads. Not for single web parts or for non-SPFx MGT usage."
metadata:
  skill_id: "skl_H34L6Iw8jCgyXT5RZ5eiDA"
  title: "Multiple MGT web parts on one page crash: mgt-person already used with this registry"
  version: "skv_pHKuiJVKLbU8DKxpG1j4KA"
  updated: "2026-10-03T05:56:06.091282+00:00"
  canonical_url: "https://vectle.com/skills/skl_H34L6Iw8jCgyXT5RZ5eiDA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://vectle.com/threads/thr_o2wmZE94dnpzcvFikZS4hA\",\"https://github.com/microsoftgraph/microsoft-graph-toolkit/issues/229\"]"
---

TL;DR: if two or more SPFx web parts using the Microsoft Graph Toolkit on the same SharePoint page crash the second one with `the name "mgt-person" has already been used with this registry`, the MGT SPFx packaging registered the same custom elements once per web part. Update `@microsoft/mgt-spfx` to a version containing the fix; users confirmed multiple web parts then work. Also keep imports consistent: import everything from `@microsoft/mgt-spfx` or from `@microsoft/mgt-react/dist/es6/spfx` (e.g. `MgtTemplateProps` comes from the spfx path), never a mix of top-level `@microsoft/mgt-react` paths, or duplicate module instances re-register the elements.

```text
Failed to execute 'define' on 'CustomElementRegistry': the name "mgt-person" has already been used with this registry
```

## Steps

1. Update @microsoft/mgt-spfx to a release containing the packaging fix.

2. Normalize imports to a single path family.

3. Load two web parts on one page.

   Expected: both load. Success check: no registry crash on the second part.

## When to use this

- First web part loads, second crashes with the already-used registry error.
- Reinstalling node_modules does not help.

## When NOT to use this

- A single web part fails; that is a different problem.
- Non-SPFx MGT usage; the packaging bug was SPFx-specific.

## Compatibility

- @microsoft/mgt-spfx fixed releases.

## Variant phrasings

- "mgt-person already used with this registry"
- "multiple MGT web parts same page crash"

## Root cause

Each web part bundle registered the same custom elements, and the CustomElementRegistry rejects duplicate definitions.

## Edge cases

- Mixed import paths create duplicate module instances even on fixed versions; keep them consistent.

Source: https://vectle.com/threads/thr_o2wmZE94dnpzcvFikZS4hA

---

Source: [Vectle](https://vectle.com/skills/skl_H34L6Iw8jCgyXT5RZ5eiDA). Version: `skv_pHKuiJVKLbU8DKxpG1j4KA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
