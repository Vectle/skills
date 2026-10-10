---
name: "docusign-php-client-apiexception-getre-45ce9a5251e33e2e"
description: "Shows how to fix docusign-php-client: ApiException#getResponseObject returns serialized PHP string instead of object. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_bCGMZgmDMeGw0jeFL_gdAg"
  title: "docusign-php-client: ApiException#getResponseObject returns serialized PHP string instead of object"
  version: "skv_hNGsN-5lBQXquwbxU32D3w"
  updated: "2026-10-03T14:17:30.683965+00:00"
  canonical_url: "https://vectle.com/skills/skl_bCGMZgmDMeGw0jeFL_gdAg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

The situation: In docusign-php-client v4.0.0, ApiException#getResponseObject() stopped returning a deserialized ErrorDetails object and instead returned a serialized PHP object as a string, breaking error handling that worked in v3.0.1.

## Steps

1. In docusign-php-client v4.0.0, ApiException#getResponseObject() stopped returning a deserialized ErrorDetails object and instead returned a serialized PHP object as a string, breaking error handling that worked in v3.0.1. The reporter traced it to a new code path in ApiClient::callApi that serialized the response without ObjectSerializer ever deserializing it back. The change was not listed in the breaking changes notes.

2. What actually fixes it (verified in the thread):

3. Upgrade to v5.5, where the maintainer fixed it: composer require docusign/esign-client:^5.5 (the fix was first available in the 5.5.0-RC). The DocuSign team confirmed the fix on the issue before closing it. Source: https://github.com/docusign/docusign-esign-php-client/issues/83

## When to use

You are seeing this: The reporter traced it to a new code path in ApiClient::callApi that serialized the response without ObjectSerializer ever deserializing it back. Use this skill when you run into "docusign-php-client: ApiException#getResponseObject returns serialized PHP string instead of object".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

Versions mentioned in the source: docusign-php-client v4.0.0, v3.0.1, v5.5, 5.5.0-RC. If you are on something much newer or older, the details may have shifted.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.

## Sources

- https://github.com/docusign/docusign-esign-php-client/issues/83


---

Source: [Vectle](https://vectle.com/skills/skl_bCGMZgmDMeGw0jeFL_gdAg). Version: `skv_hNGsN-5lBQXquwbxU32D3w`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
