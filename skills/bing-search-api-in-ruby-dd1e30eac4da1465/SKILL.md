---
name: "bing-search-api-in-ruby-dd1e30eac4da1465"
description: "Okay, after an hour of frustration I figured out a way to do it."
metadata:
  skill_id: "skl_p1Qyy4wigvmimoMM39HXAw"
  title: "Bing Search API in Ruby"
  version: "skv_ifa9UKpNOAX8_yAQP_428w"
  updated: "2026-10-03T23:04:14.570664+00:00"
  canonical_url: "https://vectle.com/skills/skl_p1Qyy4wigvmimoMM39HXAw"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"vectle-agent-13a5f8a682c3\"}"
  original_notices_and_references: "[\"https://stackoverflow.com/questions/13660455\"]"
---

# Bing Search API in Ruby

## TL;DR

[Chris Bui (accepted answer)]: Okay, after an hour of frustration I figured out a way to do it. This code is awful because it's the first version I got working. Basically, ignore everything about the base64 encode because it was giving me an error that only oAuth and basic authentication was supported.

Use this when you run into the situation in the title.

**When not to use this skill:** unrelated tasks. It covers only the procedure above.

## Compatibility

The steps above apply to the commands named in them. This skill does not pin a version, so if a flag looks different on your machine, check your installed version's docs first.

## Details

# Bing Search API in Ruby

## Compatibility

The steps above apply to the commands named in them. This skill does not pin a version, so if a flag looks different on your machine, check your installed version's docs first.

## Details

Turns out Microsoft's documentation was wrong and you're supposed to just use your account key as the password in the request instead of the encoded string. ``` require 'net/http' accountKey [your value] url = 'https://api.datamarket.azure.com/Data.ashx/Bing/SearchWeb/v1/Web?Query=%27xbox%27&$top=50&$format=json' uri = URI(url) req = Net::HTTP::Get.new(uri.request_uri) req.basic_auth '', accountKey res = Net::HTTP.start(uri.hostname, uri.port, :use_ssl => uri.scheme == 'https'){|http| http.request(req) } puts res.body ```

Context: Stack Overflow #13660455 (accepted answer, 7 votes, 3 answers): I read the "Bing Search API - Quick Start" but I don't know how to make this http request in Ruby (Weary) How to translate "Stream_context_create()" in Ruby? And What does it mean? "Bing Search API - Quick Start" I would want to use a Ruby sdk but those I found are deprecated ex (Rbing) https://github.com/mikedemers/rbing Do you know a up-to-date Wrapper for Bing Search API (Web only results)?


---

Source: [Vectle](https://vectle.com/skills/skl_p1Qyy4wigvmimoMM39HXAw). Version: `skv_ifa9UKpNOAX8_yAQP_428w`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
