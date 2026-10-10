---
name: "anchor-browser-browser-close-doesnt-en-d559965f08dbe9fd"
description: "Guide Anchor Browser: browser.close() doesnt end the cloud session - call End Browser Session: Always call End Browser Session when the automation is done, or configure session timeouts at create time so idle sessions get reaped. Use this when you hit exactly this in Anchor Browser. Not for different errors or different tools."
metadata:
  skill_id: "skl_Qc9naFcpUweuluHAWkZ3uw"
  title: "Anchor Browser: browser.close() doesnt end the cloud session - call End Browser Session"
  version: "skv_6AteW_LZi23IT0mgDEHTRQ"
  updated: "2026-10-03T05:55:42.213132+00:00"
  canonical_url: "https://vectle.com/skills/skl_Qc9naFcpUweuluHAWkZ3uw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: Always call End Browser Session when the automation is done, or configure session timeouts at create time so idle sessions get reaped. [Anchor Browser official docs, Code Quick Start]: browser.close() in Playwright or Puppeteer only drops the CDP connection, it does not end the cloud session. Otherwise sessions run to timeout and keep burning usage.

## Fix
1. Always call End Browser Session when the automation is done, or configure session timeouts at create time so idle sessions get reaped.
   Expected: this specific failure stops.
2. Otherwise sessions run to timeout and keep burning usage.
   Expected: this specific failure stops.
3. Closing the Playwright or Puppeteer connection does NOT end the Anchor session; the cloud browser stays active until it times out or you explicitly call End Browser Session.
   Expected: this specific failure stops.

## Details
[Anchor Browser official docs, Code Quick Start]: browser.close() in Playwright or Puppeteer only drops the CDP connection, it does not end the cloud session.

## When to use
You hit exactly this: Anchor Browser: browser.close() doesnt end the cloud session - call End Browser Session in Anchor Browser.

## When not to use
A different error, or the same symptom in a different tool. This page only covers the failure above.

## Compatibility
Anchor Browser.

## Edge cases
- Source context: Official docs (Code Quick Start): documents the session lifecycle gotcha that trips agents automating Anchor Browser.

---

Source: [Vectle](https://vectle.com/skills/skl_Qc9naFcpUweuluHAWkZ3uw). Version: `skv_6AteW_LZi23IT0mgDEHTRQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
