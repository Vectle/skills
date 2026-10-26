---
name: "async-await-is-not-yet-supported-in-cl-aef3a3080f4f8c43"
description: "Stop awaiting directly in the client component; fetch in a server component and pass the data down as props. The error disappears once the client file has no top-level await. Applies to: Next.js 13+ app router."
metadata:
  skill_id: "skl_K3aCS7lWXghBuXVLRtxhSg"
  title: "async/await is not yet supported in Client Components, only Server Components"
  version: "skv_elF4ys89JtlfolQN4VygKA"
  updated: "2026-10-03T05:39:52.058106+00:00"
  canonical_url: "https://vectle.com/skills/skl_K3aCS7lWXghBuXVLRtxhSg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://nextjs.org/docs/app/building-your-application/rendering/client-components\"]"
---

## TL;DR
Stop awaiting directly in the client component; fetch in a server component and pass the data down as props. The error disappears once the client file has no top-level await.

## The exact error
```text
async/await is not yet supported in Client Components, only Server Components
```

## Steps to fix
1. Find the async function or await the error points at in your "use client" file
2. Move the data fetch into the parent server component or a server action
3. Pass the resolved data to the client component as a prop
4. Rebuild; the error should clear

## When this applies
- Next.js 13+ app router
- A client component tries to await data directly

## When this does NOT apply
- Server components, where async/await is fine
- Fetching inside useEffect, which never needed this

## Tool + versions
Next.js 13+ app router

## Why it happens
Client components are bundled for the browser and cannot suspend on a promise during render the way server components can, so Next.js blocks the pattern at build time.

## Edge cases
- Server actions are the other legal way to run async work from a client component
- Passing a promise as a prop and awaiting it in the client still fails

## Where this came from
Resolved from a real public thread: https://nextjs.org/docs/app/building-your-application/rendering/client-components (docs:client-components-async).

---

Source: [Vectle](https://vectle.com/skills/skl_K3aCS7lWXghBuXVLRtxhSg). Version: `skv_elF4ys89JtlfolQN4VygKA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
