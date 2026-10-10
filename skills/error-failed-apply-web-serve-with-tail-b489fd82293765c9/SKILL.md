---
name: "error-failed-apply-web-serve-with-tail-b489fd82293765c9"
description: "Fixes Tailscale's 'failed apply web serve' error when running tailscale serve or tailscale funnel with a relative path. Use when serving a directory or file fails with the 'only YOUR_HOST or the loopback address proxies' message even though you meant to serve local files. Covers the absolute-path fix for both serve and funnel. Not for serve configs that fail to persist, funnel TLS errors, or backends that genuinely are not local."
metadata:
  skill_id: "skl_lDY1KHbolC48N27rbusezA"
  title: "error: failed apply web serve with tailscale serve (use an absolute path)"
  version: "skv_ZMzu5uscuk_m-nyQu_hBcw"
  updated: "2026-10-03T04:34:56.148602+00:00"
  canonical_url: "https://vectle.com/skills/skl_lDY1KHbolC48N27rbusezA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# Fix "failed apply web serve" when using tailscale serve

**TL;DR:** That scary proxy error is just Tailscale telling you it got a relative path. Pass an absolute path instead: `tailscale serve "$(pwd)"` rather than `tailscale serve .`. Same fix for `tailscale funnel`.

## The error

```text
error: failed apply web serve: only YOUR_HOST or the loopback address proxies are currently supported
```

You get it from `tailscale serve .`, `tailscale serve ./`, or `tailscale funnel` with a relative file path. The message talks about proxies, but the real complaint is the path.

## Fix it

### 1. Use an absolute path

```
tailscale serve "$(pwd)"
```

Or spell it out:

```
tailscale serve [HOME]/...
```

Expected: `Available within your tailnet:` followed by the HTTPS URL, instead of the error.

### 2. Same for funnel

```
tailscale funnel "$(pwd)/index.html"
```

Expected: funnel serves the file publicly instead of erroring.

### 3. Sanity-check what got configured

```
tailscale serve status
```

Expected: your path listed under the right handler. If you see the old broken entry, reset and redo it:

```
tailscale serve reset
```

## When this applies

- `tailscale serve .` or `tailscale serve ./` prints the "failed apply web serve" proxy error
- `tailscale funnel` with a relative path fails the same way
- You are definitely serving local files or a local port, not a remote proxy

## When it does not apply

- You actually are proxying to a remote host (then the error is accurate: only local targets are supported)
- `tailscale serve` config does not survive restarts (different bug, macOS Keychain related)
- Funnel TLS or certificate errors (see the funnel HTTPS skills)

## Tool compatibility

Tailscale 1.60 and newer, all platforms. Reported on Linux (Manjaro, NixOS) and macOS.

## Variant phrasings

### `tailscale serve ./` vs `tailscale serve .`

Both fail identically. Any relative path triggers it; only absolute paths work.

### Same error from `tailscale funnel`

Funnel shares the serve config path, so the same relative-path mistake produces the same message. Absolute path fixes it there too.

## Why it happens

Serve parses a bare `.` or `./` as a proxy target instead of a directory, then rejects it because proxy targets must be local addresses. The error message describes the proxy rule, not the actual mistake, which is why it confuses everyone.

## Edge cases

- **Quoting:** wrap `$(pwd)` in quotes so paths with spaces survive.
- **Trailing slash:** `tailscale serve /path/` and `/path` both work once absolute.
- **After fixing, still failing:** run `tailscale serve reset` to clear the half-applied config, then re-run with the absolute path.

---

Source: [Vectle](https://vectle.com/skills/skl_lDY1KHbolC48N27rbusezA). Version: `skv_ZMzu5uscuk_m-nyQu_hBcw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
