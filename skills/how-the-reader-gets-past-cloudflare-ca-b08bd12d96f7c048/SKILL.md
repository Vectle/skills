---
name: "how-the-reader-gets-past-cloudflare-ca-b08bd12d96f7c048"
description: "The Reader does not beat Cloudflare with stealth plugins alone. Use this skill when the task matches the title above. Not for unrelated tools or errors; check the tool's own docs for those."
metadata:
  skill_id: "skl_PQY88awJpfZaw6j1jxjj2w"
  title: "How the Reader gets past Cloudflare: cache salvage and bot user agents"
  version: "skv_tFmb72ZqqiBeelQDBQwqcQ"
  updated: "2026-10-03T05:07:21.320566+00:00"
  canonical_url: "https://vectle.com/skills/skl_PQY88awJpfZaw6j1jxjj2w"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/jina-ai/reader/issues/66\"]"
---

## TL;DR

The Reader does not beat Cloudflare with stealth plugins alone. Per the maintainer, it falls back to a salvage path: query the Google web cache (now discontinued) or the Web Archive for the page, and set the user agent to a well-known bot like Slackbot, GPTBot, or GoogleSpider, which many sites let through.

## Fix

The Reader does not beat Cloudflare with stealth plugins alone. Per the maintainer, it falls back to a salvage path: query the Google web cache (now discontinued) or the Web Archive for the page, and set the user agent to a well-known bot like Slackbot, GPTBot, or GoogleSpider, which many sites let through. If you are building your own reader and stealth fails on a protected page, try the same ladder: fetch from the Web Archive first, then retry with a bot user agent before burning effort on captcha solving.

Context: Issue jina-ai/reader#66 (closed, 7 comments): a user asked how the Jina Reader gets past Cloudflare protection on heavily guarded pages when puppeteer-extra-plugin-stealth alone is not enough, since the source shows no captcha solving. A maintainer explained the actual mechanisms.

## Matched source
Source: Published skill
Original query: "How the Reader gets past Cloudflare: cache salvage and bot user agents"
Key terms: agents, cache, cloudflare, gets, past, reader, salvage, user

## When to use this

- Use this when your task, error, or question matches the title above and the setup in the Fix section.

## When not to use this

- Skip it when the error text, tool, or situation is different. Forcing a mismatched fix usually costs more time than searching again.

## Compatibility

The original write-up does not pin tool versions. Treat the commands and UI paths above as reflecting the author's setup, and check your tool's own docs if your version looks different.


---

Source: [Vectle](https://vectle.com/skills/skl_PQY88awJpfZaw6j1jxjj2w). Version: `skv_tFmb72ZqqiBeelQDBQwqcQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
