---
name: "datadog-dd-site-the-region-parameter-t-66b433cd86412841"
description: "DD_SITE tells the agent which Datadog region your org lives in. US1 is datadoghq.com, EU is datadoghq.eu, plus us3, us5, ap1, ap2 and gov sites. Wrong site means a healthy-looking agent that never shows up."
metadata:
  skill_id: "skl_2U0nGcmKetKnrAV4xrxvxg"
  title: "Datadog DD_SITE: the region parameter that must match where your org lives"
  version: "skv_IonGJfqOHP3iNIeWwzjAkg"
  updated: "2026-10-03T05:07:59.890624+00:00"
  canonical_url: "https://vectle.com/skills/skl_2U0nGcmKetKnrAV4xrxvxg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** DD_SITE tells the agent which Datadog region your org lives in. US1 is datadoghq.com, EU is datadoghq.eu, plus us3, us5, ap1, ap2 and gov sites. The agent installs fine, starts fine, and your hosts never appear. The tracers default to US1, so EU/APAC orgs must set it or traces go nowhere. - API calls: the API hostname changes too, e.g. https://api.datadoghq.eu for EU.

# Datadog site parameter: match it to your org or nothing works

This is the number one silent failure in Datadog setups. The agent installs fine, starts fine, and your hosts never appear. Nine times out of ten it is the site.

## The table (from the docs, Access the Datadog site)

| Your org lives at | DD_SITE / site parameter |
|---|---|
| app.datadoghq.com (US1) | datadoghq.com |
| us3.datadoghq.com | us3.datadoghq.com |
| us5.datadoghq.com | us5.datadoghq.com |
| app.datadoghq.eu (EU1, Germany) | datadoghq.eu |
| ap1.datadoghq.com (Japan) | ap1.datadoghq.com |
| ap2.datadoghq.com | ap2.datadoghq.com |
| app.ddog-gov.com (US1-FED) | ddog-gov.com |

Rule: look at the URL in your browser when you log into Datadog. That domain minus `app.` and the scheme is your site parameter.

## Where it goes

- **Host agent**: `site:` in `datadog.yaml`, or `DD_SITE` in the environment when you run the installer.
- **Containers**: `DD_SITE` env var on the agent container. The docs call this out explicitly as one of the two required container env vars alongside `DD_API_KEY`.
- **Tracers/SDKs**: `DD_SITE` env var. The tracers default to US1, so EU/APAC orgs must set it or traces go nowhere.
- **API calls**: the API hostname changes too, e.g. `https://api.datadoghq.eu` for EU. The API reference lists every regional endpoint.

## How to confirm you got it right

After install, `datadog-agent status` shows the site the agent is reporting to. If the agent is up but the host never appears in Infrastructure, check that line first. A 403 on intake payloads is the other classic symptom: your key is valid, just valid in a different region.

## Trap

Docs and blog posts almost always show `datadoghq.com` examples. If your org is EU or APAC, copy-pasting those examples without changing the site is exactly how you end up debugging a ghost.

## When to use this

- This covers exactly what the title says: Datadog DD_SITE.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Datadog; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current Datadog behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_2U0nGcmKetKnrAV4xrxvxg). Version: `skv_IonGJfqOHP3iNIeWwzjAkg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
