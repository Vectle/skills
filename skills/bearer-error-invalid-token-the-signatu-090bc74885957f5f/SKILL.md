---
name: "bearer-error-invalid-token-the-signatu-090bc74885957f5f"
description: "Shows how to fix bearer error - invalid_token - The signature key was not found. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_hnLFuW3CXvpcCxzKoX680Q"
  title: "Bearer error - invalid_token - The signature key was not found"
  version: "skv_WyazOWTJLAcAneWiV99AEg"
  updated: "2026-10-03T20:29:11.975984+00:00"
  canonical_url: "https://vectle.com/skills/skl_hnLFuW3CXvpcCxzKoX680Q"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

## TL;DR

For "): WWW-Authenticate: Bearer error=": [Muhammad Maaz (top answer)] I was facing the same issue. i was missing the authority..make sure authority and api name is correct now this code in configure services in startup file works for me: `` services.AddAuthentication(IdentityServerAuthenticationDefaults.AuthenticationScheme).AddIdentityServerAuthentication( x => { x.Authority = "YOUR\_HOST (port 5000)"; //idp address x.RequireHttpsMetadata = false; x.ApiName = "api2"; //api name }); `` Context: Stack Overflow #58563661 (top answer, 22 votes, 13 answers): I have an Angular 7 application interf

```text
): WWW-Authenticate: Bearer error=
```

## Steps

1. [Muhammad Maaz (top answer)] I was facing the same issue. i was missing the authority..make sure authority and api name is correct now this code in configure services in startup file works for me:

``` services.AddAuthentication(IdentityServerAuthenticationDefaults.AuthenticationScheme) .AddIdentityServerAuthentication( x => { x.Authority = "YOUR_HOST (port 5000)"; //idp address x.RequireHttpsMetadata = false; x.ApiName = "api2"; //api name }); ```

## When to use

You are seeing this: This is interfacing with Azure Active Directory. Use this skill when you run into "Bearer error - invalid_token - The signature key was not found".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_hnLFuW3CXvpcCxzKoX680Q). Version: `skv_WyazOWTJLAcAneWiV99AEg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
