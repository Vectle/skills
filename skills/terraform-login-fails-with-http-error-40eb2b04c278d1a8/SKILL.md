---
name: "terraform-login-fails-with-http-error-40eb2b04c278d1a8"
description: "terraform login fails with HTTP ERROR 422 during HCP Terraform sign-in and account linking"
metadata:
  skill_id: "skl_iG7v_7v5F92iEl9WaLj_vQ"
  title: "terraform login fails with HTTP ERROR 422 during HCP Terraform sign-in and account linking"
  version: "skv_MJa9abNiD79PyZOb5kbGHQ"
  updated: "2026-11-08T11:56:56.275382+00:00"
  canonical_url: "https://vectle.com/skills/skl_iG7v_7v5F92iEl9WaLj_vQ"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Get a user token from the web UI first. Sign in to HCP Terraform in the browser (use the same GitHub account), open User Settings (avatar menu), then Tokens, then Create an API token, name it for your machine, and copy the value shown once. Success check: the new token appears in your token list with todays date.

Hand the token to the CLI instead of finishing the browser flow. Run terraform login, wait for the CLI to open the browser and print its Enter a token prompt, ignore the browser tab, and paste the copied token into the terminal. Success check: the CLI prints a success message saying you are signed in, and it writes a credentials file in your home directory under the .terraform.d folder.

Verify the CLI can actually use it. Run terraform organizations or open a configuration that uses the HCP backend for the workspace you created and run terraform init. Success check: the workspace is found and init completes with no login or authentication error.

If you want the browser flow itself fixed, clear the linking conflict. A GitHub identity can be linked to only one HCP account: if you ever made a second HCP account (for example an email and password one with the same email), the linking step refuses with 422. Sign in to the older account, or finish the original accounts onboarding (an organization must exist) before linking, then retry terraform login. Success check: the browser flow ends on the You may now close this window page instead of the 422 page.

Rule out the browser session as the cause once. Retry the flow in a private window with third-party cookies allowed for the HCP sign-in pages: the login redirect hands off between the CLI callback, the HCP site, and GitHub, and a dropped session cookie in that chain can also surface as an unprocessable response. Success check: the private-window attempt either completes or still 422s, which tells you it is the account link, not the browser.

---

Source: [Vectle](https://vectle.com/skills/skl_iG7v_7v5F92iEl9WaLj_vQ). Version: `skv_MJa9abNiD79PyZOb5kbGHQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
