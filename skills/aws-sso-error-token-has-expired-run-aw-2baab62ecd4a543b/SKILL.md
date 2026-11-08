---
name: "aws-sso-error-token-has-expired-run-aw-2baab62ecd4a543b"
description: "aws sso error token has expired run aws sso login fails"
metadata:
  skill_id: "skl_fFyER6HTHDvUFygZLD8Pew"
  title: "aws sso error token has expired run aws sso login fails"
  version: "skv_JWqaFxqGUHfHUNS7L2ZcgQ"
  updated: "2026-11-08T13:53:46.931158+00:00"
  canonical_url: "https://vectle.com/skills/skl_fFyER6HTHDvUFygZLD8Pew"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Check the system date and time are set automatically and are correct.

Run aws sso logout, then run aws sso login with your named profile flag if you use one.

Approve the sign in in the browser and return to the terminal.

If login still reports an expired session, delete the cached SSO files in the sso cache folder inside your .aws folder, then repeat step 2.

Verify with aws sts get-caller-identity using the same profile.

---

Source: [Vectle](https://vectle.com/skills/skl_fFyER6HTHDvUFygZLD8Pew). Version: `skv_JWqaFxqGUHfHUNS7L2ZcgQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
