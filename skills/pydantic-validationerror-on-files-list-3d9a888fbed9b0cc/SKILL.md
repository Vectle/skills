---
name: "pydantic-validationerror-on-files-list-3d9a888fbed9b0cc"
description: "Guide pydantic ValidationError on files.list() means the API shape changed; upgrade the client: Takeaways: (1) upgrade merge-python-client to the latest release when you hit pydantic ValidationError on list() calls, spec drift is the usual culprit; (2) if you cannot upgrade, skip the SDK and. Use this when you hit exactly this in pydantic. Not for different errors or different tools."
metadata:
  skill_id: "skl_FBWFx44R9iLkmDM7-jhG5w"
  title: "pydantic ValidationError on files.list() means the API shape changed; upgrade the client"
  version: "skv_XnMcYQQ9bL-nRiMOwceSkQ"
  updated: "2026-10-03T13:56:35.198142+00:00"
  canonical_url: "https://vectle.com/skills/skl_FBWFx44R9iLkmDM7-jhG5w"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: Takeaways: (1) upgrade merge-python-client to the latest release when you hit pydantic ValidationError on list() calls, spec drift is the usual culprit; (2) if you cannot upgrade, skip the SDK and call the REST endpoint directly ( The root cause was in the OpenAPI spec, not your code: the `permissions`

## Fix
1. Takeaways: (1) upgrade merge-python-client to the latest release when you hit pydantic ValidationError on list() calls, spec drift is the usual culprit; (2) if you cannot upgrade, skip the SDK and call the REST endpoint directly (.
   Expected: this specific failure stops.

## Details
The root cause was in the OpenAPI spec, not your code: the `permissions` field changed shape (from a list of string ids to a list of objects) and the generated SDK's parsing model rejected real responses. Maintainer rmkonnur pushed a corrected File Storage spec and regenerated the client, which fixed it. `GET YOUR_HOST.merge.dev/api/filestorage/v1/files`

## When to use
You hit exactly this: pydantic ValidationError on files.list() means the API shape changed; upgrade the client in pydantic.

## When not to use
A different error, or the same symptom in a different tool. This page only covers the failure above.

## Compatibility
pydantic (versions mentioned here: v1).

## Edge cases
- with your API key and account token headers) and parse the JSON yourself.

---

Source: [Vectle](https://vectle.com/skills/skl_FBWFx44R9iLkmDM7-jhG5w). Version: `skv_XnMcYQQ9bL-nRiMOwceSkQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
