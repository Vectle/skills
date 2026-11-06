---
name: "github-output-syntax-error-multiline-o-eae042def6b536aa"
description: "GITHUB_OUTPUT syntax error multiline output breaks workflow bug"
metadata:
  skill_id: "skl_Tb9iNUj2sY3ADMV_yoQMLw"
  title: "GITHUB_OUTPUT syntax error multiline output breaks workflow bug"
  version: "skv_af9xA-WFwBnx9dVHaao7sg"
  updated: "2026-11-06T01:54:16.96655+00:00"
  canonical_url: "https://vectle.com/skills/skl_Tb9iNUj2sY3ADMV_yoQMLw"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

**Find the step that writes the output.** Look for a line that appends a multiline variable, command output, or file contents to GITHUB_OUTPUT with the plain name=value form. Expected: you have the exact run block that produces the invalid format error or the truncated value.

**Rewrite it with a unique delimiter.** Use the delimiter form below, with a delimiter string that cannot appear inside the value; a random suffix or a guid works well. Success check: the step finishes without the file command error.

**Remove any old set-output lines.** The deprecated set-output workflow command is disabled on current runners and fails the step; every output must go through the GITHUB_OUTPUT file instead. Search the workflow for set-output and convert each one to the file form. Expected: no set-output text remains in the workflow files.

**Check the reading side.** Later steps and jobs read the value from the step outputs by the exact output name declared in the step and the job outputs mapping. A spelling difference between the written name and the read name gives an empty value with no error. Success check: the names match character by character in the write, the step outputs, and the job outputs.

**Test with a value that has trailing newlines and special lines.** Lines inside the value that look like name=value pairs are safe inside the delimiter block, but a line equal to the delimiter ends the value early. Run the workflow once with realistic content, then print the received value length in the next step. Expected: the length matches the source value and the content arrives whole.

**For outputs built in a script file, write the file from the script.** Scripts in any language can append the same delimiter block to the path stored in the GITHUB_OUTPUT environment variable. Success check: the script based step passes the same workflow test as the shell based step.

---

Source: [Vectle](https://vectle.com/skills/skl_Tb9iNUj2sY3ADMV_yoQMLw). Version: `skv_af9xA-WFwBnx9dVHaao7sg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
