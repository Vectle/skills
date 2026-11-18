---
name: "error-loading-sso-token-token-for-sso-a7b1d42670bfc1aa"
description: "error loading sso token token for sso does not exist aws cli fails bug"
metadata:
  skill_id: "skl_ieQ8LkPjjkGfCU-3S3sYtA"
  title: "error loading sso token token for sso does not exist aws cli fails bug"
  version: "skv_ifEv1i8_MAKkJ15dW3MebA"
  updated: "2026-11-18T01:54:13.645004+00:00"
  canonical_url: "https://vectle.com/skills/skl_ieQ8LkPjjkGfCU-3S3sYtA"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Run the failing command with the exact named profile you intend to use and note the profile name.

Run an SSO login for that same profile and complete the browser sign-in.

Retry the original command immediately with the same profile.

If the error returns later, compare the SSO start URL and region in the profile with the values used at login; a renamed session or a changed start URL uses a different cache entry.

Check whether a cleanup tool, a roaming profile reset, or a container rebuild deletes the AWS cache folder between sessions.

---

Source: [Vectle](https://vectle.com/skills/skl_ieQ8LkPjjkGfCU-3S3sYtA). Version: `skv_ifEv1i8_MAKkJ15dW3MebA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
