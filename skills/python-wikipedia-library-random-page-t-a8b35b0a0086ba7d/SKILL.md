---
name: "python-wikipedia-library-random-page-t-a8b35b0a0086ba7d"
description: "Shows how to fix python wikipedia library: random()/page() throws JSONDecodeError (429 on default user-agent). Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_qqxvSQboBexlyiopoyDeiQ"
  title: "python wikipedia library: random()/page() throws JSONDecodeError (429 on default user-agent)"
  version: "skv_CXWiQ2ATi7D3_w4jby2_zw"
  updated: "2026-10-03T04:48:48.083081+00:00"
  canonical_url: "https://vectle.com/skills/skl_qqxvSQboBexlyiopoyDeiQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

For "python wikipedia library: random()/page() throws JSONDecodeError (429 on default user-agent)": set your own User-Agent instead of Python/requests' default: too many clients share the default UA and get collectively rate-limited by Wikipedia, which surfaces as a JSONDecodeError because the 429 response has no JSON body. Configure a descriptive UA per the Wikimedia user-agent policy (identify your app + contact). Search for your exact error text instead of forcing this one to fit. It documents the symptom and the fix that resolved it.

```text
python wikipedia library: random()/page() throws JSONDecodeError (429 on default user-agent)
```

## When to use

You are seeing this: The reporter confirmed the errors stopped after setting a custom user-agent. Use this skill when you run into "python wikipedia library: random()/page() throws JSONDecodeError (429 on default user-agent)".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Steps

1. Set your own User-Agent instead of Python/requests' default: too many clients share the default UA and get collectively rate-limited by Wikipedia, which surfaces as a JSONDecodeError because the 429 response has no JSON body.

2. 1. Set your own User-Agent instead of Python/requests' default: too many clients share the default UA and get collectively rate-limited by Wikipedia, which surfaces as a JSONDecodeError because the 429 response has no JSON body. Configure a descriptive UA per the Wikimedia user-agent policy (identify your app + contact). The reporter confirmed the errors stopped after setting a custom user-agent.

3. You are seeing this: wikipedia.random() (and other calls) started throwing requests.exceptions.JSONDecodeError: Expecting value: line 1 column 1 (char 0), raised from wikipedia.py's _wiki_request at r.json(). Use this skill when you run into "python wikipedia library: random()/page() throws JSONDecodeError (429 on default user-agent)".

4. If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

5. No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

6. The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_qqxvSQboBexlyiopoyDeiQ). Version: `skv_CXWiQ2ATi7D3_w4jby2_zw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
