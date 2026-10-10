---
name: "mojoauth-oidc-hosted-login-you-get-acc-43d6d18cf2e0b33d"
description: "use the hosted OIDC flow when you dont want to own login UI."
metadata:
  skill_id: "skl_a-SfVsJ4ezofMiWannrGpw"
  title: "MojoAuth OIDC hosted login: you get access, ID, and refresh token semantics for free"
  version: "skv_i_McdPuZZ_C-cbrQkCOKRA"
  updated: "2026-10-03T19:21:08.682188+00:00"
  canonical_url: "https://vectle.com/skills/skl_a-SfVsJ4ezofMiWannrGpw"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

# MojoAuth OIDC hosted login: you get access, ID, and refresh token semantics for free

## TL;DR

use the hosted OIDC flow when you dont want to own login UI. Register your redirect URI in the MojoAuth dashboard, send users to the hosted login, and handle the callback by validating the ID token server-side before creating your session. Store the refresh token securely server-side and use it to renew sessions without re-prompting the user.

Use this when you run into the situation in the title.

**When not to use this skill:** unrelated tasks. It covers only the procedure above.

## Compatibility

The steps above apply to the commands named in them. This skill does not pin a version, so if a flag looks different on your machine, check your installed version's docs first.

## Details

Because the channel list lives in MojoAuths config, enabling passkeys later is a dashboard toggle, not a code change. Keep your redirect URI allowlist tight: an open redirect there undermines the whole flow.

Context: Web: a MojoAuth OIDC integration guide documents what the hosted login flow hands you. Instead of building login UI, you redirect to MojoAuths hosted page and get back the standard OIDC set: an access token, an ID token, and refresh token semantics, plus session handling the guide wires into the apps login event. The guide also notes the same flow supports passkey, magic link, email OTP, phone OTP, and social logins without you changing the integration. Source: https://securityboulevard.com/2025/10/unlock-passwordless-login-on-bubble-with-mojoauth-next-gen-openid-connect-oidc-authentication/


---

Source: [Vectle](https://vectle.com/skills/skl_a-SfVsJ4ezofMiWannrGpw). Version: `skv_i_McdPuZZ_C-cbrQkCOKRA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
