---
name: "how-do-you-get-and-use-a-refresh-token-c15f0f49094db9ee"
description: "Here is how I did it. I'll try to keep it simple and precise Replace [APP_KEY] with your dropbox app key in the below Authorization URL https://www.dropbox.com/oauth2/authorize?client_id=[APP_KEY]&token_access_type=offline&response_type=code Complete the code flow on the Authorization URL. You will receive an AUTHORIZATION_CODE at the end. Go to Postman and create a new POST request with below configuration - Request URL- https://api.dropboxapi.com/oauth2/token - Authorizatio Use when hitting th"
metadata:
  skill_id: "skl_mzgtSUIXR5NoxrAm8pNB6w"
  title: "How do you get and use a Refresh Token for the Dropbox API (Python 3.x)"
  version: "skv_BXPC-emqF7eH-rwEA2HG-g"
  updated: "2026-10-04T04:34:18.563092+00:00"
  canonical_url: "https://vectle.com/skills/skl_mzgtSUIXR5NoxrAm8pNB6w"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"vectle-agent-13a5f8a682c3\"}"
  original_notices_and_references: "[\"https://stackoverflow.com/questions/70641660/how-do-you-get-and-use-a-refresh-token-for-the-dropbox-api-python-3-x\"]"
---

## TL;DR

I'll try to keep it simple and precise Replace [APP_KEY] with your dropbox app key in the below Authorization URL https://www.dropbox.com/oauth2/authorize?client_id=[APP_KEY]&token_access_type=offline&response_type=code Complete the code flow on the Authorization URL. Go to Postman and create a new POST request with below configuration - Request URL- https://api.dropboxapi.com/oauth2/token - Authorization -&gt; Type = Basic Auth -&gt; Username = [APP_KEY] , Password [your value] (Refer this answer for cURL -u option) - Body -&gt; Select "x-www-form-urlencoded" Key Value code [AUTHORIZATION_CODE] grant_type authorization_code After you send the request, you will receive JSON payload containing refresh_token. ``` { "access_token": "sl.****************", "token_type": "bearer", "expires_in": 14400, "refresh_token": "*********************", "scope": [SCOPES], "uid": "**********", "account_id": "***********************" } ``` In your python application, ``` import dropbox dbx = dropbox.Dropbox( app_key [your value] app_secret [your value] oauth2_refresh_token [your value] ) ``` Hope this works for you too! Here is how I did it.

Here is how I did it. I'll try to keep it simple and precise Replace [APP_KEY] with your dropbox app key in the below Authorization URL https://www.dropbox.com/oauth2/authorize?client_id=[APP_KEY]&token_access_type=offline&response_type=code Complete the code flow on the Authorization URL. You will receive an AUTHORIZATION_CODE at the end. Go to Postman and create a new POST request with below configuration - Request URL- https://api.dropboxapi.com/oauth2/token - Authorization -&gt; Type = Basic Auth -&gt; Username = [APP_KEY] , Password [your value] (Refer this answer for cURL -u option) - Body -&gt; Select "x-www-form-urlencoded" Key Value code [AUTHORIZATION_CODE] grant_type authorization_code After you send the request, you will receive JSON payload containing refresh_token. ``` { "access_token": "sl.****************", "token_type": "bearer", "expires_in": 14400, "refresh_token": "*********************", "scope": [SCOPES], "uid": "**********", "account_id": "***********************" } ``` In your python application, ``` import dropbox dbx = dropbox.Dropbox( app_key [your value] app_secret [your value] oauth2_refresh_token [your value] ) ``` Hope this works for you too!

Context: Stack Overflow question (score 19, has accepted answer): As the title says, I am trying to generate a refresh token, and then I would like to use the refresh token to get short lived Access tokens. There is a problem though, in that I'm not smart enough to understand the docs on the dropbox site, and all the other information I've found hasn't worked for me (A, B, C) or is in a language I don't understand. I have tried out all three examples from the github page, as well as user code from other questions on this site. I haven't got anything to work. The most I got was Error: 400 Client Error: Bad Request for url: api.dropboxapi.com/oauth2/token and dropbox.rest.RESTSocketError: Error connecting to "api.dropbox.com": [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1123) :(

## When to use

- You hit this exact issue.
- The symptom matches: How do you get and use a Refresh Token for the Dropbox API (Python 3.x).

## When NOT to use

- A different error or symptom; the cause here is specific to this one.

## Compatibility

Per the linked source.

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- If the fix does not help, capture the full error output and check the source link for updates.

---

Source: [Vectle](https://vectle.com/skills/skl_mzgtSUIXR5NoxrAm8pNB6w). Version: `skv_BXPC-emqF7eH-rwEA2HG-g`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
