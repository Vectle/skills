---
name: "datadog-api-key-vs-application-key-the-05f85b4d6874184d"
description: "The Datadog agent submits with an API key. Programmatic API calls need the API key plus an application key. Mixing them up is the most common auth failure, and it looks identical to a wrong key. Not the full reference manual."
metadata:
  skill_id: "skl_DCX_IBF-Ai7FpUT3XuVzFA"
  title: "Datadog API key vs application key - the agent takes the API key, scripts take both"
  version: "skv_RzY3t6RigFk_jk-ku8cn2w"
  updated: "2026-10-03T13:55:50.117111+00:00"
  canonical_url: "https://vectle.com/skills/skl_DCX_IBF-Ai7FpUT3XuVzFA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** The Datadog agent submits with an API key. Programmatic API calls need the API key plus an application key. Create and rotate it under Organization Settings, API Keys. Add the DD-APPLICATION-KEY header. - API call with an app key from a user who lost permissions: it worked last month and now 403s.

# Datadog API key vs application key

Two keys, two jobs. Agents confuse them constantly because both are long hex strings and the error for using the wrong one is just 403.

## Which is which

- **API key**: belongs to the organization, not a person. The agent uses it to submit metrics, events, logs, traces. Create and rotate it under Organization Settings, API Keys. If this leaks, rotate it: agents everywhere will need the new one, so plan that.
- **Application key**: belongs to a user, inherits that users permissions by default. Used together with an API key for programmatic API access (curl, Terraform provider, scripts). Some API endpoints need extra scopes granted on the app key before they work, see Actions API access in the docs.

## The mapping agents get wrong

| Task | Key needed |
|---|---|
| Install/configure the agent | API key only |
| DogStatsD, APM, log intake via agent | API key only (on the agent) |
| curl to the API, Terraform provider, custom scripts | API key AND application key |
| RUM browser SDK | client token, neither key |

## Symptoms of mixing them up

- Agent install with an application key pasted as the API key - agent starts, intake returns 403, nothing appears. The fix is replacing it with a real API key.
- API call with only an API key and no app key - 401/403 on most endpoints. Add the `DD-APPLICATION-KEY` header.
- API call with an app key from a user who lost permissions: it worked last month and now 403s. Check the key owners role.

## Hygiene

- One-Time Read mode exists for viewing a key value a single time. Use it, then store the key in a secret manager, not in a repo or chat.
- Name keys by purpose (terraform-prod, ci-read) so rotation does not become archaeology.
- Application keys die with offboarding: if the user who created it is deactivated, integrations using it break. Prefer keys owned by a service account user for automation.

## When to use this

- This covers exactly what the title says: Datadog API key vs application key.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Datadog; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current Datadog behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_DCX_IBF-Ai7FpUT3XuVzFA). Version: `skv_RzY3t6RigFk_jk-ku8cn2w`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
