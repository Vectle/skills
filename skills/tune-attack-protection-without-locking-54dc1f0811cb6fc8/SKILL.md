---
name: "tune-attack-protection-without-locking-54dc1f0811cb6fc8"
description: "Attack protection defaults are aggressive. Tune before launch: brute-force shield thresholds, breached-password behavior, suspicious IP throttling, and bot detection, in that order. Not the full reference manual."
metadata:
  skill_id: "skl_J0zTFJpv_glFNTJiPk5IQw"
  title: "Tune attack protection without locking out real users: shields, throttles, alerts"
  version: "skv_NXmVDf1Si6TEcuLWjwcS9A"
  updated: "2026-10-03T05:54:10.682974+00:00"
  canonical_url: "https://vectle.com/skills/skl_J0zTFJpv_glFNTJiPk5IQw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://auth0.com/docs/secure/attack-protection\"]"
---

**TL;DR:** Attack protection defaults are aggressive. Tune before launch: brute-force shield thresholds, breached-password behavior, suspicious IP throttling, and bot detection, in that order. Enable it; it is the cheapest layer. Never silently allow a known-breached password on an admin account.

# Attack protection tuning

## The layers

Dashboard > Security > Attack Protection:

1. Bot Detection: scores login traffic by IP reputation and behavior; challenges suspected bots. Enable it; it is the cheapest layer.
2. Suspicious IP Throttling: throttles auth attempts from an IP after thresholds, before blocking accounts. This catches distributed guessing without punishing users.
3. Brute-Force Protection: blocks the account after N failed attempts for that account. The shield that pages you at 3am when a shared office IP trips it.
4. Breached Password Detection: checks passwords against breach corpuses at login/signup; options are block, notify, or notify-admin.

## Tuning without friendly fire

- Order matters: throttling before shields. Throttling absorbs the spray; the shield only fires on targeted account attacks.
- Shared IPs (offices, universities, VPNs): raise brute-force thresholds or rely more on throttling, or every typo storm blocks real users behind the NAT.
- Notify: enable the blocked-account email so users self-serve the unblock instead of filing tickets.
- Breached passwords: "block and require reset" for new signups; for existing users prefer "notify user" first, then escalate. Never silently allow a known-breached password on an admin account.

## Monitoring

Attack protection events are in tenant logs (separate event types). Stream them to your SIEM and alert on spikes, not on single blocks. A sudden 10x in throttled IPs is the signal; one blocked account is noise.

## What not to do

- Do not disable everything because of one false positive; tune the threshold.
- Do not load-test login with bad passwords against production; use a test tenant.

## Checklist

- Each layer enabled with deliberate thresholds before launch.
- Unblock path tested (do you know the clicks?).

## When to use this

- This covers exactly what the title says: Tune attack protection without locking out real users.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Tune; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current Tune behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_J0zTFJpv_glFNTJiPk5IQw). Version: `skv_NXmVDf1Si6TEcuLWjwcS9A`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
