---
name: "track-upstream-backports-and-tooling-r-10b8d2e4d7628579"
description: "Track upstream backports and tooling refresh in small release waves: Task 1 is ready for hosted validation in #61 (`04e606ac770edde2f3d7a85887988d7f29188c63`). Use when hitting this exact issue. Not for unrelated errors."
metadata:
  skill_id: "skl_8Ud76vNnAweVQyAIlNjhaQ"
  title: "Track upstream backports and tooling refresh in small release waves"
  version: "skv_OzjTzKEnhU33QwDWgvztWg"
  updated: "2026-10-03T14:36:12.813784+00:00"
  canonical_url: "https://vectle.com/skills/skl_8Ud76vNnAweVQyAIlNjhaQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

All reproduced high/medium findings are resolved. Task 1 is ready for hosted validation in #61 (`04e606ac770edde2f3d7a85887988d7f29188c63`).

[CBEPX]: Task 1 is ready for hosted validation in #61 (`04e606ac770edde2f3d7a85887988d7f29188c63`). Final Opus 5.5/high review approved. Parent verification passed: 1027 unit tests, 120 integration tests, 24 native Codex E2E tests, lint/typechecks, live Claude Stop boundary, candidate adversarial structured output, and actual stdio Git MCP staged/untracked qualification. No skips. The PR also keeps large/omitted changes reviewable without Bash: staged-only MCP diff, MCP-based fallback instructions, and complete untracked status regardless of user Git settings. All reproduced high/medium findings are resolved. CI and Mutation are running; merge remains pending their results. Task 2 follows after this part is accepted.

Context: GitHub issue CBEPX/cc-plugin-codex#60 (closed, 2 comments, reported 2026-09-25): Track selective Sendbird backports and tooling updates from the qualified v1.7.7 baseline (`66846d9080dd749dcc0b9ef9c37af8d5fd4cc203`). Ship one small PR per item, sequentially, with releases after local qualification of each wave. Owner: Codex coordinator with Claude through cc for planning, implementation, fresh review, verification analysis and release evidence review. Record exact source SHAs, requested/final models, cc job IDs, tests, CI and artifact readbacks below as work completes. ## Wave 1 , released v1.7.8 - [x] Stop-review through bundled Git MCP: exact read-only tool grants, st

## Matched source
Source: GitHub issue: https://github.com/CBEPX/cc-plugin-codex/issues/60
Original query: "Track upstream backports and tooling refresh in small release waves"
Key terms: backports, refresh, release, small, tooling, track, upstream, waves

## When to use

- You hit this exact issue.
- The symptom matches: Track upstream backports and tooling refresh in small release waves.

## When NOT to use

- A different error or symptom; the cause here is specific to this one.

## Compatibility

Per the linked source (mentions 5.5, v1.7.7, v1.7.8).

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- If the fix does not help, capture the full error output and check the source link for updates.

## Source

GitHub issue: https://github.com/CBEPX/cc-plugin-codex/issues/60

---

Source: [Vectle](https://vectle.com/skills/skl_8Ud76vNnAweVQyAIlNjhaQ). Version: `skv_OzjTzKEnhU33QwDWgvztWg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
