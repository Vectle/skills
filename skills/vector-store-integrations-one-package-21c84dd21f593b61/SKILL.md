---
name: "vector-store-integrations-one-package-21c84dd21f593b61"
description: "LangChain core does not bundle any vector store. Each store is its own package you install separately. Training data still teaches old combined imports, so check the package name first when an import fails."
metadata:
  skill_id: "skl_aV69Nt1UXDmPl9Cr75-JJw"
  title: "Vector store integrations: one package per store, none bundled in core"
  version: "skv_IrRdNuCA59oIDnheleWWjA"
  updated: "2026-10-03T14:04:42.128728+00:00"
  canonical_url: "https://vectle.com/skills/skl_aV69Nt1UXDmPl9Cr75-JJw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** LangChain core does not bundle any vector store. Each store is its own package you install separately.

## The fix

1. There is no vector store inside the `langchain` package. If docs or old code import a store from `langchain.vectorstores`, that path is legacy; the store now lives in its own `langchain-[store]` package.

2. Pin the store package alongside langchain-core. Store integrations lag core releases, and a major bump on either side is the usual cause of weird serialization errors.

3. The full provider list with Python and JS package names is on the integrations providers page; check there before guessing a package name.

## When to use this

- This covers exactly what the title says: Vector store integrations.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Vector; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current Vector behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_aV69Nt1UXDmPl9Cr75-JJw). Version: `skv_IrRdNuCA59oIDnheleWWjA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
