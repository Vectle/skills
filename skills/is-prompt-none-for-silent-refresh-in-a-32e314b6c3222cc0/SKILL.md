---
name: "is-prompt-none-for-silent-refresh-in-a-32e314b6c3222cc0"
description: "Shows how to fix is prompt=none for silent refresh in a SPA possible with FusionAuth and its provided oauth endpoint?. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_mdcw3Ai40Nuh5fehmEHqeg"
  title: "Is prompt=none for silent refresh in a SPA possible with FusionAuth and its provided oauth endpoint?"
  version: "skv_u98F1iRdwRwg-y6nSbfDlw"
  updated: "2026-10-03T14:11:10.607735+00:00"
  canonical_url: "https://vectle.com/skills/skl_mdcw3Ai40Nuh5fehmEHqeg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://stackoverflow.com/questions/55859793\"]"
---

## TL;DR

I expect prompt=none to work according to OpenID Connect Core 1.0 Thanks for all your help! [voidmain (top answer)] FusionAuth doesn't currently support the prompt=none option for the authorization code grant. This is something we are planning on adding in one of the upcoming releases. However, there is a work-around that others have used.

## When to use

You are seeing this: [voidmain (top answer)] FusionAuth doesn't currently support the prompt=none option for the authorization code grant. Use this skill when you run into "Is prompt=none for silent refresh in a SPA possible with FusionAuth and its provided oauth endpoint?".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

[voidmain (top answer)] FusionAuth doesn't currently support the prompt=none option for the authorization code grant. This is something we are planning on adding in one of the upcoming releases. However, there is a work-around that others have used. You can make an AJAX request to the authorize endpoint of FusionAuth and then check the result to determine if the user needs to log in again or refresh their access token. Here's how it works: User not logged in - Your application makes an AJAX request requests the /oauth2/authorize endpoint - FusionAuth will respond with a 200 and HTML that contains our login form if the user is no longer logged in. - Your application can check the response and see that the user needs to log in and take them to FusionAuth's interface to log back in.

Context: Stack Overflow #55859793 (top answer, 5 votes, 1 answers): I am trying to integrate silent refreshing of access tokens within an iframe by using prompt=none using the oauth authorize endpoint. I can't seem to figure out how to do this or if it is even supported and do not see any information in the documentation here: https://fusionauth.io/docs/v1/tech/oauth/overview I've tried using prompt=none in the URL but it doesn't seem to do anything. I expect prompt=none to work according to OpenID Connect Core 1.0 Thanks for all your help!


---

Source: [Vectle](https://vectle.com/skills/skl_mdcw3Ai40Nuh5fehmEHqeg). Version: `skv_u98F1iRdwRwg-y6nSbfDlw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
