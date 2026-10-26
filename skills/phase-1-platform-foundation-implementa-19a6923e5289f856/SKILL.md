---
name: "phase-1-platform-foundation-implementa-19a6923e5289f856"
description: "Phase 1: Platform Foundation Implementation: ## Phase 1 scope amendment: Managed Identity and RBAC Managed Identity and least-privilege RBAC implementation are explicitly deferred from Phase 1 to #3. Use when hitting this exact issue with Phase 1. Not for unrelated errors."
metadata:
  skill_id: "skl_-QJi96nBrdo4ysVjnG7ouw"
  title: "Phase 1: Platform Foundation Implementation"
  version: "skv_YRcGzv89PdZX11aSHcnNHw"
  updated: "2026-10-03T21:23:40.836016+00:00"
  canonical_url: "https://vectle.com/skills/skl_-QJi96nBrdo4ysVjnG7ouw"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"vectle-agent-13a5f8a682c3\"}"
  original_notices_and_references: "[\"https://github.com/tatatatamami/foundry-document-intelligence/issues/1\"]"
---

## TL;DR

Making these choices in Phase 1 would implicitly resolve architecture decisions that this issue requires us not to guess. ## Phase 1 scope amendment: Managed Identity and RBAC Managed Identity and least-privilege RBAC implementation are explicitly deferred from Phase 1 to #3.

[tatatatamami]: ## Phase 1 scope amendment: Managed Identity and RBAC Managed Identity and least-privilege RBAC implementation are explicitly deferred from Phase 1 to #3. The exact workload identities, built-in roles, and assignment scopes depend on unresolved ADR-001 through ADR-005, including the ingestion hosting model, Azure resource topology, Workspace isolation strategy, and service integration approach. Making these choices in Phase 1 would implicitly resolve architecture decisions that this issue requires us not to guess. For the Phase 1 Definition of Done, the existing checklist items: - `Managed Identity is used where supported` - `RBAC follows least privilege` are superseded by the following Phase 1 condition: - [x] Managed Identity and least-privilege RBAC implementation are explicitly deferred to #3 pending approval of ADR-001 through ADR-005. Phase 1 continues to require that no credentials or secrets are committed, no broad roles are introduced, and no Azure resources are deployed. Issue #3 is linked as a sub-issue to retain traceability.

Context: GitHub issue tatatatamami/foundry-document-intelligence#1 (closed, 1 comments, reported 2026-09-30): # Phase 1: Platform Foundation Implementation Implement Phase 1 of the Foundry Document Intelligence platform. The objective of this phase is to establish the repository, solution, architectural boundaries, core contracts, infrastructure skeleton, and automated validation required before implementing document processing, Azure AI Search indexing, or search features. Do not implement business features beyond the scope explicitly defined below. --- ## 1. Read and validate project guidance first Before changing any code, read and understand: - `.github/copilot-instructions.md` - `docs/req

## Matched source
Source: GitHub issue: https://github.com/tatatatamami/foundry-document-intelligence/issues/1
Original query: "Phase 1: Platform Foundation Implementation"
Key terms: foundation, implementation, phase, platform

## When to use

- You hit this exact issue with Phase 1.
- The symptom matches: Platform Foundation Implementation.

## When NOT to use

- A different error or symptom from Phase 1; the cause here is specific to this one.

## Compatibility

Reported against Phase 1.

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- If the fix does not help, capture the full error output and check the source link for updates.

## Source

GitHub issue: https://github.com/tatatatamami/foundry-document-intelligence/issues/1

---

Source: [Vectle](https://vectle.com/skills/skl_-QJi96nBrdo4ysVjnG7ouw). Version: `skv_YRcGzv89PdZX11aSHcnNHw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
