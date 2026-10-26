---
name: "invitation-links-broken-with-your-kong-fb79dd594ed9e0cf"
description: "Shows how to fix invitation links broken with YOUR_KONG_HOST as the domain. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_3vPnZDNtsRrAZXJ11PHR7g"
  title: "Invitation links broken with YOUR_KONG_HOST as the domain"
  version: "skv_s22xHrY2rZwfpNCfjwjcXA"
  updated: "2026-10-03T14:15:43.478529+00:00"
  canonical_url: "https://vectle.com/skills/skl_3vPnZDNtsRrAZXJ11PHR7g"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/supabase/auth/issues/1228\"]"
---

## TL;DR

Set it to your project's external host (your SITE_URL) so the links generated in emails use the right domain. [kangmingtay (maintainer)]: Fixed with a new config param: GOTRUE_MAILER_EXTERNAL_HOSTS.

## Steps

1. [kangmingtay (maintainer)]: Fixed with a new config param: GOTRUE_MAILER_EXTERNAL_HOSTS. Set it to your project's external host (your SITE_URL) so the links generated in emails use the right domain. If your self-hosted Supabase emails link to http://kong, this setting is the fix, no code changes needed.

2. _Source: https://github.com/supabase/auth/issues/1228 (Supabase Auth)_

## When to use

Use this skill when you run into "Invitation links broken with YOUR_KONG_HOST as the domain".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.

## Sources

- YOUR_KONG_HOST

- https://github.com/supabase/auth/issues/1228


---

Source: [Vectle](https://vectle.com/skills/skl_3vPnZDNtsRrAZXJ11PHR7g). Version: `skv_s22xHrY2rZwfpNCfjwjcXA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
