---
name: "gh-auth-login-hangs-with-no-browser-or-600502f198f9ef32"
description: "Gets gh authenticated on headless servers and CI where gh auth login hangs, via piped token login or GH_TOKEN. Use when there is no browser or TTY. Not for interactive desktops."
metadata:
  skill_id: "skl_aUS5jd4jzgnFjHjor62zhQ"
  title: "gh auth login hangs with no browser or prompt in CI and headless servers"
  version: "skv_vDl6WE4aF4s8yL7SigrMDg"
  updated: "2026-10-03T05:59:57.649397+00:00"
  canonical_url: "https://vectle.com/skills/skl_aUS5jd4jzgnFjHjor62zhQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/genxsirai/jloop/blob/HEAD/cron-headless-github-auth.md\"]"
---

Never run interactive gh auth login on a headless box. Pipe a token in instead: echo [token] | gh auth login --with-token, or just export GH_TOKEN. If --with-token hangs too, write the token straight into hosts.yml.

```text
gh auth login
(hangs forever waiting for a browser or device prompt that never comes)
```

## Fix it
1. On a machine with a browser, create a fine-grained or classic PAT with the scopes you need.
   Success check: You have a token value copied.
2. On the headless machine, run: echo [your token] | gh auth login --hostname github.com --with-token
   Success check: gh reports authentication succeeded.
3. Verify with gh auth status.
   Success check: The account shows as logged in for the host.
4. If --with-token hangs (known flakiness in some environments), fall back to writing the token into ~/.config/gh/hosts.yml directly.
   Success check: gh auth status shows the account.

## When this applies
- gh auth login hangs or cannot open a browser on a server, container, or CI runner
- you need gh working non-interactively

## When this does NOT apply
- you have a working browser on the machine (just use the normal flow)
- GH_TOKEN is already exported (gh already authenticates; check gh auth status)

## Compatibility
gh CLI 2.x on Linux servers, containers, CI runners. github.com and GHES.

## Variant phrasings
### GH_TOKEN env var
Exporting GH_TOKEN skips stored auth entirely. Good for CI, but remember it shadows keyring accounts for every gh command in that shell.

## Why it happens
gh auth login's default flow needs a human with a browser. Headless environments have neither, so the flow blocks forever. Piping the token with --with-token performs the same credential storage without any interactive step.

## Edge cases
- Never echo a real token into a shared shell history; prefer a file redirect or a secret manager.
- --with-token has been observed hanging in some VPS environments; the hosts.yml fallback is the reliable escape hatch.
- Tokens minted for CI should be fine-grained with minimal scopes and an expiry.

Source: https://github.com/genxsirai/jloop/blob/HEAD/cron-headless-github-auth.md

---

Source: [Vectle](https://vectle.com/skills/skl_aUS5jd4jzgnFjHjor62zhQ). Version: `skv_vDl6WE4aF4s8yL7SigrMDg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
