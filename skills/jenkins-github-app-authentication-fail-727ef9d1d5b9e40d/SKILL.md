---
name: "jenkins-github-app-authentication-fail-727ef9d1d5b9e40d"
description: "Jenkins GitHub App authentication failed: remote Repository not found, fatal Authentication failed on git ls-remote"
metadata:
  skill_id: "skl_AF3k1VDj6DEE6dQDFj3klA"
  title: "Jenkins GitHub App authentication failed: remote Repository not found, fatal Authentication failed on git ls-remote"
  version: "skv_GEOYqcOTP8bv6fPodNqhlw"
  updated: "2026-11-08T11:55:45.45714+00:00"
  canonical_url: "https://vectle.com/skills/skl_AF3k1VDj6DEE6dQDFj3klA"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Check the GitHub App installation before touching Jenkins. In GitHub, open Settings, Developer settings, GitHub Apps, pick the app, then Install App: the app must be installed on the account that owns the target repository, its repository access must include that repository (All repositories, or the repo named under Only select repositories), and its permissions must include Contents set to Read-only. Success check: the target repository appears in the installation's repository list. An app that is created but not installed on the owning account produces exactly this Repository not found response.

Re-validate the Jenkins credential. In Manage Jenkins, Credentials, open the GitHub App credential: the App ID must be the app's numeric ID from its GitHub settings page, the private key must be the converted PKCS#8 version (the credential form's Convert button produces it from the key GitHub issued), and the Owner field must match the repository owner exactly. Save, then open the job configuration: the repository connection check should pass instead of reporting Failed to connect to repository.

Sync the controller clock. A GitHub App signs a JWT that lives about 10 minutes and exchanges it for an installation access token that lives 1 hour, so a controller clock that drifts produces intermittent authentication failures that come and go on their own. On RHEL check timedatectl and chronyc tracking, enable NTP synchronisation, and confirm the offset is under a second. Success check: timedatectl reports the clock synchronised and repeated repository scans an hour apart both pass.

If installation, credential, and clock all check out and the failures began with a plugin upgrade, roll the GitHub Branch Source plugin back to the previous version as a test, restart Jenkins, and run Scan Repository Now on the multibranch pipeline. Success check: if authentication passes consistently on the older version, the regression is in the upgrade; stay on the older version and link the upstream plugin issue from the job thread instead of re-upgrading.

Verify over time, not once. Trigger Scan Repository Now and one build, then repeat the scan after more than an hour (past one installation token lifetime). Success check: the ls-remote connection check and the build's checkout both pass on every attempt; a single pass followed by later failures means a step above was only partly right.

---

Source: [Vectle](https://vectle.com/skills/skl_AF3k1VDj6DEE6dQDFj3klA). Version: `skv_GEOYqcOTP8bv6fPodNqhlw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
