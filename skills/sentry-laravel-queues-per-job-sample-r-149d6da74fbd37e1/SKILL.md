---
name: "sentry-laravel-queues-per-job-sample-r-149d6da74fbd37e1"
description: "Queued jobs fail differently from web requests: they retry, they run long, and they can dominate trace volume. Per-job sample rates and failed-job capture in Laravel. Not the full reference manual."
metadata:
  skill_id: "skl_c-4RjYU4YggzFS4rw-ENQw"
  title: "Sentry Laravel queues: per-job sample rates for noisy workers"
  version: "skv_jzk9xbvMfiSBI-it_t6dCA"
  updated: "2026-10-03T05:06:07.353585+00:00"
  canonical_url: "https://vectle.com/skills/skl_c-4RjYU4YggzFS4rw-ENQw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.sentry.io/platforms/php/guides/laravel/\",\"https://docs.sentry.io/product/releases/\"]"
---

**TL;DR:** Queued jobs fail differently from web requests: they retry, they run long, and they can dominate trace volume. Per-job sample rates and failed-job capture in Laravel. Keep the web rate where it is useful and pin chatty jobs near zero. Make sure the release identifier for worker deploys matches the web deploy, or issues from workers land on a phantom release and resolve-in-release stops working.

## The volume problem

A queue worker processing thousands of jobs an hour at `traces_sample_rate=1.0` generates more spans than your web tier. The docs anticipate exactly this: if queued jobs generate more traces than web requests, lower the rate per job.

```php
use Sentry\Laravel\Jobs\Middleware\SentryTracesSampleRate;

class ProcessPodcast implements ShouldQueue
{
    public function middleware(): array
    {
        return [new SentryTracesSampleRate(0.01)];
    }
}
```

Keep the web rate where it is useful and pin chatty jobs near zero. One middleware per job class, tuned by how often the job runs and how much you care about its traces.

## Failed jobs

Failed job exceptions are captured with the job context. Make sure the release identifier for worker deploys matches the web deploy, or issues from workers land on a phantom release and resolve-in-release stops working. If you deploy workers separately, run the `sentry-cli releases` notify step in that pipeline too.

## Long-running workers

Queue workers are long-lived processes. Scope data (tags, user, breadcrumbs) can leak from one job into the next if you set it globally. Prefer setting context inside the job's `handle()` or via job middleware, so each job starts clean.

## Verify

Dispatch a job that throws, let it fail, and confirm one issue appears with the job class and queue name attached. Two issues for one failure usually means both the worker capture and a manual `captureException` fired; keep one path.

## When to use this

- This covers exactly what the title says: Sentry Laravel queues.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Sentry; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Mentions 1.0, 0.01 in the original; behavior may differ on much older or newer releases.

---

Source: [Vectle](https://vectle.com/skills/skl_c-4RjYU4YggzFS4rw-ENQw). Version: `skv_jzk9xbvMfiSBI-it_t6dCA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
