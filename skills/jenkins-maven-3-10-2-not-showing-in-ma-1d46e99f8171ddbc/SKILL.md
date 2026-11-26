---
name: "jenkins-maven-3-10-2-not-showing-in-ma-1d46e99f8171ddbc"
description: "Jenkins Maven 3.10.2 not showing in Maven tool installations: installer list stops at 3.10.1"
metadata:
  skill_id: "skl_nnnkyJbcxbdgQA-tVcFKaA"
  title: "Jenkins Maven 3.10.2 not showing in Maven tool installations: installer list stops at 3.10.1"
  version: "skv_TSEqQmI3io8u32WQ8EyWQA"
  updated: "2026-11-26T12:07:42.766067+00:00"
  canonical_url: "https://vectle.com/skills/skl_nnnkyJbcxbdgQA-tVcFKaA"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Confirm the release really is published. Open the Maven Central directory for org/apache/maven/apache-maven and check the new version folder exists with its bin zip (for 3.10.2, apache-maven-3.10.2-bin.zip). Success check: the folder and zip are listed. If they are there, the gap is only in the Jenkins installer list, which is generated on the Jenkins infrastructure side and refreshes on its own schedule.

Fastest workaround, per agent: in Manage Jenkins, Tools, Maven installations, add a new installation named Maven 3.10.2, untick Install automatically, and instead add the zip extraction installer from the installer dropdown. Set the download URL to the Maven Central bin zip for the new version and the sub directory to the folder inside the zip (apache-maven-3.10.2). Success check: on the next build that selects this installation, the log shows the zip being downloaded and extracted, and mvn -version reports Apache Maven 3.10.2.

Alternative that works fully offline: download and unpack the same bin zip on the controller and on every agent that will run Maven, then add a Maven installation with Install automatically unticked and no installer, and set its home field to the unpacked directory (the folder containing bin/mvn). Success check: a freestyle or pipeline step running mvn -version with this installation prints 3.10.2 on each agent label you use.

In pipelines, select the version by the installation name you just created (tool name Maven 3.10.2, type maven) rather than the version string from the Apache installer list. Success check: the build runs with the new Maven and no tool resolution error appears in the log.

When the generated list catches up, you can switch the installation back to Install automatically from Apache and pick 3.10.2 there, then delete the temporary zip based installation. Success check: the version appears in the Apache installer dropdown without the custom installer present.

---

Source: [Vectle](https://vectle.com/skills/skl_nnnkyJbcxbdgQA-tVcFKaA). Version: `skv_TSEqQmI3io8u32WQ8EyWQA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
