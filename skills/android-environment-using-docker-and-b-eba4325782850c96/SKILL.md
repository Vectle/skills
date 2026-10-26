---
name: "android-environment-using-docker-and-b-eba4325782850c96"
description: "Guide android environment using docker and bitbucket pipelines: If I understand your question correctly: you technically don't even need to install Docker on your local machine in order to use it in your Bitbucket Pipelines (although it can be quite helpful for. Use this when you hit exactly this in android. Not for different errors or different tools."
metadata:
  skill_id: "skl_QySovucaFQOC2TlB08QN7Q"
  title: "android environment using docker and bitbucket pipelines"
  version: "skv_YzmfaKV3o99m0ch7hrQGJA"
  updated: "2026-10-03T13:55:27.978036+00:00"
  canonical_url: "https://vectle.com/skills/skl_QySovucaFQOC2TlB08QN7Q"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://stackoverflow.com/questions/39806261/android-environment-using-docker-and-bitbucket-pipelines\"]"
---

TL;DR: If I understand your question correctly: you technically don't even need to install Docker on your local machine in order to use it in your Bitbucket Pipelines (although it can be quite helpful for debugging). Bitbucket Pipelines can be configured to use a Docker from Docker Hub , and the one you mentioned ( uber/android-build-environment ) worked well for me.

If I understand your question correctly: you technically don't even need to install Docker on your local machine in order to use it in your Bitbucket Pipelines (although it can be quite helpful for debugging). 

 Bitbucket Pipelines can be configured to use a Docker from Docker Hub , and the one you mentioned ( uber/android-build-environment ) worked well for me. 

 Simply add a `bitbucket-pipelines.yml` to the root of your project, for example: 

 [code: image: uber/android-build-environment:latest

pipelines:
 default:
 - step:
 script:
 - build.sh ] 

 I like to organize my build process in it's own ash script file (`build.sh`) but that is optional (you could instead put multiple bulleted commands in the yaml file under the `script` directive). Examples of (and more details about) the `bitbucket-pipelines.yml` file can be found on the Language guides for Bitbucket Pipelines page. 

 My `build.sh` script (also in the root of the project, but could be placed in a subdirectory as long as you refer to it as such in your `bitbucket-pipelines.yml`, e.g. `scripts/build.sh`): 

 [code: #!/bin/sh

mkdir "${ANDROID_HOME}/licenses" || true
echo "8933bad161af4178b1185d1a37fbf41ea5269c55" > "${ANDROID_HOME}/licenses/android-sdk-license"

./gradlew assembleDebug ] 

 The licenses portion allows the Android Gradle process to automatically download Android dependencies for you, as mentioned in this answer . 

 For good measure, set the permissions on the build script accordingly: 

 [code: git update-index --chmod=+x build.sh ] 

 Make sure that you've enabled Bitbucket Pipelines (from your repo page: `Settings` -> `Pipelines: Settings` -> `Enable Pipelines`). 

 Then just commit the `bitbucket-pipelines.yml` and `build.sh` and push to your BitBucket repo. The Bitbucket Pipelines build for your project should begin shortly after your push. The Bitbucket Pipelines will download the `uber/android-build-environment` Docker from Docker Hub and checkout your project and run the `build.sh` script within the Docker. 

 The process you were describing of setting up the Docker on your local machine can be really helpful if your Bitbucket Pipelines build fails and you want to have the same environment running on your local machine so you can experiment with it and test changes to the `build.sh` script before actually committing and pushing to your repo. 

 Might also prove helpful

## When to use
You hit exactly this: android environment using docker and bitbucket pipelines in android.

## When not to use
A different error, or the same symptom in a different tool. This page only covers the failure above.

## Compatibility
android.

---

Source: [Vectle](https://vectle.com/skills/skl_QySovucaFQOC2TlB08QN7Q). Version: `skv_YzmfaKV3o99m0ch7hrQGJA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
