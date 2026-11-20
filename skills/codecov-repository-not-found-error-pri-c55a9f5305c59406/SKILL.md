---
name: "codecov-repository-not-found-error-pri-c55a9f5305c59406"
description: "codecov repository not found error private repo token missing fails"
metadata:
  skill_id: "skl_g0LTTNT9iys5mBqrz0Lq5w"
  title: "codecov repository not found error private repo token missing fails"
  version: "skv_SY9ex4nlB8qiuFhhOfvtdQ"
  updated: "2026-11-20T01:51:57.838857+00:00"
  canonical_url: "https://vectle.com/skills/skl_g0LTTNT9iys5mBqrz0Lq5w"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Confirm the repo is private and note the exact owner and repo slug the uploader is using.

Open the repo in Codecov and open its settings to find the repository upload token for that repo.

Store that value as a CI secret in your provider and pass it to the Codecov uploader step or action input.

Rerun the CI job that generates coverage and uploads it.

If it still fails, check that the secret is available to the job, for example fork pull requests often cannot read repository secrets.

---

Source: [Vectle](https://vectle.com/skills/skl_g0LTTNT9iys5mBqrz0Lq5w). Version: `skv_SY9ex4nlB8qiuFhhOfvtdQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
