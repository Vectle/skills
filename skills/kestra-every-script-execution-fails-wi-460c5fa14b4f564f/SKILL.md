---
name: "kestra-every-script-execution-fails-wi-460c5fa14b4f564f"
description: "Fixes Kestra script tasks failing on the Docker runner because the script file (e.g. main.py from inputFiles) is not accessible inside the runner container. Use this when every script execution fails with missing input files across Windows WSL2, Docker Desktop, and Linux Swarm alike. Not for process-runner failures or missing Docker images."
metadata:
  skill_id: "skl_GTf8T-UoBd1bCDmxUvuoRQ"
  title: "Kestra: every script execution fails with Docker runner (script file not accessible)"
  version: "skv_3QsvOlZi9v6DUK1_7O7uFA"
  updated: "2026-10-03T04:30:25.984249+00:00"
  canonical_url: "https://vectle.com/skills/skl_GTf8T-UoBd1bCDmxUvuoRQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://vectle.com/threads/thr_I8KpgO7pHtrS15QmGlxpkw\",\"https://github.com/kestra-io/kestra/issues/3590\"]"
---

TL;DR: if every Kestra script task fails on the Docker runner because the script file is not accessible inside the container, your tmp path is misaligned between Kestra and the runner. Mount the same host directory into the Kestra container at the same path and point Kestra's `tmp-dir.path` at it. Two reporters confirmed this exact config fixed it on Ubuntu Swarm and elsewhere.

## Steps

1. Create the host directories first:

```sh
mkdir -p /mnt/storage-pool/appdata/kestra/tmp/kestra-wd/tmp
```

   (Use your own base path; the example path above is from the verified thread.)

2. In your compose file, mount the working directory at the same path inside the Kestra container and share the Docker socket:

```yaml
services:
  app:
    volumes:
      - /mnt/storage-pool/appdata/kestra/tmp/kestra-wd:/mnt/storage-pool/appdata/kestra/tmp/kestra-wd
      - /var/run/docker.sock:/var/run/docker.sock
    environment:
      KESTRA_CONFIGURATION: |
        kestra:
          tasks:
            tmp-dir:
              path: /mnt/storage-pool/appdata/kestra/tmp/kestra-wd/tmp
```

   Expected: Kestra and the runner container resolve the temp working directory to the identical path.

3. Recreate the Kestra container and re-run a script task with an inputFile.

   Expected: the script finds its input files and runs. Success check: the task log shows the script executing instead of a missing-file error.

## When to use this

- Every script task using the Docker runner fails with the script file not accessible.
- It happens on multiple platforms (WSL2, Docker Desktop, Linux Swarm), so it is not OS-specific.

## When NOT to use this

- You use the process runner, which runs locally and does not need the volume alignment.
- The failure is about a missing image or registry auth, not missing input files.

## Compatibility

- Kestra with the Docker task runner; config syntax shown for Docker Compose setups.

## Variant phrasings

- "Kestra Docker runner input files not found"
- "Kestra script task fails with Docker worker tmp dir"
- "Kestra inputFiles missing in Docker container"

## Root cause

The Docker runner mounts a shared volume for the working directory, so the temp path has to be identical on the Kestra side and the runner side. The Kestra team reproduced it: the runner could not create the input files in the temp working directory because the tmp path was not aligned between Kestra and the runner container.

## Edge cases

- Skip the `mkdir -p` and you get a bind mount error instead of the script error, which is a different failure to debug.
- Only the working-directory path needs to match; other Kestra config can stay as-is.

Source: https://github.com/kestra-io/kestra/issues/3590

---

Source: [Vectle](https://vectle.com/skills/skl_GTf8T-UoBd1bCDmxUvuoRQ). Version: `skv_3QsvOlZi9v6DUK1_7O7uFA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
