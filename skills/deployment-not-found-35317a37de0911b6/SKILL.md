---
name: "deployment-not-found-35317a37de0911b6"
description: "deployment_not_found"
metadata:
  skill_id: "skl_qvQiM9_pSxnbRhIMppUbXA"
  title: "deployment_not_found"
  version: "skv_eG1YbsO7bjher_P7etWjEg"
  updated: "2026-11-05T01:53:28.682342+00:00"
  canonical_url: "https://vectle.com/skills/skl_qvQiM9_pSxnbRhIMppUbXA"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

**Get the id from the source, not from memory.** Open the deployment list for the project in the dashboard or run the platform list command for that project. Expected: you can see the deployments that actually exist, with their ids, urls, and states.

**Compare the failing id character by character.** Stale ids from an earlier deploy, a copied preview url, and ids trimmed by a shell variable all produce this exact 404. Success check: the id in your command or alias config matches an id in the list from step 1, or you have confirmed it is absent.

**Check team and project scope.** Deployment ids are scoped, so querying under the wrong team, the wrong project, or a personal account instead of the team returns not found even when the deployment is healthy. Switch to the team and project shown in the dashboard for that deployment and retry. Expected: the inspect or lookup call returns the deployment details.

**Check the deployment state.** A canceled, failed-early, or deleted deployment, and preview deployments removed by retention cleanup, cannot be inspected or aliased. In the dashboard, open the project history and look for a deleted or canceled entry at the time the link worked. Success check: you know whether the record still exists.

**Redeploy if the record is gone.** Run a fresh deploy for the same commit or branch, note the new deployment id and url from the output, and update any alias, bookmark, or pipeline variable that pointed at the old one. Expected: the new url serves the site and the alias resolves to the new deployment.

**For CLI lookups, pass the url you just verified.** Inspect commands accept a deployment url or id from the current scope. Run the inspect command against the verified url from step 5 (or step 1). Success check: it prints build and route details instead of the 404.

---

Source: [Vectle](https://vectle.com/skills/skl_qvQiM9_pSxnbRhIMppUbXA). Version: `skv_eG1YbsO7bjher_P7etWjEg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
