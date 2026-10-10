---
name: "refinery-panics-on-rules-reload-send-o-7d2e1f44010caeb0"
description: "Fixes Refinery panicking with 'send on closed channel' every time the rules file is live-reloaded. The metrics/libhoney client was torn down on reload and later reports went to a closed channel; upgrade to a Refinery release containing the PR #810 fix. Use when Refinery 1.18/1.19 crashes on rules reload with libhoney-go in the stack. Not for panics at startup or under load."
metadata:
  skill_id: "skl_EO8a4zEDYdsmaqpCrpl7iA"
  title: "Refinery panics on rules reload (send on closed channel)"
  version: "skv_QAE2WwG1ixn64ez3_qDMcw"
  updated: "2026-10-03T05:38:20.496356+00:00"
  canonical_url: "https://vectle.com/skills/skl_EO8a4zEDYdsmaqpCrpl7iA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: if Refinery panics with `send on closed channel` every time you update the rules file, you are on a version with the live-reload bug (tracked in refinery issue #807). The metrics/libhoney client gets torn down on rules reload, and the next metric report goes to a closed channel. Upgrade to a Refinery release containing the PR #810 fix.

The error, verbatim:

```text
panic: send on closed channel
in libhoney-go transmission.tryAdd, on rules file reload
```

## Steps

1. Confirm the pattern: the panic happens exactly when the rules file on disk is updated, with `libhoney-go transmission.tryAdd` in the stack. Expected: crash reproduces on every reload.

2. Check your Refinery version: affected are 1.19.0 and 1.18 (with Logger and Metrics set to "honeycomb").

3. Upgrade to a release containing the PR #810 fix. Expected: upgrade completes, service restarts cleanly.

4. Update the rules file to trigger a live reload. Success check: no panic, service keeps running, rules apply.

## When to use this

- Refinery panics on every rules reload with `send on closed channel` in libhoney-go.
- Refinery 1.18/1.19 with honeycomb logger and metrics.

## When NOT to use this

- Panics at startup or under load without a reload; different bug.
- You do not use live rules reload; the trigger is the reload path.

## Compatibility

- Refinery 1.18, 1.19.0 (honeycomb logger + metrics). Fix landed in PR #810 shortly after the 1.19/2.0.2 era.

## Variant phrasings

- refinery crash on rules reload send on closed channel
- libhoney-go transmission.tryAdd panic refinery
- refinery rules file update crashes service

## Root cause

On rules reload, the metrics/libhoney client was torn down along with the old config, but subsequent metric reports were still sent through the old client's channel, which was already closed. Sending on a closed channel panics in Go, crashing the whole service.

## Edge cases

- Restarting the service instead of live-reloading dodges the panic but loses the point of hot reload; upgrade instead.
- If you see the panic without touching the rules file, something else is rewriting it (config management, editor temp files); check file watchers.

Source: https://github.com/honeycombio/refinery/issues/595

---

Source: [Vectle](https://vectle.com/skills/skl_EO8a4zEDYdsmaqpCrpl7iA). Version: `skv_QAE2WwG1ixn64ez3_qDMcw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
