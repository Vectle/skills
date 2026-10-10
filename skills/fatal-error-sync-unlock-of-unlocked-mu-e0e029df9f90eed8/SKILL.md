---
name: "fatal-error-sync-unlock-of-unlocked-mu-e0e029df9f90eed8"
description: "Fix for fatal error: sync: unlock of unlocked mutex (v8.5.0 stmtctx.go:803): What was reported: GitHub issue pingcap/tidb#58600 (closed, 25 comments): ## Bug Report Please answer these questions before submitting your issue. Thanks! ### 1. Use this when you hit exactly this in fatal error. Not for different errors or different tools."
metadata:
  skill_id: "skl_msSNXyd4ztU4UYx1YW_ROQ"
  title: "fatal error: sync: unlock of unlocked mutex (v8.5.0 stmtctx.go:803)"
  version: "skv_KQt_KaPddVridd8QI1HE9A"
  updated: "2026-10-03T05:57:35.888306+00:00"
  canonical_url: "https://vectle.com/skills/skl_msSNXyd4ztU4UYx1YW_ROQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: What was reported: GitHub issue pingcap/tidb#58600 (closed, 25 comments): ## Bug Report Please answer these questions before submitting your issue. Thanks! ### 1. Minimal reproduce step (Required) I'm sorry, but I'm not sure how to reproduce the issue.

```text
fatal error: sync: unlock of unlocked mutex (v8.5.0 stmtctx.go:803)
```

## Fix
1. What was reported: GitHub issue pingcap/tidb#58600 (closed, 25 comments): ## Bug Report Please answer these questions before submitting your issue.
   Expected: this specific failure stops.
2. Thanks! ### 1.
   Expected: this specific failure stops.
3. Minimal reproduce step (Required) I'm sorry, but I'm not sure how to reproduce the issue.
   Expected: this specific failure stops.
4. It occurs sporadically on multiple running TiDB processes. ### 2.
   Expected: this specific failure stops.

## Details
What was reported: GitHub issue pingcap/tidb#58600 (closed, 25 comments): ## Bug Report Please answer these questions before submitting your issue. Thanks! ### 1. Minimal reproduce step (Required) I'm sorry, but I'm not sure how to reproduce the issue. It occurs sporadically on multiple running TiDB processes. ### 2. What did you expect to see? (Required) ### 3. What did you see instead (Required) fatal error on YOUR_HOST.com/pingcap/tidb/blob/d13e52ed6e22cc5789bed7c64c861578cd2ed55b/pkg/sessionctx/stmtctx/stmtctx.go#L800-L804 . These errors always occur on the same line. `` ` fatal error: sync: unlock of unlocked mutex goroutine 322590843 [running]: sync.fatal( What works: [chibiegg (reporter)]: Based on what I’ve seen, in my environment, every occurrence of the panic happened during calls originating from setDataForProcessList (infoschema_reader.go:1843). I’ll try running the patch you provided on my local environment. If it works, should we skip the previously committed workaround and only introduce the handling of RefCountOfStmtCtx? Or is it better to keep both changes?

## When to use
You hit exactly this: fatal error: sync: unlock of unlocked mutex (v8.5.0 stmtctx.go:803) in fatal error.

## When not to use
A different error, or the same symptom in a different tool. This page only covers the failure above.

## Compatibility
fatal error.

---

Source: [Vectle](https://vectle.com/skills/skl_msSNXyd4ztU4UYx1YW_ROQ). Version: `skv_KQt_KaPddVridd8QI1HE9A`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
