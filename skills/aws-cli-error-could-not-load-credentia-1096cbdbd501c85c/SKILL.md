---
name: "aws-cli-error-could-not-load-credentia-1096cbdbd501c85c"
description: "aws cli error could not load credentials token is expired sso login fails bug"
metadata:
  skill_id: "skl_6wp9EdArpgrn6-dHNoRwnQ"
  title: "aws cli error could not load credentials token is expired sso login fails bug"
  version: "skv_waS8Mpd3RWL-7lbFgVXN0w"
  updated: "2026-11-03T13:52:51.71707+00:00"
  canonical_url: "https://vectle.com/skills/skl_6wp9EdArpgrn6-dHNoRwnQ"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

**Confirm which profile the failing command uses.** Check the command itself, your shell, and your config for a profile name: most SSO setups use a named profile, not the default. Expected: you can name the exact profile, for example the one set in AWS_PROFILE or passed with the profile flag.

**Re-login to SSO for that profile.** Run aws sso login with the same profile name and complete the browser sign-in when it opens. Success check: the command finishes with a success message for that profile instead of a token expired error.

**Verify the refreshed credentials load.** Run aws sts get-caller-identity with the same profile. Expected: it prints an account id, a user id, and an ARN for the SSO role. If this still fails, the login refreshed a different profile than the one your command uses.

**Retry the original command unchanged.** Run it with the same profile flag or environment you used before. Success check: the command reaches AWS and returns data instead of stopping at credential loading.

**If login itself fails in the browser step, fix the session start.** Sign out of stale SSO sessions in the browser, sign in with the account that has the assigned role, and run the login step again. Expected: the browser approval completes and the CLI caches a fresh session with a later expiry.

---

Source: [Vectle](https://vectle.com/skills/skl_6wp9EdArpgrn6-dHNoRwnQ). Version: `skv_waS8Mpd3RWL-7lbFgVXN0w`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
