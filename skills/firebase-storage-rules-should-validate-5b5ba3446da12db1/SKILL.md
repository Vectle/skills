---
name: "firebase-storage-rules-should-validate-5b5ba3446da12db1"
description: "Shows how to fix firebase Storage rules should validate size and type, not just auth. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_ItosHVmtChCMkwy6m11Shg"
  title: "Firebase Storage rules should validate size and type, not just auth"
  version: "skv_wqumQJUFLdJFWs50TQLFQA"
  updated: "2026-10-03T14:18:54.815559+00:00"
  canonical_url: "https://vectle.com/skills/skl_ItosHVmtChCMkwy6m11Shg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/ahmedbna/ui/blob/HEAD/packages/starters/overlays/firebase/README.md\"]"
---

## TL;DR

Write storage rules that validate the file, not just the user: cap request.resource.size, restrict request.resource.contentType to the types you expect, and do not grant delete to clients unless the feature needs it.

## Steps

1. Write storage rules that validate the file, not just the user: cap request.resource.size, restrict request.resource.contentType to the types you expect, and do not grant delete to clients unless the feature needs it. Test the rules against the emulator with adversarial uploads before publishing.

## When to use

You are seeing this: Test the rules against the emulator with adversarial uploads before publishing. Use this skill when you run into "Firebase Storage rules should validate size and type, not just auth".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_ItosHVmtChCMkwy6m11Shg). Version: `skv_wqumQJUFLdJFWs50TQLFQA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
