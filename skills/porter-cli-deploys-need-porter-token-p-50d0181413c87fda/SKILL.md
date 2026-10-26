---
name: "porter-cli-deploys-need-porter-token-p-50d0181413c87fda"
description: "# Porter CI deploys need PORTER_TOKEN, PORTER_PROJECT, and PORTER_CLUSTER From Porter's official docs on using other CI tools, the three-variable contract for CLI-driven deploys: The Porter CLI targets an application through three environment variables: `PORTER_TOKEN`, `PORTER_PROJECT`, and `PORTER_CLUSTER`."
metadata:
  skill_id: "skl_WKQe4FfhYwEN_1dJQ0yYlg"
  title: "Porter: CLI deploys need PORTER_TOKEN, PORTER_PROJECT, PORTER_CLUSTER set"
  version: "skv_RxnM_2l7KTzdaN45r-9mdg"
  updated: "2026-10-03T04:46:05.390858+00:00"
  canonical_url: "https://vectle.com/skills/skl_WKQe4FfhYwEN_1dJQ0yYlg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/porter-dev/docs/blob/HEAD/applications/deploy/using-other-ci-tools.mdx\"]"
---

# Porter: CLI deploys need PORTER_TOKEN, PORTER_PROJECT, PORTER_CLUSTER set

## TL;DR

Context: Porter official docs (applications/deploy/using-other-ci-tools.mdx, porter-dev/docs): to deploy from CircleCI, GitLab, Travis CI, or any CI tool, use the public Porter CLI Docker image ghcr.io/porter-dev/releases/porter-cli:latest. The CLI requires three environment variables to target an application: PORTERTOKEN, PORTERPROJECT, PORTERCLUSTER. Obtain their values by logging into the Porter CLI and running porter config.

Use this when you run into the situation in the title.

**When not to use this skill:** unrelated tasks. It covers only the procedure above.

## Compatibility

The steps above apply to the commands named in them. This skill does not pin a version, so if a flag looks different on your machine, check your installed version's docs first.

## Details

# Porter CI deploys need PORTER_TOKEN, PORTER_PROJECT, and PORTER_CLUSTER From Porter's official docs on using other CI tools, the three-variable contract for CLI-driven deploys: The Porter CLI targets an application through three environment variables: `PORTER_TOKEN`, `PORTER_PROJECT`, and `PORTER_CLUSTER`. Miss any one and the CLI cannot resolve which app to update. Get their values by logging into the CLI and running `porter config`. The documented pattern for any CI system (CircleCI, GitLab, Travis): 1. Run the public image `ghcr.io/porter-dev/releases/porter-cli:latest` as the job image. 2. Store the three variables in the CI system's secret store (e.g. one CircleCI Context per Porter cluster). 3. Update the app with `porter app update-tag [APP_NAME] --tag $CIRCLE_SHA1 --stream`. If a CI deploy fails to find the app, check the three variables before the YAML: a wrong PORTER_CLUSTER silently targets a different cluster's app list, and the error reads like the app does not exist.

Example CircleCI flow: store the three variables in a CircleCI Context per cluster, then run porter app update-tag [APP_NAME] --tag $CIRCLE_SHA1 --stream in a job using the CLI image.


---

Source: [Vectle](https://vectle.com/skills/skl_WKQe4FfhYwEN_1dJQ0yYlg). Version: `skv_RxnM_2l7KTzdaN45r-9mdg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
