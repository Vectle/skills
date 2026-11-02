---
name: "notauthorizedexception-user-is-disable-eed9e130a0304732"
description: "notauthorizedexception: user is disabled."
metadata:
  skill_id: "skl_3AQtj9Q-dQgLrBeDBExszQ"
  title: "notauthorizedexception: user is disabled."
  version: "skv_lEHuw9bHx73IsIUww62ZpA"
  updated: "2026-11-02T16:08:32.258054+00:00"
  canonical_url: "https://vectle.com/skills/skl_3AQtj9Q-dQgLrBeDBExszQ"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Confirm the state with `aws cognito-idp admin-get-user --user-pool-id POOL_ID --username USERNAME`. Expected: the output shows Enabled set to false, which proves the disable and rules out a password or app client problem.

Re-enable sign-in with `aws cognito-idp admin-enable-user --user-pool-id POOL_ID --username USERNAME`. Expected: the command returns success with no error body, and a repeat of step 1 shows Enabled set to true.

Retry the sign-in exactly as the user did. Expected: authentication proceeds past the disabled check (to a token response or the next challenge such as MFA), with no User is disabled message.

If the user lands back at disabled, find what disabled them: an admin-disable-user call in your own admin tooling, an offboarding or cleanup script, or a Lambda trigger. CloudTrail records the AdminDisableUser event with the caller, so check there before re-enabling a second time. Expected: you can name the actor or automation that ran the disable.

If the disable was deliberate (offboarding, abuse), leave the account disabled and make the app handle this error with a clear account-disabled message instead of a generic login failure. Expected: the user sees an intentional message, and support stops treating it as a password reset case.

---

Source: [Vectle](https://vectle.com/skills/skl_3AQtj9Q-dQgLrBeDBExszQ). Version: `skv_lEHuw9bHx73IsIUww62ZpA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
