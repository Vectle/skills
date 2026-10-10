---
name: "neon-help-printed-my-neon-api-key-valu-8ebe20dc4b857cd4"
description: "Fixes the leak where older neonctl printed the NEON_API_KEY value inside --help output in CI logs. Use when you spot the raw key in build logs. Upgrades neonctl to the fixed version, rotates the exposed key, and scrubs the logs. Not for keys leaked through other commands."
metadata:
  skill_id: "skl_AQVEMeGJrgEZjRY3fBkatA"
  title: "neon --help printed my NEON_API_KEY value in CI logs"
  version: "skv_3Ow-Esr7q9GjoU7p0M20hQ"
  updated: "2026-10-03T05:54:52.281143+00:00"
  canonical_url: "https://vectle.com/skills/skl_AQVEMeGJrgEZjRY3fBkatA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# neon --help printed my NEON_API_KEY value in CI logs

TL;DR: older neonctl versions interpolated the actual NEON_API_KEY value into `--help` output, so any CI step that printed help leaked the key into logs. Upgrade neonctl to a version with the fix (help shows the variable name, not the value), then treat the old key as compromised: revoke it in the Neon console and issue a new one. Scrub or expire the affected build logs.

```text
neon --help printed the NEON_API_KEY value
```

## Steps

1. Upgrade neonctl to the latest version. Verify: `neon --help` now shows the variable name where the key value used to appear.

2. In the Neon console, revoke the exposed key and create a replacement. Update the CI secret to the new value.

3. Expire or redact the build logs that contain the old key; anyone with log access had the key.

4. Rerun the pipeline. Expected: help output is clean and commands authenticate with the new key.

## When this applies

- NEON_API_KEY visible in CI logs after a --help or --version step
- any credential-adjacent output printed by an old CLI version
- post-incident rotation after a log leak

## When it doesn't

- keys leaked via other commands or misconfigured logging — rotate but the upgrade does not apply
- invalid-key 401s with no leak involved
- local terminal history leaks (different cleanup)

## Compatibility

neonctl; Neon console key revocation; CI log retention controls. Verified against the neon-pkgs neonctl changelog.

## Variant phrasings

- neonctl help printed api key
- NEON_API_KEY leaked CI logs
- neonctl changelog help api key

## Root cause

Old neonctl built help text by interpolating live config values, including the secret. The fixed version prints the variable name as documentation instead of the value. Upgrading stops future leaks but cannot un-leak the old value, so rotation is mandatory.

## Edge cases

- assume any exposed key is compromised even if logs look private; rotate first, investigate second
- check forks/caches of logs (artifacts, mirrors) for the same leak
- pin a minimum neonctl version in CI setup so the old behavior cannot regress

---

Source: [Vectle](https://vectle.com/skills/skl_AQVEMeGJrgEZjRY3fBkatA). Version: `skv_3Ow-Esr7q9GjoU7p0M20hQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
