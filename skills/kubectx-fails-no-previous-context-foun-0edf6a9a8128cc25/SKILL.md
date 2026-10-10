---
name: "kubectx-fails-no-previous-context-foun-0edf6a9a8128cc25"
description: "Routes kubectx dash-toggle failures. Use when kubectx - reports no previous context found. Not for unknown names or general switch failures."
metadata:
  skill_id: "skl_ucsLKWtKMrWw6Qqxx5MkVA"
  title: "kubectx - fails: no previous context found"
  version: "skv_jpJSXPLAvc2tcdTxpTj49A"
  updated: "2026-10-03T16:13:32.234341+00:00"
  canonical_url: "https://vectle.com/skills/skl_ucsLKWtKMrWw6Qqxx5MkVA"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

The dash toggles to the previously used context, but kubectx has not recorded one yet - fresh shell, cleared cache, or you have not switched since starting. Switch contexts once with kubectx [name] (that records the previous one), and kubectx - toggles from then on.

## The error
```text
no previous context found
```

## What to do
1. Switch once to record a previous context:
```bash
kubectx [first]
kubectx [second]
```
   Expected: Each prints `Switched to context "[name]".`.
2. Toggle:
```bash
kubectx -
```
   Expected: Prints `Switched to context "[first]".`.
3. If it still fails, check the cache file:
```bash
ls ~/.kube/cache/kubectx 2>/dev/null || ls ~/.cache/kubectx
```
   Expected: File exists after a successful switch.

## When this applies
- the exact no previous context found message
- first use of kubectx - in a fresh home directory
- after wiping the kubectx cache

## When it does NOT apply
- no context exists with the name (different error)
- the dash switching to the wrong context (stale cache - switch twice to refresh)

## Works with
kubectx (ahmetb/kubectx)

### No previous namespace found for current context (kubens -)
The kubens twin of this error. Same shape: switch namespaces once first.

## Why it happens
kubectx stores the previous context in a cache file under your home on every switch. No switches yet means no file, and the toggle has nothing to go back to.

## Edge cases
- Containers or CI with a fresh HOME on every run never accumulate a previous context - use explicit names there.
- sudo -s changes HOME, so root's kubectx has a different previous-context file than yours.

## Resolved from
gh:nao1215/atago (e2e kubectx behavior spec) - https://github.com/nao1215/atago/blob/HEAD/doc/e2e/kubectx.md

---

Source: [Vectle](https://vectle.com/skills/skl_ucsLKWtKMrWw6Qqxx5MkVA). Version: `skv_jpJSXPLAvc2tcdTxpTj49A`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
