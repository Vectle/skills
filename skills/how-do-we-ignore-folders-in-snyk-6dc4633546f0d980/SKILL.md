---
name: "how-do-we-ignore-folders-in-snyk-6dc4633546f0d980"
description: "Shows how to fix how do we ignore folders in Snyk. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_UGzPsZrtKDOkvdssqjyl-g"
  title: "How do we ignore folders in Snyk"
  version: "skv_L_oBBgsMZ7raoj_gQhsT7A"
  updated: "2026-10-04T04:44:25.097892+00:00"
  canonical_url: "https://vectle.com/skills/skl_UGzPsZrtKDOkvdssqjyl-g"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"vectle-agent-13a5f8a682c3\"}"
  original_notices_and_references: "[\"https://stackoverflow.com/questions/76145644/how-do-we-ignore-folders-in-snyk\"]"
---

## TL;DR

To exclude directories for the open source part, you need to: In an SCM import, add the list to exclude (screenshot) In a CLI import, add the directories as arguments (syntax below) --exclude=DIRECTORY[,DIRECTORY]...&gt; (only in test and monitor commands) Can be used with --all-projects and --yarn-workspaces to indicate sub-directories and files to exclude. This is confusing because these are two separate mechanisms.

## When to use

You are seeing this: From the accepted Stack Overflow answer: Yes, unfortunately this is confusing today. Use this skill when you run into "How do we ignore folders in Snyk".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

From the accepted Stack Overflow answer: Yes, unfortunately this is confusing today. For historical reasons, the .snyk file only applies to Snyk Code (SAST). To exclude directories for the open source part, you need to: In an SCM import, add the list to exclude (screenshot) In a CLI import, add the directories as arguments (syntax below) --exclude=DIRECTORY[,DIRECTORY]...&gt; (only in test and monitor commands) Can be used with --all-projects and --yarn-workspaces to indicate sub-directories and files to exclude. Must be comma separated. This is confusing because these are two separate mechanisms. In the future, both mechanisms will be the same, but for now, both need to be done.

Context: Problem: Accepted solution (score 5): Yes, unfortunately this is confusing today. For historical reasons, the .snyk file only applies to Snyk Code (SAST). To exclude directories for the open source part, you need to: In an SCM import, add the list to exclude (screenshot) In a CLI import, add the directories as arguments (syntax below) --exclude=DIRECTORY[,DIRECTORY]...&gt; (only in test and monitor commands) Can be used with --all-projects and --yarn-workspaces to indicate sub-directories and files to exclude. Must be comma separated. This is confusing because these are two separate mechanisms. In the future, both mechanisms will be the same, but for now, both need to be done.


---

Source: [Vectle](https://vectle.com/skills/skl_UGzPsZrtKDOkvdssqjyl-g). Version: `skv_L_oBBgsMZ7raoj_gQhsT7A`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
