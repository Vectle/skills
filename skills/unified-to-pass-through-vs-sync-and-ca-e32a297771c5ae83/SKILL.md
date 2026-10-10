---
name: "unified-to-pass-through-vs-sync-and-ca-e32a297771c5ae83"
description: "Guide Unified.to: pass-through vs sync-and-cache, and when not to use it: Real-time pass-through routes every request live to the source system with no customer payload data stored at rest; sync-and-cache serves reads from a scheduled cache that can be hours stale. Use this when you hit exactly this in Unified.to. Not for different errors or different tools."
metadata:
  skill_id: "skl_DzA_ySwwJ8wbPGe3143Vaw"
  title: "Unified.to: pass-through vs sync-and-cache, and when not to use it"
  version: "skv_mF3WndJkqEtUgMPziYDA1A"
  updated: "2026-10-03T05:09:52.350437+00:00"
  canonical_url: "https://vectle.com/skills/skl_DzA_ySwwJ8wbPGe3143Vaw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: Real-time pass-through routes every request live to the source system with no customer payload data stored at rest; sync-and-cache serves reads from a scheduled cache that can be hours stale. Context: Official docs (docs.unified.to, What is a Unified API): teaches the architecture decision that determines freshness, compliance, and cost.

Context: Official docs (docs.unified.to, What is a Unified API): teaches the architecture decision that determines freshness, compliance, and cost. Real-time pass-through routes every request live to the source system with no customer payload data stored at rest; sync-and-cache serves reads from a scheduled cache that can be hours stale. The choice drives data freshness, compliance scope (pass-through is not a sub-processor for payload data), latency (full source round-trip per request vs fast cache reads), and pricing (per API call vs per linked account). Well-designed unified APIs add capabilities vendors lack: polling-based virtual webhooks for vendors without native webhooks, consistent pagination, centralized rate-limit management. The docs also name three cases where a unified API is the wrong choice: only one or two vendors with no plans to add more (direct integration is faster), internal workflow automation (an iPaaS fits better), and per-customer unique integration logic (embedded iPaaS fits better).

How to apply it: 1. If reads must reflect source state at request time (reconciliation, AI agents), choose real-time pass-through and budget for the round-trip latency. 2. If reads can be minutes or hours stale and need sub-100ms latency, sync-and-cache works, but accept the vendor as a data sub-processor. 3. Confirm webhook support per integration; where native webhooks are missing, check whether the vendor offers virtual webhooks (polling plus change detection with unified event delivery) instead of building your own polling. 4. Match the pricing model to your shape: per-linked-account scales with customers times integrations, per-API-call scales with actual data activity. 5. Do not adopt a unified API for one or two deep integrations or for workflow orchestration; direct vendor code or an iPaaS is the better fit there.

## When to use
You hit exactly this: Unified.to: pass-through vs sync-and-cache, and when not to use it in Unified.to.

## When not to use
A different error, or the same symptom in a different tool. This page only covers the failure above.

## Compatibility
Unified.to.

---

Source: [Vectle](https://vectle.com/skills/skl_DzA_ySwwJ8wbPGe3143Vaw). Version: `skv_mF3WndJkqEtUgMPziYDA1A`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
