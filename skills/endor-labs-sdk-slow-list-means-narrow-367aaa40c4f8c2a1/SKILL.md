---
name: "endor-labs-sdk-slow-list-means-narrow-367aaa40c4f8c2a1"
description: "Guide Endor Labs SDK: slow list() means narrow to a child namespace before traverse=True: [Official Endor Labs SDK docs (troubleshooting.md)]: If list() hangs or crawls, narrow scope first: list from a child namespace without traverse before going tenant-wide with traverse=True. Use this when you hit exactly this in Endor Labs SDK. Not for different errors or different tools."
metadata:
  skill_id: "skl_xnoYMbRbWCDv5FrS_cF99A"
  title: "Endor Labs SDK: slow list() means narrow to a child namespace before traverse=True"
  version: "skv_dmEIxPgxnTOCOQiWtoNL1g"
  updated: "2026-10-03T04:46:37.196413+00:00"
  canonical_url: "https://vectle.com/skills/skl_xnoYMbRbWCDv5FrS_cF99A"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: [Official Endor Labs SDK docs (troubleshooting.md)]: If list() hangs or crawls, narrow scope first: list from a child namespace without traverse before going tenant-wide with traverse=True. Tighten filter where the resource supports selective filters, and avoid broad unfiltered lists on large tenants. max_pages/page_size caps the client loop but does not guarantee cheap server-side work for the first page.

[Official Endor Labs SDK docs (troubleshooting.md)]: If list() hangs or crawls, narrow scope first: list from a child namespace without traverse before going tenant-wide with traverse=True. Tighten filter where the resource supports selective filters, and avoid broad unfiltered lists on large tenants. max_pages/page_size caps the client loop but does not guarantee cheap server-side work for the first page. If listing a resource kind at tenant root raises ServerError, retry at a child namespace; if endorctl succeeds at the same scope but the SDK fails, treat it as model-sync drift instead. Compare SDK vs endorctl on the same resource, namespace, filter, and traverse to isolate client vs backend latency.

Context: Official docs (endorlabs-sdk troubleshooting.md): documents how to fix slow or hanging list operations. Broad list() at tenant root with traverse=True is the expensive path; narrowing to a child namespace first is the documented fix, and capping pages does not make the first page cheap.

## When to use
You hit exactly this: Endor Labs SDK: slow list() means narrow to a child namespace before traverse=True in Endor Labs SDK.

## When not to use
A different error, or the same symptom in a different tool. This page only covers the failure above.

## Compatibility
Endor Labs SDK.

---

Source: [Vectle](https://vectle.com/skills/skl_xnoYMbRbWCDv5FrS_cF99A). Version: `skv_dmEIxPgxnTOCOQiWtoNL1g`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
