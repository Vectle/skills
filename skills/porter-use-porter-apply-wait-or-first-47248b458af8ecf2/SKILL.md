---
name: "porter-use-porter-apply-wait-or-first-47248b458af8ecf2"
description: "# Porter: porter apply without --wait fails first deploys against fresh datastores From Porter's official porter.yaml docs, the ordering gotcha in multi-app deploys: `porter apply -f porter.yaml` creates datastores and deploys apps, but by default it does not wait."
metadata:
  skill_id: "skl_jjPi8J7UT06gJrF5mzKFsw"
  title: "Porter: use porter apply --wait or first deploys fail with missing-environment-group"
  version: "skv_x-gngPxatVd1tbOi6yjb9A"
  updated: "2026-10-03T04:48:28.010111+00:00"
  canonical_url: "https://vectle.com/skills/skl_jjPi8J7UT06gJrF5mzKFsw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# Porter: use porter apply --wait or first deploys fail with missing-environment-group

## TL;DR

Context: Porter official docs (applications/configuration-as-code/addons-porter-yaml.mdx, porter-dev/docs): porter apply deploys apps and datastores from one porter.yaml. Without --wait, the CLI proceeds about 10 seconds after creating a datastore, and apps may fail their first deploy with a missing-environment-group error until the datastore finishes provisioning. With --wait, apply holds until each datastore is fully available (up to 10 minutes) before any apps deploy, guaranteeing the datastores' environment groups and credentials exist when apps start.

Use this when you run into the situation in the title.

**When not to use this skill:** unrelated tasks. It covers only the procedure above.

## Compatibility

The steps above apply to the commands named in them. This skill does not pin a version, so if a flag looks different on your machine, check your installed version's docs first.

## Porter: porter apply without --wait fails first deploys against fresh datastores From Porter's official porter.yaml docs, the ordering gotcha in multi-app deploys: `porter apply -f porter.yaml` creates datastores and deploys apps, but by default it does not wait. The CLI moves on about 10 seconds after creating a datastore, while provisioning takes minutes. Apps that reference the datastore's environment group then fail their first deploy with a missing-environment-group error, and succeed on a later retry once the datastore exists. It looks flaky; it is just ordering. The fix: `porter apply -f porter.yaml --wait`. The flag holds the apply until each datastore is fully available (up to 10 minutes) before any apps deploy, so environment groups and credentials exist when apps start. It also waits for each app's rollout to succeed before exiting. Related: provisioning a datastore automatically creates an environment group with the same name as the datastore. Link it in the app's `envGroups` with the exact name. A typo there is the same missing-environment-group error, but --wait will not save you.

Context: Porter official docs (applications/configuration-as-code/addons-porter-yaml.mdx, porter-dev/docs): porter apply deploys apps and datastores from one porter.yaml. Without --wait, the CLI proceeds about 10 seconds after creating a datastore, and apps may fail their first deploy with a missing-environment-group error until the datastore finishes provisioning. With --wait, apply holds until each datastore is fully available (up to 10 minutes) before any apps deploy, guaranteeing the datastores' environment groups and credentials exist when apps start. Provisioning a datastore auto-creates an environment group with the same name as the datastore; link it via envGroups with the exact name.


---

Source: [Vectle](https://vectle.com/skills/skl_jjPi8J7UT06gJrF5mzKFsw). Version: `skv_x-gngPxatVd1tbOi6yjb9A`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
