---
name: "sentry-python-init-first-sample-delibe-8edbbd6b4bdb3f79"
description: "Wire up the Sentry Python SDK without the usual first-day mistakes: init before anything else can throw, pick sample rates deliberately, and verify from a real file instead of a REPL. Not the full reference manual."
metadata:
  skill_id: "skl_UmCXBXzdm7CbN9N2XnsgbQ"
  title: "Sentry Python: init first, sample deliberately, verify from a file"
  version: "skv_AWs2wrp23vBprcTBK34mbg"
  updated: "2026-10-03T04:37:34.974134+00:00"
  canonical_url: "https://vectle.com/skills/skl_UmCXBXzdm7CbN9N2XnsgbQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** Wire up the Sentry Python SDK without the usual first-day mistakes: init before anything else can throw, pick sample rates deliberately, and verify from a real file instead of a REPL. In production start low (0.05-0.2) and watch usage, or use traces_sampler for dynamic per-request decisions (it must return a float between 0 and 1, and returning 0 filters the transaction out). Note the semantics: traces_sample_rate=0 means no new traces start, but traces_sample_rate=None (the default) disables tracing entirely, including continuing incoming traces.

## Install and init

```
pip install sentry-sdk
```

Call `sentry_sdk.init()` as early as possible in your app's entry point, before importing modules that could throw during import. In async programs, init inside the first async function so async code gets instrumented properly:

```python
import sentry_sdk

sentry_sdk.init(
    dsn="___PUBLIC_DSN___",
    send_default_pii=True,  # adds request headers and IP; opt in consciously
    traces_sample_rate=0.1,  # NOT 1.0 in production (see below)
    # release defaults to the SENTRY_RELEASE env var, else the git SHA
)
```

## The sample-rate trap

The docs example uses `traces_sample_rate=1.0` because it is a getting-started snippet. At 1.0 every transaction becomes a billed span. In production start low (0.05-0.2) and watch usage, or use `traces_sampler` for dynamic per-request decisions (it must return a float between 0 and 1, and returning 0 filters the transaction out). Note the semantics: `traces_sample_rate=0` means no new traces start, but `traces_sample_rate=None` (the default) disables tracing entirely, including continuing incoming traces.

## Verify from a file, not a REPL

Errors raised in an interactive shell like IPython do not trigger error monitoring. Verify with a script file:

```python
# verify_sentry.py
import sentry_sdk
sentry_sdk.init(dsn="___PUBLIC_DSN___")
1 / 0
```

Run it, then check the issue stream. If nothing arrives, turn on `debug=True` in init to see SDK diagnostics in stderr, and confirm the DSN matches your project's DSN exactly (wrong project or org slug means events get rejected).

## Shutdown behavior

The SDK sends from a background queue with `shutdown_timeout` defaulting to 2 seconds. Short-lived scripts and CLI tools can lose the last events; call `sentry_sdk.flush()` before exit in those cases.

## When to use this

- This covers exactly what the title says: Sentry Python.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Sentry; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Mentions 0.1, 1.0 in the original; behavior may differ on much older or newer releases.

---

Source: [Vectle](https://vectle.com/skills/skl_UmCXBXzdm7CbN9N2XnsgbQ). Version: `skv_AWs2wrp23vBprcTBK34mbg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
