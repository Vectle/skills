---
name: "sentry-rails-initializer-gems-and-the-59badd2fc83cf769"
description: "Rails setup lives in config/initializers/sentry.rb with two gems (three for profiling). Ruby defaults to restrictive data collection, and profiles_sample_rate is relative to the trace sample rate. Not the full reference manual."
metadata:
  skill_id: "skl_vXd2zAYETE-c-nzv1gIKaw"
  title: "Sentry Rails: initializer, gems, and the relative profile rate"
  version: "skv_CjrPfzYTzP375hKbCsjREA"
  updated: "2026-10-03T04:35:24.094216+00:00"
  canonical_url: "https://vectle.com/skills/skl_vXd2zAYETE-c-nzv1gIKaw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.sentry.io/platforms/ruby/guides/rails/\"]"
---

**TL;DR:** Rails setup lives in config/initializers/sentry.rb with two gems (three for profiling). Ruby defaults to restrictive data collection, and profiles_sample_rate is relative to the trace sample rate. Verify Raise in a controller action and hit it through a real request. Missing events with a correct DSN usually mean the initializer never ran (check it is in config/initializers and not behind a conditional that skips your environment).

## Setup

```ruby
# Gemfile
gem "sentry-ruby"
gem "sentry-rails"
gem "stackprof" # only if you want profiling
```

```ruby
# config/initializers/sentry.rb
Sentry.init do |config|
  config.dsn = '___PUBLIC_DSN___'
  config.breadcrumbs_logger = [:active_support_logger, :http_logger]
  config.traces_sample_rate = 0.1 # docs example is 1.0; adjust for production
  config.profiles_sample_rate = 1.0 # relative to traces_sample_rate, not absolute
end
```

## profiles_sample_rate is relative

This is the trap: `profiles_sample_rate = 1.0` does not mean profile everything. It means profile 100% of sampled traces. With `traces_sample_rate = 0.1` you get profiles for ~10% of requests. If profiling data looks thin, the trace rate is usually the bottleneck, not the profile rate.

## Ruby defaults to restrictive data collection

Unlike the JavaScript SDK, the Ruby SDK does not send user identity data, HTTP bodies, or URL query params by default. You opt in per category with the `data_collection` option. If your Rails events feel sparse compared to a JS frontend's events, that is the default, not a bug. Turn on the categories you need deliberately, and keep PII review in the loop when you do.

## Verify

Raise in a controller action and hit it through a real request. Then check the issue stream. Missing events with a correct DSN usually mean the initializer never ran (check it is in config/initializers and not behind a conditional that skips your environment).

## When to use this

- This covers exactly what the title says: Sentry Rails.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Sentry; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Mentions 0.1, 1.0 in the original; behavior may differ on much older or newer releases.

---

Source: [Vectle](https://vectle.com/skills/skl_vXd2zAYETE-c-nzv1gIKaw). Version: `skv_CjrPfzYTzP375hKbCsjREA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
