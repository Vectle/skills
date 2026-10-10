---
name: "google-secret-manager-nodejs-accesssec-45fed0fe76e9d409"
description: "Fixes the Node.js @google-cloud/secret-manager client returning null from accessSecretVersion when the bluebird promise library is loaded. Use this when the client constructs fine and the path is correct but calls silently yield nothing. Not for wrong paths or auth errors."
metadata:
  skill_id: "skl_EDGciXGT5N9TriB2BW3vPA"
  title: "Google Secret Manager nodejs accessSecretVersion returns null with bluebird promise"
  version: "skv_OERtpyWrj2QVkk3o-akueQ"
  updated: "2026-10-03T05:36:35.986211+00:00"
  canonical_url: "https://vectle.com/skills/skl_EDGciXGT5N9TriB2BW3vPA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: if `accessSecretVersion` with the Node.js `@google-cloud/secret-manager` client returns null instead of the secret payload, check for the bluebird promise library. Bluebird shims promises globally and breaks the google-cloud client internals. Remove the global bluebird shim and the call starts returning the payload.

## Steps

1. Search your dependency tree for bluebird (or any promise-shimming library) loaded globally.

2. Remove the global shim (or scope it so it does not touch the google-cloud client).

3. Re-run the secret access.

   Expected: the payload returns. Success check: no more null results.

## When to use this

- Node.js google-cloud clients return null silently with correct paths and working auth.
- Bluebird is in the dependency tree.

## When NOT to use this

- The secret path is wrong; fix the path.
- Auth fails; check credentials.

## Compatibility

- @google-cloud/secret-manager Node.js client with bluebird present.

## Variant phrasings

- "secret manager nodejs returns null bluebird"
- "google cloud node null response promise"

## Root cause

Global promise shims replace the promise implementation the client library was built against, corrupting its async internals.

## Edge cases

- Other shimming libraries can cause the same symptom; bluebird is just the common one.

---

Source: [Vectle](https://vectle.com/skills/skl_EDGciXGT5N9TriB2BW3vPA). Version: `skv_OERtpyWrj2QVkk3o-akueQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
