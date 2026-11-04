---
name: "exception-in-thread-main-java-lang-out-53e238f81a409c73"
description: "Exception in thread main java.lang.OutOfMemoryError\" GATK HaplotypeCaller fails: how to fix"
metadata:
  skill_id: "skl_Mh_HVnWsEaJ56dt9dakwMg"
  title: "Exception in thread main java.lang.OutOfMemoryError\" GATK HaplotypeCaller fails: how to fix"
  version: "skv_-0QawsSWYLd0CuKEGJNr2w"
  updated: "2026-11-04T01:57:12.059731+00:00"
  canonical_url: "https://vectle.com/skills/skl_Mh_HVnWsEaJ56dt9dakwMg"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

**Confirm the heap GATK actually started with.** Check the GATK log header for the Java command line and the max heap value. Expected: the log shows a small default heap, often far below the memory free on the machine.

**Rerun with an explicit larger heap.** Add the java options setting to the HaplotypeCaller command, for example a heap of 8 gigabytes on a machine that has that memory free, keeping the rest of the command unchanged. Success check: the log header now shows the larger max heap you set.

**Test on one small interval first.** Run the same command limited to a single short interval or a small chromosome region. Expected: the test run finishes and writes a valid VCF instead of ending with OutOfMemoryError.

**Split large jobs by interval.** If whole genome runs still exhaust a reasonable heap, run HaplotypeCaller per interval in parallel and merge the resulting VCF files afterwards. Success check: each interval job completes on its own heap and the merged VCF contains records from every interval.

**Check for an oversized input problem.** Look for an unindexed BAM, a BAM with an unusually deep region, or a missing interval list that makes the tool load more than intended. Expected: the input BAM has an index file beside it and the run is scoped to the intended genome.

---

Source: [Vectle](https://vectle.com/skills/skl_Mh_HVnWsEaJ56dt9dakwMg). Version: `skv_-0QawsSWYLd0CuKEGJNr2w`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
