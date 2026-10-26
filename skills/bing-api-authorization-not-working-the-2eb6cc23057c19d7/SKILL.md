---
name: "bing-api-authorization-not-working-the-2eb6cc23057c19d7"
description: "Fix for Bing API Authorization not working - The authorization type you provided is not supported. Only Basic and: What was asked: Stack Overflow #11989959 (accepted answer, 3 votes, 4 answers): I recently got an email from Microsoft saying that the Bing API was moving to the Windows Azure Marketplace. Use this when you hit exactly this in Bing API Authorization. Not for different errors or different tools."
metadata:
  skill_id: "skl__cyg2aJ29gSk9Q0xNeV46g"
  title: "Bing API Authorization not working - The authorization type you provided is not supported. Only Basic and OAuth are supp"
  version: "skv_4D3qcidYWblv8xP4HWS4_A"
  updated: "2026-10-03T14:00:15.920042+00:00"
  canonical_url: "https://vectle.com/skills/skl__cyg2aJ29gSk9Q0xNeV46g"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://stackoverflow.com/questions/11989959\"]"
---

TL;DR: What was asked: Stack Overflow #11989959 (accepted answer, 3 votes, 4 answers): I recently got an email from Microsoft saying that the Bing API was moving to the Windows Azure Marketplace. It seemed that the main difference between the new request was the authentication. After reading many posts on forums, I found this:

```text
Bing API Authorization not working - The authorization type you provided is not supported. Only Basic and OAuth are supp
```

## Fix
1. What was asked: Stack Overflow #11989959 (accepted answer, 3 votes, 4 answers): I recently got an email from Microsoft saying that the Bing API was moving to the Windows Azure Marketplace.
   Expected: this specific failure stops.
2. It seemed that the main difference between the new request was the authentication.
   Expected: this specific failure stops.
3. After reading many posts on forums, I found this:.
   Expected: this specific failure stops.
4. ``` $accountKey [your value] $api = 'YOUR_HOST.datamarket.azure.com/Bing/Search/Web?$format=json&$top=8&Query='; $context = stream_context_create(array( 'http' => array( 'request_fulluri' => true, 'header' => "Authorization: Basic " . base64_encode($accountKey . ":" . $accountKey) ) )); $request = $api.'%27'.$q.'%27&$skip='.$start; $result = file_get_c

What works:
[user94559 (accepted answer)]: I think the URLs have changed. This code works. Note the URL in the first line: ```.
   Expected: this specific failure stops.

## Details
What was asked: Stack Overflow #11989959 (accepted answer, 3 votes, 4 answers): I recently got an email from Microsoft saying that the Bing API was moving to the Windows Azure Marketplace. It seemed that the main difference between the new request was the authentication. After reading many posts on forums, I found this: ``` $accountKey [your value] $api = 'YOUR_HOST.datamarket.azure.com/Bing/Search/Web?$format=json&$top=8&Query='; $context = stream_context_create(array( 'http' => array( 'request_fulluri' => true, 'header' => "Authorization: Basic " . base64_encode($accountKey . ":" . $accountKey) ) )); $request = $api.'%27'.$q.'%27&$skip='.$start; $result = file_get_c

What works:
[user94559 (accepted answer)]: I think the URLs have changed. This code works. Note the URL in the first line: ``` $api = 'YOUR_HOST.datamarket.azure.com/Data.ashx/Bing/Search/v1/Web?$format=json&$top=8&Query='; $context = stream_context_create(array( 'http' => array( 'request_fulluri' => true, 'header' => "Authorization: Basic " . base64_encode($accountKey . ":" . $accountKey) ) )); $q = 'test'; $request = $api.'%27'.$q.'%27'; echo file_get_contents($request, 0, $context); `` `

## When to use
You hit exactly this: Bing API Authorization not working - The authorization type you provided is not supported. Only Basic and OAuth are supp in Bing API Authorization.

## When not to use
A different error, or the same symptom in a different tool. This page only covers the failure above.

## Compatibility
Bing API Authorization (versions mentioned here: v1).

---

Source: [Vectle](https://vectle.com/skills/skl__cyg2aJ29gSk9Q0xNeV46g). Version: `skv_4D3qcidYWblv8xP4HWS4_A`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
