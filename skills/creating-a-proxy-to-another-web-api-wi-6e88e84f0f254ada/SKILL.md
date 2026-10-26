---
name: "creating-a-proxy-to-another-web-api-wi-6e88e84f0f254ada"
description: "[Gimly (accepted answer)] I ended up implementing a proxy middleware inspired by a project in Asp.Net's GitHub. Use this skill when the task matches the title above. Not for unrelated tools or errors; check the tool's own docs for those."
metadata:
  skill_id: "skl_5ihf8LDwre8Hr_od0fIxwg"
  title: "Creating a proxy to another web api with Asp.net core"
  version: "skv_I_soNk_FBGBclbpaceszqw"
  updated: "2026-10-03T05:04:13.661969+00:00"
  canonical_url: "https://vectle.com/skills/skl_5ihf8LDwre8Hr_od0fIxwg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://stackoverflow.com/questions/42000362\"]"
---

## TL;DR

[Gimly (accepted answer)] I ended up implementing a proxy middleware inspired by a project in Asp.Net's GitHub. It basically implements a middleware that reads the request received, creates a copy from it and sends it back to a configured service, reads the response from the service and sends it back to the caller.

## Fix

[Gimly (accepted answer)] I ended up implementing a proxy middleware inspired by a project in Asp.Net's GitHub. It basically implements a middleware that reads the request received, creates a copy from it and sends it back to a configured service, reads the response from the service and sends it back to the caller.

Context: Stack Overflow #42000362 (accepted answer, 26 votes, 9 answers): I'm developing an ASP.Net Core web application where I need to create a kind of "authentication proxy" to another (external) web service. What I mean by authentication proxy is that I will receive requests through a specific path of my web app and will have to check the headers of those requests for an authentication token that I'll have issued earlier, and then redirect all the requests with the same request string / content to an external web API which my app will authenticate with through HTTP Basic auth. Here's the whole process in pseudo-code - Client requests a token by making a POST

## Matched source
Source: Published skill
Original query: "Creating a proxy to another web api with Asp.net core"
Key terms: another, core, creating, proxy

## When to use this

- Use this when your task, error, or question matches the title above and the setup in the Fix section.

## When not to use this

- Skip it when the error text, tool, or situation is different. Forcing a mismatched fix usually costs more time than searching again.

## Compatibility

The original write-up does not pin tool versions. Treat the commands and UI paths above as reflecting the author's setup, and check your tool's own docs if your version looks different.


---

Source: [Vectle](https://vectle.com/skills/skl_5ihf8LDwre8Hr_od0fIxwg). Version: `skv_I_soNk_FBGBclbpaceszqw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
