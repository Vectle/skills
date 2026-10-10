---
name: "downloading-file-though-box-api-2-0-gi-9317ff7fbe8423d3"
description: "With respect to @Miguel-F's comment, I've surfed and found a solution from Ben Nadel's post. I've got 200 as response, this is because ColdFusion followed the redirect to dl.boxcloud.com (since by default, the REDIRECT attribute is TRUE), and the redirected request's response is 200. Actually we should stop the redirect by setting REDIRECT attribute to FALSE. So that Coldfusion will return actual response to the invoking code. So I've set REDIRECT attribute to FALSE. ``` [cfh Use when hitting th"
metadata:
  skill_id: "skl_I_FrhAUiT6eURV_351VAqg"
  title: "Downloading file though Box API 2.0 giving 200 as response instead of 302 found"
  version: "skv_xGhxfYyHjwAu5a3AgZMs9w"
  updated: "2026-10-04T04:45:14.575007+00:00"
  canonical_url: "https://vectle.com/skills/skl_I_FrhAUiT6eURV_351VAqg"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

## TL;DR

With respect to @Miguel-F's comment, I've surfed and found a solution from Ben Nadel's post. I've got 200 as response, this is because ColdFusion followed the redirect to dl.boxcloud.com (since by default, the REDIRECT attribute is TRUE), and the redirected request's response is 200. Actually we should stop the redirect by setting REDIRECT attribute to FALSE.

With respect to @Miguel-F's comment, I've surfed and found a solution from Ben Nadel's post. I've got 200 as response, this is because ColdFusion followed the redirect to dl.boxcloud.com (since by default, the REDIRECT attribute is TRUE), and the redirected request's response is 200. Actually we should stop the redirect by setting REDIRECT attribute to FALSE. So that Coldfusion will return actual response to the invoking code. So I've set REDIRECT attribute to FALSE. ``` [cfhttp url="https://api.box.com/2.0/files/(FILE_ID)/content/" method="GET" redirect="false" ] [cfhttpparam type="header" name="Authorization" value="Bearer (DEVELOPER_TOKEN)"] [/cfhttp] ``` And now I'm getting 302 found as response as per the documentation. With this response, we're having Location key (in which the code was redirected earlier) in the ResponseHeader. So by using the Location URL we can download the file using CFHEADER and CFCONTENT tags. Reference : https://www.bennadel.com/blog/934-ask-ben-handling-redirects-with-coldfusion-cfhttp.htm

Context: Stack Overflow question (score 5, has accepted answer): I'm trying to download a file from Box.com through API using the following code. ``` [cfhttp url="https://api.box.com/2.0/files/(FILE_ID)/content/" method="GET" redirect="true" ] [cfhttpparam type="header" name="Authorization" value="Bearer (DEVELOPER_TOKEN)"] [/cfhttp] ``` As per documentation it should return 302 Found as response. And redirects to dl.boxcloud.com for download. But I'm getting 200 as response. Not sure why I'm getting 200 as response. I need to download the file through the API call. Did I missed anything?

## When to use

- You hit this exact issue.
- The symptom matches: Downloading file though Box API 2.0 giving 200 as response instead of 302 found.

## When NOT to use

- A different error or symptom; the cause here is specific to this one.

## Compatibility

Per the linked source (mentions 2.0).

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- If the fix does not help, capture the full error output and check the source link for updates.

---

Source: [Vectle](https://vectle.com/skills/skl_I_FrhAUiT6eURV_351VAqg). Version: `skv_xGhxfYyHjwAu5a3AgZMs9w`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
