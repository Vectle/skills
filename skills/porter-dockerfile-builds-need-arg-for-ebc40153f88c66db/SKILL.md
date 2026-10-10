---
name: "porter-dockerfile-builds-need-arg-for-ebc40153f88c66db"
description: "# Porter: Dockerfile builds need ARG for build-time env vars; buildpacks dont From Porter's official build docs, the build-method split that breaks builds: - Dockerfile builds: environment variables are NOT available at build time unless you declare them with `ARG`."
metadata:
  skill_id: "skl_2pw-R6R8j6C2x60Sg8BjTA"
  title: "Porter: Dockerfile builds need ARG for build-time env vars; enable BuildKit for COPY --chown"
  version: "skv_J-oBtyDvu2-2PKq39fskQg"
  updated: "2026-10-03T04:47:48.981253+00:00"
  canonical_url: "https://vectle.com/skills/skl_2pw-R6R8j6C2x60Sg8BjTA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# Porter: Dockerfile builds need ARG for build-time env vars; enable BuildKit for COPY --chown

## TL;DR

Context: Porter official docs (applications/deploy/builds.mdx, porter-dev/docs): build-time environment variables differ by build method. Dockerfile builds require the ARG keyword to make variables available at build time (ARG PORTERENVVARIABLE, referenced as ${PORTERENVVARIABLE}); buildpack builds need no extra configuration for build-time variables. Builds using COPY --chown require BuildKit: set DOCKERBUILDKIT to 1.

Use this when you run into the situation in the title.

**When not to use this skill:** unrelated tasks. It covers only the procedure above.

## Compatibility

The steps above apply to the commands named in them. This skill does not pin a version, so if a flag looks different on your machine, check your installed version's docs first.

## Details

# Porter: Dockerfile builds need ARG for build-time env vars; buildpacks dont From Porter's official build docs, the build-method split that breaks builds: - Dockerfile builds: environment variables are NOT available at build time unless you declare them with `ARG`. Add `ARG PORTER_ENV_VARIABLE` to the Dockerfile and reference `${PORTER_ENV_VARIABLE}` where needed. Without the ARG line, the variable is empty during the build and your build fails or bakes in a blank value. - Buildpack builds: no extra configuration needed. Build-time environment variables are available to the build process automatically. - `COPY --chown` in a Dockerfile requires BuildKit. Set `DOCKER_BUILDKIT` to `1` (e.g. at the top level of your GitHub Actions workflow env) or the build fails. After a successful build, Porter pushes the image into a container registry in your connected cloud account and updates the app to the new build. If your app is not picking up changes, check which build method the app uses first: the ARG fix only applies to Dockerfile builds.

After a successful build, Porter pushes the image to a container registry in your connected cloud account and updates the app.


---

Source: [Vectle](https://vectle.com/skills/skl_2pw-R6R8j6C2x60Sg8BjTA). Version: `skv_J-oBtyDvu2-2PKq39fskQg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
