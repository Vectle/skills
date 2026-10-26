---
name: "sendgrid-api-key-scopes-use-restricted-e5b85ab7659b0908"
description: "Choosing SendGrid API key permissions: Full vs Restricted vs Billing scopes, the 100-key limit, the shown-once key, and why a 403 usually means a scope gap. Not for key rotation scheduling or SMTP credential setup."
metadata:
  skill_id: "skl_NAWv1TTlPZ_y9B7dzx2j5Q"
  title: "SendGrid API key scopes: use Restricted Access with Mail Send only"
  version: "skv_ROVNw3IOCtWqVikEZEUM5w"
  updated: "2026-10-03T05:03:00.772122+00:00"
  canonical_url: "https://vectle.com/skills/skl_NAWv1TTlPZ_y9B7dzx2j5Q"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.sendgrid.com/ui/account-and-settings/api-keys\",\"https://docs.sendgrid.com/api-reference/how-to-use-the-sendgrid-v3-api/authentication\",\"https://docs.sendgrid.com/api-reference/how-to-use-the-sendgrid-v3-api/errors\"]"
---

TL;DR: When you create a SendGrid API key, choose the smallest permission that does the job. For production sending, pick Restricted Access and grant only Mail Send. Full Access grants every endpoint and is for development only; Billing Access is for billing endpoints, not mail. If mail send returns 403, check the key's scopes first, not the request body. Copy the key the moment it appears: the console shows it exactly once.

Steps:

1. Go to Settings, API Keys in the SendGrid console and click Create API Key. Success: the creation form is open.
2. Name it something you will recognize in the key list, like prod-mail-send. Success: the name says what it is for.
3. Pick Restricted Access and grant only Mail Send for production sending. Success: the key has exactly the scopes it needs.
4. Copy the key the moment it appears. The console shows it exactly once; a lost key cannot be retrieved or restored. Success: the key is stored before you leave the page.
5. Store it in an environment variable (SENDGRID_API_KEY) and never in code or chat logs. Success: no key in version control.
6. Test the new key with a sandbox-mode request before it carries real traffic. Success: the sandbox send works.

When to use: creating API keys for SendGrid senders and integrations.

When not to use: SMTP credential setup (different mechanism), scheduled rotation (see the rotation skill), or debugging send content.

Compatibility: SendGrid API keys, v3 API.

Variants:
- sendgrid api key permissions
- sendgrid 403 mail send scope
- sendgrid restricted access key

Root cause of most key problems: Full Access keys lying around, or a 403 that is really a scope gap. A Mail Send restricted key can send mail but cannot read suppressions, manage templates, or touch stats, and that is by design.

Edge cases:
- Hard limits: 100 API keys per account max, and a key can never have greater permissions than the user who created it.
- Rotation: to replace a key, create the new scoped key first, deploy it, then delete the old one.

---

Source: [Vectle](https://vectle.com/skills/skl_NAWv1TTlPZ_y9B7dzx2j5Q). Version: `skv_ROVNw3IOCtWqVikEZEUM5w`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
