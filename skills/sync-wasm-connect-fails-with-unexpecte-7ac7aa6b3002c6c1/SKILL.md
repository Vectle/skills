---
name: "sync-wasm-connect-fails-with-unexpecte-7ac7aa6b3002c6c1"
description: "Fixes @tursodatabase/sync-wasm connect() failing with 'unexpected path .db-log: files must be created in advance for OPFS IO'. Use this on 0.7.2 through 0.8.0-pre.7 against a hosted Turso database negotiating MVCC sync. Not for non-MVCC sync or for local-only databases."
metadata:
  skill_id: "skl_4m48L6__h4CCUsXXEV2dBQ"
  title: "sync-wasm connect() fails with 'unexpected path .db-log: files must be created in advance for OPFS IO'"
  version: "skv_rOeiamzj546DNmjSNCP3Tg"
  updated: "2026-10-03T04:39:23.717121+00:00"
  canonical_url: "https://vectle.com/skills/skl_4m48L6__h4CCUsXXEV2dBQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://vectle.com/threads/thr__yMa-1MECBvM0MiWigVY1Q\",\"https://github.com/tursodatabase/turso/issues/8516\"]"
---

TL;DR: if `@tursodatabase/sync-wasm` `connect()` rejects with `unexpected path fresh-[id].db-log: files must be created in advance for OPFS IO` before any application SQL runs, the sync engine needs an MVCC logical-log sidecar file that the OPFS worker registry never registered. Use 0.8.0-pre.9 or newer, where PR #8524 registers the MVCC log path before connecting. As a stopgap, build locally (`yarn workspace @tursodatabase/sync-wasm build` in bindings/javascript) and install the built package directly.

```text
Internal error: unexpected path fresh-[id].db-log: files must be created in advance for OPFS IO
```

## Steps

1. Upgrade:

```sh
npm install @tursodatabase/sync-wasm@^0.8.0-pre.9
```

   Expected: the installed build includes PR #8524.

2. Re-run `connect()` against the hosted database.

   Expected: the connection proceeds to sync. Success check: application SQL runs without the db-log error.

## When to use this

- sync-wasm 0.7.2 through 0.8.0-pre.7, hosted Turso database negotiating MVCC sync.
- The error names a `.db-log` path.

## When NOT to use this

- Non-MVCC sync setups; the sidecar requirement is MVCC-specific.
- Local-only databases; OPFS registration is about the sync path.

## Compatibility

- @tursodatabase/sync-wasm 0.8.0-pre.9+. The maintainer re-tagged main to push it to npm after the pre.8 release job failed.

## Variant phrasings

- "sync-wasm connect db-log OPFS"
- "turso sync-wasm MVCC unexpected path"

## Root cause

The JavaScript OPFS worker registry registered the main db, `-wal`, `-wal-revert`, `-info`, and `-changes` paths but not the MVCC log sidecar, so the sync engine's first access to it was rejected.

## Edge cases

- The local-build stopgap works but you lose npm updates; prefer the fixed release.

Source: https://github.com/tursodatabase/turso/issues/8516

---

Source: [Vectle](https://vectle.com/skills/skl_4m48L6__h4CCUsXXEV2dBQ). Version: `skv_rOeiamzj546DNmjSNCP3Tg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
