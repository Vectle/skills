---
name: "functions-cannot-be-passed-directly-to-93f61cabd8f54d38"
description: "Add the \"use server\" directive at the top of the file (or inside the function body) that defines the server action. The build passes once the function is marked. Applies to: Next.js 13.4+ app router."
metadata:
  skill_id: "skl_ffwaNtG2lmqnUqG5FDSKyg"
  title: "Functions cannot be passed directly to Client Components unless you explicitly expose it by marking it with \"use"
  version: "skv_ZPqNtbHODJGbgV0Ps9wePA"
  updated: "2026-10-03T05:42:01.572635+00:00"
  canonical_url: "https://vectle.com/skills/skl_ffwaNtG2lmqnUqG5FDSKyg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR
Add the "use server" directive at the top of the file (or inside the function body) that defines the server action. The build passes once the function is marked.

## The exact error
```text
Functions cannot be passed directly to Client Components unless you explicitly expose it by marking it with "use server"
```

## Steps to fix
1. Find the function you are passing from the server component to the client component
2. Add "use server" as the first line of that function or its module
3. Make sure the function only takes and returns serializable values
4. Rebuild; the error should be gone

## When this applies
- Next.js 13.4+ app router
- Passing a server-defined function to a client component as a prop

## When this does NOT apply
- Plain callbacks defined inside the client component itself
- Server components calling other server code

## Tool + versions
Next.js 13.4+ app router

## Why it happens
Functions are not serializable across the server/client boundary. The "use server" mark tells Next.js to expose the function as a server action with an RPC-style reference instead of trying to serialize it.

## Edge cases
- Only serializable arguments cross the boundary
- Inline "use server" inside the function body works for single functions

## Where this came from
Resolved from a real public thread: https://nextjs.org/docs/app/building-your-application/data-fetching/server-actions-and-mutations (docs:server-actions-use-server).

---

Source: [Vectle](https://vectle.com/skills/skl_ffwaNtG2lmqnUqG5FDSKyg). Version: `skv_ZPqNtbHODJGbgV0Ps9wePA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
