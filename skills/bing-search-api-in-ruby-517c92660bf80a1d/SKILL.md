---
name: "bing-search-api-in-ruby-517c92660bf80a1d"
description: "Guide Bing Search API in Ruby: \"Bing Search API - Quick Start\" I would want to use a Ruby sdk but those I found are deprecated ex (Rbing) https://github. Use this when you hit exactly this in Bing Search API. Not for different errors or different tools."
metadata:
  skill_id: "skl_forI6J_VDteLIpwuTeNVfA"
  title: "Bing Search API in Ruby"
  version: "skv_dMjr3IyVBlHlARACpRjF6w"
  updated: "2026-10-03T05:10:59.159481+00:00"
  canonical_url: "https://vectle.com/skills/skl_forI6J_VDteLIpwuTeNVfA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: "Bing Search API - Quick Start" I would want to use a Ruby sdk but those I found are deprecated ex (Rbing) https://github.com/mikedemers/rbing Do you know a up-to-date Wrapper for Bing Search API (Web only results)? What was asked: Stack Overflow #13660455 (accepted answer, 7 votes, 3 answers): I read the "Bing Search API - Quick Start" but I don't know how to make this http request in Ruby (Weary) How to translate "Stream_context_create()" in Ruby?

## Fix
1. "Bing Search API - Quick Start" I would want to use a Ruby sdk but those I found are deprecated ex (Rbing) https://github.com/mikedemers/rbing Do you know a up-to-date Wrapper for Bing Search API (Web only results)?
   Expected: this specific failure stops.
2. Turns out Microsoft's documentation was wrong and you're supposed to just use your account key as the password in the request instead of the encoded string.
   Expected: this specific failure stops.

## Details
What was asked: Stack Overflow #13660455 (accepted answer, 7 votes, 3 answers): I read the "Bing Search API - Quick Start" but I don't know how to make this http request in Ruby (Weary) How to translate "Stream_context_create()" in Ruby? And What does it mean? What works: [Chris Bui (accepted answer)]: Okay, after an hour of frustration I figured out a way to do it. ``` require 'net/http' accountKey [your value] url = 'https://api.datamarket.azure.com/Data.ashx/Bing/SearchWeb/v1/Web?Query=%27xbox%27&$top=50&$format=json' uri = URI(url) req = Net::HTTP::Get.new(uri.request_uri) req.basic_auth '', accountKey res = Net::HTTP.start(uri.hostname, uri.port, :use_ssl => uri.scheme == 'https'){|http| http.request(req) } puts res.body ```

## When to use
You hit exactly this: Bing Search API in Ruby in Bing Search API.

## When not to use
A different error, or the same symptom in a different tool. This page only covers the failure above.

## Compatibility
Bing Search API (versions mentioned here: v1).

## Root cause
This code is awful because it's the first version I got working. Basically, ignore everything about the base64 encode because it was giving me an error that only oAuth and basic authentication was supported.

---

Source: [Vectle](https://vectle.com/skills/skl_forI6J_VDteLIpwuTeNVfA). Version: `skv_dMjr3IyVBlHlARACpRjF6w`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
