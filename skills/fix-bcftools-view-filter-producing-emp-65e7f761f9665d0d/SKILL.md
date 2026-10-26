---
name: "fix-bcftools-view-filter-producing-emp-65e7f761f9665d0d"
description: "Diagnose bcftools filtering failures: classify usage-dump parse errors (shell quoting) vs silent zero-record output (flag-tag =1/=0 semantics, -q minor-allele-frequency, FILTER exact-vs-subset matching) vs regions-file parse errors (tab delimiter) vs unindexed VCF region queries, then apply the matching fix."
metadata:
  skill_id: "skl_7AvXrYAuRJ6ar_0KlvGTHw"
  title: "Fix bcftools view/filter producing empty or wrong output"
  version: "skv_iEXUNQfdNH84oDmKC1-3cQ"
  updated: "2026-10-03T04:10:39.365736+00:00"
  canonical_url: "https://vectle.com/skills/skl_7AvXrYAuRJ6ar_0KlvGTHw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://www.biostars.org/p/9540212/\",\"https://www.biostars.org/p/9526118/\",\"https://www.biostars.org/p/9578253/\",\"http://www.htslib.org/doc/1.21/bcftools.html\"]"
---

# Fix bcftools view/filter producing empty or wrong output

## TL;DR

`bcftools view`/`filter`/`query` returning zero or wrong records is almost always one of four things: a shell-quoting parse failure, an expression that matches nothing, an index/region mismatch, or a header/sample-name assumption. Classify from the exact symptom first using the sections below; re-running with a different guess at the expression wastes the most time.

Use this when `bcftools view` / `bcftools filter` / `bcftools query` with
`-i`/`-e` expressions, `-q`, `-f`, or `-T`/`-R` region options returns zero
records, the wrong records, or an error. These failures look identical ("my
filter didn't work") but split into four classes with different fixes.
Classify from the exact symptom FIRST.

**When not to use this skill:** `bcftools` itself is not installed or crashes on startup (install/environment problem); the VCF is malformed and fails `bcftools view` with no filter at all (validate the file first); you need help writing a complex new filter expression from scratch rather than debugging an existing one. — re-running with a different guess at
the expression wastes the most time here.

## 1. Classify the symptom

### A. bcftools prints the usage text and exits

The expression failed to parse — usually **shell quoting**, not bcftools
logic. Classic real case: `-i "INFO/IMP'` (mismatched quote) makes the shell
hand bcftools a broken argument and bcftools dumps usage. Rule: wrap the
whole expression in single quotes and never mix quote types:

```bash
# right
bcftools view -i 'INFO/IMP=1' in.vcf.gz
# wrong: the double-quote never closes
bcftools view -i "INFO/IMP' in.vcf.gz
```

If quoting looks fine, simplify the expression until it parses, then rebuild
it — the parser chokes on the first bad token, and the usage dump doesn't
say which one.

### B. No error, but zero (or far too few) records out

The expression parsed; it just doesn't match what you think it matches.
**Do not eyeball `| head`** — a VCF header alone is often >10 lines, so
`bcftools view -i '...' file.vcf | head -10` showing "only header" proves
nothing. Count records properly:

```bash
bcftools view -H -i 'INFO/IMP=1' in.vcf.gz | wc -l   # -H: no header
```

Then check the three classic mismatches, in order:

1. **Flag tags need `=1` / `=0`.** An INFO flag (`Number=0,Type=Flag` in the
   header, e.g. `##INFO=&lt;ID=IMP,Number=0,Type=Flag,...&gt;`) has no value to
   compare — test presence, per the docs ("1 (or 0) to test the presence
   (or absence) of a flag"):

   ```bash
   bcftools view -i 'INFO/IMP=1' in.vcf.gz    # flag present
   bcftools view -i 'INFO/IMP=0' in.vcf.gz    # flag absent
   ```

   Bare `'INFO/IMP'` also tests presence, but `=1` is explicit and matches
   the documented idiom.

2. **`-q` / `--min-af` is a minor-allele-frequency filter, not "AF column
   greater than x".** `bcftools view -q 0.1` keeps sites with MAF ≥ 0.1 and
   drops everything else — if your AF annotation is missing, computed
   differently, or mostly rare variants, you get an empty VCF with no error.
   Inspect what the filter actually sees before assuming:

   ```bash
   bcftools view -h in.vcf.gz | grep '##INFO=&lt;ID=AF'   # is AF even annotated?
   bcftools query -f '%CHROM\t%POS\t%INFO/AF\n' in.vcf.gz | head
   ```

   If you wanted "AF > 0.1", write it as an expression instead:
   `bcftools view -i 'AF>0.1' in.vcf.gz`.

3. **FILTER-column matching is exact vs subset.** In expressions,
   `FILTER="PASS"` is an exact match (`"A;B"` fails it), while `FILTER~"A"`
   is a subset match. And `-f/--apply-filters` *skips* sites whose FILTER
   lacks every listed string — to keep unfiltered sites, include `.`:
   `bcftools view -f .,PASS in.vcf.gz`.

General probe for any suspicious `-i`/`-e`: run the same expression through
`bcftools query -f` printing the tags involved, on a file you can inspect:

```bash
bcftools query -f '%CHROM\t%POS\t%FILTER\t%INFO/DP\n' -i 'DP>10' in.vcf.gz | head
```

If the printed rows don't satisfy your mental model of the expression,
the model — not the data — is wrong.

### C. `[E::bcf_sr_regions_init] Could not parse N-th line of file`

The regions/targets file format is wrong. bcftools expects **tab-delimited**,
2 columns (`CHROM`, `POS`, 1-based inclusive) or 3 columns (`CHROM`, `BEG`,
`END`) — never space-delimited. The recurring real-world cause: `awk`
prints with `OFS=" "` by default. Fix at creation:

```bash
awk -F';' 'NR>1 {OFS="	"; print $1,$2}' chr.csv > regions.txt
bcftools view -T regions.txt -Oz -o filtered.vcf.gz in.vcf.gz
```

(`-T`/`--targets-file` streams by POS; `-R`/`--regions-file` index-jumps and
checks proper overlaps including indel ends.)

### D. Region query fails or returns nothing on an indexed-looking file

1. **The VCF/BCF must actually be indexed** for `-r`/`-R` ("This option
   requires indexed VCF/BCF files"). Index it:

   ```bash
   bcftools index in.vcf.gz        # creates in.vcf.gz.csi
   ```

   Note `-T` is stricter still: its targets file "must be compressed and
   indexed" (`bgzip` + `tabix` the targets file, or use `-R` with a plain
   text list instead).

2. **Contig names must match exactly.** Per the docs: `"chr20"` is not the
   same as `"20"`. Compare `bcftools view -h in.vcf.gz | grep '^##contig'`
   against your region strings; normalize one side (`bcftools annotate
   --rename-chrs`) if they disagree.

3. `-r` and `-R` can't be combined; `-t` and `-T` can't be combined.
   Pick one.

## 2. Useful expression idioms (documented)

```bash
bcftools view -i 'QUAL>20 && DP>10' in.vcf.gz          # compound threshold
bcftools view -e 'FILTER!="PASS"' in.vcf.gz           # drop non-PASS (exact match)
bcftools view -i 'FILTER~"q10"' in.vcf.gz             # FILTER contains q10 (subset)
bcftools view -m2 -M2 -v snps in.vcf.gz               # biallelic SNPs only
bcftools view -i 'GT="alt"' in.vcf.gz                 # at least one alt genotype
bcftools view -i 'DP="."' in.vcf.gz                   # DP is missing
```

Tags can be written `INFO/DP` or bare `DP`, `FORMAT/DV` / `FMT/DV` / `DV`.

## Quick decision tree

1. Usage text dumped → quoting/parse error (class A); single-quote the expression.
2. Zero records, no error → count with `-H | wc -l`, then flag `=1`/`=0`, then `-q`-is-MAF, then FILTER exact-vs-subset (class B).
3. `Could not parse N-th line` → tab-delimit the regions file (class C).
4. Region query broken → index the VCF (`bcftools index`), check exact contig names, `-T` needs bgzipped+indexed targets (class D).

## Compatibility

- bcftools 1.15+ (filter expression syntax stable since 1.10; `-T`/`-R` region handling unchanged).
- Works on VCFv4.2–v4.5 and BCF2.

## Variant phrasings

- bcftools view filter returns no records
- bcftools filter expression not working
- bcftools query empty output
- bcftools -i -e expression wrong results


---

Source: [Vectle](https://vectle.com/skills/skl_7AvXrYAuRJ6ar_0KlvGTHw). Version: `skv_iEXUNQfdNH84oDmKC1-3cQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
