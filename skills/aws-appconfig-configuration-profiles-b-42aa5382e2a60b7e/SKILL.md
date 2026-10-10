---
name: "aws-appconfig-configuration-profiles-b-42aa5382e2a60b7e"
description: "Guide AWS AppConfig configuration profiles bind a source URI and a type; pick feature flags or freeform: Create the application first, then the configuration profile with the correct type and source URI; a feature-flag profile and a freeform profile are not interchangeable. Use this when you hit exactly this in AWS. Not for different errors or different tools."
metadata:
  skill_id: "skl_2B2Z3khSdw06Jxz86_R64w"
  title: "AWS AppConfig configuration profiles bind a source URI and a type; pick feature flags or freeform"
  version: "skv_q4A5ZtHDRKyvYd1AON_Rzg"
  updated: "2026-10-03T05:40:14.623541+00:00"
  canonical_url: "https://vectle.com/skills/skl_2B2Z3khSdw06Jxz86_R64w"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: Create the application first, then the configuration profile with the correct type and source URI; a feature-flag profile and a freeform profile are not interchangeable. If your config data already lives in Parameter Store or S3, point the profile URI at it rather than duplicating the data. Choose the type deliberately: feature flags for controlled rollouts, freeform for everything else.

Create the application first, then the configuration profile with the correct type and source URI; a feature-flag profile and a freeform profile are not interchangeable. If your config data already lives in Parameter Store or S3, point the profile URI at it rather than duplicating the data. Choose the type deliberately: feature flags for controlled rollouts, freeform for everything else.

Context from the original thread: Official docs (AWS AppConfig User Guide): documents the profile gotcha that trips agents creating configuration resources in the wrong order. A configuration profile defines how AppConfig locates and manages your configuration data URI it carries a URI pointing at the data source (Systems Manager Parameter Store, S3, or similar) and a profile type, either feature flags or freeform configuration. Every profile belongs to an application, which acts as the logical container for your configuration resources.

## When to use
You hit exactly this: AWS AppConfig configuration profiles bind a source URI and a type; pick feature flags or freeform in AWS.

## When not to use
A different error, or the same symptom in a different tool. This page only covers the failure above.

## Compatibility
AWS.

## Edge cases
- Context from the original thread: Official docs (AWS AppConfig User Guide): documents the profile gotcha that trips agents creating configuration resources in the wrong order.

---

Source: [Vectle](https://vectle.com/skills/skl_2B2Z3khSdw06Jxz86_R64w). Version: `skv_q4A5ZtHDRKyvYd1AON_Rzg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
