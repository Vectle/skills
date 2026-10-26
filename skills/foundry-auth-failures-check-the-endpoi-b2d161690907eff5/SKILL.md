---
name: "foundry-auth-failures-check-the-endpoi-b2d161690907eff5"
description: "Guide Foundry auth failures: check the endpoint and deployment name variables first: On auth failures with a new Foundry project, check config before credentials. Verify the project endpoint variable is set to the full project URL and the model deployment name variable is set to the. Use this when you hit exactly this in Foundry auth failures. Not for different errors or different tools."
metadata:
  skill_id: "skl_uOP55OKNNopw1L2EaRL6VA"
  title: "Foundry auth failures: check the endpoint and deployment name variables first"
  version: "skv_ZWuu_OedX0COUhhh8LdXoA"
  updated: "2026-10-03T04:47:50.192118+00:00"
  canonical_url: "https://vectle.com/skills/skl_uOP55OKNNopw1L2EaRL6VA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/arturo-quiroga/PDF-ANALYZER/blob/HEAD/QUICKSTART.md\"]"
---

TL;DR: On auth failures with a new Foundry project, check config before credentials. Verify the project endpoint variable is set to the full project URL and the model deployment name variable is set to the exact deployment name from the dashboard. An unset connection string surfaces as a generic auth or connection failure that looks like a bad key.

On auth failures with a new Foundry project, check config before credentials. Verify the project endpoint variable is set to the full project URL and the model deployment name variable is set to the exact deployment name from the dashboard. An unset connection string surfaces as a generic auth or connection failure that looks like a bad key. Set the variables in the environment, restart the process so they are picked up, and only then test with a minimal chat completion. If key auth keeps failing, switch to DefaultAzureCredential and confirm the identity has the Azure AI User role.

## When to use
You hit exactly this: Foundry auth failures: check the endpoint and deployment name variables first in Foundry auth failures.

## When not to use
A different error, or the same symptom in a different tool. This page only covers the failure above.

## Compatibility
Foundry auth failures.

---

Source: [Vectle](https://vectle.com/skills/skl_uOP55OKNNopw1L2EaRL6VA). Version: `skv_ZWuu_OedX0COUhhh8LdXoA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
