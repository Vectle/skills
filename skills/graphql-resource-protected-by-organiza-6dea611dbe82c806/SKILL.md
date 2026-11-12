---
name: "graphql-resource-protected-by-organiza-6dea611dbe82c806"
description: "graphql: resource protected by organization saml enforcement. you must grant your oauth token access to this..."
metadata:
  skill_id: "skl_-nj71BNf5FjB3GG__T4AiQ"
  title: "graphql: resource protected by organization saml enforcement. you must grant your oauth token access to this..."
  version: "skv_EQBXjfWCBLAmgTDKhlcErA"
  updated: "2026-11-12T13:53:38.723222+00:00"
  canonical_url: "https://vectle.com/skills/skl_-nj71BNf5FjB3GG__T4AiQ"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Confirm the failing repository belongs to the organization named in your workflow and that calls to repositories outside that organization succeed with the same credential.

Sign in to GitHub in a browser as the account that owns the credential and complete the organization single sign on flow so the session is SAML authenticated.

Open the credential settings page. For a personal access token open the token list, for an OAuth app open the authorized applications list, and find the credential used by the failing call.

Use the configure or authorize control next to that organization and complete the authorization prompt.

Retry the exact GraphQL query that failed, without changing the query or the endpoint.

If the call runs from CI or an agent, confirm the secret or stored credential in that environment is the same credential you just authorized, not an older copy.

---

Source: [Vectle](https://vectle.com/skills/skl_-nj71BNf5FjB3GG__T4AiQ). Version: `skv_EQBXjfWCBLAmgTDKhlcErA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
