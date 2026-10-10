---
name: "make-variable-visible-across-steps-in-58d230b44e912750"
description: "Guide Make variable visible across steps in Bitbucket pipelines?: April 2025: now it's possible without tricks You can now export variables and use them in all subsequent steps as shown below. Use this when you hit exactly this in this tool. Not for different errors or different tools."
metadata:
  skill_id: "skl_N6g09OSlMVCHpo9jQsOmnw"
  title: "Make variable visible across steps in Bitbucket pipelines?"
  version: "skv_W6Vc-wPoX1KwXfK-0AbPsw"
  updated: "2026-10-03T05:42:29.819081+00:00"
  canonical_url: "https://vectle.com/skills/skl_N6g09OSlMVCHpo9jQsOmnw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: April 2025: now it's possible without tricks You can now export variables and use them in all subsequent steps as shown below. [code: pipelines: default: - step: name: Export Variable script: - echo "VAR_1=12345" >> $BITBUCKET_PIPELINES_VARIABLES_PATH output-variables: - VAR_1 - step: name: Use Variable script: - echo $VAR_1 ] The feature was first released and explained on 31st of March 2025: [Atlassian News Blog] Easily share data between steps in Bitbucket Pipelines .

April 2025: now it's possible without tricks 
 You can now export variables and use them in all subsequent steps as shown below. 
 [code: pipelines:
 default:
 - step:
 name: Export Variable
 script:
 - echo "VAR_1=12345" >> $BITBUCKET_PIPELINES_VARIABLES_PATH
 output-variables:
 - VAR_1
 - step:
 name: Use Variable
 script:
 - echo $VAR_1 ] 
 The feature was first released and explained on 31st of March 2025: [Atlassian News Blog] Easily share data between steps in Bitbucket Pipelines . 
 This feature is explicitly meant to replace the old way: 
 
 Previously, sharing variables between steps required more effort than desired, doing things like saving variables in an artifact file and using that artifact in subsequent steps. With this new feature, you can now share variables seamlessly and efficiently, reducing complexity and potential errors in your pipeline configurations. ~ the Blog article 
 
 Read the docs: Output Variables step option (in Bitbucket Pipelines configuration reference). 
 
 Responding to a comment: it works with anchored steps, too. 
 I tested it in a branch `test-output-variables-and-anchors`: 
 [code: definitions:
 steps:
 - step: &output-variables
 name: Export Variable
 script:
 - echo "VAR_1=12345" >> $BITBUCKET_PIPELINES_VARIABLES_PATH
 - echo "VAR_2=67890" >> $BITBUCKET_PIPELINES_VARIABLES_PATH
 output-variables:
 - VAR_1
 - VAR_2

 - step: &log-variables
 name: Log Variables
 script:
 - echo $VAR_1
 - echo $VAR_2

pipelines:
 branches:
 test-output-variables-and-anchors:
 - step: *output-variables
 - step: *log-variables ] 
 This worked and flawlessly did output the `VAR_1` and `VAR_2` values correctly in the second step.

## When to use
You hit exactly this: Make variable visible across steps in Bitbucket pipelines?.

## When not to use
A different error, or the same symptom in a different tool. This page only covers the failure above.

## Compatibility
the tool named in the title.

## Edge cases
- With this new feature, you can now share variables seamlessly and efficiently, reducing complexity and potential errors in your pipeline configurations. ~ the Blog article Read the docs: Output Variables step option (in Bitbucket Pipelines configuration reference).

---

Source: [Vectle](https://vectle.com/skills/skl_N6g09OSlMVCHpo9jQsOmnw). Version: `skv_W6Vc-wPoX1KwXfK-0AbPsw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
