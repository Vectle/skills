---
name: "supabase-team-invitation-flow-invite-a-f925605b08ebf3df"
description: "Shows how to fix supabase team invitation flow: invite, accept, and join the org in one transaction. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_KTuYyiPlpnhJeo_H_8B7Gw"
  title: "Supabase team invitation flow: invite, accept, and join the org in one transaction"
  version: "skv_7zqP7seXHLXFLKUxWN0g7Q"
  updated: "2026-10-03T14:07:50.662793+00:00"
  canonical_url: "https://vectle.com/skills/skl_KTuYyiPlpnhJeo_H_8B7Gw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://supabase.com/docs/guides/auth/managing-user-data\"]"
---

## TL;DR

Revocation deletes or expires the invite row; already-accepted memberships are removed separately. Invite row before the email. Membership inside the accept transaction, never earlier.

## When to use

You are seeing this: Inviting someone to a team is a multi-step workflow across Auth and your membership tables. Use this skill when you run into "Supabase team invitation flow: invite, accept, and join the org in one transaction".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Team invitations: from invite email to org member without gaps

Inviting someone to a team is a multi-step workflow across Auth and your membership tables. Agents implement half of it: the invite goes out but accepting it does not create the membership, or the membership exists before the user accepts.

## Checkable procedure

1. Create an `invites` table (email, org_id, role, token, expires_at, accepted_at). The invite is data you can list, revoke, and expire, not just an email.
2. Send the invite with `inviteUserByEmail`, redirecting to your accept-invite page. Store the invite row first so the accept step has something to match.
3. On the accept page, the invitee sets their password (or completes OAuth), then your server marks the invite accepted and inserts the `org_members` row in the same transaction. Accept without membership is a dead end; membership without accept is a backdoor.
4. Expire invites (7 days is typical) and enforce single use. Re-accepting an old invite link must not create a second membership or error confusingly.
5. RLS on the invites table: org admins can read and create invites for their org, invitees can read only their own pending invite.

## Ordering constraints

Invite row before the email. Membership inside the accept transaction, never earlier. Revocation deletes or expires the invite row; already-accepted memberships are removed separately.

## Verification

Invite a test email, accept via the link, and confirm exactly one membership with the right role. Try the link again and confirm it is rejected. Expire an invite manually and confirm acceptance fails.


---

Source: [Vectle](https://vectle.com/skills/skl_KTuYyiPlpnhJeo_H_8B7Gw). Version: `skv_7zqP7seXHLXFLKUxWN0g7Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
