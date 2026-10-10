---
name: "passwordless-magic-links-connection-se-69122de080257128"
description: "Magic links remove passwords but add device-binding and expiry traps. Configure the connection, set the link lifetime deliberately, and design for the newest-link-wins behavior. Not the full reference manual."
metadata:
  skill_id: "skl_9W91gDHWTpsfBdazIu1LcA"
  title: "Passwordless magic links: connection setup, link lifetime, UX traps"
  version: "skv_wnotvHQzb_XC4IMe-xRcQw"
  updated: "2026-10-03T04:38:15.9881+00:00"
  canonical_url: "https://vectle.com/skills/skl_9W91gDHWTpsfBdazIu1LcA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** Magic links remove passwords but add device-binding and expiry traps. Configure the connection, set the link lifetime deliberately, and design for the newest-link-wins behavior. Enable Dashboard > Authentication > Passwordless > Email: enable, choose Link (or Code, or both). Configure the email provider first (custom provider for production).

## The fix

# Passwordless magic links

## 1. Enable

Dashboard > Authentication > Passwordless > Email: enable, choose Link (or Code, or both). Configure the email provider first (custom provider for production). Enable the passwordless connection on the application.

## 2. Link lifetime

Links expire (configurable, minutes to hours). Shorter is safer; too short and slow inboxes make every link dead on arrival. 15-30 minutes is the sane band for most products.

## 3. The device trap

The link is bound to the browser session that requested it (PKCE verifier in storage). User requests on desktop, opens email on phone: fails. Mitigations:

- Offer the OTP code alongside the link (device-independent).
- Say it in the UI: "Open this link on the device where you requested it."
- Or use codes only, no links, if your users are cross-device.

## 4. Newest wins

Requesting a second link invalidates the first. Users who double-click "send link" then click the first email fail. The UI should say "use the newest email" and throttle resends with a countdown.

## 5. Login call

```
authorizationParams: { connection: "email" }
```

Pin the connection or users fall into the database flow. Universal Login renders the passwordless prompt automatically when the connection is passwordless.

## Checklist

- Link lifetime set deliberately; code fallback offered.
- Resend UI throttled; newest-wins communicated.

## When to use this

- This covers exactly what the title says: Passwordless magic links.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Passwordless; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current Passwordless behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_9W91gDHWTpsfBdazIu1LcA). Version: `skv_wnotvHQzb_XC4IMe-xRcQw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
