---
name: "adyen-encrypted-data-used-outside-of-v-49787ef3158270c5"
description: "Fixes Adyen error 172 Encrypted data used outside of valid time period. Explains the server clock must be correct because encrypted card data is only valid within about 24 hours, the fix of enabling NTP time sync and re-encrypting, and that containers and VMs are the usual drifters. Not for 174 decryption failures, which are key or environment mismatches."
metadata:
  skill_id: "skl_QyrGjQ7lj0XZZ46kvr6BwA"
  title: "Adyen: Encrypted data used outside of valid time period (172)"
  version: "skv_BgsEzB_9psWNPdLX0VuU_w"
  updated: "2026-10-03T04:38:22.094151+00:00"
  canonical_url: "https://vectle.com/skills/skl_QyrGjQ7lj0XZZ46kvr6BwA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.adyen.com/development-resources/error-codes/\"]"
---

# Adyen: Encrypted data used outside of valid time period (172)

**TL;DR:** Your server clock is wrong. Adyen's client-side encrypted card data is only valid within about 24 hours of the real time, so a server stuck in the past (or future) produces 172. Fix the clock with NTP; dont try to work around it in code.

```text
172 - Encrypted data used outside of valid time period
```

## Steps

1. **Check the server time.** Compare `date -u` on the server against real UTC. If it is off by hours, days or years, you found it.
   - *Success check:* server UTC matches actual UTC within a minute.
2. **Enable time sync.** Turn on NTP (chrony/ntpd/systemd-timesyncd) and make sure it actually syncs. Containers and VMs are the usual drifters.
   - *Success check:* the time service reports synchronized, and the offset stays small after a reboot.
3. **Regenerate the encrypted payload.** The old encrypted blob was minted against the wrong clock. Have the shopper re-enter the card (or re-encrypt) and retry.
   - *Success check:* /payments accepts the fresh encrypted data.

## When to use this

- /payments fails with 172, especially on a new server, container, or dev VM.
- The error appears for every card, not just one shopper's.

## When NOT to use this

- 174 (unable to decrypt data). That is a key or environment mismatch, not the clock.
- One shopper out of many. Then it is their data, not your server time.

## Compatibility

Adyen client-side encryption (Web, iOS, Android), Checkout API and classic API.

## Why it happens

The encrypted blob embeds a timestamp so stolen ciphertext cant be replayed forever. Adyen rejects anything encrypted too far from the current time, and a skewed server clock makes fresh encryptions look ancient (or from the future).

## Edge cases

- Docker containers inherit the host clock but can drift if the host does. Fix the host.
- If your CI builds test fixtures with encrypted card data, they rot after 24 hours. Generate them fresh in the test run.


---

Source: [Vectle](https://vectle.com/skills/skl_QyrGjQ7lj0XZZ46kvr6BwA). Version: `skv_BgsEzB_9psWNPdLX0VuU_w`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
