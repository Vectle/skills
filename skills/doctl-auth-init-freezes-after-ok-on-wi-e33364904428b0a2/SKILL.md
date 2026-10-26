---
name: "doctl-auth-init-freezes-after-ok-on-wi-e33364904428b0a2"
description: "Fixes doctl auth init freezing after printing OK on Windows. Use this when the interactive init accepts the token but never returns to the prompt. Not for auth rejections or non-Windows installs."
metadata:
  skill_id: "skl_DAj8jw8V_lI-D27QgblMFw"
  title: "doctl auth init freezes after OK on Windows"
  version: "skv_WsUAejw5EPucCN_yUc_NEw"
  updated: "2026-10-03T04:48:15.332096+00:00"
  canonical_url: "https://vectle.com/skills/skl_DAj8jw8V_lI-D27QgblMFw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://vectle.com/threads/thr_hJMXmqBl7rWBL3o1CwHwlw\",\"https://github.com/digitalocean/doctl/issues/891\"]"
---

TL;DR: if `doctl auth init` on Windows accepts your API token, prints OK, then freezes and never returns to the prompt (even though --trace shows the API call returned 200), skip the interactive flow entirely. Create the config file yourself at `%APPDATA%\doctl\config.yaml` with just the access-token entry, then run doctl normally. The reporter confirmed doctl works after manually filling the file, and the maintainer confirmed that is all the file needs to contain.

## Steps

1. Create `%APPDATA%\doctl\config.yaml` containing only the access-token entry for your token.

2. Run doctl normally (no elevated CMD needed, just read/write access to the file).

   Expected: commands authenticate. Success check: a simple `doctl account get` works.

## When to use this

- doctl 1.48.1 on Windows 10, auth init freezes post-OK.

## When NOT to use this

- Auth is rejected; check the token.
- Non-Windows; the interactive flow works there.

## Compatibility

- doctl 1.48.1 on Windows (thread closed 2020; the workaround stands).

## Variant phrasings

- "doctl auth init hangs windows"
- "doctl freezes after OK"

## Root cause

The interactive init flow hung on Windows after the token validated, never completing its final steps.

## Edge cases

- You do not need an elevated CMD; plain read/write access to the config file is enough.

---

Source: [Vectle](https://vectle.com/skills/skl_DAj8jw8V_lI-D27QgblMFw). Version: `skv_WsUAejw5EPucCN_yUc_NEw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
