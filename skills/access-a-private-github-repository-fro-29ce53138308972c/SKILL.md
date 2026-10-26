---
name: "access-a-private-github-repository-fro-29ce53138308972c"
description: "Shows how to give a Cloud Build step access to a private GitHub repository for Go dependency fetching. Use this when glide install or git clone fails in Cloud Build with host-key or credential errors. Not for public repos or for non-Cloud Build CI."
metadata:
  skill_id: "skl_5kACJY9SUrULtPi6jUlAtg"
  title: "Access a private GitHub repository from a Cloud Build step (glide install fails)"
  version: "skv_K-G3fOhwzRvAoqvUp8yxwg"
  updated: "2026-10-03T04:40:02.545417+00:00"
  canonical_url: "https://vectle.com/skills/skl_5kACJY9SUrULtPi6jUlAtg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://vectle.com/threads/thr_ug35OVIWokBJ45IwGV3y8Q\",\"https://github.com/GoogleCloudPlatform/cloud-builders/issues/44\"]"
---

TL;DR: Cloud Build steps have no GitHub credentials by default, so private repos are unreachable until you inject them. Store a deploy key or token encrypted, pull it into the build from Cloud Storage in an early step, then use it for git operations (add GitHub to known_hosts to avoid the host-key verification failure). Google's tutorial on using encrypted files in builds covers exactly this pattern.

```text
[WARN] Unable to checkout github.com/[org]/[repo]
[ERROR] Update failed ... Unable to get repository
```

## Steps

1. Create a GitHub deploy key (or token) for the private repo and store it encrypted where the build can fetch it (e.g. Cloud Storage).

2. In an early build step, fetch the key and add GitHub to known_hosts.

3. Run the git operations (clone, glide install) using the injected key.

   Expected: the private repo fetches. Success check: `glide install` completes without the checkout errors.

## When to use this

- Cloud Build, Go project depending on a private GitHub repo.
- Errors like "Host key verification failed", "Could not read from remote repository", or "could not read Username for 'https://github.com'".

## When NOT to use this

- Public repos; no credentials needed.
- Non-Cloud Build CI; the injection mechanism differs.

## Compatibility

- Google Cloud Build with the git builder; follow Google's encrypted-files tutorial for the key handling.

## Variant phrasings

- "cloud build private github repo"
- "cloud build glide install private repo"
- "cloud build git host key verification failed"

## Root cause

Build steps run with the build service account, which has no GitHub credentials, so both SSH and HTTPS clones fail in their characteristic ways.

## Edge cases

- Never bake the key into the image or repo; fetch it at build time from encrypted storage.

---

Source: [Vectle](https://vectle.com/skills/skl_5kACJY9SUrULtPi6jUlAtg). Version: `skv_K-G3fOhwzRvAoqvUp8yxwg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
