---
name: "sentry-laravel-sentry-laravel-dsn-is-n-236328d27603cade"
description: "Laravel's Sentry setup uses SENTRY_LARAVEL_DSN (not SENTRY_DSN), a publish command, and a test command. Plus the php.ini flag for stack trace args and the quota warning on the trace sample rate."
metadata:
  skill_id: "skl_lwsuMc50A5h2mMjKUf5Iwg"
  title: "Sentry Laravel: SENTRY_LARAVEL_DSN is not SENTRY_DSN"
  version: "skv_ETp78Z3zaxkESzx7QzdWZw"
  updated: "2026-10-03T05:03:47.614083+00:00"
  canonical_url: "https://vectle.com/skills/skl_lwsuMc50A5h2mMjKUf5Iwg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.sentry.io/platforms/php/guides/laravel/\"]"
---

**TL;DR:** Laravel's Sentry setup uses SENTRY_LARAVEL_DSN (not SENTRY_DSN), a publish command, and a test command. Plus the php.ini flag for stack trace args and the quota warning on the trace sample rate. Note the prefix: the generic SENTRY_DSN env var is ignored by this SDK. If events never arrive and the config looks right, check you did not set the unprefixed name.

## The fix

# Sentry Laravel: SENTRY_LARAVEL_DSN is not SENTRY_DSN

## Setup

```
composer require sentry/sentry-laravel
php artisan sentry:publish --dsn=___PUBLIC_DSN___
```

The publish command creates `config/sentry.php` and writes the DSN to your `.env` as `SENTRY_LARAVEL_DSN`. Note the prefix: the generic `SENTRY_DSN` env var is ignored by this SDK. If events never arrive and the config looks right, check you did not set the unprefixed name.

Verify with the built-in command before writing any test routes:

```
php artisan sentry:test
```

## Stack trace arguments

To receive function arguments in stack traces, set in php.ini:

```
zend.exception_ignore_args = Off
```

PHP strips exception args by default, so without this your frames show signatures with no values.

## The quota warning is literal

```
SENTRY_TRACES_SAMPLE_RATE=1.0
```

The docs say, verbatim: be sure to lower this value in production otherwise you could burn through your quota quickly. The example ships at 1.0. For granular control use `traces_sampler`, and if queued jobs generate more traces than web requests, lower the rate per job with the `SentryTracesSampleRate` job middleware.

## Keep it out of dev and test

Sentry is active while developing and running tests unless you stop it, which slows your suite and pollutes your issue stream. Set `SENTRY_LARAVEL_DSN=null` (or leave it undefined) in your local and testing env files.

## When to use this

- This covers exactly what the title says: Sentry Laravel.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Sentry; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Mentions 1.0 in the original; behavior may differ on much older or newer releases.

## Edge cases

- Keep it out of dev and test Sentry is active while developing and running tests unless you stop it, which slows your suite and pollutes your issue stream.

---

Source: [Vectle](https://vectle.com/skills/skl_lwsuMc50A5h2mMjKUf5Iwg). Version: `skv_ETp78Z3zaxkESzx7QzdWZw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
