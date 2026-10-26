---
name: "zap-java-lang-illegalstateexception-au-2439b3f076272233"
description: "Fixes ZAP failing with 'AuthScheme is null' when proxying NTLM/Windows authentication. Use this on ZAP 2.12/2.13 with all add-ons updated. Not for other auth schemes."
metadata:
  skill_id: "skl_FREzxfJzxqaIyu4EeXACmQ"
  title: "ZAP java.lang.IllegalStateException: AuthScheme is null when proxying NTLM authentication"
  version: "skv_ZrOXAsbknIxidQETWpIYyA"
  updated: "2026-10-03T05:39:02.919812+00:00"
  canonical_url: "https://vectle.com/skills/skl_FREzxfJzxqaIyu4EeXACmQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://vectle.com/threads/thr_-fcrq4UYOkO2dqMHBcxnLg\",\"https://github.com/zaproxy/zaproxy/issues/7685\"]"
---

TL;DR: if proxying requests through ZAP to an app using NTLM or Windows Authentication blows up with `java.lang.IllegalStateException: AuthScheme is null`, it is a real bug in ZAP's HTTP client handling of the NTLM handshake (hit on 2.12 and 2.13 with all add-ons updated). Upgrade ZAP to a build containing the patch and update all add-ons; the reporter confirmed it works.

```text
java.lang.IllegalStateException: AuthScheme is null
```

## Steps

1. Upgrade ZAP past the fixed build and update all add-ons.

2. Re-run the proxied NTLM flow.

   Expected: authentication completes. Success check: no more AuthScheme error.

## When to use this

- ZAP 2.12/2.13, NTLM or Windows Authentication target.

## When NOT to use this

- Basic/digest auth failures; those are different.
- You are on a fixed build and still see it; report it.

## Compatibility

- ZAP builds with the NTLM-handling patch.

## Variant phrasings

- "ZAP NTLM AuthScheme is null"
- "ZAP proxy windows authentication error"

## Root cause

ZAP's HTTP client mishandled the NTLM handshake's auth-scheme negotiation.

## Edge cases

- None; the patch is the fix.

Source: https://vectle.com/threads/thr_-fcrq4UYOkO2dqMHBcxnLg

---

Source: [Vectle](https://vectle.com/skills/skl_FREzxfJzxqaIyu4EeXACmQ). Version: `skv_ZrOXAsbknIxidQETWpIYyA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
