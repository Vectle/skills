---
name: "google-ads-destination-90c1889642cfd7dc"
description: "Covers the confirmed gotchas when setting up the PostHog Google Ads destination: conversion goals in the right account, the 6-hour wait on new conversion actions, no gclid filter needed, frontend events for empty gclid, and the fixed 401 auth bug. Use when wiring PostHog to Google Ads conversions. Not for other ad destinations, or for Google Ads API issues outside PostHog."
metadata:
  skill_id: "skl_NvogKKe_VhEMr6mOdJYLGg"
  title: "Google Ads destination"
  version: "skv_X7xQlkwr3twPrZYVvQih0g"
  updated: "2026-10-03T04:40:36.778717+00:00"
  canonical_url: "https://vectle.com/skills/skl_NvogKKe_VhEMr6mOdJYLGg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/posthog/posthog/issues/27712\"]"
---

The confirmed gotchas from the thread, in order of how often they bite:

```text
the click ID is associated with an Ads account you do not have access to
```

1. Create the conversion goals in the same Google Ads account where the campaigns live. Otherwise you get the click-ID error above. Expected: no account-access errors when importing conversions.
2. Newly created conversion actions can take up to 6 hours before Google lets you import conversions into them. PostHog does not retry failed requests, so wait and use the testing tab to resend events. Expected: imports succeed after the wait.
3. You do not need a gclid filter. The destination already skips events without a valid gclid. Expected: nothing to configure here.
4. If gclid is empty, use a frontend event instead of a backend event, since gclid comes from the browser. Expected: events carry a valid gclid.
5. If you saw 401 'invalid authentication credentials' in early 2025: that was a PostHog environment-variable migration bug, fixed server-side. Users confirmed calls started succeeding again. Expected: no action needed now.

When to use: setting up or debugging the PostHog Google Ads destination.

When not to use: other ad destinations (Meta, TikTok), or Google Ads API problems that have nothing to do with PostHog.

Compatibility: PostHog Google Ads destination. Thread from the PostHog Feature Flags repo.

Variants:
- "posthog google ads destination conversion import"
- "posthog gclid empty frontend event"
- "posthog google ads 401 invalid authentication credentials"

Root cause: mostly setup ordering and account scoping, not one single bug. The 401s were a PostHog-side migration bug.

Edge cases: the 6-hour wait applies per new conversion action. Resend via the testing tab to retry, since PostHog does not retry failed requests on its own.

---

Source: [Vectle](https://vectle.com/skills/skl_NvogKKe_VhEMr6mOdJYLGg). Version: `skv_X7xQlkwr3twPrZYVvQih0g`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
