---
name: "unsupported-startup-parameter-the-clie-9e3acad144957eb0"
description: "Shows how to fix \"unsupported startup parameter\": the client sends what Neon rejects. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_MruYfT3aaJpLJuHKUct49A"
  title: "\"unsupported startup parameter\": the client sends what Neon rejects"
  version: "skv_1tCRYFpBYwpqulTH0tTyNQ"
  updated: "2026-10-03T16:33:18.125365+00:00"
  canonical_url: "https://vectle.com/skills/skl_MruYfT3aaJpLJuHKUct49A"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

## TL;DR

Neon's proxy rejects unknown startup parameters instead of ignoring them. The parameter name in the error; check whether your driver added it by default or via config.

## Steps

1. Some clients/drivers send extra startup parameters on connect (common with newer drivers sending options the proxy allowlist does not include). Neon's proxy rejects unknown startup parameters instead of ignoring them.

2. The parameter name in the error; check whether your driver added it by default or via config.
2. Other clients without that parameter connect fine with the same string.

3. - Remove or override the parameter in the client configuration/connection options.
- If the driver requires it, check the driver's docs for a compatibility flag; as a last resort use a different driver version.
- Report it: parameters that mainstream drivers send by default are worth flagging to Neon support.

## When to use

You are seeing this: Connection fails immediately with unsupported startup parameter: [parameter-name]. Use this skill when you run into ""unsupported startup parameter": the client sends what Neon rejects".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

Some clients/drivers send extra startup parameters on connect (common with newer drivers sending options the proxy allowlist does not include).


---

Source: [Vectle](https://vectle.com/skills/skl_MruYfT3aaJpLJuHKUct49A). Version: `skv_1tCRYFpBYwpqulTH0tTyNQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
