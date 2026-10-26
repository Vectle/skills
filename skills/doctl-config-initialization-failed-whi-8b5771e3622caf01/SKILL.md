---
name: "doctl-config-initialization-failed-whi-8b5771e3622caf01"
description: "Fixes doctl dying at startup with Config initialization failed: While parsing config after v1.158.0 writes a config file it cannot read back. Use when every doctl command, including auth init and auth list, fails with a yaml parse error at startup. Not for Unable to authenticate you after auth init, which is a bad token, not a broken config file."
metadata:
  skill_id: "skl_2Ae2RH-2EWlozOCfbSuv6A"
  title: "doctl: Config initialization failed: While parsing config: yaml: did not find expected key"
  version: "skv_MR54VcfPCPT9DVeXWHSN4Q"
  updated: "2026-10-03T04:41:21.106955+00:00"
  canonical_url: "https://vectle.com/skills/skl_2Ae2RH-2EWlozOCfbSuv6A"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/digitalocean/doctl/issues/1842\"]"
---

# doctl: Config initialization failed: While parsing config: yaml: did not find expected key

TL;DR: your doctl config file got mangled. doctl v1.158.0 writes a config.yaml that its own parser rejects, so every command dies at startup. Fix: move the broken config aside and re-run `doctl auth init` to generate a fresh one. If the problem comes back on that version, downgrade to v1.157.0, which reads the same file fine.

```text
doctl: 2026/05/07 21:08:20 Config initialization failed: While parsing config: yaml: line 2228: did not find expected key
```

## Steps

1. Back up the broken config, then remove it:

```bash
cp ~/.config/doctl/config.yaml ~/.config/doctl/config.yaml.bak
rm ~/.config/doctl/config.yaml
```

Expected: no output. `ls ~/.config/doctl/` no longer shows config.yaml.

2. Re-authenticate to regenerate the config:

```bash
doctl auth init
```

Expected: doctl prompts for your DigitalOcean access token, then prints a success message. A fresh config file is created.

3. Verify auth works:

```bash
doctl auth list
```

Expected: your context listed, e.g. `default (current)`.

## When this applies

- every doctl command fails at startup with `Config initialization failed: While parsing config` and a yaml line number
- the error names a line at or past the end of the file (the parser expects more YAML than the writer produced)
- it started right after upgrading doctl to v1.158.0

## When it doesnt

- `Error: Unable to authenticate you` after `doctl auth init` — that is a bad or expired token, not a config file problem
- `doctl: command not found` — that is a PATH or install problem

## Compatibility

doctl v1.158.0 (the broken writer). v1.157.0 reads the same files fine, and later releases fixed the writer. Config lives at `~/.config/doctl/config.yaml` on Linux and macOS.

## Why it happens

v1.158.0 shipped a config schema change for DOKS SSO per-cluster config (PR #1835). The serializer writes YAML the bundled parser cannot read back: it emits a truncated section, then expects more keys than exist. PyYAML parses the same file fine, so the file itself is valid YAML — the bug is doctl's own read path.

## Edge cases

- In CI, prefer the DIGITALOCEAN_ACCESS_TOKEN env var over auth init so a bad config can never block a run
- If you had multiple contexts, re-add each one after regenerating; the .bak file keeps the old values for reference (keep it out of version control)
- The same failure also shows up worded as `could not find expected ':'`

## Find this skill again

```bash
curl -s 'https://vectle.com/api/v1/search?q=doctl+config+initialization+failed+yaml'
```


---

Source: [Vectle](https://vectle.com/skills/skl_2Ae2RH-2EWlozOCfbSuv6A). Version: `skv_MR54VcfPCPT9DVeXWHSN4Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
