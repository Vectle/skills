---
name: "you-are-attempting-to-export-metadata-408c6e72f5087490"
description: "Move the metadata export into a server component, usually the parent layout or page. The build passes once no \"use client\" file exports metadata. Applies to: Next.js 13+ app router."
metadata:
  skill_id: "skl_0KIE72x25FAJ-KMcKmWn6g"
  title: "You are attempting to export \"metadata\" from a component marked with \"use client\""
  version: "skv_i1maGVzIJITwb6_qe9KIAA"
  updated: "2026-10-03T05:36:34.960601+00:00"
  canonical_url: "https://vectle.com/skills/skl_0KIE72x25FAJ-KMcKmWn6g"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://nextjs.org/docs/app/building-your-application/optimizing/metadata\"]"
---

## TL;DR
Move the metadata export into a server component, usually the parent layout or page. The build passes once no "use client" file exports metadata.

## The exact error
```text
You are attempting to export "metadata" from a component marked with "use client"
```

## Steps to fix
1. Open the file the build error names and confirm it has "use client" at the top
2. Cut the metadata export out of that file
3. Paste it into the nearest server component (the layout.tsx or page.tsx above it)
4. Run the build again; the error should be gone

## When this applies
- Next.js 13+ app router
- You want page metadata but the file also needs client interactivity

## When this does NOT apply
- Pages router (metadata works differently there)
- Metadata that must be computed from client-side state

## Tool + versions
Next.js 13+ app router

## Why it happens
Metadata is a server-only feature. A "use client" file runs in the browser where the metadata API does not exist, so Next.js rejects the export at build time.

## Edge cases
- generateMetadata has the same restriction
- You can still read the metadata in the client component via props

## Where this came from
Resolved from a real public thread: https://nextjs.org/docs/app/building-your-application/optimizing/metadata (docs:metadata-client-component).

---

Source: [Vectle](https://vectle.com/skills/skl_0KIE72x25FAJ-KMcKmWn6g). Version: `skv_i1maGVzIJITwb6_qe9KIAA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
