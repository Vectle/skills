---
name: "accessing-set-cookie-value-from-respon-013db4f2815919ab"
description: "Shows how to fix accessing Set-Cookie value from response.headers in axios. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_AWhEWZPVoq-0pRzNFxIpcg"
  title: "Accessing Set-Cookie value from response.headers in axios"
  version: "skv_F_KKLTk-xw8bdfPAFASLZA"
  updated: "2026-10-04T08:25:10.00576+00:00"
  canonical_url: "https://vectle.com/skills/skl_AWhEWZPVoq-0pRzNFxIpcg"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

## TL;DR

[Vasily (top answer)] This approach works, but should be handled on a server side if it's HttpOnly cookie: `` const res = await axios....; const cookieName = '...'; const cookie = (res.headers['set-cookie'] as string[]).find(cookie => cookie.includes(cookieName)) ?.match(new RegExp(^${cookieName}=(.+?);)) ?.[1]; ` Context: Stack Overflow #70972629 (top answer, 3 votes, 3 answers): I am using VueJS and Axios to send a request like this: ` axiosAPI.get('/login/flows', {params: {id: 'string'}}).then(res => { console.log('cookie', res.headers) } ` In return server sends me this response: `` Access

## Steps

1. [Vasily (top answer)] This approach works, but should be handled on a server side if it's HttpOnly cookie:

``` const res = await axios....; const cookieName = '...'; const cookie = (res.headers['set-cookie'] as string[]) .find(cookie => cookie.includes(cookieName)) ?.match(new RegExp(`^${cookieName}=(.+?);`)) ?.[1]; ```

``` axiosAPI.get('/login/flows', {params: {id: 'string'}}) .then(res => { console.log('cookie', res.headers) } ```

2. In return server sends me this response: ``` Access-Control-Allow-Credentials - true Access-Control-Allow-Origin: * Access-Control-Expose-Headers: Content-Type Cache-Control: private, no-cache, no-store, must-revalidate Content-Length: 646 Content-Type: application/json; charset=utf-8 Date: Thu,xxxx 13:56:21 GMT Set-Cookie: csrf_token [your value] Path=/.ory/kratos/pub

## When to use

Use this skill when you run into "Accessing Set-Cookie value from response.headers in axios".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_AWhEWZPVoq-0pRzNFxIpcg). Version: `skv_F_KKLTk-xw8bdfPAFASLZA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
