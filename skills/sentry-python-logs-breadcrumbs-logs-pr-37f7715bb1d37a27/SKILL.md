---
name: "sentry-python-logs-breadcrumbs-logs-pr-37f7715bb1d37a27"
description: "The Python SDK has three log paths: breadcrumbs from loggers (default), the Logs product, and before_send_log to filter. Which to use and how to keep log volume from eating quota. Not the full reference manual."
metadata:
  skill_id: "skl_OBc1WcP7zxBmSz1f-vlgXg"
  title: "Sentry Python logs: breadcrumbs, Logs product, and before_send_log"
  version: "skv__GQiE7zi9VKmiJqbPA2nrw"
  updated: "2026-10-03T04:40:17.422187+00:00"
  canonical_url: "https://vectle.com/skills/skl_OBc1WcP7zxBmSz1f-vlgXg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** The Python SDK has three log paths: breadcrumbs from loggers (default), the Logs product, and before_send_log to filter. Which to use and how to keep log volume from eating quota. Start with before_send_log dropping the known-noise categories (health checks, debug chatter), then watch the logs quota for a week. Verify Emit a log line at error level from a file (not a REPL), trigger it, and confirm it appears both as a breadcrumb on the issue and in the Logs view if the product is enabled.

## Three different things

1. **Breadcrumbs** (default on): the Logging integration records log lines as breadcrumbs attached to error events. Free context, no extra quota beyond the error itself.
2. **Logs product**: structured logs sent to Sentry as their own data type, searchable and correlatable with errors. This is the opt-in product you enable in init.
3. **before_send_log** (SDK 2.35.0+): a hook called for each log; return None to drop it, or mutate it.

```python
def before_send_log(log, hint):
    if "healthcheck" in log.get("message", ""):
        return None  # drop noisy logs before they bill
    return log

sentry_sdk.init(
    dsn="___PUBLIC_DSN___",
    before_send_log=before_send_log,
)
```

## The volume trap

Logs are their own quota category. Enabling the Logs product on a chatty app without a filter is the logs version of traces_sample_rate=1.0. Start with `before_send_log` dropping the known-noise categories (health checks, debug chatter), then watch the logs quota for a week.

## Breadcrumb noise

If breadcrumbs are full of framework debug logs, raise the logger level for the noisy logger rather than disabling the Logging integration. Breadcrumbs on the error that matters are worth more than a quiet breadcrumb trail on every event.

## Verify

Emit a log line at error level from a file (not a REPL), trigger it, and confirm it appears both as a breadcrumb on the issue and in the Logs view if the product is enabled. If logs appear but errors do not, your log pipeline is fine and the problem is in error capture, not transport.

## When to use this

- This covers exactly what the title says: Sentry Python logs.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Sentry; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

---

Source: [Vectle](https://vectle.com/skills/skl_OBc1WcP7zxBmSz1f-vlgXg). Version: `skv__GQiE7zi9VKmiJqbPA2nrw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
