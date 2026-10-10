---
name: "403-forbidden-on-intake-the-api-key-is-7d94b16c813e5207"
description: "The agent logs 403 Forbidden on intake payloads when the API key is wrong, revoked, or belongs to another region. Data stops flowing but the agent keeps running. Not for different error messages."
metadata:
  skill_id: "skl_igDoa8jpcobu1cyZHlcevg"
  title: "403 Forbidden on intake: the API key is wrong, revoked, or for another region"
  version: "skv_N9n0P52lrzUAE5qW9OOAGw"
  updated: "2026-10-03T04:44:12.588112+00:00"
  canonical_url: "https://vectle.com/skills/skl_igDoa8jpcobu1cyZHlcevg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** The agent logs 403 Forbidden on intake payloads when the API key is wrong, revoked, or belongs to another region. Data stops flowing but the agent keeps running. Fix - Open Organization Settings, API Keys in the app and confirm the key exists and is enabled. - Compare the configured key with the stored one (secret manager, not chat). Fix it in the same place. - Re-run datadog-agent status: forwarder accepted payloads means you are done.

## The fix

1. **Wrong key pasted.** An application key was used where the API key goes, or the key has a typo/whitespace. The agent needs the org API key, nothing else.

2. **Key revoked or rotated.** Someone rotated the key in Organization Settings and this host still has the old one.

3. **Right key, wrong region.** The key is valid but your `DD_SITE` points at a region where that org does not exist. Classic after copy-pasting a US1 example into an EU setup.

4. Open Organization Settings, API Keys in the app and confirm the key exists and is enabled.

5. Compare the configured key with the stored one (secret manager, not chat). If they differ, update `datadog.yaml` or the `DD_API_KEY` env and restart.

6. Confirm the site: the URL you log into the app with determines `DD_SITE`. Fix it in the same place.

7. Re-run `datadog-agent status`: forwarder accepted payloads means you are done.

## When to use this

- You are seeing this exact error message; match the block above, not just part of it.
- The failing call matches the scenario in the title: 403 Forbidden on intake.
- You want the fastest verified fix before digging through logs.

## When not to use this

- Your error text differs from the block above; close cousins often have different causes.
- The stack trace points at a different component than the one in the title.
- You already applied this fix and the error persists; look for a second cause instead of reapplying.

## Compatibility

- Not pinned to a specific version; follows current 403 behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_igDoa8jpcobu1cyZHlcevg). Version: `skv_N9n0P52lrzUAE5qW9OOAGw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
