---
name: "fix-rclone-icloud-backend-invalid-sess-004d72e9d304c99d"
description: "Fixes rclone iCloud 'Invalid Session Token' by updating to rclone v1.74.0+, which uses SRP auth after Apple deprecated the plaintext endpoint. Use when a previously working iCloud remote breaks without config changes. Not for rate limits or initial setup problems."
metadata:
  skill_id: "skl__hzIcAOhIatfP_E4f_2a9g"
  title: "Fix rclone iCloud backend Invalid Session Token error"
  version: "skv_d5ZNyww3bcKCsTHXDEgsQw"
  updated: "2026-10-03T04:11:44.051997+00:00"
  canonical_url: "https://vectle.com/skills/skl__hzIcAOhIatfP_E4f_2a9g"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[]"
---

## TL;DR

Update rclone to v1.74.0 or later. Apple replaced the plaintext-password auth endpoint rclone's iCloud backend used with SRP, so every older build fails the handshake permanently. If 2FA still fails after updating and your Apple ID has uppercase letters, update to the latest patch (SRP hashes are case-sensitive).

## Symptom
rclone fails to connect to an iCloud Drive remote with an Invalid Session Token error, often working previously and breaking without any local config change.

## Root cause
Apple deprecated the plaintext password-posting auth endpoint rclone's iCloud backend relied on, replacing it with SRP, Secure Remote Password. Any rclone build predating the SRP rewrite fails this handshake permanently, not intermittently.

## Fix
1. Update rclone to v1.74.0 or later. This alone resolves the error for most users.
2. If two-factor authentication fails after updating and your Apple ID contains uppercase letters, this is a known follow-up bug since SRP hashes are case sensitive, fixed shortly after the initial SRP release. Make sure you are on the latest patch, not just anything at or above 1.74.0.

## If you cannot update yet
Extract iCloud session cookies from a browser login and inject them into rclone.conf manually. This is a stopgap, not a fix. Plan to update instead of maintaining a cookie refresh workflow.

**When not to use this skill:** the iCloud remote never worked (check the remote config first); the error is a rate limit or quota problem rather than auth.

## Do not
Do not attempt to patch the old plaintext auth flow yourself, or store iCloud Apple ID passwords in plaintext in scripts or config as some early workarounds attempted. The SRP requirement exists because Apple deprecated the insecure path for a reason.

## Compatibility

- rclone v1.74.0+: iCloud backend uses SRP auth. Older builds fail permanently.
- Apple ID with 2FA; uppercase letters in the Apple ID need the latest patch.

## Variant phrasings

- rclone iCloud Invalid Session Token
- rclone icloud drive auth failed SRP
- rclone Apple ID uppercase 2FA fails



---

Source: [Vectle](https://vectle.com/skills/skl__hzIcAOhIatfP_E4f_2a9g). Version: `skv_d5ZNyww3bcKCsTHXDEgsQw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
