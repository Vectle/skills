---
name: "chronosphere-notifier-doesn-t-trigger-f4d3c8123c49d0ca"
description: "Chronosphere: notifier doesn't trigger after an alert fires. Either wait for the alert to trigger again (the default repeat interval is one hour) or recreate the alert. Use when hitting this exact issue with Chronosphere. Not for unrelated errors or different features."
metadata:
  skill_id: "skl_nEtHA2pd_MWk8Tb3Gkc1rQ"
  title: "Chronosphere: notifier doesn't trigger after an alert fires"
  version: "skv_oz1O5orZ3ZaRC3yfPYwyDw"
  updated: "2026-10-03T14:09:23.524816+00:00"
  canonical_url: "https://vectle.com/skills/skl_nEtHA2pd_MWk8Tb3Gkc1rQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Either wait for the alert to trigger again (the default repeat interval is one hour) or recreate the alert. Notifier changes take effect only after the next alert trigger.

## Fix

1. Either wait for the alert to trigger again (the default repeat interval is one hour) or recreate the alert.
   Expected: You get the expected result; the problem is gone.

## When to use

- You are setting up or using this Chronosphere feature.
- The symptom matches: notifier doesn't trigger after an alert fires.

## When NOT to use

- Unrelated Chronosphere issues (different feature, different failure).
- You need general documentation for the tool; check the official docs instead.

## Compatibility

Reported against Chronosphere. Source: https://docs.chronosphere.io/investigate/alerts/troubleshooting.

## Variant phrasings

### notifier doesn't trigger after an alert fires

## Why it happens

The alert fired but the notifier change you made didn't take effect. Notifications send after the alert triggers, so notifier edits apply from the next trigger.

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- If the fix does not help, capture the full error output and check the source link for updates.

## Source

https://docs.chronosphere.io/investigate/alerts/troubleshooting

---

Source: [Vectle](https://vectle.com/skills/skl_nEtHA2pd_MWk8Tb3Gkc1rQ). Version: `skv_oz1O5orZ3ZaRC3yfPYwyDw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
