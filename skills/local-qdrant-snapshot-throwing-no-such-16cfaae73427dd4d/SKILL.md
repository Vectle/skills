---
name: "local-qdrant-snapshot-throwing-no-such-16cfaae73427dd4d"
description: "Qdrant: local Qdrant Snapshot throwing No such file or directory (OS error 2). The verified fix is Fix: (1) Unstable storage (WSL mounts, NFS) - not reliably fixable, use supported storage. Use this when you hit the symptoms above in qdrant; not for unrelated qdrant errors or general setup questions."
metadata:
  skill_id: "skl_B-o_sQxsfYVUmadNGyqYTA"
  title: "Local Qdrant Snapshot throwing No such file or directory (OS error 2)"
  version: "skv_uatFLCGo4x0bnRDQ114pEg"
  updated: "2026-10-03T04:41:37.377107+00:00"
  canonical_url: "https://vectle.com/skills/skl_B-o_sQxsfYVUmadNGyqYTA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/qdrant/qdrant/issues/2620\"]"
---

## TL;DR

Fix: ((1) Unstable storage (WSL mounts, NFS) - not reliably fixable, use supported storage. ((2) Concurrent snapshot creation and WAL flushing conflicting - fixed in Qdrant 1.16.0. Lesson for self-hosted agents: keep Qdrant storage on a local disk (not WSL/NFS mounts) and avoid snapshotting during heavy flushes; upgrade to >= 1.16.0 for the conflict fix.

## The error

```text
POST /collections/[name]/snapshots on a local Docker instance fails with 'Error while copy WAL ... No such file or directory (os error 2)', HTTP 500.
```

## Fix

1. ((1) Unstable storage (WSL mounts, NFS) - not reliably fixable, use supported storage.
2. ((2) Concurrent snapshot creation and WAL flushing conflicting - fixed in Qdrant 1.16.0.
3. Lesson for self-hosted agents: keep Qdrant storage on a local disk (not WSL/NFS mounts) and avoid snapshotting during heavy flushes; upgrade to >= 1.16.0 for the conflict fix.

Success check: the symptom above is gone and the original operation completes.

## When to use

- You hit this exact symptom in qdrant.
- You want the verified fix without digging through the thread.

## When not to use

- A different error in qdrant, even a similar-looking one.
- General qdrant setup or credential questions.

## Compatibility

- Qdrant (qdrant/qdrant)

## Variant phrasings

- How to fix "local Qdrant Snapshot throwing No such file or directory (OS error 2)" in qdrant
- qdrant: local Qdrant Snapshot throwing No such file or directory (OS error 2)
- local Qdrant Snapshot throwing No such file or directory (OS problem 2)

## Source

- https://github.com/qdrant/qdrant/issues/2620

---

Source: [Vectle](https://vectle.com/skills/skl_B-o_sQxsfYVUmadNGyqYTA). Version: `skv_uatFLCGo4x0bnRDQ114pEg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
