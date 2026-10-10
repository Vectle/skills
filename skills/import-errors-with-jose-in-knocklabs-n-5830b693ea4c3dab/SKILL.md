---
name: "import-errors-with-jose-in-knocklabs-n-5830b693ea4c3dab"
description: "Resolves import errors and broken token signing when @knocklabs/node is bundled in ESM builds alongside a direct jose dependency. Use this when ESM bundlers misinterpret the SDK's rewritten require('jose') import. Not for CommonJS builds or for jose problems unrelated to the Knock SDK."
metadata:
  skill_id: "skl_9XtDblbMPDldGhqjvYIiVw"
  title: "Import errors with jose in @knocklabs/node ESM builds (jose version conflict)"
  version: "skv_FaRP96OCUa9TxdPUhrgjnw"
  updated: "2026-10-03T04:29:38.667665+00:00"
  canonical_url: "https://vectle.com/skills/skl_9XtDblbMPDldGhqjvYIiVw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: if `@knocklabs/node` breaks token signing in ESM builds because its vendored `jose` (capped at 5.2.0) clashes with your own `jose` (e.g. 5.9.6 for edge-runtime JWKS caching), upgrade to the `@knocklabs/node` 1.x release line. 1.x dropped the `jose` dependency entirely, which removes the conflict.

## Steps

1. Upgrade the SDK:

```sh
npm install @knocklabs/node@^1.0.0
```

   Expected: no `jose` in the SDK's own dependencies.

2. Rebuild your ESM bundle.

   Expected: no more import errors around jose. Success check: token signing works in the ESM build the way it already did in CommonJS.

3. On edge runtimes, import the signer explicitly with the latest version:

```js
import { signUserToken } from '@knocklabs/node/lib/tokenSigner'
```

## When to use this

- You use `jose` directly (e.g. 5.9.6 for stable edge-runtime JWKS caching) and `@knocklabs/node` pulls its own older `jose`.
- ESM-mode bundlers break on the SDK's rewritten `require("jose")` import while your own jose usage is fine.

## When NOT to use this

- You build in CommonJS, where the conflict does not bite.
- Your jose errors have nothing to do with the Knock SDK.

## Compatibility

- `@knocklabs/node` 1.x (jose dependency dropped). Note: dropping jose initially broke edge runtimes; that was fixed separately, so use the latest 1.x, not the first 1.0 cut.

## Variant phrasings

- "knock node ESM jose import error"
- "@knocklabs/node token signing fails ESM build"
- "knock SDK jose version conflict"

## Root cause

Knock's build rewrites the import to `const jose_1 = require("jose")`, which ESM-mode bundlers interpret as a default import, breaking token signing in ESM builds. The version cap at 5.2.0 made the conflict unavoidable until the dependency was dropped.

## Edge cases

- If you are pinned below 1.x for other reasons, there is no clean fix; the dependency drop only exists on the 1.x line.

---

Source: [Vectle](https://vectle.com/skills/skl_9XtDblbMPDldGhqjvYIiVw). Version: `skv_FaRP96OCUa9TxdPUhrgjnw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
