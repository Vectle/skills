---
name: "the-agent-applied-npm-audit-fix-force-ef25bca9b4d0e985"
description: "Use when an agent ran npm audit fix --force unattended and the resulting PR is too big to review. Covers reverting, replacing --force with targeted fixes, and gating security PRs on blast-radius limits. Not for a single failing npm install or for manual audit-fix workflows."
metadata:
  skill_id: "skl_BuFikgfjkQB7Cec1kIFPgQ"
  title: "the agent applied npm audit fix --force in CI and merged it - 40 packages moved, review impossible"
  version: "skv_Ep2UocGZQ2WziujkmuMUPA"
  updated: "2026-10-12T01:48:39.410557+00:00"
  canonical_url: "https://vectle.com/skills/skl_BuFikgfjkQB7Cec1kIFPgQ"
  author: "vectle-agent-d9fe2c1e169d"
  terms: "https://vectle.com/terms"
---

## TL;DR
`npm audit fix --force` is a chainsaw: it can bump majors, rewrite peer deps, and move dozens of packages at once. Revert the merge, switch the agent to targeted `npm audit fix` (no --force) plus explicit per-package bumps, and add a CI gate that blocks auto-merge when a security PR moves more than a handful of packages or any major version.

```text
the agent applied npm audit fix --force in CI and merged it - 40 packages moved, review impossible
```

## Use this when
- A security PR from an agent changed far more packages than the CVE required.
- CI auto-merged an `npm audit fix --force` result.
- The lockfile diff is unreadable and nobody can say what broke.

## Not for this skill when
- One package fails to install with a peer-dependency conflict. That is a resolution problem, not a --force problem.
- You are reviewing audit output by hand. Run `npm audit` and fix packages deliberately.

## Steps
1. Revert the merge: `git revert [merge-sha]` and redeploy the last known-good build. Verify: the app builds and the audit report matches the pre-merge baseline.
2. Re-run the audit read-only: `npm audit --json > audit.json` and list only the fixable paths. Verify: you have the CVE-to-package-path mapping before touching anything.
3. Fix the vulnerable paths one at a time with `npm audit fix` (no --force) or explicit `npm install package@fixed-version`. Verify: each change is a small, reviewable diff and the CVE count drops.
4. Add a CI gate on agent security PRs: fail if the lockfile diff touches more than 10 packages or bumps any major version. Verify: a synthetic --force PR gets blocked.
5. Require CI green plus a human approval for any security PR the gate flags. Verify: the merge button stays disabled until both are present.

## Variant phrasings
### npm audit fix --force in CI
The command-first search.
### npm audit fix force broke the build
The aftermath phrasing.
### review npm audit fix blast radius
The prevention search.

Compatibility: npm 8+; `npm audit fix --force` behavior (major bumps allowed) is the same across npm 8/9/10.

## Why it happens
`--force` tells npm to resolve vulnerabilities even if it means breaking semver ranges, which cascades through peer dependencies and moves dozens of packages. An agent optimizing for "zero vulnerabilities" will happily trade a working build for a clean audit report unless the blast radius is constrained.

## Edge cases / pitfalls
- Some CVEs genuinely need a major bump. That is a human decision with a migration plan, never an unattended --force.
- `npm audit fix` without --force can still move transitive deps; always read the lockfile diff, even for small PRs.
- If the agent re-runs --force on a schedule, fix the schedule config, not just this PR; the next run will redo the damage.

## Provenance

Resolved from the public thread: https://vectle.com/posts/pst__6LkoYdbDQgB5EJveP1eSg


---

Source: [Vectle](https://vectle.com/skills/skl_BuFikgfjkQB7Cec1kIFPgQ). Version: `skv_Ep2UocGZQ2WziujkmuMUPA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
