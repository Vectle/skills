---
name: "your-token-has-not-been-granted-the-re-5fcc408abecdb4b7"
description: "Fixes the gh CLI error 'Your token has not been granted the required scopes to execute this query' by refreshing the token with the missing scope. Use when a gh command fails naming a scope it needs. Not for SAML enforcement errors or expired tokens."
metadata:
  skill_id: "skl_iZM4_G1ILukdX5Aw8JKLrQ"
  title: "Your token has not been granted the required scopes to execute this query"
  version: "skv_QEcqku8JOEAWxD84DxtPGQ"
  updated: "2026-10-03T05:55:12.457415+00:00"
  canonical_url: "https://vectle.com/skills/skl_iZM4_G1ILukdX5Aw8JKLrQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

Run gh auth refresh -s [scope] to add the missing scope to your token, then retry the command. The gh CLI tells you which scope it needs right in the error output. This happens when a command needs a permission your token was created without, like workflow or read:project.

```text
Your token has not been granted the required scopes to execute this query
```

## Fix it
1. Read the full error. gh usually names the missing scope and even prints the exact refresh command to run.
   Success check: You see a scope name like `workflow`, `read:org`, or `project` in the output.
2. Run gh auth refresh -s [scope] -h github.com, swapping in the scope from step 1.
   Success check: A browser or device-code flow opens; complete it.
3. Re-run the original gh command.
   Success check: It succeeds instead of printing the scope error.
4. Confirm with gh auth status that the scope is now listed for the active account.
   Success check: The scope appears under Token scopes.

## When this applies
- gh prints 'not been granted the required scopes'
- a gh command worked before and broke after a token refresh or re-login with fewer scopes

## When this does NOT apply
- the error mentions SAML enforcement instead (different fix: authorize the token for the org)
- the token itself is expired or revoked (re-authenticate instead)

## Compatibility
gh CLI 2.x on macOS, Linux, Windows. Works for github.com and GitHub Enterprise Server hosts.

## Variant phrasings
### Fine-grained token variant
Fine-grained PATs show resource-level denials instead of this message. Check the token's repository access under Developer settings.

## Why it happens
GitHub issues tokens with exactly the scopes granted at creation. When gh calls an endpoint outside those scopes, the API rejects it and gh surfaces the missing scope. Refreshing re-authorizes the same token with the extra scope instead of making you start over.

## Edge cases
- gh auth refresh has no --user flag: it targets the currently active account, so gh auth switch --user [name] first on multi-account setups.
- In headless environments the browser flow cannot open; use a device code or refresh from a machine with a browser.
- Some scopes (like admin:org) need org admin approval before the refresh completes.

Source: https://github.com/hive-consensus/support/blob/HEAD/BOARD_TEMPLATE_RUNBOOK.md

---

Source: [Vectle](https://vectle.com/skills/skl_iZM4_G1ILukdX5Aw8JKLrQ). Version: `skv_QEcqku8JOEAWxD84DxtPGQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
