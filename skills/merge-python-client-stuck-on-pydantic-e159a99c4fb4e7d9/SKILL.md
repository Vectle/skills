---
name: "merge-python-client-stuck-on-pydantic-e159a99c4fb4e7d9"
description: "Guide merge-python-client stuck on pydantic v1 breaks v2 codebases; upgrade to the v2 release: Merge resolved this by shipping the SDK on pydantic 2.0 (collaborator dsinghvi confirmed the migration was done). Use this when you hit exactly this in merge-python-client. Not for different errors or different tools."
metadata:
  skill_id: "skl_W5SupfcTuk840XCOyoSn6A"
  title: "merge-python-client stuck on pydantic v1 breaks v2 codebases; upgrade to the v2 release"
  version: "skv_9tXpuCytJAAwHjMT_aAq-Q"
  updated: "2026-10-03T04:47:08.913583+00:00"
  canonical_url: "https://vectle.com/skills/skl_W5SupfcTuk840XCOyoSn6A"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/merge-api/merge-python-client/issues/82\"]"
---

TL;DR: Merge resolved this by shipping the SDK on pydantic 2.0 (collaborator dsinghvi confirmed the migration was done). If your project runs pydantic v2, upgrade merge-python-client past the v2-based release instead of fighting interop. If you are pinned to pydantic v1 for other reasons, keep the v1-based client and convert merge models to plain dicts before mixing them into your own models.

Merge resolved this by shipping the SDK on pydantic 2.0 (collaborator dsinghvi confirmed the migration was done). If your project runs pydantic v2, upgrade merge-python-client past the v2-based release instead of fighting interop. If you are pinned to pydantic v1 for other reasons, keep the v1-based client and convert merge models to plain dicts before mixing them into your own models. Rule of thumb for generated SDKs: a version-mismatch import error is a signal to upgrade the SDK, not to pin your whole dependency tree around it.

## When to use
You hit exactly this: merge-python-client stuck on pydantic v1 breaks v2 codebases; upgrade to the v2 release in merge-python-client.

## When not to use
A different error, or the same symptom in a different tool. This page only covers the failure above.

## Compatibility
merge-python-client (versions mentioned here: 2.0, v2, v1).

---

Source: [Vectle](https://vectle.com/skills/skl_W5SupfcTuk840XCOyoSn6A). Version: `skv_9tXpuCytJAAwHjMT_aAq-Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
