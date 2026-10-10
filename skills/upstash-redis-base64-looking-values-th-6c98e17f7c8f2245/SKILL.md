---
name: "upstash-redis-base64-looking-values-th-6c98e17f7c8f2245"
description: "Shows how to fix upstash/redis base64-looking values: the responseEncoding default and when to disable it. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_Enw7r80FSZJfuXpsAUMsSg"
  title: "upstash/redis base64-looking values: the responseEncoding default and when to disable it"
  version: "skv_mkS7e5mFKjWnVBG1RrusIQ"
  updated: "2026-10-03T13:54:54.656568+00:00"
  canonical_url: "https://vectle.com/skills/skl_Enw7r80FSZJfuXpsAUMsSg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

This avoids a class of res.json() deserialization failures on odd byte sequences. Re-run the set/get round trip and get back the original string without manual decoding.

## Steps

1. The SDK asks the REST API for base64-encoded responses by default.
This avoids a class of res.json() deserialization failures on odd
byte sequences. The SDK usually decodes before returning, but raw
config or manual REST calls surface the encoded form.

2. Turn it off if your data is plain text or JSON:

3. const redis = new Redis({
 // ...
 responseEncoding: false,
});

4. Keep it on if you store binary data URIs base64 survives the JSON
transport cleanly, which is the point of the default.

## When to use

You are seeing this: await redis.set("key", "value"); const data = await redis.get("key"); console.log(data); // dmFsdWU= The value stored fine. Use this skill when you run into "upstash/redis base64-looking values: the responseEncoding default and when to disable it".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The SDK asks the REST API for base64-encoded responses by default.


---

Source: [Vectle](https://vectle.com/skills/skl_Enw7r80FSZJfuXpsAUMsSg). Version: `skv_mkS7e5mFKjWnVBG1RrusIQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
